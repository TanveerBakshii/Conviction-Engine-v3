"""
Conviction Engine v3 - Skeleton Implementation

This module provides a simple demonstration of a multi-indicator trading engine.
It includes functions to compute simple moving averages, relative strength index (RSI),
generate trading signals based on indicator thresholds, and a main function
to simulate the engine with synthetic price data.

The purpose of this skeleton is to illustrate structure and type hints for further development.
"""

from typing import List, Optional
import random


def calculate_moving_average(data: List[float], period: int) -> List[Optional[float]]:
    """
    Calculate the simple moving average (SMA) for a given list of values.

    :param data: List of numerical values (prices).
    :param period: Number of periods to average over.
    :return: A list of SMA values, where entries prior to the period are None.
    """
    if period <= 0:
        raise ValueError("Period must be positive")
    ma: List[Optional[float]] = []
    for i in range(len(data)):
        if i + 1 < period:
            ma.append(None)
        else:
            window = data[i - period + 1:i + 1]
            ma.append(sum(window) / period)
    return ma


def calculate_rsi(prices: List[float], period: int) -> List[Optional[float]]:
    """
    Calculate the Relative Strength Index (RSI) using the Wilder smoothing method.

    :param prices: List of price values.
    :param period: Lookback period for RSI.
    :return: List of RSI values, with None for the initial period.
    """
    if period <= 0:
        raise ValueError("RSI period must be positive")
    if len(prices) < period + 1:
        # Not enough data to compute RSI
        return [None] * len(prices)

    deltas = [prices[i] - prices[i - 1] for i in range(1, len(prices))]
    gains = [max(delta, 0) for delta in deltas]
    losses = [abs(min(delta, 0)) for delta in deltas]

    # Initialize average gain and loss
    avg_gain = sum(gains[:period]) / period
    avg_loss = sum(losses[:period]) / period
    rs_values: List[Optional[float]] = [None] * (period)  # no RSI for first 'period' items
    # Compute initial RSI
    rs = avg_gain / avg_loss if avg_loss != 0 else 0
    rs_values.append(100 - (100 / (1 + rs)))

    # Compute subsequent RSI values using Wilder smoothing
    for i in range(period + 1, len(prices)):
        gain = gains[i - 1]
        loss = losses[i - 1]
        avg_gain = ((avg_gain * (period - 1)) + gain) / period
        avg_loss = ((avg_loss * (period - 1)) + loss) / period
        rs = avg_gain / avg_loss if avg_loss != 0 else 0
        rs_values.append(100 - (100 / (1 + rs)))
    return rs_values


def generate_signals(
    prices: List[float],
    short_period: int,
    long_period: int,
    rsi_period: int,
    oversold: float = 30,
    overbought: float = 70
) -> List[str]:
    """
    Generate basic trading signals based on moving average crossovers and RSI.

    :param prices: List of price values.
    :param short_period: Period for the short moving average.
    :param long_period: Period for the long moving average.
    :param rsi_period: Period for the RSI calculation.
    :param oversold: RSI threshold considered oversold (default 30).
    :param overbought: RSI threshold considered overbought (default 70).
    :return: List of signal strings: "BUY", "SELL", or "HOLD".
    """
    ma_short = calculate_moving_average(prices, short_period)
    ma_long = calculate_moving_average(prices, long_period)
    rsi = calculate_rsi(prices, rsi_period)

    signals: List[str] = []
    for i in range(len(prices)):
        # If indicators are not ready, hold
        if (
            ma_short[i] is None
            or ma_long[i] is None
            or rsi[i] is None
        ):
            signals.append("HOLD")
            continue

        # Buy when short MA crosses above long MA and RSI is oversold
        if ma_short[i] > ma_long[i] and rsi[i] < oversold:
            signals.append("BUY")
        # Sell when short MA crosses below long MA and RSI is overbought
        elif ma_short[i] < ma_long[i] and rsi[i] > overbought:
            signals.append("SELL")
        else:
            signals.append("HOLD")
    return signals


def main() -> None:
    """
    Entry point for testing the conviction engine with synthetic data.
    Generates a list of random price values and prints sample signals.
    """
    # Generate synthetic price series
    prices = [100 + random.uniform(-1, 1) for _ in range(100)]

    # Configure indicator periods
    short_ma_period = 5
    long_ma_period = 20
    rsi_period = 14

    signals = generate_signals(prices, short_ma_period, long_ma_period, rsi_period)

    # Display the first few signals for demonstration
    for idx in range(20):
        price = prices[idx]
        signal = signals[idx]
        print(f"Index {idx:02d} - Price: {price:.2f} -> Signal: {signal}")


if __name__ == "__main__":
    main()
