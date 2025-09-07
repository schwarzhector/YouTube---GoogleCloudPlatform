from google.cloud import bigquery, storage
import os


# Setear la variable de entorno
key_path = os.path.join(os.getcwd(), 'Keys', 'credencial_bigquery.json')
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_path

PROJECT_ID = ''
DATASET_ID = ""
TABLE_ID = ""
DEST_CSV_LOCAL = ""


# Cliente de BigQuery
bq_client = bigquery.Client(project=PROJECT_ID)

query = f"""
SELECT cuenca, areapermisoconcesion, yacimiento, tipo_reservorio 
FROM `{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}`
where anio = 2025
"""

try:
    query_job = bq_client.query(query)
    results = query_job.result()

    with open(DEST_CSV_LOCAL, "w", encoding="utf-8") as f:
        f.write("cuenca,areapermisoconcesion,yacimiento,tipo_reservorio\n")
        for row in results:
            f.write(f"{row.cuenca},{row.areapermisoconcesion},{row.yacimiento},{row.tipo_reservorio}\n")
    print(f"✅ Resultado guardado en: {DEST_CSV_LOCAL}")
except Exception as e:
    print(f"❌ Error durante la consulta o guardado del CSV: {e}")