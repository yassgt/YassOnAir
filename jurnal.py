
import pandas as pd 
import streamlit as st

alt = { 'Alternatif'    : ["Alternatif-1","alternatif-2","alternatif-3","Alternatif-4","alternatif-5"],
        'K1'            : [3,3,5,5,7],
        'K2'            : [7,9,5,3,9],
        'K3'            : [5,7,7,7,7],
        'K4'            : [3,5,7,9,9],
}

bobot = {'Bobot':[0.25,0.25,0.45,0.05]}
dfb = pd.DataFrame(bobot)
df = pd.DataFrame(alt)

st.dataframe(df)

max1 = max(df['K1'])
max2 = max(df['K2'])
max3 = max(df['K3'])
max4 = max(df['K4'])

min1 = min(df['K1'])
min2 = min(df['K2'])
min3 = min(df['K3'])
min4 = min(df['K4'])

max = pd.DataFrame([[max1,max2,max3,max4]],
        columns=['K1','K2','K3','K4'],index=['MAX'])
min = pd.DataFrame([[min1,min2,min3,min4]],
        columns=['K1','K2','K3','K4'],index=['MIN'])
st.write(min4)
minmax= max.append(min)

df['W1'] = df['K1']/max1
df['W2'] = df['K2']/max2
df['W3'] = df['K3']/max3
df['W4'] = df['K4']/min4
st.dataframe(minmax)

n = df[['Alternatif','W1','W2','W3','W4']]
st.dataframe(n.style.format(precision=2))

st.dataframe(dfb.style.format(precision=2))

df['WSM1'] = df['W1'] * 0.25
df['WSM2'] = df['W2'] * 0.25
df['WSM3'] = df['W3'] * 0.45
df['WSM4'] = df['W4'] * 0.05
df['Sum'] = df['WSM1'] + df['WSM2'] + df['WSM3'] + df['WSM4']

df['WPM1'] = df['W1'] ** 0.25
df['WPM2'] = df['W2'] ** 0.25
df['WPM3'] = df['W3'] ** 0.45
df['WPM4'] = df['W4'] ** 0.05
df['Product'] = df['WPM1'] * df['WPM2'] * df['WPM3'] * df['WPM4']


wsm = df[['Alternatif','WSM1','WSM2','WSM3','WSM4','Sum']]
wpm = df[['Alternatif','WPM1','WPM2','WPM3','WPM4','Product']]

df['Joint(Q)'] = (df['Sum'] + df['Product'])/2
qj = df[['Alternatif','Joint(Q)']]
l = df['Product'] / (df['Sum']*df['Product'])

st.write(l)
df['Joint(𝝀)'] = (l*df['Sum']) + ((1-l)*df['Product'])
st.dataframe(wsm.style.format(precision=2))
st.dataframe(wpm.style.format(precision=2))
st.dataframe(qj.style.format(precision=3))

st.bar_chart(df[['Joint(Q)','Joint(𝝀)']], y='Joint(𝝀)')
