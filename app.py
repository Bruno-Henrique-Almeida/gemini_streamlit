import sqlite3
import utils
import json
import os
import re

import google.generativeai as genai
import streamlit as st


assert os.getenv('GOOGLE_API_KEY'), 'GOOGLE_API_KEY environment variable is not set'

conn = sqlite3.connect('development.db')

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

assistent_query_model = genai.GenerativeModel(
    system_instruction='''
        only use SQLite sintax.
        use the onlydatabase schema to create a ddl query to answer the question.
    ''',
    model_name='gemini-1.5-flash-latest',
    generation_config={
        'candidate_count': 1,   # number of candidates to return
        'temperature':     0.1, # temperature ("creativity") of the model
    }
)

assistent_answer_model = genai.GenerativeModel(
    system_instruction='''
        use the prompt and the result to construct a humanized response.
    ''',
    model_name='gemini-1.5-flash-latest',
    generation_config={
        'candidate_count': 1,   # number of candidates to return
        'temperature':     0.5, # temperature ("creativity") of the model
    }
)

st.image('img/gemini_logo.png', output_format='PNG', width=180)

st.divider()

prompt = st.chat_input('Pergunta sobre produtos, vendas, fornecedores, clientes:')

if prompt:
    response = assistent_query_model.generate_content(
        f'Question: {prompt}: SQLite Database Schema: {json.dumps(utils.get_schema())}'
    )

    sql = re.search(f'```sqlite\n(.*)\n```', response.text, re.DOTALL).group(1).strip()

    with conn:
        cursor = conn.cursor()
        result = cursor.execute(sql).fetchall()
        cursor.close()

    response = assistent_answer_model.generate_content(
        f'Question: {prompt}: Result: {result}'
    )

    st.markdown(response.text)
