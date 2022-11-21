import streamlit as st
from zipfile import ZipFile


# here the title   
st.title("Welcome")

# list of uploaded files
files=st.file_uploader("Sélectionnez les fichiers", accept_multiple_files=True)


list_nicknames=st.text_input("Surnoms:").split(" ")


# zip file
myZip=ZipFile("list_files.zip","w")

for file in files:
    before=file.split(".")[0]
    after=file.split(".")[1]
    nickname=''.join(random.sample(list_nicknames,1))
    new_name=nickname+"."+after
    list_nicknames.remove(nickname)
    myZip.writestr(new_name,file.getvalue())
            

myZip.close()

with open("list_files.zip","rb") as f:
    st.download_button("Télécharger les documents",f,file_name="files.zip")

if st.button("CLEAR"):
    del files
    myZip=ZipFile("list_nicknames.zip","w")
    myZip.close()

