import base64
import json
from google.cloud import bigquery
from datetime import datetime


client = bigquery.Client()

def pubsub_handler(request):
    try:
        print("<----- pubsub_handler ----->")
        if request:            
            envelope = request.get_json(silent=True)
            if not envelope:
                print("No data")

            pubsub_message = envelope.get("message")
            if not pubsub_message:
                print("No message field")

            data_b64 = pubsub_message.get("data")
            if data_b64:
                try:
                    decoded = base64.b64decode(data_b64).decode("utf-8")                                            
                    data_json = json.loads(decoded)                                                                                                                                      
                    filtered_data = {
                        "Close": data_json["Close"],
                        "Date": data_json["Date"],
                        "ticker": data_json["ticker"]
                    }
                    print("FILTERED DATA")
                    print(filtered_data)
                
                    # Validar y convertir los datos                
                    close_value = float(data_json["Close"])
                    if close_value < 0:
                        print("El valor de cierre no puede ser menor a cero")

                    date_str = data_json["Date"]                    
                    date_value = datetime.strptime(date_str, "%d/%m/%Y").strftime("%Y-%m-%d")                    
                    

                    ticker_value = data_json["ticker"]
                    if not ticker_value or not isinstance(ticker_value, str):
                        print("Invalid ticker value: %s", ticker_value)                    

                    filtered_data = {
                        "Close": close_value,
                        "Date": date_value,
                        "ticker": ticker_value
                    }
                    # BigQuery
                    print("<--- BigQuery --->")
                    project_id = ""
                    dataset_id = ""
                    table_id = ""
                    
                    table_ref = f"{project_id}.{dataset_id}.{table_id}"
                    
                    rows_to_insert = [filtered_data]
                    errors = client.insert_rows_json(table_ref, rows_to_insert)  
                    if errors == []:
                        print("✅ Insert correcto en BigQuery")
                    else:
                        print("❌ Error al insertar en BigQuery:")
                        for err in errors:
                            print(err)

                    print("<--- /BigQuery --->")
                except Exception as e:
                    print(f"❌ Error: {str(e)}")        
            
        return "OK", 200

    except:
        return "Error", 400
