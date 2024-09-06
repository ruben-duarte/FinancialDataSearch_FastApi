# Financial Data exploration with FastApi

## Description

This project is a web application built with FastAPI that provides endpoints for financial data, including quotations, options, and historical data. The application allows users to download data as ZIP files containing JSON representations of the requested information.

## Features

- **Get Financial Quotes**: Retrieve financial quotes for specified symbols.
- **Get Stock Options**: Fetch available options for a specific stock symbol.
- **Get Historical Data**: Obtain historical data for a given stock symbol.
- **Download Data**: Download the results of the above queries as a ZIP file with JSON content.

## API Documentation

- **YAHOO API Documentation**: [FinanceAPI](https://www.financeapi.net/)

### Available Stock and Asset Symbols for the API

- **Microsoft Corporation**: `MSFT`
- **Twitter, Inc.**: `TWTR`
- **Bitcoin**: `BTC`
- **Ethereum**: `ETH`
- **Crude Oil**: `CL=F`
- **Gold**: `GC=F`
- **EUR/USD**: `EURUSD=X`
- **EUR/CAD**: `EURCAD=X`

**Example symbols for requests**: `"TWTR,EURUSD=X,AAPL"`

### Available Country Symbols for the API

The following country symbols are available for searches in the endpoints:

- **AU**: Australia
- **CA**: Canada
- **DE**: Netherlands
- **ES**: Spain
- **FR**: France
- **GB**: United Kingdom
- **HK**: Hong Kong
- **IN**: India
- **IT**: Italy
- **US**: United States

### Available Language Symbols for the API

The following language symbols are available for requests in the endpoints:

- **en**: English
- **es**: Spanish
- **de**: Dutch
- **fr**: French
- **it**: Italian
- **zh**: Chinese

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name```

### create and activate virtual enviroment
```python3 -m venv venv
   source venv/bin/activate or 
   python -m venv venv
   venv\Scripts\activate

   pip install -r requirements.txt

   Add .env to .gitignore according to example in source code

   run the application -> uvicorn main:app --reload

   check localhost:8000/docs  and play with the API
```
