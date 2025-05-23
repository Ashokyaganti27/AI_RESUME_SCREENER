
import  fitz

path = "C:\\Users\\yagan\\OneDrive\\Documents\\hemanthvellankicv.pdf"

def extract_text_from_pdf(path):

    doc=fitz.open(path)
    text=""
    for page in doc:

        text=text+page.get_text()
    
    return text

