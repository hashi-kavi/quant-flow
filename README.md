# STOCK_ANALYZER

Lightweight stock analysis project using `yfinance` + NumPy vectorized indicators.

This repository currently focuses on:
- downloading close-price data
- computing Bollinger Bands with `sliding_window_view`
- computing daily percentage returns
- exploring results in a Jupyter notebook

## Current Project Status

The implemented analysis flow is notebook-based.

- `scripts/data_loader.py` is implemented.
- `scripts/indicators.py` is implemented.
- `notebooks/analysis_test.ipynb` demonstrates the workflow.
- `notebooks/stock_analysis.ipynb` is currently an empty placeholder.
- `main.py/` exists as an empty folder (no CLI entry script is implemented yet).
- `data/` is currently empty.

## Project Structure

```text
STOCK_ANALYZER/
|-- README.md
|-- data/
|-- main.py/
|-- notebooks/
|   |-- analysis_test.ipynb
|   `-- stock_analysis.ipynb
`-- scripts/
    |-- __init__.py
    |-- data_loader.py
    `-- indicators.py
```

## Requirements

- Python 3.10+
- `numpy`
- `yfinance`
- `matplotlib`
- Jupyter (optional, for notebook workflow)

Install dependencies:

```bash
pip install numpy yfinance matplotlib notebook
```

## Implemented APIs

### `scripts.data_loader.get_stock_data(ticker, start_date, end_date)`

- Downloads historical market data using `yfinance`.
- Returns flattened NumPy array of close prices.
- Returns `None` if download fails or returns empty data.

### `scripts.indicators.calculate_bollinger_bands(prices, window_size=20, num_std=2)`

- Uses NumPy vectorization and `sliding_window_view`.
- Returns `(upper_band, sma, lower_band)` as NumPy arrays.

### `scripts.indicators.calculate_daily_return(prices)`

- Uses `np.diff(prices) / prices[:-1]`.
- Returns daily percentage returns.

## How To Use

### Option 1: Notebook (current primary workflow)

Open and run:

```text
notebooks/analysis_test.ipynb
```

This notebook currently:
- downloads data for a selected ticker/date range
- plots close prices
- computes and plots Bollinger Bands
- computes and plots daily returns

### Option 2: Python script snippet

```python
from scripts.data_loader import get_stock_data
from scripts.indicators import calculate_bollinger_bands, calculate_daily_return

ticker = "NVDA"
prices = get_stock_data(ticker, "2024-01-01", "2026-01-01")

if prices is not None:
    upper, sma, lower = calculate_bollinger_bands(prices, window_size=20, num_std=2)
    daily_returns = calculate_daily_return(prices)
    print(len(prices), len(sma), len(daily_returns))
```

## Notes and Limitations

- Internet connection is required for `yfinance` downloads.
- Always validate `prices is not None` before indicator calculations.
- `window_size` must be greater than 0 and not larger than the number of price points.
- A CLI entrypoint is not yet implemented in this repository.

## Suggested Next Improvements

- Add input validation inside indicator functions (`None`, scalar, short arrays).
- Add a real `main.py` CLI script for ticker/date arguments.
- Add tests for `data_loader.py` and `indicators.py`.
- Add additional indicators (EMA, RSI, MACD).
