# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 21:26:24 2020

@author: aadit
"""


import cv2
from matplotlib import pyplot as plt
import easyocr
import requests
reader = easyocr.Reader(['en'])

car_cascade = cv2.CascadeClassifier('cars.xml')
r = requests.get(url = "https://us-central1-smart-car-parking-system-b6c28.cloudfunctions.net/number")
data = r.json()
print(data)

vid = cv2.VideoCapture(0) 
  
while(True): 
      
    # Capture the video frame 
    # by frame 
    ret, frame = vid.read() 
    # Display the resulting frame 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cars = car_cascade.detectMultiScale(gray, 1.1, 1)

    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 2)
        text = (reader.readtext(frame, detail = 0))
        if text != []:
            print(text[0])
            a = str(text[0])
            try:
                print(data[a])
            except:
                print('Invalid number')
        cars = cars + 1

    #plt.figure(figsize=(10,20))
    plt.imshow(frame)
    cv2.imshow('frame', frame) 
    # the 'q' button is set as the 
    # quitting button you may use any 
    # desired button of your choice 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
  
# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv2.destroyAllWindows() 