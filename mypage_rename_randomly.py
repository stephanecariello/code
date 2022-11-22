import streamlit as st
import random
from zipfile import ZipFile
def changeFileName(file_name,nickname):
    before=file_name.split(".")[0]
    after=file_name.split(".")[1]
    new_name=nickname+"."+after
    return new_name


# here the title   
st.title("Welcome")

#lsit of nicknames
list_nicknames=st.text_input("Surnoms:").split(" ")
# list of uploaded files
files=st.file_uploader("Sélectionnez les fichiers", accept_multiple_files=True)




# zip file
myZip=ZipFile("list_files.zip","w")

f = open("nicknames.txt", "w")

for file in files:
    nickname=''.join(random.sample(list_nicknames,1))
    name=changeFileName(file.name,nickname)
    myZip.writestr(name,file.getvalue())
    list_nicknames.remove(nickname)
    f.write(file+" "+"="+" "+nickname+"\n")
f.close()
 
myZip.write("nicknames.txt")
myZip.close()

with open("list_files.zip","rb") as f:
    st.download_button("Télécharger les documents",f,file_name="files.zip")

if st.button("CLEAR"):
    del files
    myZip=ZipFile("list_files.zip","w")
    myZip.close()
