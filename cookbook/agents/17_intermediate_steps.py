"""
株価取得エージェントのデモンストレーション

このスクリプトは、YFinance APIを使用して株価データを取得し、
ストリーミング形式でレスポンスを返すエージェントの実装例を示します。

主な機能:
- リアルタイムの株価データ取得
- ストリーミング形式でのレスポンス
- 中間処理ステップの表示
"""

# 必要なライブラリのインポート
from typing import Iterator
from rich.pretty import pprint
from phi.agent import Agent, RunResponse
from phi.model.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools

# エージェントの設定
# YFinance APIを使用して株価データを取得するエージェントを初期化
agent = Agent(
    model=OpenAIChat(id="gpt-4o"),  # GPT-4モデルを使用
    tools=[YFinanceTools(stock_price=True)],  # 株価取得ツールを有効化
    markdown=True,  # マークダウン形式での出力を有効化
    show_tool_calls=True,  # ツール呼び出しの表示を有効化
)

# エージェントの実行とストリーミングレスポンスの取得
run_stream: Iterator[RunResponse] = agent.run(
    "NVDAの現在の株価を教えてください",  # 株価照会クエリ
    stream=True,  # ストリーミングを有効化
    stream_intermediate_steps=True  # 中間ステップの表示を有効化
)

# ストリーミングレスポンスの処理と表示
for chunk in run_stream:
    # messagesを除外したレスポンスデータを表示
    pprint(chunk.model_dump(exclude={"messages"}))
    # 区切り線の表示
    print("---" * 20)
