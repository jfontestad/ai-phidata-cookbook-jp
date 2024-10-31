"""
メトリクス分析付き株価取得エージェントのデモンストレーション

このスクリプトは、株価データの取得に加えて、
実行時の詳細なメトリクス情報を表示するエージェントの実装例を示します。

主な機能:
- 株価データの取得
- ストリーミング形式でのレスポンス
- メッセージごとのメトリクス表示
- 集計メトリクスの分析
"""

# 必要なライブラリのインポート
from typing import Iterator
from rich.pretty import pprint
from phi.agent import Agent, RunResponse
from phi.model.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools
from phi.utils.pprint import pprint_run_response

# 株価取得エージェントの設定
# メトリクス分析機能を含むエージェントを初期化
agent = Agent(
    model=OpenAIChat(id="gpt-4o"),  # GPT-4モデルを使用
    tools=[YFinanceTools(stock_price=True)],  # 株価取得ツールを有効化
    markdown=True,  # マークダウン形式での出力を有効化
    show_tool_calls=True,  # ツール呼び出しの表示を有効化
)

# ストリーミング形式での株価情報取得
run_stream: Iterator[RunResponse] = agent.run(
    "NVDAの現在の株価を教えてください",
    stream=True  # ストリーミングモードを有効化
)
# レスポンスの表示（マークダウン形式）
pprint_run_response(run_stream, markdown=True)

# メッセージごとのメトリクス表示
if agent.run_response.messages:
    for message in agent.run_response.messages:
        if message.role == "assistant":
            # メッセージ内容の表示
            if message.content:
                print(f"メッセージ内容: {message.content}")
            # ツール呼び出し情報の表示
            elif message.tool_calls:
                print(f"使用ツール: {message.tool_calls}")
            # メッセージごとのメトリクス表示
            print("---" * 5, "個別メトリクス", "---" * 5)
            pprint(message.metrics)
            print("---" * 20)

# 集計メトリクスの表示
print("---" * 5, "総合メトリクス", "---" * 5)
pprint(agent.run_response.metrics)
