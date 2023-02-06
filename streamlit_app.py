import json
import base64
import streamlit as st
import requests
from PIL import Image


page_title = "Serverless"
page_icon = "💛"
layout = "centered"
st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)

# --- HIDE STREAMLIT STYLE ---
hide_st_style = """
            <style>      
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


if __name__ == '__main__':

    st.title('Intel Scene Classification on Serverless!')
    instructions = """ To test, select a Image from [here](https://github.com/Project-Kidu/code-repo/tree/main/tests/resources/intel-scene) """
    st.write(instructions)

    file = st.file_uploader('Upload An Image', type= ['png', 'jpg', 'jpeg'])


    if file:  # if user uploaded file
        img = Image.open(file)
        st.title("Here is the image you've selected")
        resized_image = img.resize((224, 224))
        st.image(resized_image)
        st.title("Here are the Predictions")

        url = "https://5hbrm6xu63.execute-api.ap-south-1.amazonaws.com"
        ext = file.name.split('.')[-1]
        prefix = f'data:image/{ext};base64,'

        bytes_data = file.getvalue()
        
        base64_data = prefix + base64.b64encode(bytes_data).decode('utf-8')

        payload = json.dumps({"body": [base64_data]})
        headers = {"content-type": "application/json"}
        response = requests.request("POST", url, json=payload, headers=headers)

        st.json(response.json())

