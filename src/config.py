"""Configuration file to load and retrieve environment variables"""

import os
from dotenv import load_dotenv

load_dotenv()  # Load .env once, at import time

ACCESS_KEY = os.getenv("ACCESS_KEY")
