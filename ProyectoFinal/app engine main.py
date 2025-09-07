from flask import Flask, render_template
from google.cloud import bigquery
import os

# Inicializa la app Flask
app = Flask(__name__)

# Configura el cliente de BigQuery
client = bigquery.Client()

# ID del proyecto y tabla
PROJECT_ID = ""
DATASET = ""
TABLE = ""

@app.route('/')
def get_tickers():
    # Consulta para obtener tickers únicos
    query = f"""
        SELECT DISTINCT ticker
        FROM `{PROJECT_ID}.{DATASET}.{TABLE}`
        ORDER BY ticker
    """
    query_job = client.query(query)
    tickers = [row.ticker for row in query_job]

    # Renderiza la plantilla con los tickers
    return render_template('index.html', tickers=tickers)

if __name__ == '__main__':
    # Solo para pruebas locales
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))