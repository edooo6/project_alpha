import pyttsx3
import datetime
import speech_recognition as sr
import cv2
import os
import pandas as pd
import datetime
import time
import csv
import numpy as np
import faceRecognition as fr
import os
import time



engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio): 
    engine.say(audio)
    engine.runAndWait()


def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 15:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("   My name is Alpha!...  At your service sir!")
    


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        query=query.lower()
        listen.query = query    
        

    except Exception as e:

        print("Please say that again....")
        return "None"
    return query



def askname():
    speak('Before that , I would like to know Your name sir?')
    a = listen()
    global always
    always = a
    

def path(): 
    count = 0
    while True:
        try:
            parent_dir = "test"
            global directories
            directories = "{}".format(count)
            path = os.path.join(parent_dir, directories)
            os.mkdir(path)
            pass
        except:
            count += 1
            continue
        break

def TakeImages():
    speak('I am capturing your images from the frame')     
    speak('Face the camera and please dont move away. Until I say')
    path()
    cap = cv2.VideoCapture(0)
    count = 0
    while count <= 100:
        ret, test_img = cap.read()
        if not ret:
            continue
        cv2.imwrite("test/{}/%d.jpg".format(directories) % count, test_img)     # save frame as jpg file
        count += 1
        #resized_img = cv2.resize(test_img, (1000, 700))
        #cv2.imshow('face detection Tutorial ',resized_img)
        
    speak('I have captured the frames to our system') 
    cap.release()   
    cv2.destroyAllWindows()

def saved():
    '''
    try:
        directory = always
        parent = 'saved'
        path = os.path.join(parent, directory)
        os.makedirs(path)
    except OSError as error:
        print(error)

    '''
    


    count = 1
    
    

    while count<=1:
        cap = cv2.VideoCapture(0)
        ret,frame = cap.read()
        time.sleep(12)  # return a single frame in variable `frame`
        if not ret:
            continue
        cv2.imwrite('saved/{}.jpg'.format(always),frame)
        count +=1
           
                
        break

    
    cap.release()
    cv2.destroyAllWindows()

def welcome():
    speak('Welcome to alpha networks')


'''
def resize_images():
    
    try:
        directory = directories
        parent = 'resized/'
        path = os.path.join(parent, directory)
        os.makedirs(path)
    except OSError as error:
        print(error)
    
    
    speak('Sorry for the wait, I need to process your image before registration, please bear with me.')
    count = 0
    for path, subdirnames, filenames in os.walk("test/{}".format(directories)):
        for filename in filenames:
            if filename.startswith("."):
                print("Skipping File:",filename)#Skipping files that startwith .
                continue
            img_path=os.path.join(path, filename)#fetching image path
            print("img_path",img_path)
            id=os.path.basename(path)#fetching subdirectory names
            img = cv2.imread(img_path)
            if img is None:
                print("Image not loaded properly")
                continue
            resized_image = cv2.resize(img, (100, 100))
            new_path="resized"+"/"+ "{}".format(directories) + str(id)
            print("desired path is",os.path.join(new_path, "frame%d.jpg" % count))#write all images to resizedTrainingImages/id directory
            cv2.imwrite(os.path.join(new_path, "frame%d.jpg" % count),resized_image)
            count += 1
'''
def face():
    speak('Processing Facial Recognition')
    test_img = cv2.imread('saved/{}.jpg'.format(always))
    faces_detected, gray_img = fr.faceDetection(test_img)
    speak("I found your data from our system")

    faces,faceID=fr.labels_for_training_data('test')
    face_recognizer = fr.train_classifier(faces, faceID)
    face_recognizer.write('trainingData.yml')

    
    users_list()

    for face in faces_detected:
        (x,y,w,h)=face
        roi_gray=gray_img[y:y+h,x:x+h]
        label,confidence=face_recognizer.predict(roi_gray)#predicting the label of given image
        print("Confidence:",confidence)
        print("label:",label)
        fr.draw_rect(test_img,face)
        predicted_name = name[label]
        if(confidence>37):#If confidence more than 37 then don't print predicted face text on screen
            welcome()
            break
        fr.put_text(test_img, predicted_name, x, y)

    resized_img = cv2.resize(test_img, (1000, 1000))
    cv2.imshow("Face", resized_img)
    cv2.waitKey(0)#Waits indefinitely until a key is pressed
    cv2.destroyAllWindows




def users_list():
    global name
    name = {"edwin":0,"jarvis":1}
    
    






while True:
    a = listen()
    if 'alpha' in a:
        greet()
    else:
        continue
    
    speak('Sir, may I ask? Is this your first time here?')
    
    while True:
        a=listen()
        if 'yes' in a:
            askname()
            speak(f'Mr.{always},  Good to meet you')
            speak('I will surely assist with the registration part')


    
    
    
    


 
            #path()
            
            TakeImages()
            #resize_images()
            saved()
            speak(f'Hello {always}, glad to meet you')
            speak('Since you are registered, I help you logging in')
            face()
           



        elif 'no' in a:
            askname()
            users_list()
            if always in name:
                speak(f"welcome back Mr.{always}")
                speak('Please give me a moment I will do a facial recognition for your')
                speak(f'Please face toward the webcam Mr. {always}')
                face()
                speak('User authenticated')
                continue   

            
        break


    


    











