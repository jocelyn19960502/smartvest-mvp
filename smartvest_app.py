import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# RSI 計算
def calculate_rsi(data, period=14):
    delta = data['Close'].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def explain_rsi(rsi_value):
    if rsi_value < 30:
        return "RSI indicates the stock may be oversold — a rebound could be imminent."
    elif rsi_value > 70:
        return "RSI shows the stock may be overbought — a price drop could follow."
    else:
        return "RSI is neutral, suggesting no strong momentum."

# MA 解釋
def explain_ma(ma20, ma50):
    if ma20 > ma50:
        return "Short-term trend (MA20) is stronger than the mid-term (MA50) — the stock may be in an uptrend."
    elif ma20 < ma50:
        return "Short-term trend is weaker than the mid-term — the stock may be in a downtrend."
    else:
        return "Short and mid-term trends are aligned — no clear direction."

# MACD 計算
def calculate_macd(data):
    ema12 = data['Close'].ewm(span=12, adjust=False).mean()
    ema26 = data['Close'].ewm(span=26, adjust=False).mean()
    macd = ema12 - ema26
    signal = macd.ewm(span=9, adjust=False).mean()
    return macd, signal

def explain_macd(macd_value, signal_value):
    if macd_value > signal_value:
        return "MACD is above the signal line — upward momentum may be building."
    elif macd_value < signal_value:
        return "MACD is below the signal line — downward trend may be forming."
    else:
        return "MACD is crossing the signal line — possible trend reversal."

# Streamlit app
st.title("📈 SmartVest - Investment Assistant")
ticker = st.text_input("Enter Stock Ticker (e.g., AAPL)", value="AAPL")

if ticker:
    stock = yf.Ticker(ticker)
    hist = stock.history(period="6mo")

    if not hist.empty:
        # RSI
        hist['RSI'] = calculate_rsi(hist)
        latest_rsi = hist['RSI'].dropna().iloc[-1]

        # MA
        hist['MA20'] = hist['Close'].rolling(window=20).mean()
        hist['MA50'] = hist['Close'].rolling(window=50).mean()

        # MACD
        hist['MACD'], hist['Signal'] = calculate_macd(hist)
        latest_macd = hist['MACD'].dropna().iloc[-1]
        latest_signal = hist['Signal'].dropna().iloc[-1]

        # 價格圖 + MA
        st.subheader("Price Chart with Moving Averages")
        fig1, ax1 = plt.subplots()
        ax1.plot(hist['Close'], label='Close Price')
        ax1.plot(hist['MA20'], label='MA20')
        ax1.plot(hist['MA50'], label='MA50')
        ax1.set_title("Stock Price with MA20 & MA50")
        ax1.legend()
        st.pyplot(fig1)
        st.info(explain_ma(hist['MA20'].dropna().iloc[-1], hist['MA50'].dropna().iloc[-1]))
        with st.expander("ℹ️ What is a Moving Average?"):
            st.write("Moving Averages help identify the trend of a stock by smoothing price data. MA20 tracks short-term movements, while MA50 reflects mid-term trends. When MA20 crosses above MA50, it may signal a bullish trend.")

        # RSI 區塊
        st.subheader("RSI Analysis")
        st.write(f"Latest RSI: {latest_rsi:.2f}")
        st.info(explain_rsi(latest_rsi))
        fig2, ax2 = plt.subplots()
        ax2.plot(hist['RSI'], label='RSI')
        ax2.axhline(70, color='red', linestyle='--')
        ax2.axhline(30, color='green', linestyle='--')
        ax2.set_title("RSI Trend")
        ax2.legend()
        st.pyplot(fig2)
        with st.expander("ℹ️ What is RSI?"):
            st.write("RSI (Relative Strength Index) measures the speed and change of price movements. A value above 70 indicates overbought, below 30 indicates oversold. It's used to assess potential reversal points.")

        # MACD 區塊
        st.subheader("MACD Analysis")
        st.write(f"MACD: {latest_macd:.2f}, Signal Line: {latest_signal:.2f}")
        st.info(explain_macd(latest_macd, latest_signal))
        fig3, ax3 = plt.subplots()
        ax3.plot(hist['MACD'], label='MACD')
        ax3.plot(hist['Signal'], label='Signal Line')
        ax3.axhline(0, color='gray', linestyle='--')
        ax3.set_title("MACD vs Signal Line")
        ax3.legend()
        st.pyplot(fig3)
        with st.expander("ℹ️ What is MACD?"):
            st.write("MACD (Moving Average Convergence Divergence) shows the relationship between two moving averages. When MACD crosses above the Signal Line, it may indicate a bullish signal, and vice versa.")

    else:
        st.warning("No data found. Please check the ticker symbol.")
