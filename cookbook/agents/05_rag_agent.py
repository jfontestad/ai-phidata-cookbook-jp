"""
AI駆動のレシピ推薦システム

このスクリプトは、PDFから料理レシピの知識を抽出し、
OpenAIのGPT-4を使用して料理のレシピや手順について
インタラクティブな質問応答を行うシステムを実装します。

主な機能:
- PDF形式のレシピ本からの知識抽出
- ベクトルデータベースを使用した効率的な検索
- 自然言語での料理手順の説明
- コンテキストを考慮した質問応答

必要なパッケージのインストール:
pip install openai lancedb tantivy pypdf sqlalchemy
"""

from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.embedder.openai import OpenAIEmbedder
from phi.knowledge.pdf import PDFUrlKnowledgeBase
from phi.vectordb.lancedb import LanceDb, SearchType

# PDFからレシピの知識ベースを作成
knowledge_base = PDFUrlKnowledgeBase(
    # タイ料理のレシピPDFを指定
    urls=["https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    # ベクトルデータベースにLanceDBを使用
    vector_db=LanceDb(
        table_name="recipes",  # テーブル名の設定
        uri="tmp/lancedb",     # データベースの保存先
        search_type=SearchType.vector,  # ベクトル検索の使用
        # テキスト埋め込みモデルの設定
        embedder=OpenAIEmbedder(model="text-embedding-3-small"),
    ),
)
# 初回実行後はコメントアウトしてください（知識ベースは既にロード済み）
knowledge_base.load()

# エージェントの設定
agent = Agent(
    # GPT-4モデルの使用
    model=OpenAIChat(id="gpt-4o"),
    # 知識ベースの追加
    knowledge=knowledge_base,
    # 以下の指示をエージェントに与える
    instructions=[
        "レシピの手順を分かりやすく説明してください",
        "材料の代替案があれば提案してください",
        "調理のコツやポイントも含めて説明してください",
        "質問に応じて具体的なアドバイスを提供してください"
    ],
    show_tool_calls=True,  # ツール呼び出しの表示
    markdown=True,         # マークダウン形式での出力
)

# ココナッツミルクスープのレシピについて質問
agent.print_response(
    "ガラムガルとチキンのココナッツミルクスープの作り方を教えてください",
    stream=True  # 回答をストリーミング形式で表示
)
