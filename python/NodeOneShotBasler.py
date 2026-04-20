# Version for Node-RED integration with JSON object
'''
This program returns the QR code offset from the ideal QR code position. See constants below.
'''

# Pseudo constant for camera calibration
# When the QR code is centered in this circle with sensor U300 at 250 mm of the plate.
# We suppose the gripper is centererd on Nest Number 6
DEFAULT_QR_CODE_CIRCLE_X_CENTER = 2417
DEFAULT_QR_CODE_CIRCLE_Y_CENTER = 618   
DEFAULT_QR_CODE_CIRCLE_RADIUS = 598
DEFAULT_QR_CODE_CIRCLE_PIXEL_PER_MM = 23.3  # 8 pixels per mm


from pypylon import pylon
from datetime import datetime
import sys
import cv2
import json
import math
import numpy as np
from qreader import QReader

camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())

# Grabing Continusely (video) with minimal delay
camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
camera.ExposureAuto.SetValue("Continuous") # TODO : tester si le paramétre est bien changé !
converter = pylon.ImageFormatConverter()

# converting to opencv bgr format
converter.OutputPixelFormat = pylon.PixelType_BGR8packed
converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned

def getOnePicture():
    img=None
    grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)

    if grabResult.GrabSucceeded():
        # Access the image data
        image = converter.Convert(grabResult)
        img = image.GetArray()

    grabResult.Release()

    return img

def read_image(path):
    image = cv2.imread(path)
    if image is None:
        raise FileNotFoundError(f"Image not found or could not be read: {path}")
    return image

# Calculate the orientation in degrees
def calculate_orientation(polygon):
    # Get the first two points
    p1 = polygon[0]
    p2 = polygon[1]
    
    # Calculate the angle in radians
    angle_rad = np.arctan2(p2[1] - p1[1], p2[0] - p1[0])
    
    # Convert to degrees
    angle_deg = np.degrees(angle_rad)
    
    return angle_deg

if __name__ == "__main__":

    # One Shot
    grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)

    if grabResult.GrabSucceeded():
            # Access the image data
            image = converter.Convert(grabResult)
            img = image.GetArray()
            cv2.namedWindow('FromRobot One Shot', cv2.WINDOW_NORMAL)

            # Get image size
            # print(f"Image Width is {img.shape[1]}")
            # print(f"Image Height is {img.shape[0]}")

            # Get time
            now = datetime.now()
            # print(f"Today's Time is: , {now.hour}_{now.minute}_{now.second}")
            
            # Using resizeWindow() 
            cv2.resizeWindow("FromRobot One Shot", 824, 600) 

            # Create a QReader instance
            # print("Image read successfully.")
            # Create a QReader instance
            myReader = QReader()
        
            qrInfo = myReader.detect_and_decode(image=img,  return_detections=True)
            # print("QR Info:", qrInfo)

            if qrInfo :
                # Use the detect_and_decode function to get the decoded QR data
                
                # print("QR Code detected.")
                # print("QR Info:", qrInfo)
                # Accessing 'cxcy'
                cxcy_value = qrInfo[1][0]['cxcy']
                # print("Center:", cxcy_value)
                # Get angle aroud Z axis
                polygone_quad = qrInfo[1][0]['padded_quad_xy']
                # print("Polygon pad:", polygone_quad)
                orientation = calculate_orientation(polygone_quad)
                # print("Orientation (degrees):", orientation)

                # Print a circle on the image, centered at center of the circle.       
                # cv2.circle(img, center=(2048, 1500), radius=598, color=(0, 255, 0), thickness=20) 
                qrCode_X_center = cxcy_value[0]
                qrCode_Y_center = cxcy_value[1] 


                cv2.circle(img, center=(DEFAULT_QR_CODE_CIRCLE_X_CENTER, DEFAULT_QR_CODE_CIRCLE_Y_CENTER), radius=DEFAULT_QR_CODE_CIRCLE_RADIUS, color=(0, 255, 0), thickness=20) 

                # Build JSON object
                qrJson = {
                    "pxCenter_x": int(qrCode_X_center-DEFAULT_QR_CODE_CIRCLE_X_CENTER),
                    "pxCenter_y": int(qrCode_Y_center-DEFAULT_QR_CODE_CIRCLE_Y_CENTER),
                    "mmCenter_x": int((qrCode_X_center-DEFAULT_QR_CODE_CIRCLE_X_CENTER)/DEFAULT_QR_CODE_CIRCLE_PIXEL_PER_MM*100)/100,
                    "mmCenter_y": int((qrCode_Y_center-DEFAULT_QR_CODE_CIRCLE_Y_CENTER)/DEFAULT_QR_CODE_CIRCLE_PIXEL_PER_MM*100)/100,
                    "z_angle": int(orientation),
                    "xQR_Valid": True,
                    "strMessage" : "QRCode read successfully"
                } 

            else:
                if (img is not None):
                    # print("Aucun QRCode détecté")
                    # Create JSON object
                    qrJson = {
                        "pxCenter_x": 0,
                        "pxCenter_y": 0,
                        "mmCenter_x": 0,
                        "mmCenter_y": 0,
                        "z_angle": 0,
                        "xQR_Valid": False,
                        "strMessage" : "No QRCode detected"        
                    }
                else :
                    qrJson = {
                        "strMessage" : "Image not found or could not be read",
                        "xQR_Valid": False        
                    }
                qrInfo = None


            # Show image with the QR code bounding box.
            # Convert JSON object to string and print
            # This value is sent back to the Node.js server
            print(json.dumps(qrJson))

            # Show the image on the screen
            cv2.imshow('FromRobot One Shot', img)

            # Using cv2.imwrite() method
            # Saving the image
            filename = f"C:/Users/cedric.lenoir/Documents/AutRob/imgRobot/OneShot_{now.hour}_{now.minute}_{now.second}.jpg"
            cv2.imwrite(filename, img)
            # print(f"Written image in {filename}")

            # Wait until the user closes the window
            while True:
                # Wait for 1 millisecond for a key event
                key = cv2.waitKey(1) & 0xFF
    
                # Check if the window is still open
                if cv2.getWindowProperty('FromRobot One Shot', cv2.WND_PROP_VISIBLE) < 1:
                    break         
        
    # Releasing the resource
    camera.StopGrabbing()

    cv2.destroyAllWindows()


