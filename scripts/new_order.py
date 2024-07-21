import os, json, sys, logging
from dotenv import load_dotenv
from binance.um_futures import UMFutures
from binance.lib.utils import config_logging
from binance.error import ClientError

# Charger les variables d'environnement depuis le fichier .env
load_dotenv(dotenv_path="./config/.env")

# Utiliser les variables d'environnement
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")

config_logging(logging, logging.DEBUG)

um_futures_client = UMFutures(api_key, api_secret)

try:
    response = um_futures_client.new_order(
        symbol=sys.argv[1],
        side=sys.argv[2],
        type="MARKET",
        quantity=(sys.argv[3]),
    )
    print(json.dumps(response))
except ClientError as error:
    logging.error(
        "Found error. status: {}, error code: {}, error message: {}".format(
            error.status_code, error.error_code, error.error_message
        )
    )
