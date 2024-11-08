"""
Webサーチ機能を持つAIアシスタントのデモンストレーション

このスクリプトは、Web検索機能を活用してユーザーの質問に回答する
AIアシスタントの基本的な使用方法を示します。

主な機能:
- Web検索ツールの統合
- 検索結果に基づく回答生成
- 情報の正確性と最新性の確保
"""

from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo

# Web検索機能を持つエージェントの作成
web_agent = Agent(
    name="web_agent",
    model=OpenAIChat(id="gpt-4o"),  # または "gpt-3.5-turbo" を使用
    tools=[DuckDuckGo()],
    instructions=[
        "あなたは優秀なリサーチ専門家です。",
        "Web検索を活用して最新の情報を収集します",
        "信頼できる情報源からデータを取得します",
        "検索結果を分析し、正確な回答を提供します",
        "情報の出典を明確に示します"
    ],
    show_tool_calls=True,
    markdown=True,
)

# エージェントの実行例
if __name__ == "__main__":
    web_agent.print_response(
        "2024年の人工知能の主要なトレンドについて教えてください。",
        stream=True
    )
