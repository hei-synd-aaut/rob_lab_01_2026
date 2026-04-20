import cv2
import numpy as np




Avec OpenCV eb Python, la détection de QR code ne fonctionne pas correctement si l'image est trop lumineuse, que faire ?

def detect_qr_code(image_path):
    # Read the image
    image = cv2.imread(image_path)
    
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply adaptive thresholding
    thresh = cv2.adaptiveThreshold(
        gray, 255, 
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
        cv2.THRESH_BINARY, 11, 2
    )
    
    # Optional: Apply histogram equalization
    # clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    # gray = clahe.apply(gray)
    
    # Initialize QR Code detector
    qr_detector = cv2.QRCodeDetector()
    
    # Detect and decode
    data, bbox, straight_qrcode = qr_detector.detectAndDecode(thresh)
    
    if bbox is not None:
        print(f"QR Code data: {data}")
        # Draw the bounding box
        bbox = bbox.astype(int)
        cv2.polylines(image, [bbox], True, (0,255,0), 2)
        return True, data, image
    
    return False, None, image

# Example usage
image_path = "path_to_your_image.jpg"
success, data, result_image = detect_qr_code(image_path)

