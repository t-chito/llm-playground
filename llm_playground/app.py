import streamlit as st
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

# ./settings.py
from settings import OPENAI_API_KEY

st.title("Quick LLM Playground")


def generate_response(input_text):
    llm = ChatOpenAI(temperature=0.7, model="gpt-4", openai_api_key=OPENAI_API_KEY)
    messages = [
        HumanMessage(content=input_text),
    ]

    st.info(llm.invoke(messages).content)


with st.form("my_form"):
    text = st.text_area(
        "テキストを入力してください:",
        "ああああ と返してください。",
    )
    submitted = st.form_submit_button("Submit")

    if submitted:
        if text:
            st.warning("なにかテキストを入力してください", icon="⚠")
        else:
            generate_response(text)
