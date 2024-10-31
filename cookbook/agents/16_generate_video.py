"""
AI動画生成システム

このスクリプトは、ModelsLabsのVideoGen APIを使用して
自然言語の説明から動画を自動生成する
システムを実装します。

主な機能:
- テキストプロンプトからの動画生成
- 生成過程のリアルタイム監視
- 詳細なデバッグ情報の表示
- 生成動画のURL提供
"""

from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.models_labs import ModelsLabs

# 動画生成エージェントの設定
agent = Agent(
    # エージェントの基本設定
    name="Video Generation Agent",         # エージェント名
    agent_id="video-generation-agent",     # エージェントID
    # GPT-4モデルの使用
    model=OpenAIChat(id="gpt-4o"),
    # VideoGen APIツールの追加
    tools=[ModelsLabs()],
    # 出力設定
    markdown=True,       # マークダウン形式での出力
    debug_mode=True,     # デバッグモードの有効化
    show_tool_calls=True,  # ツール呼び出しの表示
    # エージェントへの指示
    instructions=[
        "VideoGen APIを使用して動画を生成するアシスタントとして動作します",
        "動画生成要求には generate_video 関数を使用してください",
        "特に指定がない限り、generate_video 関数には 'prompt' パラメータのみを渡してください",
        "生成状況（status）と推定所要時間（eta）を応答に含めてください",
        "生成完了後は、APIからの動画URLのみを返してください"
    ],
    # システムメッセージ
    system_message="ユーザーから明示的な指定がない限り、" \
                  "generate_video 関数のデフォルトパラメータは変更しないでください。"
)

# 猫の動画を生成
agent.print_response(
    "ボールで遊ぶ猫の動画を生成してください。" \
    "可愛らしく楽しげな雰囲気を演出してください。",
    stream=True  # 生成過程をリアルタイムで表示
)
