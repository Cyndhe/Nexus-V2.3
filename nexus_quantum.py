import numpy as np
import pandas as pd
import requests

# Funciones de Análisis
def fetch_live_data(match_id):
    url = f"https://api.sportsdata.io/v4/soccer/scores/json/GamesByDate/{match_id}"
    response = requests.get(url)
    return response.json()

def main():
    print("Iniciando análisis...")

if __name__ == "__main__":
    main()
