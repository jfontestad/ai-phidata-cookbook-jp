"""
総合企業分析レポート生成エージェントのデモンストレーション

このスクリプトは、企業の財務情報とニュースを統合し、
包括的な分析レポートを生成するエージェントの実装例を示します。

必要なパッケージのインストール:
pip install openai duckduckgo-search yfinance

主な機能:
- 株式市場データの取得と分析
- ウェブ検索によるニュース収集
- 表形式でのデータ表示
- ストリーミング形式でのレポート生成
"""

# 必要なライブラリのインポート
from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

# 総合レポート生成エージェントの設定
# 財務情報とニュース検索機能を持つエージェントを初期化
agent = Agent(
    model=OpenAIChat(id="gpt-4o"),  # GPT-4モデルを使用
    tools=[
        DuckDuckGo(),                    # ウェブ検索機能を有効化
        YFinanceTools(enable_all=True)   # 全ての財務情報取得機能を有効化
    ],
    instructions=[
        "データは表形式で分かりやすく表示してください",
        "財務情報とニュースを適切に整理して提示してください"
    ],
    show_tool_calls=True,  # ツール呼び出しの表示を有効化
    markdown=True,         # マークダウン形式での出力を有効化
)

# 総合企業分析レポートの生成
agent.print_response(
    "NVDAについて、財務情報と最新ニュースを含む詳細なレポートを作成してください",
    stream=True  # ストリーミング形式での出力を有効化
)
