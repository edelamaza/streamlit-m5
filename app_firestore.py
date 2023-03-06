import streamlit as st
import pandas as pd
from google.cloud import firestore
import json
from google.oauth2 import service_account
# db = firestore.Client.from_service_account_json('test-demo-names.json')

key_dict = json.loads(st.secrets["textkey"])
creds = service_account.Credentials.from_service_account_info(key_dict)
db = firestore.Client(credentials=creds, project="names-project-demo-esteban")

dbNames = db.collection("names")

st.header('New Entry')

index = st.number_input('Index', min_value=0, max_value=1000, value=0, step=1)
name = st.text_input('Name')
sex = st.selectbox("select Sex", options=['M', 'F', 'Other'])

submit = st.button('Submit')

if (index and name and sex and submit):
    doc_ref = dbNames.document(name)
    doc_ref.set({
        'index': index,
        'name': name,
        'sex': sex
    })
    st.sidebar.write("New entry added successfully")

names_ref = list(dbNames.stream())
names_dict = list(map(lambda x: x.to_dict(), names_ref))

df = pd.DataFrame(names_dict)
st.dataframe(df)


def loadByName(name):
    names_ref = dbNames.where('name', '==', name)
    currentName = None
    for myname in names_ref.stream():
        currentName = myname
    return currentName


st.sidebar.subheader('Search by name')
nameSearch = st.sidebar.text_input('NameSearch')
btnFilter = st.sidebar.button('Search')

if (nameSearch and btnFilter):
    doc = loadByName(nameSearch)
    if doc is None:
        st.sidebar.write("Name not found")
    else:
        st.sidebar.write(doc.to_dict())

st.sidebar.markdown("""...""")
btnDelete = st.sidebar.button('Delete')

if (nameSearch and btnDelete):
    doc = loadByName(nameSearch)
    if doc is None:
        st.sidebar.write("Name not found")
    else:
        dbNames.document(doc.id).delete()
        st.sidebar.write("Name deleted")

st.sidebar.markdown("""...""")
new_name = st.sidebar.text_input('New Name')
btnUpdate = st.sidebar.button('Update')

if (nameSearch and btnUpdate):
    doc = loadByName(nameSearch)
    if doc is None:
        st.sidebar.write("Name not found")
    else:
        dbNames.document(doc.id).update({
            "name": new_name
        })
        st.sidebar.write("Name updated")
