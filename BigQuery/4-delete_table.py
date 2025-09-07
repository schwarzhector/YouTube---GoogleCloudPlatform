from google.cloud import bigquery, storage
import os

# Setear la variable de entorno
key_path = os.path.join(os.getcwd(), 'Keys', 'credencial_bigquery.json')
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_path


PROJECT_ID = ''
DATASET_ID = ""
TABLE_ID = ""

# Cliente de BigQuery
bq_client = bigquery.Client(project=PROJECT_ID)

table_ref = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"
dataset_ref = f"{PROJECT_ID}.{DATASET_ID}"

# Primero borrar la tabla
bq_client.delete_table(table_ref, not_found_ok=True)
print(f"🗑️  Tabla eliminada: {table_ref}")

# Después borrar el dataset (solo si está vacío)
try:
    bq_client.delete_dataset(dataset_ref, delete_contents=True, not_found_ok=True)
    print(f"🗑️  Dataset eliminado: {dataset_ref}")
except Exception as e:
    print(f"❌ Error eliminando dataset: {e}")