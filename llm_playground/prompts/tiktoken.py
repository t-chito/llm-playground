"""
- コード: https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb
- テスト: https://platform.openai.com/tokenizer
- モデル情報: https://note.com/mega_gorilla/n/n298af1f3563b
"""

import tiktoken


def get_token_count(text: str) -> int:
    tiktoken_encoding = tiktoken.encoding_for_model("gpt-4-turbo-preview")
    encoded = tiktoken_encoding.encode(text)
    token_count = len(encoded)
    return token_count
