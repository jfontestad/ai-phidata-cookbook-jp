"""
IMDBデータ分析エージェント

このスクリプトは、IMDBの映画データを分析する
Pythonコードを自動生成・実行できるAIエージェントを
実装したシステムです。

主な機能:
- CSVファイルからの映画データの読み込み
- 統計分析の自動実行
- 必要なパッケージの自動インストール
- 分析結果の可視化と説明
"""

from pathlib import Path

from phi.agent.python import PythonAgent
from phi.model.openai import OpenAIChat
from phi.file.local.csv import CsvFile

# 作業ディレクトリの設定
cwd = Path(__file__).parent.resolve()
# 一時ファイル用ディレクトリの作成
tmp = cwd.joinpath("tmp")
if not tmp.exists():
    tmp.mkdir(exist_ok=True, parents=True)

# Python実行可能なAIエージェントの設定
python_agent = PythonAgent(
    # GPT-4モデルの使用
    model=OpenAIChat(id="gpt-4o"),
    # 作業ディレクトリの指定
    base_dir=tmp,
    # 分析対象ファイルの設定
    files=[
        CsvFile(
            path="https://phidata-public.s3.amazonaws.com/demo_data/IMDB-Movie-Data.csv",
            description="IMDBから取得した映画情報のデータセット。" \
                      "評価、ジャンル、監督、出演者などの情報を含む。",
        )
    ],
    # エージェントへの指示
    instructions=[
        "データの前処理手順を説明してください",
        "分析結果は視覚的に分かりやすく表示してください",
        "統計的な考察も含めて解説してください",
        "異常値や欠損値の処理方法も明示してください"
    ],
    markdown=True,         # マークダウン形式での出力
    pip_install=True,     # 必要なパッケージの自動インストール
    show_tool_calls=True  # ツール呼び出しの表示
)

# 映画の平均評価点を分析
python_agent.print_response(
    "映画の平均評価点を分析してください",
    stream=True  # 分析過程をリアルタイムで表示
)
