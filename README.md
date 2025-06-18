

# SmartVest MVP

SmartVest is an online investment analysis platform created to assist retail investors in understanding technical indicators via clear visual representations and explanations in natural language.

## Key Features

- Enter a stock ticker (e.g., AAPL)
- Display stock price chart with 20-day and 50-day moving averages (MA20 & MA50)
- Show RSI (Relative Strength Index) with simple explanations
- Show MACD (Moving Average Convergence Divergence) with signal line
- Natural-language interpretation for each indicator
- Expandable sections explaining each technical concept (for UX)
- **[New] Premium Mode (simulated):**
  - Set custom RSI alert thresholds
  - Access placeholder for strategy backtesting features
  - See locked premium features if not subscribed

## Tech Stack

- **Language**: Python
- **Framework**: Streamlit (for GUI)
- **Data source**: yfinance (real-time stock data)
- **Data processing**: pandas
- **Visualization**: matplotlib

## How to Run

1. Install the required packages:


pip install yfinance pandas matplotlib streamlit


2. Run the application:


streamlit run smartvest_app.py


The web app will automatically open in your browser.


3. In the sidebar, check the box "I am a Premium user" to access additional features.

## Screenshots

* Stock price chart with MA20 & MA50
![image](https://github.com/user-attachments/assets/79e6d9f2-90ce-4f93-b064-07aed4c07681)

* RSI trend graph and insight
* MACD vs Signal Line chart and interpretation

*(Add screenshots or a demo GIF here if available.)*

## Future Improvements

* Integrate GPT API for dynamic language explanations
* Implement ML-based predictive insights
* Add backtesting tools and personalized alerts
* Connect with broker APIs or financial education platforms

## License

This project was developed as part of the FinTech course at Rotterdam School of Management (RSM) and is intended solely for academic and demonstration purposes.
It does not constitute investment advice.
