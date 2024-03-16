import streamlit as st
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

# inner import
from prompts.persona import prompt
from settings import OPENAI_API_KEY

st.title("Quick LLM Playground")


def generate_response(input_text):
    llm = ChatOpenAI(
        temperature=0.7, model="gpt-4-turbo-preview", openai_api_key=OPENAI_API_KEY
    )
    messages = [
        HumanMessage(content=input_text),
    ]
    result = llm.invoke(messages).content
    st.info(result)
    save_result(result)


def save_result(result):
    with open("result.txt", "w", encoding="utf-8") as f:
        f.write(result)


with st.form("my_form"):
    # text = st.text_area(
    #     "テキストを入力してください:",
    #     "ああああ と返してください。",
    # )
    st.text("persona 生成")
    submitted = st.form_submit_button("Submit")

    if submitted:
        generate_response(prompt)
