"""
AIエージェントチームのデモンストレーション

このスクリプトは、複数のAIエージェントが協力して問題を解決する方法を示します。
各エージェントは特定の役割を持ち、チームとして効率的に作業を進めます。

主な機能:
- 複数のエージェントによるチーム編成
- 役割に基づいた作業分担
- エージェント間のコミュニケーション
"""

from phi.assistant import Assistant
from phi.tools.search import search

# チームメンバーの定義
researcher = Assistant(
    name="researcher",
    role="Research Assistant",
    instructions="""
    あなたは優秀なリサーチアシスタントです。
    - 与えられたトピックについて詳細な調査を行います
    - 信頼できる情報源から正確な情報を収集します
    - 重要なポイントを簡潔にまとめます
    """,
    tools=[search],
)

writer = Assistant(
    name="writer",
    role="Content Writer",
    instructions="""
    あなたは経験豊富なコンテンツライターです。
    - 研究結果を魅力的な文章に変換します
    - 読者が理解しやすい構成で情報を整理します
    - 専門用語を適切に説明します
    """,
)

editor = Assistant(
    name="editor",
    role="Content Editor",
    instructions="""
    あなたは熟練した編集者です。
    - 文章の品質と正確性を確認します
    - 文法や表現の改善を提案します
    - 全体の一貫性を確保します
    """,
)

# チームの作成
team = [researcher, writer, editor]

# チーム全体での作業実行
def run_team(query: str):
    """
    チーム全体で作業を実行する関数
    
    Args:
        query: 処理するクエリ文字列
    """
    # リサーチャーによる調査
    research_results = researcher.run(
        f"""
        以下のトピックについて調査してください：
        {query}
        
        重要なポイントと事実を箇条書きでまとめてください。
        """
    )

    # ライターによるコンテンツ作成
    draft = writer.run(
        f"""
        以下の研究結果を基に、魅力的な記事を作成してください：
        {research_results}
        
        読者が理解しやすい構成で、専門用語の説明も含めてください。
        """
    )

    # エディターによる編集
    final_content = editor.run(
        f"""
        以下の記事を編集してください：
        {draft}
        
        文法、表現、一貫性を確認し、必要な改善を行ってください。
        """
    )

    return final_content

# メイン処理
if __name__ == "__main__":
    # クエリの実行例
    query = "量子コンピューティングの基本原理と現在の開発状況について"
    result = run_team(query)
    print("\n最終結果:")
    print(result)
