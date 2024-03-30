import difflib

import tiktoken
from langchain_core.messages import HumanMessage

# inner import
from models import llm_openai as llm


def get_token_count(text: str) -> int:
    """
    - コード: https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb
    - テスト: https://platform.openai.com/tokenizer
    - モデル情報: https://note.com/mega_gorilla/n/n298af1f3563b
    """
    tiktoken_encoding = tiktoken.encoding_for_model("gpt-4-turbo-preview")
    encoded = tiktoken_encoding.encode(text)
    token_count = len(encoded)
    return token_count


def get_response_once(prompt: str, llm=llm):
    """一回きりの返答を返す"""
    messages = [
        HumanMessage(content=prompt),
    ]
    result = llm.invoke(messages).content
    return result


def save_result(result, filename="result.txt"):
    """結果を保存する"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(result)


def diffplay(text_before: str, text_after: str):
    """
    文字列の差異をハイライト表示する
    https://qiita.com/youichi_io/items/a0005f9f77df2743a3fc
    """
    color_dic = {
        "red": "\033[31m",
        "green": "\033[32m",
        "end": "\033[0m",
        "BG_RED": "\033[41m",
        "BG_GREEN": "\033[42m",
    }

    d = difflib.Differ()
    diffs = d.compare(text_before, text_after)

    result = ""
    for diff in diffs:
        status, _, character = list(diff)
        if status == "-":
            character = color_dic["BG_RED"] + character + color_dic["end"]
        elif status == "+":
            character = color_dic["BG_GREEN"] + character + color_dic["end"]
        else:
            pass
        result += character

    print(result)
