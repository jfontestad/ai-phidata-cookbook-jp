"""
金融分析AIアシスタントのデモンストレーション

このスクリプトは、金融データの分析と投資アドバイスを提供する
専門的なAIアシスタントの実装例を示します。

主な機能:
- 金融市場の分析
- 投資戦略の提案
- リスク評価
"""

from phi.assistant import Assistant
from phi.tools.search import search

# 金融アシスタントの作成
finance_assistant = Assistant(
    name="finance_assistant",
    role="Financial Advisor",
    instructions="""
    あなたは経験豊富な金融アドバイザーです。
    - 金融市場の動向を分析します
    - 投資戦略について助言を提供します
    - リスクとリターンのバランスを考慮します
    - 市場データに基づいた客観的な判断を行います
    - 投資家の目標とリスク許容度を考慮します
    """,
    tools=[search],
)

# アシスタントの実行例
if __name__ == "__main__":
    response = finance_assistant.run(
        "現在の世界経済の状況と、長期投資家向けの推奨される投資戦略について分析してください。"
    )
    print("\n分析結果:")
    print(response)
