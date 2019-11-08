import numpy as np
import pandas
import glob
import os
import librosa
import re
import pandas as pd
import pdb

RAVDESS = "../data/ravdess/"
BERLIN = "../data/berlin/wav/"
AUDIO = 0
SAMPLING_RATE = 1
EMOTION = 2
ACTOR = 3
GENDER = 4
MFCC = 5

# Possible Emotions
#  - Neutral
#  - Calm
#  - Happy
#  - Sad
#  - Angry
#  - Fearful
#  - Disgust
#  - Surprised
#  - Boredom

# Possible genders
#  - male
#  - female

# 34 possible actors

class Dataset():
    def __init__(self):
        self.berlin_data = None
        self.ravdess_data = None
        self.feature_names = ["audio", "sampling_rate", "emotion", "actor", "gender"]
        
    def load(self, path):
        n = Dataset._get_num_files(path)

        if path == RAVDESS:
            self.ravdess_data = np.zeros(n, dtype=object)
        elif path == BERLIN:
            self.berlin_data = np.zeros(n, dtype=object)
        
        i = 0
        for filename in glob.iglob(path + "**", recursive=True):
            if ".wav" in filename:
                element = { "audio": None, 
                            "sampling_rate": None, 
                            "emotion": None, 
                            "actor": None, 
                            "gender": None,
                            "mfcc": None }

                audio, sampling_rate = librosa.load(filename)
                mfcc = librosa.feature.mfcc(y=audio, sr=sampling_rate, n_mfcc=12)
                emotion = Dataset._get_emotion(filename, path)
                actor = Dataset._get_actor(filename, path)
                gender = Dataset._get_gender(filename, path)
               
                element["audio"] = audio
                element["sampling_rate"] = sampling_rate
                element["emotion"] = emotion
                element["actor"] = actor
                element["gender"] = gender
                element["mfcc"] = mfcc
                if path == RAVDESS:
                    self.ravdess_data[i] = element
                elif path == BERLIN:
                    self.berlin_data[i] = element
                i += 1
     
    def save_data(self):
        np.save("./clean_data/ravdess_clean", self.ravdess_data)
        np.save("./clean_data/berlin_clean", self.berlin_data)
    
    @staticmethod
    def _get_num_files(path):
        total = 0
        for root, dirs, files in os.walk(path):
            total += len(files)
        return total

    @staticmethod
    def _get_emotion(filename, dataset_type):
        if dataset_type == RAVDESS:
            return re.findall("[0-9][0-9]", filename)[2]
        elif dataset_type == BERLIN:
            emotion = re.search("[A-Z]", filename)
            
    @staticmethod
    def _get_actor(filename, dataset_type):
        if dataset_type == RAVDESS:
            return re.findall("[0-9][0-9]", filename)[6]
        elif dataset_type == BERLIN:
            actor = re.search("[a-z][0-9][0-9]", filename)
        
    @staticmethod
    def _get_gender(filename, dataset_type):
        if dataset_type == RAVDESS:
            actor = re.findall("[0-9][0-9]", filename)[6]
            if int(actor) % 2 == 0:
                return "female"
            else:
                return "male"
        elif dataset_type == BERLIN:
            actor = re.findall("[0-9][0-9]", filename)[0]
            return Dataset._get_berlin_gender_from_actor(actor)
 
    @staticmethod
    def _get_berlin_gender_from_actor(actor):
        switch = {
                "03": "male",
                "08": "female",
                "09": "female",
                "10": "male",
                "11": "male",
                "12": "male",
                "13": "female",
                "14": "female",
                "15": "male",
                "16": "female"
        } 
        return switch.get(actor, "Invalid actor!")

if __name__ == "__main__":
    dataset = Dataset()
    dataset.load(RAVDESS)
    dataset.load(BERLIN)
    dataset.save_data()
