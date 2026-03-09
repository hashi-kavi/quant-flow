# Quant Flow - Stock Analyzer

A lightweight stock market technical analysis tool using `yfinance` for market data and NumPy vectorization for fast indicator computation.

This project demonstrates quantitative finance fundamentals, numerical computing techniques, and clean Python architecture for financial analysis tools.

## Features

- CLI-based analysis using command-line arguments
- Fast vectorized NumPy computations (no slow loops)
- Technical indicators: Bollinger Bands, SMA, Daily Returns, RSI, MACD, EMA
- 4-panel visualization: Price + Bands, Returns, RSI, MACD
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

### Relative Strength Index (RSI)

Measures the magnitude of recent price changes to evaluate overbought/oversold conditions.

Formula:

$$
RSI = 100 - \left( \frac{100}{1 + RS} \right)
$$

Where `RS` = Average Gain / Average Loss over a 20-day window.

Usage:

- RSI > 70: Overbought (price may drop)
- RSI < 30: Oversold (price may rise)
- Identify potential reversal points

### Moving Average Convergence Divergence (MACD)

Measures trend momentum using two exponential moving averages (12-day and 26-day).

Calculation:

- `MACD Line` = EMA(12) - EMA(26)
- `Signal Line` = EMA(9) of MACD Line
- `Histogram` = MACD Line - Signal Line

Usage:

- MACD > Signal: Bullish momentum
- MACD < Signal: Bearish momentum
- Histogram crossovers indicate trend changes

### Exponential Moving Average (EMA)

Weights recent prices more heavily than older prices.

Formula:

$$
EMA_t = \alpha \cdot P_t + (1 - \alpha) \cdot EMA_{t-1}
$$

Where `α = 2 / (window + 1)`

Usage:

- Used internally for MACD calculation
- More responsive to recent price changes than SMA

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

### `indicators.calculate_rsi()`

Signature:

```python
calculate_rsi(prices, window=20)
```

Parameters:

| Parameter | Type | Description |
|---|---|---|
| `prices` | `np.ndarray` | Array of close prices |
| `window` | `int` | RSI calculation window (default: 20) |

Returns:

- NumPy array of RSI values (length = `len(prices) - 1`)

### `indicators.calculate_macd()`

Signature:

```python
calculate_macd(prices)
```

Returns:

- `macd_line`: MACD line values
- `signal_line`: Signal line (9-day EMA of MACD)
- `histogram`: Difference between MACD and Signal

All returned as NumPy arrays.

### `indicators.calculate_ema()`

Signature:

```python
calculate_ema(prices, window)
```

Parameters:

| Parameter | Type | Description |
|---|---|---|
| `prices` | `np.ndarray` | Array of prices |
| `window` | `int` | EMA window size |

Returns:

- NumPy array of EMA values

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
from scripts.indicators import (
    calculate_bollinger_bands,
    calculate_daily_return,
    calculate_rsi,
    calculate_macd
)

prices = get_stock_data("NVDA", "2024-01-01", "2026-01-01")

if prices is not None:
    # Bollinger Bands
    upper, sma, lower = calculate_bollinger_bands(prices)
    
    # Daily Returns
    daily_returns = calculate_daily_return(prices)
    
    # RSI
    rsi = calculate_rsi(prices)
    
    # MACD
    macd, signal, hist = calculate_macd(prices)
    
    print("Data points:", len(prices))
    print("Max gain:", daily_returns.max())
    print("Max loss:", daily_returns.min())
    print("Current RSI:", rsi[-1])
```

## Generated Report Format

The CLI automatically generates a four-panel chart.

**Panel 1: Price with Bollinger Bands**
- Black line: Closing price
- Blue dashed line: 20-day SMA
- Green/Red bands: Upper/Lower Bollinger Bands (±2σ)
- Gray region: Volatility channel

**Panel 2: Daily Returns**
- Purple bars: Day-to-day percentage changes
- Black horizontal line: Zero baseline

**Panel 3: RSI (Relative Strength Index)**
- Orange line: RSI values
- Red dashed line: Overbought threshold (70)
- Green dashed line: Oversold threshold (30)

**Panel 4: MACD (Moving Average Convergence Divergence)**
- Blue line: MACD line
- Red line: Signal line
- Gray bars: Histogram (MACD - Signal)

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

- Portfolio comparison
- Strategy backtesting engine
- CSV / JSON export
- Unit tests
- Stochastic Oscillator
- Average True Range (ATR)
- Support/Resistance level detection

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
