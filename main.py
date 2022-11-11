import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
import pickle
import streamlit as st

#loding the saved model
loaded_model = pickle.load(open('trained_model.sav','rb'))

def prediction(input_data):
    input_data_array = np.array(input_data)
    input_data_reshaped = input_data_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshaped)
    result = "{:.2f}".format(prediction[0])
    # result = prediction[0].style.format("{:.3f}")
    return result

def replaceValue(data,value):
    if(data == 'fuel_type'):
        if(value == 'gas'):
            return 0
        else:
            return 1
    elif(data == 'aspiration'):
        if(value == 'std'):
            return 0
        else:
            return 1
    elif(data == 'num_of_doors'):
        if(value == 'four'):
            return 0
        else:
            return 1
    elif(data == 'body_style'):
        if(value == 'sedan'):
            return 0
        elif(value == 'hatchback'):
            return 1
        elif(value == 'wagon'):
            return 2
        elif(value == 'hardtop'):
            return 3
        else:
            return 4
    elif(data == 'drive_wheels'):
        if(value == 'fwd'):
            return 0
        elif(value == 'rwd'):
            return 1
        else:
            return 2
    elif(data == 'engine_location'):
        if(value == 'front'):
            return 0
        else:
            return 1
    elif(data == 'engine_type'):
        if(value == 'ohc'):
            return 0
        elif(value == 'ohcf'):
            return 1
        elif(value == 'dohc'):
            return 2
        elif(value == 'l'):
            return 3
        else:
            return 4
    elif(data == 'num_of_cylinders'):
        if(value == 'three'):
            return 0
        elif(value == 'four'):
            return 1
        elif(value == 'five'):
            return 2
        elif(value == 'six'):
            return 3
        else:
            return 4
    elif(data == 'fuel_system'):
        if(value == 'mpfi'):
            return 0
        elif(value == '2bbl'):
            return 1
        elif(value == 'idi'):
            return 2
        elif(value == '1bbl'):
            return 3
        elif(value == 'spdi'):
            return 4
        else:
            return 5  
       
def main():
    st.set_page_config(page_title='Predict Automobile Price')
    
    st.header('Predict Automobile Price')

    symboling = st.number_input('Symboling',min_value=3,max_value=204)

    col1,col2,col3 = st.columns(3)

    with col1:
        fuel_type = st.radio('Car fuel type',('gas','diesel'))
        fuel_type_replace = replaceValue('fuel_type',fuel_type)
    with col2:
        aspiration = st.radio('Aspiration used in a car',('std','turbo'))
        aspiration_replace = replaceValue('aspiration',aspiration)
    with col3:
        num_of_doors = st.radio('Number of doors in car',('four','two'))
        num_of_doors_replace = replaceValue('num_of_doors',num_of_doors)

    col4,col5,col6 = st.columns(3)

    with col4:
        body_style = st.radio('body of car',('sedan','hatchback','wagon','hardtop','convertible'))
        body_style_replace = replaceValue('body_style',body_style)
    with col5:
        drive_wheels = st.radio('type of drive wheel',('fwd','rwd','4wd'))
        drive_wheels_replace = replaceValue('drive_wheels',drive_wheels)
    with col6:
        engine_location = st.radio('location of car engine',('front','rear'))
        engine_location_replace = replaceValue('engine_location',engine_location)

    wheel_base = st.number_input('Weelbase of car',min_value=86.6,max_value=115.6)
    length = st.number_input('Length of car',min_value=141.1,max_value=202.6)
    width = st.number_input('Width of car',min_value=60.3,max_value=71.7)
    height = st.number_input('Height of car',min_value=49.4,max_value=59.8)
    curb_weight = st.number_input('The weight of a car without occupants or baggage',min_value=1488,max_value=4066)

    col7,col8,col9 = st.columns(3)

    with col7:
        engine_type = st.radio('Type of engine',('ohc','ohcf','dohc','l','ohcv'))
        engine_type_replace = replaceValue('engine_type',engine_type)
    with col8:
        num_of_cylinders = st.radio('cylinder placed in the car',('three','four','five','six','eight'))
        num_of_cylinders_replace = replaceValue('num_of_cylinders',num_of_cylinders)  
    with col9:
        fuel_system = st.radio('Fuel system of car',('mpfi','2bbl','idi','1bbl','spdi','mfi'))
        fuel_system_replace = replaceValue('fuel_system',fuel_system)

    engine_size = st.number_input('Size of car',min_value=61,max_value=258)

    bore = st.number_input('Boreratio of car',min_value=2.54,max_value=3.94)
    stroke = st.number_input('Stroke or volume inside the engine',min_value=2.07,max_value=4.17)
    compression_ratio = st.number_input('compression ratio of car',min_value=7.00,max_value=23.00)
    horsepower = st.number_input('Horsepower',min_value=48,max_value=200)
    peak_rpm = st.number_input('car peak rpm',min_value=4150,max_value=6600,step=50)
    city_mpg = st.number_input('Mileage in city',min_value=15,max_value=49)
    highway_mpg = st.number_input('Mileage on highway',min_value=18,max_value=54)

    predicted = ''

    if(st.button('submit to predict')):
        predicted = prediction([symboling, fuel_type_replace, aspiration_replace, num_of_doors_replace, body_style_replace, 
                                drive_wheels_replace, engine_location_replace, wheel_base, length, width, height, curb_weight, 
                                engine_type_replace, num_of_cylinders_replace, engine_size, fuel_system_replace, bore, stroke, 
                                compression_ratio, horsepower, peak_rpm, city_mpg,highway_mpg])
    st.success(predicted)

main()