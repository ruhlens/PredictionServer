import pandas as pd
from getData import getData
from pycaret.time_series import *

class ArimaModel:

    def __init__(self):
        pass

    '''
    Setup Pycaret framework and determine which model best suits the data
    '''
    def assembleModel(self, df):
        setup(df, fh=7, session_id=123)
        #best = compare_models()
        best = create_model('arima')
        result = best
        return result

    '''
    Generate predictions based on the best model
    '''
    def predictModel(self, days, model):
        model = finalize_model(model)
        prediction = predict_model(model, fh=days)
        return prediction

    '''
    Return predictions data for a given ticker
    '''
    def createPredictionsDF(self, ticker):
        data = getData().assembleDF(ticker)
        model = self.assembleModel(data)
        prediction = self.predictModel(1,model)
        return prediction
