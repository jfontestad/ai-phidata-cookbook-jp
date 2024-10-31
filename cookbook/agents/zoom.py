"""
Zoomミーティング自動スケジューリングエージェントのデモンストレーション

このスクリプトは、Zoom APIを使用して会議を自動的にスケジュールし、
会議の詳細情報を管理するエージェントの実装例を示します。

必要な環境変数:
- ZOOM_ACCOUNT_ID: ZoomアカウントID
- ZOOM_CLIENT_ID: ZoomクライアントID
- ZOOM_CLIENT_SECRET: Zoomクライアントシークレット

主な機能:
- Zoomミーティングの自動スケジュール
- 会議詳細情報の取得と表示
- エラーハンドリング
"""

# 必要なライブラリのインポート
import os
from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.zoom import ZoomTool

# Zoom API認証情報の取得
ACCOUNT_ID = os.getenv("ZOOM_ACCOUNT_ID")
CLIENT_ID = os.getenv("ZOOM_CLIENT_ID")
CLIENT_SECRET = os.getenv("ZOOM_CLIENT_SECRET")

# カスタムZoomツールクラスの定義
class CustomZoomTool(ZoomTool):
    def schedule_meeting(self, topic: str, start_time: str, duration: int) -> str:
        """
        ミーティングをスケジュールし、詳細情報を整形して返却します
        
        Parameters:
            topic (str): ミーティングの題目
            start_time (str): 開始時刻（ISO 8601形式）
            duration (int): 所要時間（分）
        
        Returns:
            str: フォーマットされたミーティング情報
        """
        response = super().schedule_meeting(topic, start_time, duration)

        if isinstance(response, str):
            import json
            try:
                meeting_info = json.loads(response)
            except json.JSONDecodeError:
                return "ミーティング情報の解析に失敗しました。"
        else:
            meeting_info = response

        if meeting_info:
            meeting_id = meeting_info.get("id")
            join_url = meeting_info.get("join_url")
            start_time = meeting_info.get("start_time")
            return (
                f"ミーティングが正常にスケジュールされました！\n\n"
                f"**ミーティングID:** {meeting_id}\n"
                f"**参加URL:** {join_url}\n"
                f"**開始時刻:** {start_time}"
            )
        else:
            return "申し訳ありません。ミーティングのスケジュールに失敗しました。"

# Zoomツールのインスタンス化
zoom_tool = CustomZoomTool(
    account_id=ACCOUNT_ID,
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET
)

# スケジューリングエージェントの設定
agent = Agent(
    name="Zoom Scheduling Agent",  # エージェント名
    agent_id="zoom-scheduling-agent",  # エージェントID
    model=OpenAIChat(id="gpt-4o"),  # GPT-4モデルを使用
    tools=[zoom_tool],  # カスタムZoomツールを使用
    markdown=True,  # マークダウン形式での出力を有効化
    debug_mode=True,  # デバッグモードを有効化
    show_tool_calls=True,  # ツール呼び出しの表示を有効化
    instructions=[
        "ZoomミーティングをスケジュールするためのエージェントとしてZoom APIを使用します。",
        "ミーティングのスケジュール時には、ZoomToolのschedule_meeting関数を使用します。",
        "特に指定がない限り、schedule_meeting関数には必要最小限のパラメータのみを渡します。",
        "スケジュール後は、ミーティングID、参加URL、開始時刻などの詳細情報を提供します。",
        "時刻は全てISO 8601形式で指定してください（例：'2024-12-28T10:00:00Z'）。",
        "エラーが発生した場合は適切に対応し、ユーザーに通知します。"
    ],
    system_message=(
        "ユーザーから明示的な指定がない限り、schedule_meeting関数のデフォルトパラメータは"
        "変更しないでください。ユーザーに確認する前に、必ずミーティングが正常に"
        "スケジュールされたことを確認してください。"
    ),
)

# エージェントを使用してミーティングをスケジュール
user_input = "「Pythonオートメーション会議」というタイトルで、2024年11月1日の午前11時（UTC）から60分間の会議をスケジュールしてください。"
response = agent.run(user_input)
