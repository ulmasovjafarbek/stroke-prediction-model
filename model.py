import pickle
import numpy as np


class Model:
    def __init__(self, model_name):
        self.model_name = model_name
        self.filepath = "models/"
        self.extension = "all"
        self.model = self.load_model()

    def load_model(self):
        classification_pkl_filename = self.filepath + \
                                      self.extension + \
                                      "_" + self.model_name + '.pkl'

        try:
            classification_model_pkl = open(classification_pkl_filename, 'rb')
            classification_model = pickle.load(classification_model_pkl)
            return classification_model
        except Exception as e:
            # Print the error message if an exception is thrown
            print(e)

    def predict(self, X):
        return self.model.predict(X)[0]

    def preprocess(self, form):
        gender = form['gender']
        age = form['age']
        is_hypertension = form['isHypertension']
        has_heart_disease = form['hasHeartDisease']
        is_married = form['isMarried']
        work_type = form['workType']
        residence_type = form['residenceType']
        glucose_level = form['glucoseLevel']
        body_mass_index = form['bodyMassIndex']
        smoke_status = form['smokeStatus']
        data = [gender, age, is_hypertension,
                has_heart_disease, is_married,
                work_type, residence_type, glucose_level,
                body_mass_index, smoke_status]
        print(data)
        return np.array(data).reshape(1, -1)


# res = [1, 20, 1, 1, 1, 3, 1, 70, 40, 2]
# data = np.array(res).reshape(1, -1)
# model = Model("forest_regression")
# result = model.predict(data)
# print(f'Possibility of having stroke: {result}')
