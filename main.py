import argparse
import os
import matplotlib.pyplot as plt
from scripts.data_loader import get_stock_data
from scripts.indicators import calculate_bollinger_bands, calculate_daily_return,calculate_macd,calculate_rsi


def run_analysis(ticker, start, end):
    print(f"--Starting Analysis for {ticker}--")

    #1. Fetch Data
    prices = get_stock_data(ticker, start, end)
    if prices is None:
        return
    if len(prices) < 30:
        print("Error: Not enough data points for a 20-day Bollinger Band calculation.")
        return

    #2. Run Math
    upper, sma, lower = calculate_bollinger_bands(prices)
    returns = calculate_daily_return(prices)

    rsi = calculate_rsi(prices)
    macd,signal,hist = calculate_macd(prices)

    #3. Generate visual report
    fig, axes = plt.subplots(4, 1, figsize=(14, 12), gridspec_kw={"height_ratios": [3,1,1,1]})
    ax1,ax2,ax3,ax4 = axes

    # Plot:price & bands

    ax1.plot(prices[19:], label="Price", color="black", lw=1.5)
    ax1.plot(upper, label="Upper Band", color="green", alpha=0.3)
    ax1.plot(lower, label="Lower Band", color="red", alpha=0.3)
    ax1.plot(sma, label="SMA", color="blue", ls="--")
    ax1.fill_between(range(len(sma)), lower, upper, color="gray", alpha=0.1)
    ax1.set_title(f"{ticker} Technical Analysis")
    ax1.legend()


    # Plot: Daily Returns

    ax2.bar(range(len(returns)), returns, color="purple", alpha=0.6)
    ax2.axhline(0, color="black", lw=0.5)
    ax2.set_ylabel("Daily Return %")

    # Plot: RSI

    ax3.plot(rsi,color='orange')
    ax3.axhline(70,linestyle='--',color='red')
    ax3.axhline(30,linestyle='--',color='green')

    ax3.set_title("Relative Strength Index (RSI)")

    # Plot: MACD

    ax4.plot(macd,color='blue',label="MACD")
    ax4.plot(signal,color='red',label="Signal")
    ax4.bar(range(len(hist)),hist,color="gray",alpha=0.5)

    ax4.legend()
    ax4.set_title("MACD")    

    #4. Save the Result

    output_dir = "reports"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    save_path = os.path.join(output_dir, f"{ticker}_report.png")
    fig.tight_layout()
    plt.savefig(save_path)
    plt.close(fig)
    print(f"Report saved to: {save_path}")

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Stock Quantitative Analyzer")
    parser.add_argument("--ticker", type=str, default="NVDA", help="Stock ticker symbol")
    parser.add_argument("--start", type=str, default="2024-01-01")
    parser.add_argument("--end", type=str, default="2026-01-01")

    args = parser.parse_args()
    run_analysis(args.ticker, args.start, args.end)

