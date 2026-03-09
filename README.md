# Quant Flow - Stock Analyzer

A lightweight stock market technical analysis tool using `yfinance` for market data and NumPy vectorization for fast indicator computation.

This project demonstrates quantitative finance fundamentals, numerical computing techniques, and clean Python architecture for financial analysis tools.

## Features

- CLI-based analysis using command-line arguments
- Fast vectorized NumPy computations (no slow loops)
- Technical indicators: Simple Moving Average (SMA), Bollinger Bands, Daily Returns
- Automatic chart generation using Matplotlib
- Generated reports saved as PNG files
- Jupyter notebook workflow for experimentation
- Clean modular architecture for expanding indicators

## Project Structure

```text
quant-flow/
|
|-- .gitignore
|-- README.md
|-- main.py                  # CLI entry point
|
|-- data/                    # Reserved for cached market data
|-- reports/                 # Generated analysis charts
|
|-- notebooks/
|   `-- analysis_test.ipynb
|
`-- scripts/
    |-- __init__.py
    |-- data_loader.py
    `-- indicators.py
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/hashi-kavi/quant-flow.git
cd quant-flow
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv .venv
```

Activate on Windows:

```bash
.venv\Scripts\activate
```

Activate on macOS/Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

Create a `requirements.txt` file:

```text
numpy
yfinance
matplotlib
jupyter
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Quick Start

Run stock analysis from the command line:

```bash
python main.py --ticker NVDA --start 2024-01-01
```

Example with full range:

```bash
python main.py --ticker NVDA --start 2024-01-01 --end 2026-01-01
```

Generated charts will appear in:

```text
reports/
```

Example output file:

```text
reports/NVDA_report.png
```

## Dependencies

| Library | Purpose |
|---|---|
| NumPy | Vectorized numerical computation |
| yfinance | Yahoo Finance market data API |
| Matplotlib | Chart generation |
| Jupyter | Interactive analysis (optional) |

Python version: `3.10+`

## Implemented Indicators

### Bollinger Bands

Measures price volatility using a moving average and standard deviation bands.

Formula:

$$
Upper\ Band = SMA + (2 \times \sigma)
$$

$$
Lower\ Band = SMA - (2 \times \sigma)
$$

Where:

- `SMA` = Simple Moving Average (default 20 days)
- `sigma` = Rolling standard deviation
- Default multiplier = `2`

Usage:

- Identify volatility expansion
- Detect possible overbought or oversold conditions
- Observe support and resistance zones

### Simple Moving Average (SMA)

Smooths price data to reveal trends.

Formula:

$$
SMA_t = \frac{1}{n} \sum_{i=0}^{n-1} P_{t-i}
$$

Where:

- `n` = Window size
- `P` = Closing price

Usage:

- Identify market trend direction
- Reduce price noise

### Daily Returns

Measures day-to-day percentage price change.

Formula:

$$
Return_t = \frac{P_t - P_{t-1}}{P_{t-1}} \times 100
$$

Usage:

- Measure volatility
- Identify abnormal market movements
- Calculate risk metrics

## Module API Reference

### `data_loader.get_stock_data()`

Downloads historical price data from Yahoo Finance.

Signature:

```python
get_stock_data(ticker, start_date, end_date)
```

Parameters:

| Parameter | Type | Description |
|---|---|---|
| `ticker` | `str` | Stock symbol |
| `start_date` | `str` | Start date (`YYYY-MM-DD`) |
| `end_date` | `str` | End date (`YYYY-MM-DD`) |

Returns:

- `numpy.ndarray` of closing prices

Example:

```python
prices = get_stock_data("MSFT", "2024-01-01", "2024-12-31")
```

### `indicators.calculate_bollinger_bands()`

Signature:

```python
calculate_bollinger_bands(prices, window_size=20, num_std=2)
```

Returns:

- `upper_band`
- `sma`
- `lower_band`

All values are returned as NumPy arrays.

Output length:

```text
len(prices) - window_size + 1
```

### `indicators.calculate_daily_return()`

Signature:

```python
calculate_daily_return(prices)
```

Returns:

- Daily return percentages

Example:

```python
returns = calculate_daily_return(prices)
volatility = np.std(returns)
```

## CLI Usage

Run analysis for any stock.

Example:

```bash
python main.py --ticker TSLA --start 2024-01-01
```

Custom date range:

```bash
python main.py --ticker AAPL --start 2023-06-01 --end 2024-12-31
```

Default parameters:

- `ticker = NVDA`
- `start = 2024-01-01`
- `end = 2026-01-01`

## Python API Usage

You can use the modules directly.

```python
from scripts.data_loader import get_stock_data
from scripts.indicators import calculate_bollinger_bands
from scripts.indicators import calculate_daily_return

prices = get_stock_data("NVDA", "2024-01-01", "2026-01-01")

if prices is not None:
    upper, sma, lower = calculate_bollinger_bands(prices)
    daily_returns = calculate_daily_return(prices)

    print("Data points:", len(prices))
    print("Max gain:", daily_returns.max())
    print("Max loss:", daily_returns.min())
```

## Generated Report Format

The CLI automatically generates a two-panel chart.

Top panel:

- Price chart with Bollinger Bands
- Black line -> Closing price
- Blue dashed line -> SMA
- Red/Green bands -> Bollinger Bands
- Gray region -> Volatility range

Bottom panel:

- Daily returns
- Purple bars -> Day-to-day returns
- Black horizontal line -> Zero baseline

Charts are saved as:

```text
reports/<TICKER>_report.png
```

Example:

```text
reports/NVDA_report.png
```

## Technical Implementation

Indicators are implemented using NumPy vectorization.

Example:

```python
from numpy.lib.stride_tricks import sliding_window_view

windows = sliding_window_view(prices, 20)
sma = np.mean(windows, axis=1)
std = np.std(windows, axis=1)
returns = np.diff(prices) / prices[:-1] * 100
```

Advantages:

- Faster than Python loops
- Efficient memory usage
- Scales to large datasets

## Future Enhancements

Planned features:

- Relative Strength Index (RSI)
- Moving Average Convergence Divergence (MACD)
- Exponential Moving Average (EMA)
- Portfolio comparison
- Strategy backtesting engine
- CSV / JSON export
- Unit tests

## Notes and Limitations

- Internet connection required for Yahoo Finance data
- Data contains trading days only
- Window size must be `<=` available price points
- Always check `prices is not None` before running indicators
- This project is intended for educational and research purposes only

## Troubleshooting

### `yfinance` download fails

Check:

- Internet connection
- Valid ticker symbol
- Valid date range

### `sliding_window_view` error

Cause: dataset is smaller than window size.

Solution:

```python
len(prices) >= window_size
```

### `ModuleNotFoundError`

Run the program from the project root directory.

## Contributing

Contributions are welcome.

Possible improvements:

- New indicators
- Better visualizations
- Performance benchmarks
- Strategy testing tools

## License

MIT License

## Author

Kavindya Ranaweera

Quantitative Analysis
Machine Learning
Numerical Computing

Building Python tools that combine financial theory with real-world data analysis.
