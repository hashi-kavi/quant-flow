import argparse
import os
import matplotlib.pyplot as plt
from scripts.data_loader import get_stock_data
from scripts.indicators import calculate_bollinger_bands,calculate_daily_return

def run_analysis(ticker,start,end):
    print(f"--Starting Analysis for {ticker}--")

    #1. Fetch Data
    prices = get_stock_data(ticker,start,end)
    if prices is None:return

    #2. Run Math
    upper,sma,lower = calculate_bollinger_bands(prices)
    returns = calculate_daily_return(prices)

    #3. Generate visual report
    fig,(ax1,ax2)= plt.subplot(2,1,figsize=(12,10),gridspec_kw ={"height_ratios":[3,1]})

    # Top Plot:price & bands

    ax1.plot(prices[19:], label='Price',color = 'black', lw = 1.5)
    ax1.plot(upper, label="Upper Band",color='green' ,alpha= 0.3)
    ax1.plot(lower, label="Lower Band",color='red', alpha= 0.3)
    ax1.plot(sma, label="SMA",color='blue', ls='--')
    ax1.fill_between(range(len(sma)),lower,upper,color='gray',alpha= 0.1)
    ax1.set_title(f"{ticker}Technical Analysis")
    ax1.legend()


    # Bottom Plot: Daily Returns

    ax2.bar(range(len(returns)),returns,color='purple', alpha= 0.6)
    ax2.axhline(0,color='black',lw = 0.5)
    ax2.set_ylabel("Daily Return %")

    #4. Save the Result

    output_dir = 'reports'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    save_path = f"{output_dir}/{ticker}_report.png"
    plt.savefig(save_path)
    print(f"Analisys complete.Report saved to : {save_path}")

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Stock Quantitative Analyzer")
    parser.add_argument("--ticker",type=str,default="NVDA",help ="Stock ticker symbol")
    parser.add_argument("--start",type=str,default="2024-01-01")
    parser.add_argument("--end",type=str,default="2026-01-01")

    args = parser.parse_args()
    run_analysis(args.ticker,args.start,args.end)

