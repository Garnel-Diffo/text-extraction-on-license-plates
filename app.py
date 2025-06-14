from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename
from model import full_plate_pipeline  # on importe depuis le notebook converti en .py

app = Flask(__name__)
CORS(app) # Active le CORS pour toutes les origines

# Répertoire temporaire de sauvegarde des fichiers
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Limite la taille max des fichiers à 10 Mo
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024

# Route API pour le traitement d'une image uploadée
@app.route('/extract-text', methods=['POST'])
def extract_text():
    if 'image' not in request.files:
        return jsonify({"error": "Aucun fichier 'image' fourni"}), 400

    file = request.files['image']
    
    if file.filename == '':
        return jsonify({"error": "Nom de fichier vide"}), 400

    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    try:
        text = full_plate_pipeline(file_path)
        return jsonify({"extracted_text": text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        # Nettoyage : on peut supprimer l’image temporaire si besoin
        if os.path.exists(file_path):
            os.remove(file_path)

if __name__ == '__main__':
    app.run(debug=True)
