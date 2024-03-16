import streamlit as st
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

st.title("Quick LLM Playground")

openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")


def generate_response(input_text):
    llm = ChatOpenAI(temperature=0.7, model="gpt-4", openai_api_key=openai_api_key)
    messages = [
        HumanMessage(content=input_text),
    ]

    st.info(llm.invoke(messages).content)


with st.form("my_form"):
    text = st.text_area(
        "Enter text:",
        "What are the three key pieces of advice for learning how to code?",
    )
    submitted = st.form_submit_button("Submit")
    if not openai_api_key.startswith("sk-"):
        st.warning("Please enter your OpenAI API key!", icon="⚠")
    if submitted and openai_api_key.startswith("sk-"):
        generate_response(text)
