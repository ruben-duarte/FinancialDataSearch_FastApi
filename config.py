
from dataclasses import dataclass
from typing import Optional
import os
from dotenv import load_dotenv

load_dotenv()
# Access to api key
API_KEY = os.getenv('API_KEY')

# Config urls
BASE_URL = "https://yfapi.net/v6/finance"

header = {
    'X-API-KEY': API_KEY,
    'User-Agent': 'Mozilla/5.0'
}

QUOTE_URL = BASE_URL + "/quote"
OPTIONS_URL = BASE_URL + "/options"
SPARK_URL = BASE_URL + "/spark"

header = {
    "Authorization": "Bearer your-api-key",
    "Content-Type": "application/json"
}

# Data model for quotation parameters
@dataclass
class QuotationParams:
    symbols: str
    lang: Optional[str] = None
    region: Optional[str] = None