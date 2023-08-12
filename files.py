import streamlit as st
import pandas as pd

st.subheader('Uploading the CSV File')
st.subheader('Uploading the CSV File')
df = st.file_uploader("Upload file here : ", type = ['csv','xlsx'])


st.subheader('Loading the CSV File')
if df is not None:
         dataframe = pd.read_csv(df)
         st.table(dataframe.head(n=7))


st.subheader('Working with Images')
st.image(r"D:\Study\Python\UserProfile\Streamlit\img.jpg")
img_file = st.file_uploader("Upload image file : ", type = ['png', 'jpeg', 'jpg'])
if img_file is not None:
        st.image(img_file)



st.subheader('Working with Videos')
video_file = st.file_uploader("Upload video file : ", type = ['mkv', 'mp4'])
if video_file is not None:
        st.video(video_file, start_time = 4)


st.subheader('Working with Audio')
audio_file = st.file_uploader("Upload audio file : ", type = ['mp3', 'wav'])
if audio_file is not None:
        st.audio(audio_file.read())
