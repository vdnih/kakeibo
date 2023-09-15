import streamlit as st
import pandas as pd
import numpy as np
import psycopg2
import plotly.express as px

# https://docs.streamlit.io/knowledge-base/tutorials/databases/postgresql
st.title('家計簿')

# Initialize connection.
# Uses st.cache_resource to only run once.
#@st.cache_resource
def init_connection():
    return psycopg2.connect(**st.secrets["postgres"])

conn = init_connection()

# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
# @st.cache_data(ttl=600)
# def run_query(query):
#     with conn.cursor() as cur:
#         cur.execute(query)
#         return cur.fetchall()

# rows = run_query("SELECT * from expense;")

# #@st.cache_data(ttl=600)
# def run_query_pd(query):
#     try:
#         with conn:
#             data = pd.read_sql_query(query, conn)
#     except Exception as e:
#         print("--- db error ---")
#         print(e)
#         st.error(e)
#     finally:
#         if conn:
#             conn.close()
#             data = "db connection error"
#     return data

def run_query_pd(query):
    with conn:
        data = pd.read_sql_query(query, conn)
    return data

data = run_query_pd("SELECT * from expense;")

st.write(data)

# Print results.
# for row in rows:
#     st.write(f"{row[0]} has a :{row[1]}:")

#棒グラフ
fig = px.bar(data, x='category', y='price', title='棒グラフ')
st.plotly_chart(fig)

#円グラフ
fig = px.pie(data, values='price', names='category', title='円グラフ')
st.plotly_chart(fig)






