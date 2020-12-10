
import cv2
import numpy as np
import imutils #redimiension de pixeles


#cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap = cv2.VideoCapture('resource\dedos.mp4')
bg = None #variable de background

# COLORES PARA VISUALIZACIÓN
color_start = (204,204,0)
color_end = (204,0,204)
color_far = (255,0,0)

color_start_far = (204,204,0)
color_far_end = (204,0,204)
color_start_end = (0,255,255)

color_contorno = (0,255,0)
color_ymin = (0,130,255) # Punto más alto del contorno
color_angulo = (0,255,255)
color_d = (0,255,255)
color_fingers = (0,255,255)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == False:
        break

    #Rotar el fotograma
    frame = cv2.flip(frame,0)

    # Redimensionar la imagen para que tenga un ancho de 640
    frame = imutils.resize(frame,width=640)     
    frame = cv2.flip(frame,1)
    frameAux = frame.copy()

    if bg is not None:
        #cv2.imshow('Fondo', bg)

        '''
        Zona de Interes
        30:300 --> puntos en Y
        60:300 --> puntos en X
        '''
        ROI = frame[30:300,60:300]
        # Dibujamos rectangulo
        cv2.rectangle(frame, (60-2,30-2), (300+2,300+2), color_fingers,1)
        #grayRoi = cv2.cvtColor(ROI)
    
    #reproduccion de fotogramas
    cv2.imshow('Frame (Video)', frame)

    k = cv2.waitKey(35)
    # si presionamos i marca el fondo
    if k == ord("i"):
        bg = cv2.cvtColor(frameAux, cv2.COLOR_RGB2GRAY)

    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
