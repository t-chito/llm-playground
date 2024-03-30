"""
- [E-3 あなたの手元の本よりいい方法がある！ UXデザインのプロはこうやってユーザーのインサイトを確実に見つける丨SESSION 講演内容丨プロダクトマネージャーカンファレンス 2022](https://2022.pmconf.jp/session/H3rn6wP6)
- [ユーザーニーズを語るなら知っておきたい！2種類の潜在ニーズとは？ | えそらLLC UX ブログ](https://esaura.jp/ux-blog/how-to-identify-users-potential-needs)
"""

from langchain.prompts import PromptTemplate

"""
事前にリサーチしたところ、一般的な資格取得者の心理には以下のようなものがありそうだとわかりました。

- 希望の仕事に就きたい
- キャリアアップしたい
- 資格の勉強をする動機づけしたい
- 受験するにあたり不安を感じる
- 将来への保険として資格がほしい
- ちゃんとした内容を学びたい
- どの資格を取るべきか知りたい
"""

template = """
あなたは経験豊富な UX リサーチャーです。
あなたは現在「{goal}」という仕事に取り組んでおり、ユーザー理解のためにインタビューを実施しました。
このインタビューのリサーチクエスチョンは、「{research_question}」です。

#タスク
[#インタビュー記録] の [## 事前アンケート 回答内容] と [## インタビュー 発話録] から、
リサーチクエスチョンに関連したユーザーの心理・考え方・価値観を取り出して要約してください。
なお、これは後の分析のための下準備であり、KA 法を行う際の背景情報として活用します。

#出力形式
markdown 形式で出力してください。
また、タスクと関係のない余計な発言は出力しないでください。

#インタビュー記録
以下は markdown 書かれたインタビューの記録です。

```markdown
{input_data}
```
"""


partial_variables = {
    "goal": "TOEIC の資格取得をサポートするスマホアプリを改善する",
    "research_question": "資格をとろうと思うきっかけの心理",
}

prompt_template = PromptTemplate.from_template(
    template=template,
    partial_variables=partial_variables,
)

with open("data/thinkit-hayama-ux-user-interview-a.md", "r", encoding="utf-8") as f:
    input_data = f.read()

prompt = prompt_template.format(input_data=input_data)
