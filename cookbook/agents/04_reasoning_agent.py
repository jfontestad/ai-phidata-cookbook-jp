"""
推論エージェントのデモンストレーション

このスクリプトは、複雑な問題に対して論理的な推論を行い、
段階的に解決策を導き出すAIエージェントの実装例を示します。

主な機能:
- 論理的思考プロセスの展開
- 段階的な問題解決
- 推論過程の明確な説明
"""

from phi.agent import Agent
from phi.model.openai import OpenAIChat

# 推論エージェントの設定
reasoning_agent = Agent(
    name="Reasoning Agent",
    model=OpenAIChat(id="gpt-4o"),
    instructions=[
        "問題を段階的に分析してください",
        "各ステップでの推論過程を明確に説明してください",
        "結論に至るまでの思考の流れを示してください",
        "必要に応じて複数の視点から検討してください"
    ],
    show_tool_calls=True,
    markdown=True,
)

# 実行例：論理パズルの解決
query = """
以下の論理パズルを解いてください：

3つの箱があり、1つには金貨、1つには銀貨、1つは空です。
各箱には表示があり、以下のうち1つだけが真実です：

箱1: 「この箱には金貨が入っている」
箱2: 「この箱は空である」
箱3: 「銀貨は箱1に入っている」

各箱の中身を論理的に導き出してください。
"""

reasoning_agent.print_response(query, stream=True)
