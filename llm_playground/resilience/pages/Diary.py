"""
https://docs.streamlit.io/library/api-reference/data/st.data_editor
"""

from datetime import date
from typing import TypedDict

import pandas as pd
import streamlit as st

title = "日記"

st.set_page_config(page_title=title)
st.markdown(f"# {title}")
st.sidebar.header(title)


class ABCDiary(TypedDict):
    date: date
    event: str
    emotion: str  # list の編集はサポートされていないので一旦 str で
    behavior: str
    rating: int


default_diary: ABCDiary = {
    "date": date.today(),
    "event": "仕事でミスをした",
    "emotion": "悔しい",
    "behavior": "自分を責めた",
    "rating": 4,
}

df = pd.DataFrame([default_diary])

# df.rename(columns={"A": "Col_1"}, inplace=True)

edited_df = st.data_editor(df, num_rows="dynamic")

targets = edited_df[edited_df["rating"] >= 4]
st.markdown(f"今回はこれらを分析してみましょう： **{'、'.join(targets.event.values)}**")
