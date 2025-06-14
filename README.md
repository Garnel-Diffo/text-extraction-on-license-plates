
# Projet Groupe 3 : Extraction des informations de la Plaques d’Immatriculation

## Description du Projet

Ce projet a pour but de développer une intelligence artificielle capable de détecter et d’extraire automatiquement le texte des plaques d’immatriculation à partir d’une image. Il repose sur un pipeline combinant :

- **OpenCV** pour le traitement et la détection des zones de plaques,
- **EasyOCR** pour l’extraction du texte,
- **Flask** pour exposer le traitement sous forme d’API REST,
- Une **interface HTML simple et dynamique** permettant d’envoyer une image et d’afficher le texte extrait.

Ce projet est **local, léger et prêt pour la production ou l’extension en web/mobile**.

---

## Fonctionnalités Implémentées

1. **Pipeline OCR robuste**
   - Lecture et prétraitement d’image
   - Détection des bords
   - Isolation de la plaque
   - Lecture du texte via EasyOCR

2. **API Flask opérationnelle**
   - Endpoint : `POST /extract-text`
   - Reçoit une image, renvoie le texte détecté

3. **Interface HTML moderne**
   - Upload d’image
   - Animation de chargement
   - Affichage du texte et de l’image traitée

---

## Installation et Utilisation

### Prérequis

- Python 3.8+
- pip (gestionnaire de paquets Python)

### Étapes

1. **Cloner le dépôt**

```bash
git clone https://github.com/Garnel-Diffo/text-extraction-on-license-plates.git
cd text-extraction-on-license-plates
```

2. **Créer un environnement virtuel (optionnel)**

```bash
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate       # Windows
```

3. **Installer les dépendances**

```bash
pip install -r requirements.txt
```

> Assurez-vous d’avoir une connexion internet pour permettre à EasyOCR de télécharger les poids de son modèle.

4. **Lancer l’API Flask**

```bash
python app.py
```

L'API sera disponible à l'adresse : [http://localhost:5000](http://localhost:5000)

5. **Lancer l'interface utilisateur**

Ouvrir simplement le fichier `index.html` dans votre navigateur.

---

## Exemple d’appel API

### Requête avec `curl`

```bash
curl -X POST http://localhost:5000/extract-text \
     -F "image=@data/plate1.png"
```

### Réponse attendue

```json
{
  "extracted_text": "CMR LT665CD"
}
```

---

## Pipeline Technique (model.py)

```python
def full_plate_pipeline(image_path):
    image = load_image(image_path)
    preprocessed = preprocess_image(image)
    edged = detect_edges(preprocessed)
    plate = find_plate_contour(edged, image)
    if plate is not None:
        return extract_text_from_plate(plate)
    return "Aucune plaque détectée"
```

Toutes les fonctions appelées sont encapsulées dans `model.py`, issu de la conversion de `model.ipynb`.

---

## Structure des Fichiers

```
text-extraction-on-license-plates/
│
├── app.py                  # Serveur Flask pour traitement de l'image
├── model.py                # Pipeline complète (OpenCV + EasyOCR)
├── model.ipynb             # Notebook d'origine (pour développement/test)
├── data/                   # Dossier contenant les images
├── index.html              # Interface web utilisateur
├── uploads/                # Dossier temporaire pour images uploadées
├── requirements.txt        # Fichier des dépendances
└── README.md               # Documentation du projet
```

---

## requirements.txt

```txt
flask==3.1.0
flask-cors==5.0.1
opencv-python==4.5.5.62
easyocr
numpy==1.24.0
matplotlib==3.6.3
werkzeug==3.1.3
```

---

## Prochaines Améliorations

- Décomposer complètement le resultat en region par exemple
- Améliorer les interfaces
- Dockerisation de l'application
- Export vers API REST cloud avec authentification

---

## Contributeurs

- DIFFO KENNE GARNEL  
- GOUFAN A ETON ARMEL
- MBIDA NGUELE LOIC
- NGUI FRANCK STEVE
- TEZEMBON DJOUFO LOIC

---

## Licence

Ce projet est sous licence MIT – voir le fichier [LICENSE](LICENSE) pour plus de détails.

---


