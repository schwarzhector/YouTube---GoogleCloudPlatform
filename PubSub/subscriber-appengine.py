import os
from google.cloud import pubsub_v1
from concurrent.futures import TimeoutError


key_path = os.path.join(os.getcwd(), 'Keys', 'credencial_appenginesubscriber.json')
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_path

subscriber = pubsub_v1.SubscriberClient()

subscription_path = ''


def callback(message):
    
    print(f'Mensaje recibido: {message}')
        
    print(f'Data: {message.data.decode("utf-8")}')
        
    message.ack()


streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)


print(f'Buscando mensajes en... {subscription_path}')


with subscriber:
    try:        
        streaming_pull_future.result()
    
    
    except KeyboardInterrupt:
        
        print("Deteniendo la ejecución...")
                
        streaming_pull_future.cancel()
                
        streaming_pull_future.result()
        
    except TimeoutError:
        
        print("Subscription timed out.")
                
        streaming_pull_future.cancel()
                
        streaming_pull_future.result()