# Deploying the NN Classifier using Streamlit!
import numpy as np
import pandas as pd
import pickle
import sklearn

import streamlit as st
import tensorflow as tf
from tensorflow import keras

# Loading the neural net
model = keras.models.load_model("nn_clf.h5")

# Loading the preprocessor as well
preprocessor = pickle.load(open("preprocessor_model.pkl", "rb"))

# Prediction function
def predict_output(input_):
    """
    k: np array of the input features.
    """
    # Preprocess the data
    input_processed = preprocessor.transform(input_)
    x1 = np.array([np.array(val) for val in input_processed])

    # Get predictions from model
    pred = (model.predict(x1) > 0.5).astype("int64")
    ans = "" if pred == 1 else "not"

    message = f"Customer will {ans} check-in."
    
    return message

def main():
    # Tittling the app
    st.title("Customer Check-In Prediction Project")

    # Creating input fields
    input_dict = {}

    # Categorical inputs
    country_list = pickle.load(open("country_list.pkl", "rb"))
    country = st.selectbox("Guest's Nationality", country_list)
    input_dict['Nationality'] = country

    segment_list = pickle.load(open("segments.pkl", "rb"))
    market_segment = st.selectbox("Market Segment", segment_list)
    input_dict['MarketSegment'] = market_segment

    channel_list = pickle.load(open("channel_list.pkl", "rb"))
    channels = st.selectbox("Distribution Channel", channel_list)
    input_dict['DistributionChannel'] = channels

    # Booking canceled?
    st.text("0 means No; 1 means Yes")
    canceled = st.selectbox("Booking Canceled?", [0, 1])
    input_dict['canceled?'] = canceled

    # Booking noshow?
    no_show = st.selectbox("Booking No Show?", [0, 1])
    input_dict['no_show?'] = no_show

    # Age 
    age = st.number_input("Guest's Age", min_value = 16, max_value = 100)
    input_dict['Age'] = age

    # Lead Time
    average_lead = st.number_input("Average Lead Time", min_value = 0)
    input_dict['AverageLeadTime'] = average_lead
    
    # Lodging Revenue
    LodgingRevenue = st.number_input("Lodging Revenue", min_value = 0)
    input_dict['LodgingRevenue'] = LodgingRevenue

    # Other Revenue
    OtherRevenue = st.number_input("Other Revenue", min_value = 0)
    input_dict['OtherRevenue'] = OtherRevenue

    # Persons Nights
    PersonsNights = st.number_input("Persons Nights", min_value = 0)
    input_dict['PersonsNights'] = PersonsNights

    # Room Nights
    RoomNights = st.number_input("Room Nights", min_value = 0)
    input_dict['RoomNights'] = RoomNights

    # DaysSinceLastStay
    DaysSinceLastStay = st.number_input("Days Since Last Stay", min_value = -1)
    input_dict['DaysSinceLastStay'] = DaysSinceLastStay

    # DaysSinceCreation
    DaysSinceCreation = st.number_input("Days Since Creation", min_value = 0)
    input_dict['DaysSinceCreation'] = DaysSinceCreation

    # DaysSinceFirstStay
    DaysSinceFirstStay = st.number_input("Days Since First Stay", min_value = -1)
    input_dict['DaysSinceFirstStay'] = DaysSinceFirstStay
    
    # SRHighFloor
    SRHighFloor = st.selectbox("High Floor", [0, 1])
    input_dict['SRHighFloor'] = SRHighFloor

    # SRHighFloor
    SRMediumFloor = st.selectbox("Medium Floor", [0, 1])
    input_dict['SRMediumFloor'] = SRMediumFloor

    # SRLowFloor
    SRLowFloor = st.selectbox("Low Floor", [0, 1])
    input_dict['SRLowFloor'] = SRLowFloor

    # SRAccessibleRoom
    SRAccessibleRoom = st.selectbox("Accessible Room", [0, 1])
    input_dict['SRAccessibleRoom'] = SRAccessibleRoom

    # SRQuietRoom
    SRQuietRoom = st.selectbox("Quiet Room", [0, 1])
    input_dict['SRQuietRoom'] = SRQuietRoom

    # SRKingSizeBed
    SRKingSizeBed = st.selectbox("King-sized Bed?", [0, 1])
    input_dict['SRKingSizeBed'] = SRKingSizeBed

    # SRTwinBed
    SRTwinBed = st.selectbox("Twin Bed?", [0, 1])
    input_dict['SRTwinBed'] = SRTwinBed

    # SRCrib
    SRCrib = st.selectbox("Crib?", [0, 1])
    input_dict['SRCrib'] = SRCrib

    # SRBathtub
    SRBathtub = st.selectbox("Bathtub?", [0, 1])
    input_dict['SRBathtub'] = SRBathtub

    # SRShower
    SRShower = st.selectbox("Shower?", [0, 1])
    input_dict['SRShower'] = SRShower
    
    # SRNoAlcoholInMiniBar
    SRNoAlcoholInMiniBar = st.selectbox("No Alcohol in Minibar?", [0, 1])
    input_dict['SRNoAlcoholInMiniBar'] = SRNoAlcoholInMiniBar

    # SRNearElevator
    SRNearElevator = st.selectbox("Near elevator?", [0, 1])
    input_dict['SRNearElevator'] = SRNearElevator
    
    # SRAwayFromElevator
    SRAwayFromElevator = st.selectbox("Away from elevator?", [0, 1])
    input_dict['SRAwayFromElevator'] = SRAwayFromElevator
    
    # st.text(input_dict)

    result = ""

    if st.button("Predict"):
        # Convert the dict to a pandas DataFrame
        input_df = pd.DataFrame([input_dict]) #, columns = input_dict.keys())

        # Get the model's prediction
        result = predict_output(input_df)
        st.snow()
    
    st.success(result)
    

if __name__== '__main__':  
    main()  

