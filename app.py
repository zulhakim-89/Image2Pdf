import streamlit as st
from PIL import Image
from io import BytesIO

def save_as_pdf(images, output_stream):
    if images:
        # Convert all images to RGB mode and save them as a PDF
        images[0].save(output_stream, format='PDF', save_all=True, append_images=images[1:], quality=95)

def main():
    st.title("Image to PDF Converter")
    
    # File uploader allows multiple file uploads
    uploaded_files = st.file_uploader("Upload image files", type=["png", "jpg", "jpeg"], accept_multiple_files=True)
    
    if uploaded_files:
        images = []
        for uploaded_file in uploaded_files:
            # Open the image file
            image = Image.open(uploaded_file)
            images.append(image.convert("RGB"))  # Ensure the image is in RGB mode
        
        # Button to convert images to PDF
        if st.button("Convert to PDF"):
            # Convert images to PDF and save to a BytesIO object
            pdf_output = BytesIO()
            save_as_pdf(images, pdf_output)
            
            # Seek to the beginning of the stream so it can be read from the start
            pdf_output.seek(0)
            
            # Provide download link
            st.success("PDF created successfully!")
            st.download_button(
                label="Download PDF",
                data=pdf_output.getvalue(),
                file_name="combined_images.pdf",
                mime="application/pdf"
            )

if __name__ == "__main__":
    main()
