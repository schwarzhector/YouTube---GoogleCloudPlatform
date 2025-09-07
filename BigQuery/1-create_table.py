# pip install google-cloud-bigquery
from google.cloud import bigquery
import os

# Setear la variable de entorno
key_path = os.path.join(os.getcwd(), 'Keys', 'credencial_bigquery.json')
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_path


PROJECT_ID = ''
DATASET_ID = ""
TABLE_ID = ""
LOCATION = ""

# Cliente de BigQuery
bq_client = bigquery.Client(project=PROJECT_ID)

dataset_ref = bigquery.Dataset(f"{PROJECT_ID}.{DATASET_ID}")
dataset_ref.location = LOCATION
try:
    bq_client.get_dataset(dataset_ref)
    print(f"ℹ️ Dataset ya existe: {DATASET_ID}")
except Exception:
    bq_client.create_dataset(dataset_ref)
    print(f"✅ Dataset creado: {DATASET_ID}")

schema = [
    bigquery.SchemaField("id_base_fractura_adjiv", "INTEGER"),
    bigquery.SchemaField("idpozo", "STRING"),
    bigquery.SchemaField("sigla", "STRING"),
    bigquery.SchemaField("cuenca", "STRING"),
    bigquery.SchemaField("areapermisoconcesion", "STRING"),
    bigquery.SchemaField("yacimiento", "STRING"),
    bigquery.SchemaField("formacion_productiva", "STRING"),
    bigquery.SchemaField("tipo_reservorio", "STRING"),
    bigquery.SchemaField("subtipo_reservorio", "STRING"),
    bigquery.SchemaField("longitud_rama_horizontal_m", "FLOAT"),
    bigquery.SchemaField("cantidad_fracturas", "INTEGER"),
    bigquery.SchemaField("tipo_terminacion", "STRING"),
    bigquery.SchemaField("arena_bombeada_nacional_tn", "FLOAT"),
    bigquery.SchemaField("arena_bombeada_importada_tn", "FLOAT"),
    bigquery.SchemaField("agua_inyectada_m3", "FLOAT"),
    bigquery.SchemaField("co2_inyectado_m3", "FLOAT"),
    bigquery.SchemaField("presion_maxima_psi", "FLOAT"),
    bigquery.SchemaField("potencia_equipos_fractura_hp", "FLOAT"),
    bigquery.SchemaField("fecha_inicio_fractura", "DATETIME"),
    bigquery.SchemaField("fecha_fin_fractura", "DATETIME"),
    bigquery.SchemaField("fecha_data", "DATETIME"),
    bigquery.SchemaField("anio_if", "INTEGER"),
    bigquery.SchemaField("mes_if", "INTEGER"),
    bigquery.SchemaField("anio_ff", "INTEGER"),
    bigquery.SchemaField("mes_ff", "INTEGER"),
    bigquery.SchemaField("anio_carga", "INTEGER"),
    bigquery.SchemaField("mes_carga", "INTEGER"),
    bigquery.SchemaField("empresa_informante", "STRING"),
    bigquery.SchemaField("mes", "INTEGER"),
    bigquery.SchemaField("anio", "INTEGER")
]

table_ref = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"
table = bigquery.Table(table_ref, schema=schema)


try:
    bq_client.create_table(table)
    print(f"✅ Tabla creada: {table_ref}")
except Exception as e:
    print(f"⚠️ Error o ya existe: {e}")