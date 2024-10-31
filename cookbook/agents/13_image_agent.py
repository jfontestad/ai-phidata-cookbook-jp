"""
画像比較分析システム

このスクリプトは、OpenAIのGPT-4を使用して
画像の内容を分析し、画像間の違いを
検出・説明するシステムを実装します。

主な機能:
- 画像内容の詳細な分析
- 複数画像の比較検証
- 視覚的特徴の言語化
- マークダウン形式での結果表示
"""

from phi.agent import Agent
from phi.model.openai import OpenAIChat

# 画像分析用エージェントの設定
agent = Agent(
    # GPT-4モデルの使用
    model=OpenAIChat(id="gpt-4o"),
    # マークダウン形式での出力を有効化
    markdown=True,
    # エージェントへの指示
    instructions=[
        "画像の視覚的特徴を詳細に説明してください",
        "特徴的な要素や目立つ部分に注目してください",
        "画像間の違いを細かく分析してください",
        "自然な言葉で分かりやすく説明してください"
    ]
)

# 画像分析と比較を実行
agent.print_response(
    "これらの画像には何が写っていますか？画像間に違いはありますか？",
    # 分析対象の画像を指定
    images=[
        # ウィスコンシン州マディソンの自然遊歩道の画像
        "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/" \
        "Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
        # 同じ画像を比較のために再度指定
        "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/" \
        "Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
    ],
    stream=True  # 分析結果をストリーミング形式で表示
)
