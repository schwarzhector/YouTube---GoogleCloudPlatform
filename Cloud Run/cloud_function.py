def upload_data(request):	
	from google.cloud import bigquery		

	PROJECT_ID = ''
	DATASET_ID = ""
	TABLE_ID = ""
	BUCKET_NAME = ''
	SOURCE_FILE = ''
	GCS_URI = f"gs://{BUCKET_NAME}/{SOURCE_FILE}"
	LOCATION = ""

	# Cliente de BigQuery
	bq_client = bigquery.Client(project=PROJECT_ID)

	job_config = bigquery.LoadJobConfig(
			source_format=bigquery.SourceFormat.CSV,
			skip_leading_rows=1,
			autodetect=False,
			write_disposition="WRITE_TRUNCATE",
			encoding="UTF-8"
		)
	try:
		load_job = bq_client.load_table_from_uri(
				GCS_URI, f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}", job_config=job_config, location=LOCATION
			)
		load_job.result()
		print("✅ Datos cargados desde el bucket")
		return "Todo OK", 200
	except Exception as e:
		print(f"❌ Error al cargar datos: {e}")
		return "Error", 400
