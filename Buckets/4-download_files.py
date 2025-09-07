import os
from google.cloud import storage

# Setear la variable de entorno
key_path = os.path.join(os.getcwd(), 'Keys', 'credencial_buckets.json')
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_path

# Inicializar el cliente
client = storage.Client()

# Configuración
nombre_bucket = ""
directorio_destino = os.path.join(os.getcwd(), "Buckets", "download")

# Crear el directorio de destino si no existe
os.makedirs(directorio_destino, exist_ok=True)

try:
    # Acceder al bucket
    bucket = client.bucket(nombre_bucket)
    
    # Listar todos los objetos en el bucket
    print("📋 Archivos en el bucket:")
    blobs = bucket.list_blobs()
    archivos = [blob.name for blob in blobs]
    
    if not archivos:
        print("⚠️ No se encontraron archivos en el bucket.")
    else:
        for nombre_objeto in archivos:
            print(f" - {nombre_objeto}")
            
            # Construir la ruta de destino
            ruta_destino = os.path.join(directorio_destino, os.path.basename(nombre_objeto))
            
            # Descargar el archivo
            blob = bucket.blob(nombre_objeto)
            blob.download_to_filename(ruta_destino)
            print(f"✅ Archivo '{nombre_objeto}' descargado a '{ruta_destino}'.")
            
except Exception as e:
    print(f"❌ Error: {str(e)}")