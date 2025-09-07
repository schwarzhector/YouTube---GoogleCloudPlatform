from google.cloud import storage
import os

# # Setear la variable de entorno
key_path = os.path.join(os.getcwd(), 'Keys', 'credencial_buckets.json')
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_path

# Inicializá el cliente
client = storage.Client()
nombre_bucket = ""

bucket = client.bucket(nombre_bucket)
blobs = list(bucket.list_blobs())
if not blobs:
    print("⚠️ El bucket está vacío.")
for blob in blobs:
    print(f"📄 Nombre: {blob.name}")
    print(f"   Tamaño: {blob.size} bytes")
    print(f"   Tipo: {blob.content_type}")
    print(f"   Última modificación: {blob.updated}")
    print("")



