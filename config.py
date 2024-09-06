
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

QUOTE_URL = "https://example.com/quote"
OPTIONS_URL = "https://example.com/options"
SPARK_URL = "https://example.com/history"
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