"""
# KA 法における出来事生成

- [ユーザーインタビューからその後どうするの？ 発話録からKA法（本質的価値抽出法）でインサイトを見つけよう！](https://www.slideshare.net/storywriterjp/ka-256785136)
- [KA法（本質的価値抽出法）の手順と実例「資格試験を受ける人のモチベーションの価値マップ」](https://www.figma.com/community/file/1142124393231568930/ka)
"""

from langchain.prompts import PromptTemplate

template = """
あなたは経験豊富な UX リサーチャーです。
あなたは現在「{goal}」という仕事に取り組んでおり、ユーザー理解のためにインタビューを実施しました。
このインタビューのリサーチクエスチョンは、「{research_question}」です。

#タスク
[#インタビュー記録] の [## インタビュー 発話録] から、KA 法の作法に従って「出来事」を 50 個以上取り出してください。
具体的な作業方法は [#作業ルール] と [#サンプル] に従ってください。

# 作業ルール
ユーザーの発話から、ユーザーの行動・気持ち・疑問などが現れている部分を「出来事」として抜き出してください。
なお、ユーザーの発言の (句点で区切られた) 一文ごとに、1 枚の出来事を作成するのが目安です。
「出来事」を書く際に守るべきことは以下です。

- 元の文章を変更せず、そのまま引用するようにしてください。
- 動詞が含まれている文章の形で引用してください。
- モデレーターの発言は「出来事」に含めてはいけません。

#サンプル
発話録の例：
```
Aさん：洋画を観て、まず洋画聞けるようになりたいなっていうのと、
あとは最終目標はやっぱりTOEFLとか、しっかり話せる状態を作りたいなとは思ったんですけど、
何もこれまでの実績がないと、TOEIC何点とかがないような状態でそこを目指すのは、
ちょっといきなりモチベーション的に持たないんじゃないかと思い、
```

出来事の例：
```
- 出来事：洋画を観て、まず洋画聞けるようになりたい
- 出来事：最終目標はやっぱりTOEFLとか、しっかり話せる状態を作りたい
- 出来事：何もこれまでの実績がないと、TOEIC何点とかがないような状態でそこを目指すのは、ちょっといきなりモチベーション的に持たない
```

#出力形式
[#サンプル] の [出来事の例] のような形式で出力してください。
繰り返しますが、「出来事」は 50 個以上取り出してください。

#インタビュー記録
以下はインタビュー調査の逐語録を含めた markdown 形式のデータです。

```markdown
{input_data}
```
"""

with open("data/thinkit-hayama-ux-user-interview-a.md", "r", encoding="utf-8") as f:
    input_data = f.read()
    # 出力がアンケートに依存しているのでトリミングしてみる
    input_data = input_data.split("## インタビュー 発話録")[1]

partial_variables = {
    "input_data": input_data,
    "goal": "TOEIC の資格取得をサポートするスマホアプリを改善する",
    "research_question": "資格をとろうと思うきっかけの心理",
}

prompt_template = PromptTemplate.from_template(
    template=template,
    partial_variables=partial_variables,
)

prompt = prompt_template.format()
