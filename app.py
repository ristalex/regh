import streamlit as st
from PIL import Image
import streamlit as st
from streamlit_lottie import st_lottie
import requests

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name)as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

lottie_coding = load_lottieurl("https://lottie.host/367e592a-163d-4e2b-8565-517e60ac083c/X66C3cpYWA.json")
img_contact_form= Image.open("msg-1001855948944-24.jpg")
image2= Image.open("ae913a74fade9e50f7ab7c12efd1d43f.jpg")

with st.container():
    st.subheader("Привет, меня зовут Алияр :wave:")
    st.write("Я родился в 2008 году 18 августа")
    


with st.container():
    st.write('##')
    image_column,text_column= st.columns((1,2,))
    with image_column:
        st.image(img_contact_form)

with st.container():
      st.write("---")
      st.subheader("Я учусь в школе Тамос")
      image_column,text_column= st.columns((1,2,))
      with image_column:
        st.image(image2)
    

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("My hobbies")
        st.write("##")
        st.write("Я люблю слушать музыку и играть в компьютерные игры" )

with right_column:
    st_lottie(lottie_coding, height=300, key="coding")




    with st.container():
        st.write("---")
        st.header("FeedBack")
        st.write('##')

        contact_form= """ <form action="https://formsubmit.co/your@email.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="your name" required>
     <input type="email" name="email" placeholder="You email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
     </form> 
     """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column: 

        st.empty()



