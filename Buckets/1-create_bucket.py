# pip install google-cloud-storage
from google.cloud import storage
import os

# # Setear la variable de entorno
key_path = os.path.join(os.getcwd(), 'Keys', 'credencial_buckets.json')
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_path

# Inicializá el cliente
client = storage.Client()

clase_almacenamiento = "STANDARD"
ubicacion  = ""
nombre_bucket = ""

try:
    bucket = client.bucket(nombre_bucket)
    bucket.storage_class = clase_almacenamiento
    #bucket.location = ubicacion esto está deprecated
    # esta es la forma actualizada para crearlo:
    bucket = client.create_bucket(bucket, location=ubicacion)
    print(f"✅ Bucket '{bucket.name}' creado en {bucket.location}.")
except Exception as e:
    print(e)

