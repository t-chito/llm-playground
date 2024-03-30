"""
- [E-3 あなたの手元の本よりいい方法がある！ UXデザインのプロはこうやってユーザーのインサイトを確実に見つける丨SESSION 講演内容丨プロダクトマネージャーカンファレンス 2022](https://2022.pmconf.jp/session/H3rn6wP6)
- [ユーザーニーズを語るなら知っておきたい！2種類の潜在ニーズとは？ | えそらLLC UX ブログ](https://esaura.jp/ux-blog/how-to-identify-users-potential-needs)
"""

from langchain.prompts import PromptTemplate

# .understand_context
from .understand import (
    input_data,
    partial_variables,
)

template = """
あなたは経験豊富な UX リサーチャーです。
あなたは現在「{goal}」という仕事に取り組んでおり、ユーザー理解のためにインタビューを実施しました。
このインタビューのリサーチクエスチョンは、「{research_question}」です。

インタビューの記録は [#インタビュー記録] に記載しています。
また、インタビューからユーザーの「リサーチクエスチョンに関連した心理・考え方・価値観」を
取り出して要約したものを [#ユーザー心理の要約] に記載しています。

#タスク
[#ユーザー心理の要約] と [#インタビュー記録] を比較して、
[#ユーザー心理の要約] に間違いや過不足が無いかを確認し、必要があれば適宜修正してください。

なお、これは後の分析のための下準備であり、KA 法を行う際の背景情報として活用します。

#出力形式
[#ユーザー心理の要約] を修正した結果を markdown 形式で出力してください。
また、例えば要約自体の評価など、修正結果以外のものは出力に含めないでください。

#ユーザー心理の要約
{context}

#インタビュー記録
以下は markdown 書かれたインタビューの記録です。

```markdown
{input_data}
```
"""

prompt_template = PromptTemplate.from_template(
    template=template,
    partial_variables=(partial_variables | {"input_data": input_data}),
)
