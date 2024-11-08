"""
AIエージェントチームのデモンストレーション

このスクリプトは、複数のAIエージェントが協力して問題を解決する方法を示します。
各エージェントは特定の役割を持ち、チームとして効率的に作業を進めます。

実行前に必要なパッケージのインストール：
pip install yfinance duckduckgo-search

主な機能:
- 複数のエージェントによるチーム編成
- 役割に基づいた作業分担
- Web検索と金融データの統合分析
"""

from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools

# リサーチャーエージェントの定義
researcher = Agent(
    name="researcher",
    role="Research Expert",
    model=OpenAIChat(id="gpt-4"),  # または "gpt-3.5-turbo" を使用
    tools=[DuckDuckGo()],
    instructions=[
        "あなたは優秀なリサーチアシスタントです。",
        "与えられたトピックについて詳細な調査を行います",
        "信頼できる情報源から正確な情報を収集します",
        "重要なポイントを簡潔にまとめます",
        "必ず情報源を含めます",
        "データは可能な限り表形式で表示します"
    ],
    show_tool_calls=True,
    markdown=True,
)

# 金融アナリストエージェントの定義
finance_analyst = Agent(
    name="finance_analyst",
    role="Financial Expert",
    model=OpenAIChat(id="gpt-4o"),  # または "gpt-3.5-turbo" を使用
    tools=[YFinanceTools(
        stock_price=True,
        analyst_recommendations=True,
        company_info=True,
        company_news=True
    )],
    instructions=[
        "あなたは金融分析の専門家です",
        "データは必ず表形式で表示します",
        "株価データと市場動向を分析します",
        "アナリストの推奨事項を考慮します",
        "企業の財務情報と最新ニュースを確認します",
        "投資リスクについての注意事項を含めます"
    ],
    show_tool_calls=True,
    markdown=True,
)

# チームエージェントの作成
agent_team = Agent(
    name="research_team",
    team=[researcher, finance_analyst],
    instructions=[
        "情報源を必ず含めて報告してください",
        "データは表形式で表示してください",
        "分析結果は簡潔に要約してください",
        "専門用語には説明を添えてください",
        "重要なポイントは箇条書きでまとめてください"
    ],
    show_tool_calls=True,
    markdown=True,
)

# メイン処理
if __name__ == "__main__":
    # チームによる分析の実行例
    agent_team.print_response(
        """
        NVIDIAについて以下の分析をお願いします：
        1. 最新の市場動向とニュース
        2. 株価分析とアナリストの推奨事項
        3. 今後の成長機会とリスク要因
        
        総合的な分析と投資判断のポイントをまとめてください。
        """,
        stream=True
    )
