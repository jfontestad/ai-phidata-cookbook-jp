"""
ニュース記事作成エージェントのデモンストレーション

このスクリプトは、指定されたトピックについて包括的な調査を行い、
ニューヨークタイムズスタイルの記事を生成するエージェントの実装例を示します。

必要なパッケージのインストール:
pip install openai duckduckgo-search newspaper4k lxml_html_clean phidata

主な機能:
- ウェブ検索による情報収集
- 記事本文の抽出と分析
- 高品質な記事の生成
- ストリーミング形式での出力
"""

# 必要なライブラリのインポート
from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.newspaper4k import Newspaper4k

# ニュース記事作成エージェントの設定
# 検索と記事抽出機能を持つエージェントを初期化
agent = Agent(
    model=OpenAIChat(id="gpt-4o"),  # GPT-4モデルを使用
    tools=[
        DuckDuckGo(),   # ウェブ検索機能を有効化
        Newspaper4k()    # 記事抽出機能を有効化
    ],
    description="ニューヨークタイムズの上級調査記者として記事を執筆します。",
    instructions=[
        "指定されたトピックについて、上位5つの関連リンクを検索してください。",
        "各URLから記事本文を抽出してください（アクセス不可能なURLは無視します）。",
        "収集した情報を分析し、ニューヨークタイムズ水準の記事を作成してください。"
    ],
    markdown=True,  # マークダウン形式での出力を有効化
    show_tool_calls=True,  # ツール呼び出しの表示を有効化
    add_datetime_to_instructions=True,  # 指示に日時情報を追加
    # debug_mode=True,  # デバッグモードの有効化（必要に応じてコメント解除）
)

# 記事生成の実行
agent.print_response(
    "シミュレーション理論について",  # 記事のトピック
    stream=True  # ストリーミング形式での出力を有効化
)
