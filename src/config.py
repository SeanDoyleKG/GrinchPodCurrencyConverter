from dotenv import load_dotenv
import os

load_dotenv()  # Load .env once, at import time

ACCESS_KEY = os.getenv("ACCESS_KEY")
