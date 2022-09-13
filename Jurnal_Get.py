import requests
import pandas as pd
from scidownl import scihub_download
import streamlit as st

search_term = "Erna Budhiarti Nababan"
# change this for different page no
page_no = 1
headers = {
    "Accept": "application/json, text/plain, */*",
    "Origin": "https://ieeexplore.ieee.org",
    "Content-Type": "application/json",
}
payload = {
    "newsearch": True,
    "queryText": search_term,
    "highlight": True,
    "returnFacets": ["ALL"],
    "returnType": "SEARCH",
    "pageNumber": page_no
}
r = requests.post(
        "https://ieeexplore.ieee.org/rest/search",
        json=payload,
        headers=headers
    )

page_data = r.json()
listDoi = []
listName = []
listYear = []
page = range(page_data["totalPages"])
for i in page:
    for record in page_data["records"]:
        listDoi.append(record["articleTitle"])
        listName.append(record["doi"])
        listYear.append(record["publicationYear"])

        
df = pd.DataFrame({'Nama Artikel': listDoi, 'Doi': listName, 'Tahun':listYear})

st.dataframe(df)
