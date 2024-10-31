"""
計算エージェントのデモンストレーション

このスクリプトは、基本的な数値計算と比較を行うエージェントの実装例を示します。
四則演算（加減乗除）の機能を持ち、数値の大小比較などの判断を行います。

主な機能:
- 四則演算の実行
- 数値の比較分析
- 結果の論理的な説明
"""

# 必要なライブラリのインポート
from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.calculator import Calculator

# 計算エージェントの設定
# 四則演算と比較分析が可能なエージェントを初期化
agent = Agent(
    model=OpenAIChat(id="gpt-4o"),  # GPT-4モデルを使用
    tools=[Calculator(
        add=True,      # 加算機能を有効化
        subtract=True, # 減算機能を有効化
        multiply=True, # 乗算機能を有効化
        divide=True    # 除算機能を有効化
    )],
    instructions=[
        "数値の比較には計算ツールを使用してください",
        "結果の根拠を明確に説明してください"
    ],
    show_tool_calls=True,  # ツール呼び出しの表示を有効化
    markdown=True,         # マークダウン形式での出力を有効化
)

# 数値比較の実行例1
agent.print_response("9.11は9.9より大きいですか？")

# 数値比較の実行例2
agent.print_response("9.11と9.9のどちらが大きいですか？")
