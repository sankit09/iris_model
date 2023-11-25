import numpy as np
import pickle
import json
import config

class Species():
    def __init__(self,SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm):
        self.SepalLengthCm = SepalLengthCm
        self.SepalWidthCm = SepalWidthCm
        self.PetalLengthCm = PetalLengthCm
        self.PetalWidthCm = PetalWidthCm
    
    def load_model(self):
        with open(config.MODEL_FILE_PATH,"rb") as f:
            self.model = pickle.load(f)
        
        with open(config.JSON_FILE_PATH,"r") as f:
            self.json_data = json.load(f)

    def get_predict_species(self):
        self.load_model()

        test_array = np.zeros(len(self.json_data["columns"]))

        test_array[0]= self.SepalLengthCm
        test_array[1]= self.SepalWidthCm
        test_array[2]= self.PetalLengthCm
        test_array[3]= self.PetalWidthCm
        
        print("Test Array :",test_array)

        predict_species = self.model.predict([test_array])

        return predict_species





