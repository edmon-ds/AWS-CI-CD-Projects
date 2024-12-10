import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object

class MLutils:
    #es importante colocar como separador "/" y no colocar "\" 
    #el modelo no se podra cargar el linux
    
    model = load_object("artifacts/model.pkl")
    preprocessor = load_object("artifacts/preprocessor.pkl")


class CustomData:
    def __init__(  self,gender: str,race_ethnicity: str,
                   parental_level_of_education,
                   lunch: str,
                   test_preparation_course: str,
                   reading_score: int,
                   writing_score: int):

        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score
        
    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score],
            }
            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise CustomException(e , sys) 
        
class PredictPipeline:
    def __init__(self):
        self.model = MLutils.model
        self.preprocessor = MLutils.preprocessor    

    def predict(self , features):
        try:
            data_transformed = self.preprocessor.transform(features)
            preds = self.model.predict(data_transformed)
            return preds
        except Exception as e:
            raise CustomException(e , sys)