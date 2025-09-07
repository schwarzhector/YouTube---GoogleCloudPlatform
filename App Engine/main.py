from flask import Flask, render_template_string, request, redirect, url_for, flash
import os
from google.cloud import pubsub_v1

app = Flask(__name__)
app.secret_key = 'supersecretkey'

publisher = pubsub_v1.PublisherClient()
topic_path = ''

HTML_TEMPLATE = """
<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <title>Pub/Sub Publisher</title>
  <style>
    body { font-family: Arial, sans-serif; max-width: 600px; margin: 2rem auto; }
    label { font-weight: bold; }
    input[type=text] { width: 100%; padding: 0.5rem; margin-top: 0.5rem; margin-bottom: 1rem; font-size: 1rem; }
    button { background-color: #007bff; color: white; padding: 0.6rem 1.2rem; border: none; cursor: pointer; font-size: 1rem; }
    button:hover { background-color: #0056b3; }
    .message { margin: 1rem 0; padding: 1rem; border-radius: 5px; }
    .success { background-color: #d4edda; color: #155724; }
    .error { background-color: #f8d7da; color: #721c24; }
  </style>
</head>
<body>
  <h1>Publicador de mensajes Pub/Sub</h1>
  {% with messages = get_flashed_messages(with_categories=true) %}
    {% if messages %}
      {% for category, message in messages %}
        <div class="message {{ category }}">{{ message }}</div>
      {% endfor %}
    {% endif %}
  {% endwith %}
  <form method="post" action="{{ url_for('publish') }}">
    <label for="message">Ingrese texto a publicar:</label>
    <input type="text" id="message" name="message" required autocomplete="off" autofocus>
    <button type="submit">Publicar</button>
  </form>
</body>
</html>
"""

@app.route('/', methods=['GET'])
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/', methods=['POST'])
def publish():
    message_text = request.form.get('message', '').strip()
    if not message_text:
        flash('⚠️ Por favor, escribe un mensaje válido.', 'error')
        return redirect(url_for('index'))

    try:
        data = message_text.encode('utf-8')
        future = publisher.publish(topic_path, data)
        message_id = future.result()
        flash(f'✅ Mensaje publicado con ID: {message_id}', 'success')
    except Exception as e:
        flash(f'❌ Error al publicar el mensaje: {e}', 'error')

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
