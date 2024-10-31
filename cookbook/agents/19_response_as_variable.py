"""
総合株式情報取得エージェントのデモンストレーション

このスクリプトは、YFinance APIを使用して以下の株式関連情報を
包括的に取得・分析するエージェントの実装例を示します。

取得可能な情報:
- 株価データ
- アナリストの推奨情報
- 企業情報
- 企業ニュース

出力形式:
- 表形式での情報表示
- 整形されたマークダウン形式
"""

# 必要なライブラリのインポート
from typing import Iterator  # noqa
from rich.pretty import pprint
from phi.agent import Agent, RunResponse
from phi.model.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools

# 総合株式情報エージェントの設定
# 複数の株式情報取得機能を持つエージェントを初期化
agent = Agent(
    model=OpenAIChat(id="gpt-4o"),  # GPT-4モデルを使用
    tools=[YFinanceTools(
        stock_price=True,              # 株価取得機能を有効化
        analyst_recommendations=True,   # アナリスト推奨情報取得を有効化
        company_info=True,             # 企業情報取得を有効化
        company_news=True              # 企業ニュース取得を有効化
    )],
    instructions=[
        "可能な限り情報を表形式で表示してください",
        "データは見やすく整理して提示してください"
    ],
    show_tool_calls=True,  # ツール呼び出しの表示を有効化
    markdown=True,         # マークダウン形式での出力を有効化
)

# 単一レスポンスでの株価情報取得
run_response: RunResponse = agent.run("NVDAの現在の株価を教えてください")
pprint(run_response)

# ストリーミングレスポンスでの株価情報取得（コメントアウト状態）
# run_response_stream: Iterator[RunResponse] = agent.run(
#     "NVDAの現在の株価を教えてください", 
#     stream=True  # ストリーミングモードを有効化
# )
# for response in run_response_stream:
#     pprint(response)  # 逐次的にレスポンスを表示
