import os
from dotenv import load_dotenv
from binance.um_futures import UMFutures

# Charger les variables d'environnement depuis le fichier .env
load_dotenv(dotenv_path="./config/.env")

# Utiliser les variables d'environnement
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")

um_futures_client = UMFutures(api_key, api_secret)

# Get account information
print(um_futures_client.account())
