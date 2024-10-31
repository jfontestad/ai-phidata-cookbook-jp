"""
マルチエージェント分析プレイグラウンド

このスクリプトは、Web検索と金融データ分析が可能な
2つの特化型AIエージェントを実装し、それらを
インタラクティブなプレイグラウンドで利用できるようにします。

主な機能:
- Webからの情報収集と分析
- 株式市場データのリアルタイム分析
- 会社情報や市場ニュースの取得
- 過去の対話履歴の保存と参照
"""

from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.storage.agent.sqlite import SqlAgentStorage
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from phi.playground import Playground, serve_playground_app

# Web検索特化型エージェントの設定
web_agent = Agent(
    name="Web Agent",  # エージェント名
    model=OpenAIChat(id="gpt-4o"),  # GPT-4モデルの使用
    # DuckDuckGoを使用したWeb検索ツールの追加
    tools=[DuckDuckGo()],
    # エージェントへの指示
    instructions=[
        "回答には必ず情報源を含めてください",
        "信頼性の高いソースを優先して参照してください",
        "最新の情報を提供するよう心がけてください",
        "複数の情報源を比較検証してください"
    ],
    # 対話履歴のSQLiteでの保存設定
    storage=SqlAgentStorage(
        table_name="web_agent",
        db_file="agents.db"
    ),
    add_history_to_messages=True,  # 過去の対話履歴を考慮
    markdown=True,  # マークダウン形式での出力
)

# 金融分析特化型エージェントの設定
finance_agent = Agent(
    name="Finance Agent",  # エージェント名
    model=OpenAIChat(id="gpt-4o"),  # GPT-4モデルの使用
    # 金融データ分析ツールの設定
    tools=[YFinanceTools(
        stock_price=True,          # 株価データの取得
        analyst_recommendations=True,  # アナリスト推奨
        company_info=True,         # 企業情報
        company_news=True          # 企業ニュース
    )],
    # エージェントへの指示
    instructions=[
        "データは表形式で分かりやすく表示してください",
        "重要な財務指標を強調して説明してください",
        "市場動向との関連性を考慮して分析してください",
        "リスク要因についても言及してください"
    ],
    # 対話履歴のSQLiteでの保存設定
    storage=SqlAgentStorage(
        table_name="finance_agent",
        db_file="agents.db"
    ),
    add_history_to_messages=True,  # 過去の対話履歴を考慮
    markdown=True,  # マークダウン形式での出力
)

# プレイグラウンドアプリケーションの設定
app = Playground(
    agents=[finance_agent, web_agent]  # 両エージェントを統合
).get_app()

# アプリケーションの起動
if __name__ == "__main__":
    # 開発モードでプレイグラウンドを起動
    serve_playground_app(
        "06_playground:app",
        reload=True  # コード変更時の自動リロード
    )
