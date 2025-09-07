import os
from google.cloud import storage
from google.cloud import exceptions



# Setear la variable de entorno
key_path = os.path.join(os.getcwd(), 'Keys', 'credencial_buckets.json')
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_path

# Inicializar el cliente
client = storage.Client()

# Nombre del bucket
nombre_bucket = ""

try:
    # Acceder al bucket
    bucket = client.bucket(nombre_bucket)
    
    # Verificar si el bucket existe
    if not bucket.exists():
        print(f"⚠️ El bucket '{nombre_bucket}' no existe.")
    else:
        # Listar y eliminar todos los objetos en el bucket
        blobs = bucket.list_blobs()
        for blob in blobs:
            print(f"Eliminando archivo '{blob.name}'...")
            blob.delete()
        
        # Eliminar el bucket
        bucket.delete()
        print(f"✅ Bucket '{nombre_bucket}' eliminado correctamente.")
except exceptions.NotFound:
    print(f"⚠️ El bucket '{nombre_bucket}' no se encontró.")
except exceptions.Conflict as e:
    print(f"❌ Error: El bucket no está vacío o hay un conflicto: {str(e)}")
except Exception as e:
    print(f"❌ Error al eliminar el bucket: {str(e)}")