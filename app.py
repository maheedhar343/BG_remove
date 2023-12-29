import streamlit as st 
from rembg import remove 
from PIL import Image 


def main():
    st.title("Alpha Matting")
    uploaded_files = st.file_uploader("Upload a file",type=['jpg','png','jpeg'],accept_multiple_files=False)
    if st.button("Generate"):
        if uploaded_files:
            img = Image.open(uploaded_files)
            res = remove(img)
            st.balloons()
            # st.snow()
            col1,col2 = st.columns([1,1],gap="medium")
            with col1:
                st.write("## Original Image")
                st.image(img)
            with col2:
                st.write("## Result Image")
                st.image(res)
        
        else:
            st.error("Please upload an image")
    
    
if __name__ == "__main__":
    main()