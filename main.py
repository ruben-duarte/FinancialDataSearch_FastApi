from fastapi import FastAPI, Query
from typing import Optional
import os
from dotenv import load_dotenv
from pathlib import Path
from fastapi.responses import FileResponse
from utils import get_quotation, get_options, history_data, get_data_as_json, create_zip
from config import  QuotationParams

app = FastAPI(
    title="Finance API",
    version="1.0.0",
    description="Search and download data from Yahoo Finance API"
)

load_dotenv()
# Access to api key
API_KEY = os.getenv('API_KEY')

#YAHOO api docs link: https://www.financeapi.net/
# Available stock and asset symbols for the API:
# 
# - Microsoft Corporation: MSFT
# - Twitter, Inc.: TWTR
# - Bitcoin: BTC
# - Ethereum: ETH
# - Crude Oil: CL=F
# - Gold: GC=F
# - EUR/USD: EURUSD=X
# - EUR/CAD: EURCAD=X
# 
# Example symbols for requests: "TWTR,EURUSD=X,AAPL"

@app.get("/api/v1/quotes", summary="Get quotations", tags=["quotes"])
async def get_financial_quotes(
    symbols: str = Query(..., description="Stock symbols separated by commas"),
    lang: Optional[str] = Query(None, description="Response language"),
    region: Optional[str] = Query(None, description="Response region")
):
    """
    Returns Yahoo Finance quotations based on the provided symbols.
    """
    search_quote = QuotationParams(symbols=symbols, lang=lang, region=region)
    return get_quotation(search_quote)

@app.get("/api/v1/options/{symbol}", summary="Get options", tags=["options"])
async def get_stock_options(symbol: str):
    """
    Returns available options for the provided symbol.
    """
    return get_options(symbol)

@app.get("/api/v1/history/{symbol}", summary="Get historical data", tags=["history"])
async def get_history_data(symbol: str):
    """
    Returns the historical data for the provided symbol.
    """
    return history_data(symbol)

@app.get("/download", summary="Download search result as ZIP")
async def download_data(
    search_type: str = Query(..., description="Type of search: 'quotation', 'option', or 'history'"),
    symbol: str = Query(..., description="Symbol of the asset")
):
    """
    Download search results (quotation, option, or history) as a JSON file inside a ZIP.
    """
    # Get data in JSON format
    json_data = get_data_as_json(search_type, symbol)

    # Create ZIP file containing the JSON file
    json_filename = f"{symbol}_{search_type}.json"
    zip_filepath = create_zip(json_data, json_filename)

    # Return the ZIP file as a response for the user to download
    return FileResponse(zip_filepath, media_type='application/zip', filename=zip_filepath.split("/")[-1])

