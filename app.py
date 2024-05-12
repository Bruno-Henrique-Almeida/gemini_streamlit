import sqlite3
import utils
import json
import os
import re

import google.generativeai as genai
import streamlit as st

conn = sqlite3.connect('development.db')

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

model = genai.GenerativeModel(
    system_instruction='''
        If a question is asked that is outside the context of the sqlite database data, respond in the same language the question was asked in.
        If a query is requested, respond with 'query' at the beginning of the message.
        If a dataset is requested, respond with 'dataset' at the beginning of the message and return the query needed to obtain the dataset.
        Never perform any insert, update or delete on the database.
    ''',
    model_name='gemini-1.5-pro-latest',
    generation_config={
        'candidate_count': 1,   # number of candidates to return
        'temperature':     0.5, # temperature ("creativity") of the model
    }, 
)

chat = model.start_chat(history=[])

st.image('img\gemini_logo.png', output_format='PNG', width=180)

st.divider()

prompt = st.chat_input('Peça um a query ou um dataset: ')

if prompt:
    response = chat.send_message(f'Question: {prompt}: SQLite Database Schema: {json.dumps(utils.get_schema())}')

    if 'query' in response.text:
        st.markdown(response.text.replace('query', ''))

    elif 'dataset' in response.text:
        sql = re.search(r'```sql\n(.*?)\n```', response.text, re.DOTALL).group(1).strip()

        with conn:
            cursor = conn.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            cursor.close()

            st.dataframe(results)
    else:
        st.markdown(response.text)
