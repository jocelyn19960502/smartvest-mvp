
````markdown
# SmartVest MVP

SmartVest is a web-based investment analysis tool designed to help retail investors interpret technical indicators through clean visualizations and natural-language explanations.

## Key Features

- Enter a stock ticker (e.g., AAPL)
- Display closing price chart with 20-day and 50-day moving averages (MA20 & MA50)
- Show RSI (Relative Strength Index) with simple explanation
- Show MACD (Moving Average Convergence Divergence) with signal line
- Provide natural-language explanations for each indicator
- Include expandable sections to explain indicator concepts (for better UX)

## Tech Stack

- **Language**: Python
- **Framework**: Streamlit (for GUI)
- **Data source**: yfinance (real-time stock data)
- **Data processing**: pandas
- **Visualization**: matplotlib

## How to Run

1. Install the required packages:

```bash
pip install yfinance pandas matplotlib streamlit
````

2. Run the application:

```bash
streamlit run smartvest_app.py
```

The web app will automatically open in your browser.

## Screenshots

* Stock price chart with MA20 & MA50
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
