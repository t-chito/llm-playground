import streamlit as st

# inner import
from prompts.extract_ka_cards import prompt
from utils import get_token_count, get_response_once, save_result

st.title("Quick LLM Playground")


def generate_response(prompt: str):

    st.info("input tokens: " + str(get_token_count(prompt)))

    result = get_response_once(prompt)
    save_result(result)
    
    st.info(result)
    st.info("output tokens: " + str(get_token_count(result)))
    


with st.form("my_form"):
    # text = st.text_area(
    #     "テキストを入力してください:",
    #     "ああああ と返してください。",
    # )
    st.text("KA カード生成")
    submitted = st.form_submit_button("Submit")

    if submitted:
        generate_response(prompt)
