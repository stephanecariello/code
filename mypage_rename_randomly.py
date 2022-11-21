import streamlit as st
from zipfile import ZipFile
def changeFileName(file_name,nickname):
    before=file_name.split(".")[0]
    after=file_name.split(".")[1]
    new_name=nickname+"."+after
    return new_name


# here the title   
st.title("Welcome")

# list of uploaded files
files=st.file_uploader("Sélectionnez les fichiers", accept_multiple_files=True)


list_nicknames=st.text_input("Surnoms:").split(" ")
nickname=''.join(random.sample(list_nicknames,1))

# zip file
myZip=ZipFile("list_files.zip","w")

for file in files:
    name=changeFileName(file.name,nickname)
    list_nicknames.remove(nickname)
    myZip.writestr(name,file.getvalue())
            

myZip.close()

with open("list_files.zip","rb") as f:
    st.download_button("Télécharger les documents",f,file_name="files.zip")

if st.button("CLEAR"):
    del files
    myZip=ZipFile("list_nicknames.zip","w")
    myZip.close()

