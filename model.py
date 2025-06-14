#Importations
import cv2
import easyocr

# 1. Fonctions modulaires avec OpenCV
# 1.1. Chargement de l'image
def load_image(image_path):
    """Charge une image depuis le disque."""
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Erreur de chargement : {image_path}")
    return image

# 1.2. Prétraitement de l'image
def preprocess_image(image):
    """Convertit l'image en niveaux de gris et applique un flou bilatéral."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.bilateralFilter(gray, d=11, sigmaColor=17, sigmaSpace=17)
    return blur

# 1.3. Détection des contours
def detect_edges(blurred_image):
    """Applique Canny Edge Detection."""
    edged = cv2.Canny(blurred_image, threshold1=30, threshold2=200)
    return edged

# 1.4. Recherche de la plaque
def find_plate_contour(edged_image, original_image):
    """Trouve la forme rectangulaire la plus probable correspondant à une plaque."""
    contours, _ = cv2.findContours(edged_image.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

    for cnt in contours:
        perimeter = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.018 * perimeter, True)
        if len(approx) == 4:  # forme rectangulaire
            x, y, w, h = cv2.boundingRect(approx)
            plate = original_image[y:y + h, x:x + w]
            return plate
    return None

def extract_text_from_plate(plate_image):
    """Utilise EasyOCR pour extraire le texte d'une plaque."""
    reader = easyocr.Reader(['en', 'fr'], gpu=False)
    result = reader.readtext(plate_image)
    texts = [item[1] for item in result]
    return " ".join(texts) if texts else "Aucun texte détecté"

def full_plate_pipeline(image_path):
    """Pipeline complet de lecture et extraction OCR sur une plaque."""
    image = load_image(image_path)
    preprocessed = preprocess_image(image)
    edged = detect_edges(preprocessed)
    plate = find_plate_contour(edged, image)

    if plate is not None:
        text = extract_text_from_plate(plate)
        return text
    else:
        return "Aucune plaque détectée"
