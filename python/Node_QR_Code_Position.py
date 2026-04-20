# Version for Node-RED integration with JSON object
'''
This program returns the QR code position from an image.
'''

import sys
import cv2
import json

def read_image(path):
    image = cv2.imread(path)
    if image is None:
        raise FileNotFoundError(f"Image not found or could not be read: {path}")
    return image


if __name__ == '__main__':             
    # print(cv2.__version__)
    # 4.6.0

    try:
#        img = read_image("C:/Users/cedric.lenoir/Documents/CtrlxNode/Plc_Test_Ui/Python/CalibrateFromQrCode.jpg")
        img = read_image("C:/Users/cedric.lenoir/Documents/GIT_Lab/aaut_rob_qr_2026/imgCalibration/OneShot_X-209_Y-58_Z-50.jpg")
        detector = cv2.QRCodeDetector()
        data, bbox, straight_qrcode = detector.detectAndDecode(img)
    except FileNotFoundError as e:
        bbox = None
        img = None

    # print("data:", data)

    if (bbox is not None) and (img is not None):
        # print("QRCode détecté")
        # print("bbox:", bbox)
        # print(bbox[0][0])
        # print(bbox[0][1])
        # print(bbox[0][3])

        angle_1 = (int(bbox[0][0][0]), int(bbox[0][0][1]))  # (x, y)
        angle_2 = (int(bbox[0][1][0]), int(bbox[0][1][1]))  # (x, y)
        angle_3 = (int(bbox[0][2][0]), int(bbox[0][2][1]))  # (x, y)
        angle_4 = (int(bbox[0][3][0]), int(bbox[0][3][1]))  # (x, y)
        color_green = (0, 255, 0)      # Green color (B, G, R)
        color_red = (0, 0, 255)      # Green color (B, G, R)
        thickness = 20           # 20 pixels thick
        cv2.line(img, angle_1, angle_2, color_green, thickness)
        cv2.line(img, angle_1, angle_4, color_red, thickness)

        # Create JSON object with pixel value
        data = {
            "pxCornerOne_x": int(bbox[0][0][0]),
            "pxCornerOne_y": int(bbox[0][0][1]),
            "pxCornerTwo_x": int(bbox[0][1][0]),
            "pxCornerTwo_y": int(bbox[0][1][1]),
            "pxCornerThree_x": int(bbox[0][3][0]),
            "pxCornerThree_y": int(bbox[0][3][1]),
            "xQR_Valid": True,
            "strMessage" : "QRCode read successfully"
        }

    else :
        if (img is not None):
            # print("Aucun QRCode détecté")
            # Create JSON object
            data = {
                "pxCornerOne_x": 0,
                "pxCornerOne_y": 0,
                "pxCornerTwo_x": 0,
                "pxCornerTwo_y": 0,
                "pxCornerThree_x": 0,
                "pxCornerThree_y": 0,
                "xQR_Valid": False,
                "strMessage" : "No QRCode detected"        
            }
        else :
            data = {
                "strMessage" : "Image not found or could not be read",
                "xQR_Valid": False        
            }


    # Convert JSON object to string and print
    # This value is sent back to the Node.js server
    print(json.dumps(data))

    if img is None:
        sys.exit(1)

    # Show image with the QR code bounding box.
    ImgResize = cv2.resize(img, (824, 600))
    imgshow = cv2.imshow('Robot QR Code postion in Pixels', ImgResize)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    sys.exit(0)
