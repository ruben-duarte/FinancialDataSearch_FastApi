import json
import zipfile
import os
from pathlib import Path
from fastapi import HTTPException
import datetime
import json
import requests
from dataclasses import asdict
import time
import os
from pathlib import Path
from config import QUOTE_URL, OPTIONS_URL, SPARK_URL, QuotationParams,header


# Function to get quotations
def get_quotation(search: QuotationParams):
    search_params = asdict(search)
    response = requests.get(QUOTE_URL, params=search_params, headers=header)
    
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, 
                            detail="Error while searching the quotaion")
    
    return response.json()

# Function to get stock options
def get_options(symbol: str):
    d = '22/03/2024'
    timestamp = int(time.mktime(datetime.datetime.strptime(d, '%d/%m/%Y').timetuple()))

    url = f"{OPTIONS_URL}/{symbol}?date={timestamp}"
    response = requests.get(url, headers=header)
    
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, 
                            detail="Error while getting options")

    return response.json()

# Function to get historical stock data
def history_data(symbol: str):
    interval = '1d'
    range = '5d'
    url = f"{SPARK_URL}?interval={interval}&range={range}&symbols={symbol}"
    
    response = requests.get(url, headers=header)
    
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, 
                            detail="Error while getting historical data")
    
    return response.json()


# Temporary directory to save zip files
ZIP_DIR = "temp_zips"

# Ensure the directory exists
Path(ZIP_DIR).mkdir(parents=True, exist_ok=True)

# Function to get data in JSON format
def get_data_as_json(search_type: str, symbol: str):
    if search_type == "quotation":
        data = get_quotation(QuotationParams(symbols=symbol))
    elif search_type == "option":
        data = get_options(symbol)
    elif search_type == "history":
        data = history_data(symbol)
    else:
        raise HTTPException(status_code=400, detail="Invalid search type")

    # Convert data to JSON format
    return json.dumps(data, indent=4)

# Function to create a ZIP file containing the JSON data
def create_zip(json_data, json_filename):
    json_filepath = os.path.join(ZIP_DIR, json_filename)
    zip_filename = f"{json_filename}.zip"
    zip_filepath = os.path.join(ZIP_DIR, zip_filename)

    # Write JSON data to a file
    with open(json_filepath, "w") as json_file:
        json_file.write(json_data)

    # Create a ZIP file containing the JSON file
    with zipfile.ZipFile(zip_filepath, 'w') as zip_file:
        zip_file.write(json_filepath, arcname=json_filename)

    # Delete the temporary JSON file after creating the ZIP
    os.remove(json_filepath)

    return zip_filepath
