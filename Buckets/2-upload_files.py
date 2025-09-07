from google.cloud import storage
import os

# # Setear la variable de entorno
key_path = os.path.join(os.getcwd(), 'Keys', 'credencial_buckets.json')
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_path

# Inicializá el cliente
client = storage.Client()

nombre_bucket = ""
    
bucket = client.bucket(nombre_bucket)

# Buscar todos los archivos del directorio upload
directorio_local = './Buckets/upload'
archivos = os.listdir(directorio_local)
archivos = [f for f in archivos if os.path.isfile(os.path.join(directorio_local, f))]

for nombre_archivo in archivos:    
    nombre_objetivo = "gcp-"+nombre_archivo
    ruta_absoluta = os.path.abspath(os.path.join(directorio_local, nombre_archivo))
    blob = bucket.blob(nombre_objetivo)
    blob.upload_from_filename(ruta_absoluta)
    print(f"✅ Archivo '{nombre_archivo}' subido como '{nombre_objetivo}'.")



