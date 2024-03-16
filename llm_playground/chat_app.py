"""
ChatGPT-like clone
see https://docs.streamlit.io/knowledge-base/tutorials/build-conversational-apps#build-a-chatgpt-like-app
"""

import streamlit as st
from openai import OpenAI

# ./settings.py
from settings import OPENAI_API_KEY

st.title("ChatGPT-like clone")

client = OpenAI(api_key=OPENAI_API_KEY)

# TODO: langchain x gpt4 に変更する
# デフォルトのモデルを設定
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

# TODO: 履歴は pickle とかで保存したい
# 履歴を初期化
if "messages" not in st.session_state:
    st.session_state.messages = []

# 履歴からメッセージを表示
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ユーザーからの入力を受け取り、OpenAI API に送信
if prompt := st.chat_input("What is up?"):
    # TODO: 履歴管理は改善したほうが良いかも
    # see https://qiita.com/ayoyo/items/07da43bbab6652d37421#tldr
    # 履歴に追加
    st.session_state.messages.append({"role": "user", "content": prompt})
    # メッセージを表示
    with st.chat_message("user"):
        st.markdown(prompt)

    # OpenAI API に送信して、返答を表示
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    # 履歴に追加
    st.session_state.messages.append({"role": "assistant", "content": response})
