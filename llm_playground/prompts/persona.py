"""
- 地理的変数
- 人口動態変数
- 心理的変数
- 行動変数

ペルソナ

- [UI/UXデザインにおけるペルソナの作り方](https://enlyt.co.jp/blog/ui-ux-persona/)
- [UXデザインにおけるペルソナの作り方を徹底解説！](https://esaura.jp/ux-blog/how-to-create-personas)
- [カスタマージャーニーにおけるペルソナの重要さと設定方法を解説](https://blog.nijibox.jp/article/persona_customer-journey/#%E3%83%9A%E3%83%AB%E3%82%BD%E3%83%8A%E3%81%A8%E3%81%AF)
- [ペルソナ設定シートの作り方｜toBとtoCの両方を紹介](https://www.uxdl.jp/column/persona-sheet)

セグメンテーション

- [セグメンテーション（セグメント分け）とは？事例で学ぶセグメンテーションと方法](https://product-senses.mazrica.com/senseslab/column/segmentation-marketing-strategy#i-2)
- [顧客分析の手順 - データの整理](https://qiita.com/hchd/items/c1c3766a2a7c4999129c)
- [セグメンテーションとは？使い方や活用事例](https://business.adobe.com/jp/blog/how-to/how-to-use-segmentation)
- [顧客分析ってどのようにやるの？実践編ー代表的な9つの手法について解説ー](https://lb-media.jp/marketing/basic_knowledge_sales_marketing_0029/#i-5)
- [マーケティング活動で重要な顧客理解を深める方法やフレームワークを解説！](https://www.incudata.co.jp/magazine/2020/000153.html)
"""

from langchain.prompts import PromptTemplate

template = """
あなたは経験豊富な UX リサーチャーです。
[# 背景] と [# データ] に記載の情報をもとに、ユーザーのペルソナを作成してください。
ただし、具体的な作業方法は [# ルール] に従い、出力形式は [# 出力形式] を厳守してください。

# 背景
あなたは「TOEIC の資格取得をサポートするスマホアプリを改善したい」と考えています。
そこであなたは、ユーザーの「資格取得の体験の全体像」や「世界観」を理解するため、半構造化インタビューを実施しました。
今回のリサーチクエスチョンは、「資格をとろうと思うきっかけの心理」です。

事前にリサーチしたところ、一般的な資格取得者の心理には以下のようなものがありそうだとわかりました。

- 希望の仕事に就きたい
- キャリアアップしたい
- 資格の勉強をする動機づけしたい
- 受験するにあたり不安を感じる
- 将来への保険として資格がほしい
- ちゃんとした内容を学びたい
- どの資格を取るべきか知りたい

# ルール
[# データ] の [## 事前アンケート 回答内容] と [## インタビュー 発話録] から、
以下の情報をまとめ上げ、ペルソナを作成してください。

- 地理的変数
- 人口動態変数
- 心理的変数

ただし、「地理的変数」「人口動態変数」については、明示的に書かれた事実を元に記載してください。
逆に、「心理的変数」については、発話内容から推測しても構いませんので、なるべく多くの情報を詳細に記載してください。

# 出力形式
以下のような、ネストしたリストの形式で出力してください。
ただし、各変数以下に並べた項目はあくまで例のために記載したものです。実態に合わせて自由に増減させてください。
当然、内容についても実際のペルソナに合わせて記載してください。

```markdown
- 地理的変数
  - 住んでいる場所：東京都
- 人口動態変数
  - 年齢：30歳
  - 性別：男性
  - 職業：会社員
- 心理的変数
  - ライフスタイル：アウトドア派で、週末は山登りをすることが多い。平日は仕事が忙しいため、家でゆっくり過ごすことが多い。
  - 価値観：失敗を恐れず、新しいことにチャレンジすることで成長できると考えている。
  - 好み：高級志向で、ブランド品を好む。また、美味しいものを食べることが好き。
  - 性格：社交的で、人とのコミュニケーションを大切にする。また、人の役に立つことが好き。
  - 悩み：資格試験の勉強時間が確保できないことが悩み。
```

# データ
以下はインタビュー調査の逐語録を含めた markdown 形式のデータです。

```markdown
{input_data}
```
"""

with open("data/thinkit-hayama-ux-user-interview-a.md", "r", encoding="utf-8") as f:
    input_data = f.read()

partial_variables = {
    "input_data": input_data,
}

prompt_template = PromptTemplate.from_template(
    template=template,
    partial_variables=partial_variables,
)

prompt = prompt_template.format()
