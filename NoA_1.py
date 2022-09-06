
from this import d
import requests
from io import BytesIO
import cv2 as cv
import numpy as np
import random as rng
from pythonosc import udp_client
import time
rng.seed(12345)
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
flag1 = True
flagcheck = False
vid = cv.VideoCapture(0)
counter = 0
scounter = 0
#highest values
highestvalues = np.zeros(100)
highestvaluescount = 0
#index for rows
rowtemp = np.zeros(2501)
indexrow = 0
indexrowy = 0
indexrange = 0
indexrangeoffset = 50
#variables
tempbiggest = 0
savebiggest = 0
indexforsaving = 0
#indexfothighestvalues
indexfinalmin = 0
indexfinalmax = 0
indexrowmaxmsp = 0
rowhighest = np.zeros(10)
#rowscount
rowscountmin = 0
rowscountmax = 10
highrowscount = 0
###################
correctindex = 1

#########
is_all_zero = False
svalues = []
firstime = True
indexonetimesend = False
tempfinal = 0
savefinal = 0
indexreset = 0
counteroffset = 0
values = []
client = udp_client.SimpleUDPClient('127.0.0.1', 8000)
superclient = udp_client.SimpleUDPClient('127.0.0.1', 9000)
picturename = "SequencerGrid/0"
sending = False
listpicture = []
saveimage = False
counterrow = 0
while(True):
      
    # Capture the video frame
    # by frame
  while(flag1 == True):
    ret, frame = vid.read()
    gray = frame.copy()
    gray = cv.cvtColor(gray, cv.COLOR_BGR2GRAY)
    # Display the resulting fr
   

        
    cv_resized_img = cv.resize(gray, (500, 500), interpolation = cv.INTER_AREA)
    src_gray = cv_resized_img.copy()
    src_gray = cv.blur(src_gray, (3,3))
    threshold = 25
      # Detect edges using Canny
    canny_output = cv.Canny(src_gray, threshold, threshold * 2)
      # Find contours
    contours, hierarchy = cv.findContours(canny_output, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
      # Draw contours
    drawing = np.zeros((canny_output.shape[0], canny_output.shape[1], 3), dtype=np.uint8)
    for i in range(len(contours)):
      color = (rng.randint(0,256), rng.randint(0,256), rng.randint(0,256))
      cv.drawContours(drawing, contours, i, color, 2, cv.LINE_8, hierarchy, 0)
    
    
    faces = face_cascade.detectMultiScale(cv_resized_img, 1.5, 4, minSize = [1,1])
    for (x, y, w, h) in faces:
      cv.rectangle(cv_resized_img, (x, y), (x+w, y+h), (255, 0, 0), 2)
      flag1 = False
      flagcheck = True
      saveimage = True
    cv.imshow('face', cv_resized_img)
      # Show in a window
    cv.imshow('Contours', drawing)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
      break
  while(flagcheck == True):
    if (saveimage == True):
        #write image to harddsik
      temp2 = drawing.copy()
        #convert to grayscale
      temp2 = cv.cvtColor(temp2, cv.COLOR_RGB2GRAY)	
        #write
      cv.imwrite(str(picturename) + '.jpg', temp2) 
        #prepare list for osc
      listpicture.append("0"+ '.jpg')
        #send list to osc
      client.send_message('/path',listpicture)
        #clear list
      listpicture.clear()
        #increment 
        #exit if
      saveimage = False
      #iterate over 50 x 50 = 2500 square 
    for x2 in range(50):
      for y2 in range(50):
        #look for biggest value inside first square
        rowtemp[counterrow] = (temp2[indexrowy + y2][indexrow + x2])
        counterrow += 1
    counterrow = 0
    
    #save the biggest value into the array of size 100
    #get the mean value of n array
    rowhighest[counter] = np.mean(rowtemp)
    rowtemp = np.zeros(rowtemp.size)
    indexrowy += 50
    #counter from 0 to 10
    

    highestvalues[highrowscount] += rowhighest[counter]
    counter +=1
    highrowscount += 1
    #if indexonetimesend == True:
    #  highestvalues[highrowscount] += np.amax(rowtemp)
    #  rowtemp = np.zeros(rowtemp.size)
    #  is_all_zero = np.all((highestvalues < 0))
    #  if is_all_zero == True:
    #    indexonetimesend = False

    if indexrowy > 450:
      indexrow += 50
      indexrange += 50
      indexrangeoffset += 50
      indexrowy = 0

      indexfinalmax = int(np.argmax(rowhighest)) + counteroffset
      indexrowmaxmsp = int(np.argmax(rowhighest))
    #reset vars
      #reset counter for first 10 values
      counter = 0
      savefinal = 0
      tempfinal = 0
      rowscountmin += 10
      rowscountmax += 10
      #if row finished send first row then repeat
      sending = True
      
        
    if (sending == True):
      values.append(255)
      values.append((indexfinalmax))

      svalues.append(scounter)
      svalues.append((indexrowmaxmsp))
      superclient.send_message('/index', svalues)
      client.send_message('/red', values )
      values.clear()
      scounter += 1
      if scounter > 9:
        scounter= 0
      print(highestvalues,'mean')
      time.sleep(5)
      highestvalues[indexfinalmax] = 0
      svalues.clear()
      
      
      
        
      
      counteroffset += 10
      if counteroffset > 90:
        counteroffset = 0
        time.sleep(1)
        client.send_message('/reset', 'resetting' )
        superclient.send_message('/reset', 1)
        indexonetimesend = True
      
      
      sending = False
      flag1 = True
      if indexrangeoffset > 500:
        
        indexrowy = 0
        indexfinalmin = 0
        indexrow = 0
        indexrowy = 0
        indexrange = 0
        indexrowy = 0
        indexrangeoffset = 50
        highrowscount = 0
        rowscountbig = 0
        highestvaluescount = 0
        flagcheck = False
        rowscountmin = 0
        rowscountmax = 10
      time.sleep(1)
    
    



# After the loop release the cap object
vid.release()
# Destroy all the windows
cv.destroyAllWindows()
#nested for loop
