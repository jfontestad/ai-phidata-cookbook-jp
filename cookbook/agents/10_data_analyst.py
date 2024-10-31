"""
DuckDBを使用した映画データ分析システム

このスクリプトは、DuckDBを使用してIMDBの映画データを
分析し、統計情報をアスキーアートで可視化する
データアナリストエージェントを実装します。

主な機能:
- DuckDBによる効率的なデータ分析
- ヒストグラムのアスキーアート表示
- 最適なバケットサイズの自動選択
- 分析プロセスの詳細な説明

必要なパッケージのインストール:
pip install duckdb
"""

import json

from phi.model.openai import OpenAIChat
from phi.agent.duckdb import DuckDbAgent

# データアナリストエージェントの設定
data_analyst = DuckDbAgent(
    # GPT-4モデルの使用
    model=OpenAIChat(model="gpt-4o"),
    markdown=True,  # マークダウン形式での出力
    # データモデルの定義
    semantic_model=json.dumps(
        {
            "tables": [
                {
                    "name": "movies",
                    "description": "IMDBから取得した映画情報のデータセット。" \
                                "評価点、公開年、ジャンルなどの情報を含む。",
                    "path": "https://phidata-public.s3.amazonaws.com/demo_data/IMDB-Movie-Data.csv",
                }
            ]
        },
        indent=2,
    ),
    # エージェントへの指示
    instructions=[
        "分析手法の選択理由を明確に説明してください",
        "データの特性を考慮した可視化を行ってください",
        "統計的な意味を持つバケットサイズを選択してください",
        "視覚的に分かりやすい表示を心がけてください"
    ]
)

# 評価点の分布を分析
data_analyst.print_response(
    """
    映画の評価点についてヒストグラムを作成してください。
    適切なバケットサイズを選択し、その選択理由も説明してください。
    結果はアスキーアートで見やすく表示してください。
    """,
    stream=True  # 分析過程をリアルタイムで表示
)
