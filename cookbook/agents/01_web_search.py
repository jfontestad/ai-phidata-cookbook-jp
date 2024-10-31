"""
Webサーチ機能を持つAIアシスタントのデモンストレーション

このスクリプトは、Web検索機能を活用してユーザーの質問に回答する
AIアシスタントの基本的な使用方法を示します。

主な機能:
- Web検索ツールの統合
- 検索結果に基づく回答生成
- 情報の正確性と最新性の確保
"""

from phi.assistant import Assistant
from phi.tools.search import search

# Web検索機能を持つアシスタントの作成
web_assistant = Assistant(
    name="web_assistant",
    role="Research Expert",
    instructions="""
    あなたは優秀なリサーチ専門家です。
    - Web検索を活用して最新の情報を収集します
    - 信頼できる情報源からデータを取得します
    - 検索結果を分析し、正確な回答を提供します
    - 情報の出典を明確に示します
    """,
    tools=[search],
)

# アシスタントの実行例
if __name__ == "__main__":
    response = web_assistant.run(
        "2024年の人工知能の主要なトレンドについて教えてください。"
    )
    print("\n回答:")
    print(response)
