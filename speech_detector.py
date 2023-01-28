from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import sys
import os
import speech_recognition as sr


def get_audio():
    r = sr.Recognizer()
    r.energy_threshold = 300
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio, language="pl_PL")
            #print(said)
        except Exception as e:
            print("")
    return said

print("Powiedz słowo pogoda...")


text = get_audio()
os.system("cls")

if "pogoda" or "otwórz pogodę" or "pokaż pogodę" in text:
   
    driver = webdriver.Firefox()
    driver.get("https://michalkarczewicz.github.io/WeatherApp/")
    while(True):
        page_title = driver.title
        search_bar = driver.find_element(By.CLASS_NAME, "search-bar")
        print("Powiedz nazwe miasta")
        city = get_audio()
        if "wyjdź" in city: 
            driver.close()
            sys.exit()      
        elif "opcje" in city:
            value = True
            while(value):
                more_details = driver.find_element(By.CLASS_NAME,"more-details").click()
                closeMoreDetails = get_audio()
                if "wyjdź" or "close" or "powrót" in closeMoreDetails:
                    more_details = driver.find_element(By.CLASS_NAME,"remove-button").click()
                    value = False
        else:
            os.system("cls")
            search_bar.clear()
            search_bar.send_keys(city)
            search_button = driver.find_element(By.CLASS_NAME, "search-button").click()