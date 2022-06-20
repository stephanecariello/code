import streamlit as st
from zipfile import ZipFile
def changeFileName(file_name,lang):
    before=file_name.split(".")[0]
    after=file_name.split(".")[1]
    new_name=Num_mandat+"_"+before+"_"+lang+"."+after
    return new_name

# here the title   
st.title("Welcome")

# list of uploaded files
files=st.file_uploader("Sélectionnez les fichiers", accept_multiple_files=True)

# list of languages
list_lang=st.text_input("Insérez langues").split(" ")

# numéro de mandat
Num_mandat=st.text_input("Insérez numéro de mandat")

# zip file
myZip=ZipFile("list_files.zip","w")

for file in files:
    for lang in list_lang:
        name=changeFileName(file.name,lang)
        myZip.writestr(name,file.getvalue())

myZip.close()

with open("list_files.zip","rb") as f:
    st.download_button("Télécharger les documents",f,file_name="files.zip")

if st.button("CLEAR"):
    del files
    myZip=ZipFile("list_files.zip","w")
    myZip.close()

