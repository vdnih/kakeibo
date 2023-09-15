import streamlit as st
import pandas as pd
import psycopg2
import plotly.express as px

# 参考：https://docs.streamlit.io/knowledge-base/tutorials/databases/postgresql
# タイトル
st.title('家計簿')

# DB接続を定義する関数（接続情報は .streamlit/secrets.toml から取得）
def init_connection():
    return psycopg2.connect(**st.secrets["postgres"])

conn = init_connection()

# DBからデータを取得する関数
def run_query_pd(query):
    with conn:
        data = pd.read_sql_query(query, conn)
    return data

#ここでSQLを定義
sql = "SELECT * from expense;"
data = run_query_pd(sql)

#取得したデータの表示
st.write(data)

#棒グラフの表示
fig = px.bar(data, x='category', y='price', title='棒グラフ')
st.plotly_chart(fig)

#円グラフの表示
fig = px.pie(data, values='price', names='category', title='円グラフ')
st.plotly_chart(fig)
