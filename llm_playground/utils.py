
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


def save_result(result):
    """結果を保存する"""
    with open("result.txt", "w", encoding="utf-8") as f:
        f.write(result)