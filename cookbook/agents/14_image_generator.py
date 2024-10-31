"""
DALL-E画像生成システム

このスクリプトは、OpenAIのGPT-4とDALL-Eを組み合わせて
自然言語の説明から画像を生成する
AIシステムを実装します。

主な機能:
- 自然言語による画像生成
- GPT-4による生成指示の最適化
- デバッグモードでの詳細な動作確認
- 生成画像のURL提供
"""

from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.dalle import Dalle

# 画像生成エージェントの設定
agent = Agent(
    # GPT-4モデルの使用
    model=OpenAIChat(id="gpt-4o"),
    # DALL-E画像生成ツールの追加
    tools=[Dalle()],
    # 出力設定
    markdown=True,      # マークダウン形式での出力
    debug_mode=True,    # デバッグモードの有効化
    # エージェントへの指示
    instructions=[
        "DALL-Eを使用して画像を生成するAIアシスタントとして動作します",
        "生成された画像のURLを必ず応答に含めてください",
        "生成画像の特徴や意図した表現について説明を添えてください",
        "画像生成の過程で考慮した要素についても言及してください",
        "生成された画像の品質や特徴を確認し、フィードバックを提供してください"
    ],
)

# シャム猫の画像を生成
agent.print_response(
    "白いシャム猫の画像を生成してください。" \
    "優雅で気品のある雰囲気を表現してください。",
    stream=True  # 生成過程をリアルタイムで表示
)
