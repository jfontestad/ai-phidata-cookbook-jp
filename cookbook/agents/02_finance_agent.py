"""
金融分析AIアシスタントのデモンストレーション

このスクリプトは、金融データの分析と投資アドバイスを提供する
専門的なAIアシスタントの実装例を示します。
実行前に以下のパッケージのインストールが必要です：
pip install yfinance

主な機能:
- 株価データの取得と分析
- アナリストの推奨事項の確認
- 企業情報の取得
- 企業ニュースの分析
"""

from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools

# 金融アシスタントの作成
finance_agent = Agent(
    name="finance_agent",
    model=OpenAIChat(id="gpt-4o"),  # または "gpt-3.5-turbo" を使用
    tools=[YFinanceTools(
        stock_price=True,           # 株価データの取得を有効化
        analyst_recommendations=True,# アナリスト推奨の取得を有効化
        company_info=True,          # 企業情報の取得を有効化
        company_news=True           # 企業ニュースの取得を有効化
    )],
    instructions=[
        "あなたは経験豊富な金融アドバイザーです。",
        "データはできるだけ表形式で表示します",
        "株価データと市場動向を分析します",
        "アナリストの推奨事項を考慮します",
        "企業の財務情報と最新ニュースを確認します",
        "客観的なデータに基づいた判断を提供します",
        "投資リスクについての注意事項を必ず含めます",
        "専門用語には簡単な説明を添えます"
    ],
    show_tool_calls=True,
    markdown=True,
)

# アシスタントの実行例
if __name__ == "__main__":
    # 例: NVIDIAの分析を要求
    finance_agent.print_response(
        """
        NVIDIAの投資分析をお願いします：
        1. 現在の株価と推移
        2. アナリストの推奨事項
        3. 最近の重要ニュース
        4. 投資リスクの評価
        """,
        stream=True
    )
