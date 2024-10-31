"""
インタラクティブ検索アシスタント

このスクリプトは、GPT-4とDuckDuckGoを組み合わせた
対話型の検索・情報分析システムを実装します。
チャット履歴を保持し、文脈を考慮した
インテリジェントな応答を提供します。

主な機能:
- Web検索との連携
- チャット履歴の管理
- 文脈を考慮した応答
- デバッグ情報の表示
- CLIベースの対話インターフェース
"""

from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo

# 検索対話エージェントの設定
agent = Agent(
    # GPT-4モデルの使用
    model=OpenAIChat(id="gpt-4o"),
    # DuckDuckGo検索ツールの追加
    tools=[DuckDuckGo()],
    # 動作設定
    show_tool_calls=True,          # ツール呼び出しの表示
    read_chat_history=True,        # チャット履歴の読み込み
    add_history_to_messages=True,  # 履歴を応答に反映
    num_history_responses=3,       # 保持する履歴応答数
    # add_history_to_messages_num=True,  # 履歴番号の付与（必要に応じて有効化）
    debug_mode=True,               # デバッグモードの有効化
    # エージェントへの指示
    instructions=[
        "ユーザーの質問に応じて適切な検索を行ってください",
        "検索結果を要約し、関連情報を整理して提供してください",
        "過去の会話文脈を考慮して応答を生成してください",
        "情報源を明確に示し、信頼性の高い情報を優先してください",
        "必要に応じて追加の質問や確認を行ってください"
    ],
)

# CLIアプリケーションの起動
agent.cli_app(
    markdown=True,  # マークダウン形式での出力を有効化
)
