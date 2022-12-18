import streamlit as st
import pandas as pd
from PIL import Image

st.title("**Social Media Analytics**")

socialMediaPic = Image.open("PICS/SocialMedia.jpg")
abhiramPic = Image.open("PICS/AbhiramAgina.png")

st.sidebar.image(abhiramPic, width = 150)
st.sidebar.markdown(
"""
About Me:
* I am a Senior at Oak Park High School in Oak Park, CA. I developed this app as a tool and portfolio of my early work in Social Media Analytics.
* [**My Github**](https://github.com/Abhiram-Agina)
* [**My LinkedIn**](https://www.linkedin.com/in/abhiram-agina/)
"""
)

nav = st.sidebar.radio("Navigation",["Statement Sentiment", "Tweet Sentiment", "Conflict Sentiment",])


if nav == "Summary":
    st.image(socialMediaPic, caption = "SOcial Media Analysis", width = 500)
    st.markdown(
    """
    ***Social Media Analysis***
    * **Making sense of our world - through Social Media** 
    )***\n
    """
    )
    col1, col2, col3, col4 = st.columns(4)
    col1.image(aauLogoPic)
    col2.image(nbaLogoPic)
    col3.image(ncaaLogoPic)
    col4.image(ophsAthleticsPic)
    
