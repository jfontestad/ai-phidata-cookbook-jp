"""
AIによる映画脚本生成システム

このスクリプトは、OpenAIのGPT-4を使用して
映画の脚本アイデアを自動生成する高度な
システムを実装します。同期・非同期両方の
実行モードをサポートし、構造化された出力を
リッチなフォーマットで表示します。

主な機能:
- 映画脚本の自動生成
- JSONモードと構造化出力の比較
- 非同期処理のサポート
- リッチな表示形式での出力
"""

import asyncio
from typing import List, Optional

from rich.align import Align
from rich.console import Console
from rich.panel import Panel
from rich.pretty import Pretty
from rich.spinner import Spinner
from rich.text import Text
from pydantic import BaseModel, Field

from phi.agent import Agent, RunResponse
from phi.model.openai import OpenAIChat

# コンソール出力の設定
console = Console()


# 映画脚本のデータモデルを定義
class MovieScript(BaseModel):
    setting: str = Field(..., description="ブロックバスター映画にふさわしい舞台設定を提供してください。")
    ending: str = Field(..., description="映画のエンディング。指定がない場合はハッピーエンドにしてください。")
    genre: str = Field(
        ..., description="映画のジャンル。指定がない場合はアクション、スリラー、ロマンティックコメディから選択してください。"
    )
    name: str = Field(..., description="この映画のタイトルを設定してください")
    characters: List[str] = Field(..., description="この映画の登場人物名のリスト。")
    storyline: str = Field(..., description="映画のストーリーラインを3文で表現してください。エキサイティングな内容にしてください！")


# JSONモードを使用するエージェントの設定
json_mode_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description="映画脚本を作成するAIアシスタントです。",
    response_model=MovieScript,
)

# 構造化出力を使用するエージェントの設定
structured_output_agent = Agent(
    model=OpenAIChat(id="gpt-4o-2024-08-06"),
    description="映画脚本を作成するAIアシスタントです。",
    response_model=MovieScript,
    structured_outputs=True,
)


# 出力表示用のヘルパー関数群
def display_header(
    message: str,
    style: str = "bold cyan",
    panel_title: Optional[str] = None,
    subtitle: Optional[str] = None,
    border_style: str = "bright_magenta",
):
    """
    スタイル付きヘッダーをパネル内に表示します。
    """
    title = Text(message, style=style)
    panel = Panel(Align.center(title), title=panel_title, subtitle=subtitle, border_style=border_style, padding=(1, 2))
    console.print(panel)


def display_spinner(message: str, style: str = "green"):
    """
    メッセージ付きのスピナーを表示します。
    """
    spinner = Spinner("dots", text=message, style=style)
    console.print(spinner)


def display_content(content, title: str = "Content"):
    """
    Richライブラリを使用してコンテンツを表示します。
    """
    pretty_content = Pretty(content, expand_all=True)
    panel = Panel(pretty_content, title=title, border_style="blue", padding=(1, 2))
    console.print(panel)


# 同期実行用の関数
def run_agents():
    try:
        # JSONモードエージェントの実行
        display_header("MovieScriptモデルを使用したエージェントを実行", panel_title="エージェント1")
        with console.status("エージェント1を実行中...", spinner="dots"):
            run_json_mode_agent: RunResponse = json_mode_agent.run("ニューヨーク")
        display_content(run_json_mode_agent.content, title="エージェント1の応答")

        # 構造化出力エージェントの実行
        display_header(
            "MovieScriptモデルと構造化出力を使用したエージェントを実行", panel_title="エージェント2"
        )
        with console.status("エージェント2を実行中...", spinner="dots"):
            run_structured_output_agent: RunResponse = structured_output_agent.run("ニューヨーク")
        display_content(run_structured_output_agent.content, title="エージェント2の応答")
    except Exception as e:
        console.print(f"[bold red]エージェントの実行中にエラーが発生しました: {e}[/bold red]")


# 非同期実行用の関数
async def run_agents_async():
    try:
        # JSONモードエージェントの非同期実行
        display_header("MovieScriptモデルを使用したエージェントを非同期実行", panel_title="非同期エージェント1")
        with console.status("エージェント1を実行中...", spinner="dots"):
            async_run_json_mode_agent: RunResponse = await json_mode_agent.arun("ニューヨーク")
        display_content(async_run_json_mode_agent.content, title="非同期エージェント1の応答")

        # 構造化出力エージェントの非同期実行
        display_header(
            "MovieScriptモデルと構造化出力を使用したエージェントを非同期実行",
            panel_title="非同期エージェント2",
        )
        with console.status("エージェント2を実行中...", spinner="dots"):
            async_run_structured_output_agent: RunResponse = await structured_output_agent.arun("ニューヨーク")
        display_content(async_run_structured_output_agent.content, title="非同期エージェント2の応答")
    except Exception as e:
        console.print(f"[bold red]非同期エージェントの実行中にエラーが発生しました: {e}[/bold red]")


# メイン実行部分
if __name__ == "__main__":
    # 同期実行
    run_agents()
    # 非同期実行
    asyncio.run(run_agents_async())
