from google.cloud import storage
from google.cloud import pubsub_v1
from io import BytesIO
import pandas as pd
import json
import time

def send_data(request):

    def publisher(stock_df):
        publisher = pubsub_v1.PublisherClient()
        topic_path = ''                               
        for _, row in stock_df.iterrows():                        
            try:        
                print("")
                mensaje = row.to_dict()
                data = json.dumps(mensaje).encode("utf-8")
                time.sleep(2)              
                future = publisher.publish(topic_path, data)                           
            except Exception as e:    
                print(f"❌ Error: {str(e)}")                    


    def data_from_bucket():        
        client = storage.Client()        
        nombre_bucket = "archivos_crudos"        
        try:
            
            bucket = client.bucket(nombre_bucket)
                        
            print("📋 Archivos en el bucket:")
            blobs = bucket.list_blobs()
            archivos = [blob.name for blob in blobs]
            
            if not archivos:
                print("⚠️ No se encontraron archivos en el bucket.")
            else:
                for nombre_objeto in archivos:
                    print(f" - {nombre_objeto}")
                    ticker = nombre_objeto.split(".")[0]
                    blob = bucket.blob(nombre_objeto)
                    with blob.open("r") as file:
                        stock_df = pd.read_csv(file)
                        stock_df["ticker"] = ticker
                        publisher(stock_df)                                   
        except Exception as e:
            print("ERROR - data_from_bucket")
            print(e)
    try:
        data_from_bucket()
        return "Funcionó!", 200
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        
    
