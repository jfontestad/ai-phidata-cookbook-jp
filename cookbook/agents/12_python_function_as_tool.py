"""
Hacker Newsトップ記事分析システム

このスクリプトは、Hacker Newsのトップ記事を
自動取得し、AIエージェントが内容を要約・分析する
システムを実装します。

主な機能:
- Hacker News APIからのリアルタイムデータ取得
- トップ記事の自動収集と整形
- AI による記事の要約と分析
- ストリーミング形式での結果表示
"""

import json
import httpx

from phi.agent import Agent


def get_top_hackernews_stories(num_stories: int = 10) -> str:
    """Hacker Newsのトップ記事を取得する関数

    Args:
        num_stories (int): 取得する記事数（デフォルト: 10）

    Returns:
        str: トップ記事のJSON文字列
    """

    # トップ記事のIDを取得
    response = httpx.get("https://hacker-news.firebaseio.com/v0/topstories.json")
    story_ids = response.json()

    # 記事の詳細情報を取得
    stories = []
    for story_id in story_ids[:num_stories]:
        # 各記事の詳細情報をAPI経由で取得
        story_response = httpx.get(
            f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
        )
        story = story_response.json()
        # 本文テキストは除外（要約対象外）
        if "text" in story:
            story.pop("text", None)
        stories.append(story)
    return json.dumps(stories)


# ニュース分析用エージェントの設定
agent = Agent(
    # ツールの設定
    tools=[get_top_hackernews_stories],
    # 動作の可視化設定
    show_tool_calls=True,  # ツール呼び出しを表示
    markdown=True,         # マークダウン形式で出力
    # エージェントへの指示
    instructions=[
        "記事の要点を簡潔に抽出してください",
        "重要なトピックスを優先的に取り上げてください",
        "技術的な内容は分かりやすく説明してください",
        "記事間の関連性があれば言及してください"
    ]
)

# トップ5記事の要約を生成
agent.print_response(
    "Hacker Newsのトップ5記事を要約してください",
    stream=True  # 要約をストリーミング形式で表示
)
