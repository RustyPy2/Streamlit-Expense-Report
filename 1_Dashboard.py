import streamlit as st
import pandas as pd

st.set_page_config('Expense Report')

hide_menu_style = """<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>"""
st.markdown(hide_menu_style, unsafe_allow_html=True)

st.header('Expense Report', anchor='dashboard')

def file_Uploaded():

    col1, col2, col3 = st.columns(3, gap='small')

    df = pd.read_excel(io=excel_File, engine= 'openpyxl', usecols='A,B,C')

    max_Val = df['Cost'].max()
    min_Val = df['Cost'].min()

    st.slider('Money Range', value=[min_Val, max_Val])
    col1.selectbox('Categories', options= df['Category'].unique())
    col2.selectbox('Vendors', options= df['Vendor'].unique())

    category_Fig = df.drop(['Vendor'], axis=1)

    fig = st.bar_chart(category_Fig, x='Category', y='Cost')


excel_File = st.sidebar.file_uploader('Excel File', type='.xlsx')

if excel_File is not None:
    file_Uploaded()
