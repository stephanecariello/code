import streamlit as st
from zipfile import ZipFile


# here the title   
st.title
("Welcome")

# list of uploaded files
files=st.file_uploader("Sélectionnez les fichiers", accept_multiple_files=True)


list_nicknames=st.text_input("Surnoms:").split(" ")


# zip file
myZip=ZipFile("list_nicknames.zip","w")

for file in files:
    before=file_name.split(".")[0]
    after=file_name.split(".")[1]
    nickname=''.join(random.sample(list_nicknames,1))
    new_name=nickname+"."+after
    list_nicknames.remove(nickname)
    shutil.copy(path+file_name,path+new_name)
    f.write(before+" "+"="+" "+nickname+"\n")
    myZip.writestr(nickname,file.getvalue())
f.close()
            

myZip.close()

with open("list_files.zip","rb") as f:
    st.download_button("Télécharger les documents",f,file_name="files.zip")

if st.button("CLEAR"):
    del files
    myZip=ZipFile("list_files.zip","w")
    myZip.close()

