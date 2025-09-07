# pip install google-cloud-pubsub

import os
from google.cloud import pubsub_v1
import time


key_path = os.path.join(os.getcwd(), 'Keys', 'credencial_pubsub.json')

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_path

publisher = pubsub_v1.PublisherClient()

topic_path = ''

def publish_message(message_text):
    try:
        
        data = message_text.encode('utf-8')
                
        future = publisher.publish(topic_path, data)
                
        message_id = future.result()
        print(f'✅ Mensaje publicado con ID: {message_id}')
    
    except Exception as e:        
        print(f'❌ Error al publicar el mensaje: {e}')

def main():
    print("📢 Publicador de mensajes para Google Cloud Pub/Sub")
    print(f"Publicando en el tema: {topic_path}")
    print("Escribe un mensaje para enviar (o 'salir' para terminar):")

    while True:        
        message_text = input("Mensaje: ")
                
        if message_text.lower() == 'salir':
            print("👋 Cerrando el publicador...")
            break
                
        if not message_text.strip():
            print("⚠️ Por favor, escribe un mensaje válido.")
            continue
                
        publish_message(message_text)
                
        time.sleep(0.5)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)