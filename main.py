import streamlit as st
import pandas

data = {
  "Series1": [1,2,3,4,5],
  "Series2": [10,20,30,40,50]}

df = pandas.DataFrame(data)

st.title('OurFirst Streamlit App')
st.subheader('Introducing Streamlit in Automate everything')
st.write('Myfirst web app')
st.write(df)
st.line_chart(df)
st.area_chart(df)

myslider = st.slider('Celsius')
st.write(myslider, 'in Fahrenheit is', myslider * 9/5 +32)
#To run locally
#streamlit run main.py