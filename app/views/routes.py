# app/views/routes.py
from flask import Blueprint, request, jsonify, render_template

app = Blueprint('app', __name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    observed_views = request.files.getlist('observed_views')
    target_pose = request.form['target_pose']
    # Aquí deberás agregar la lógica para procesar las imágenes y generar vistas
    # Por ejemplo:
    # generated_views = generate_views(observed_views, target_pose)
    # return jsonify(generated_views)
    return "Esta es una ruta de ejemplo para upload"
