# Conviction-Engine-v3

Conviction Engine v3 is a conceptual multi-indicator trading engine built with Pine v6 for TradingView. It demonstrates how to combine multiple technical indicators — such as moving averages, relative strength index (RSI), and user-defined bias scores — to generate conviction signals and alerts in a trading script.

## Features

- **Multi-indicator framework**: Combine multiple indicators (moving averages, RSI, custom bias metrics) to generate a unified conviction score.
- **Configurable parameters**: Adjustable lookback periods, oversold/overbought thresholds, and bias weights.
- **Signal generation**: Generates simple BUY, SELL, or HOLD signals based on indicator crossovers and momentum conditions.
- **Extensible design**: Written in Pine Script v6 with a Python prototype (`app.py`) for rapid experimentation.

## Getting Started

This repository contains a Python prototype of the conviction logic and can serve as a companion to a Pine Script implementation. To explore the Python prototype:

```bash
# Clone the repository
git clone https://github.com/TanveerBakshii/Conviction-Engine-v3.git
cd Conviction-Engine-v3

# (Optional) Create a virtual environment and install dependencies if needed
python3 -m venv venv
source venv/bin/activate

# Run the prototype script
python app.py
```

The script will generate synthetic price data, compute indicators, and print sample signals to the console. You can modify the `generate_signals` function in `app.py` to experiment with different strategies.

## Project Structure

- `app.py` – Python prototype demonstrating moving averages, RSI calculations, and signal generation. Use this file as a reference or testing ground before porting logic to Pine Script.
- `README.md` – Documentation and usage instructions.
- `scripts/` – *(planned)* Contains Pine v6 scripts for TradingView (to be added in the future).

## Contributing

Contributions are welcome! If you'd like to improve the engine, add new indicators, or contribute a Pine Script version, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

Please follow standard Python and Pine Script style guidelines and include docstrings or comments to explain new functions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
