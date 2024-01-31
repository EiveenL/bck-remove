from rembg import remove
import streamlit as st
from PIL import Image
import io

st.title("Background remover: :white_check_mark:")
st.markdown(":green[Una herramienta de eliminación de fondo de imagen impulsada por Remgb] :red[ Inténtalo !!!]")
st.markdown('<hr>', unsafe_allow_html=True)

uploaded_file = st.file_uploader(":red[Elige y carga una imagen aqui]", type=['.png', '.jpg', '.jpeg'])

if uploaded_file is not None:
    button = st.button("Remove Background")
    if button:
        image = uploaded_file.read()
        out_img = remove(image)
        col1, col2 = st.columns(2)
        
        with col1:
            img = st.image(image, caption='Imagen Original')
        
        with col2:
            img2 = st.image(out_img, caption='Imagen editada')
        
        # Download button
        download_button = st.download_button(
            label="Download Image",
            data=out_img,
            file_name="background_removed_image.png",
            key="download_button",
        )
