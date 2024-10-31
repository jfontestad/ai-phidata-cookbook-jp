<div align="center">
  <img src="https://raw.githubusercontent.com/Sunwood-ai-labs/phidata-cookbook-jp/refs/heads/main/docs/74ccfadcf3dc58a1d3d695087ba3c01e8818ff97ebb8457de21a464e.png" width="100%">

# 🚀 phidata Agents クックブック

</div>




このリポジトリは、[phidata](https://github.com/phidatahq/phidata)のAgentsサンプル集を日本語化し、実践的なチュートリアルとして再構成したものです。AIエージェントの基本から応用まで、ステップバイステップで学ぶことができます。

## 📚 学習コンテンツ

### 基礎編: AIエージェントの基本
1. [Webサーチエージェント](01_web_search.py)
   - Web検索機能を持つ基本的なAIエージェントの実装
   - 検索結果の整形と表示方法の習得
   - 情報源の適切な引用方法

2. [金融分析エージェント](02_finance_agent.py)
   - 株式市場データの取得と分析
   - 投資戦略の提案機能の実装
   - 財務データの視覚化

3. [エージェントチーム](03_agent_team.py)
   - 複数エージェントの協調動作
   - 役割分担と情報共有の実装
   - チームワークフローの設計

### 発展編: 特殊機能の実装
4. [推論エージェント](04_reasoning_agent.py)
   - 段階的な問題解決プロセス
   - 論理的思考の実装方法
   - 推論過程の可視化

5. [RAGエージェント](05_rag_agent.py)
   - PDFからの知識ベース構築
   - ベクトルデータベースの活用
   - コンテキストを考慮した回答生成

6. [プレイグラウンド](06_playground.py)
   - インタラクティブなUIの実装
   - 複数エージェントの統合管理
   - 対話履歴の保存と参照

### 監視・デバッグ編
7. [モニタリング](07_monitoring.py)
   - エージェントの動作監視
   - パフォーマンス分析
   - ログ管理の実装

8. [デバッグ機能](08_debugging.py)
   - エラー検出と対処
   - デバッグ情報の表示
   - トラブルシューティング手法

### 実践編: 特化型エージェント
9. [Pythonエージェント](09_python_agent.py)
   - IMDBデータの分析
   - Pythonコードの自動生成と実行
   - データ可視化の実装

10. [データアナリスト](10_data_analyst.py)
    - DuckDBを使用したSQL分析
    - データの統計処理
    - アスキーアートでの可視化

### 応用編: 高度な機能実装
11. [構造化出力](11_structured_output.py)
    - Pydanticモデルの活用
    - 映画脚本生成システム
    - 非同期処理の実装

12. [Python関数ツール](12_python_function_as_tool.py)
    - Hacker Newsデータの取得と分析
    - カスタムツールの実装
    - リアルタイムデータ処理

13. [画像分析エージェント](13_image_agent.py)
    - 画像内容の分析
    - 視覚的特徴の言語化
    - 複数画像の比較

14. [画像生成エージェント](14_image_generator.py)
    - DALL-Eを使用した画像生成
    - 生成プロセスの制御
    - 画像品質の最適化

### 実用編: 実践的なアプリケーション
15. [CLIアプリケーション](15_cli_app.py)
    - コマンドライン対話の実装
    - 検索履歴の管理
    - ユーザー入力の処理

16. [動画生成](16_generate_video.py)
    - VideoGen APIの活用
    - 動画生成プロセスの制御
    - 進捗状況の監視

17. [中間処理ステップ](17_intermediate_steps.py)
    - 処理過程の可視化
    - 段階的な結果の表示
    - デバッグ情報の活用

### 特殊編: 特定タスク向けエージェント
18. [数値比較](18_is_9_11_bigger_than_9_9.py)
    - 数値計算の実装
    - 比較ロジックの構築
    - 結果の説明生成

19. [レスポンス変数](19_response_as_variable.py)
    - 応答データの構造化
    - 変数としての処理
    - データ型の最適化

20. [システムプロンプト](20_system_prompt.py)
    - プロンプトエンジニアリング
    - システム設定の最適化
    - 応答品質の向上

### エンタープライズ編: ビジネス向け機能
21. [複数ツール統合](21_multiple_tools.py)
    - 複数APIの統合
    - データソースの連携
    - 総合分析機能の実装

22. [エージェントメトリクス](22_agent_metrics.py)
    - パフォーマンス測定
    - メトリクスの可視化
    - 最適化の指標設定

23. [リサーチエージェント](23_research_agent.py)
    - 包括的な情報収集
    - 記事生成機能
    - 信頼性の評価

## 🎯 前提条件

- Python 3.8以上
- OpenAI APIキー
- 必要に応じて各種APIキー（DALL-E, Zoom等）

## 🛠️ セットアップ

1. リポジトリのクローン:
```bash
git clone https://github.com/your-username/phidata-cookbook-jp.git
```

2. 依存パッケージのインストール:
```bash
pip install -r requirements.txt
```

3. 環境変数の設定:
```bash
cp .env.example .env
# .envファイルを編集して必要なAPIキーを設定
```

## 📖 使用方法

1. 各サンプルは独立して実行可能です
2. サンプルコードには詳細なコメントが付与されています
3. 段階的に基礎から応用へと進むことをお勧めします

## 🤝 コントリビューション

- バグ報告や機能要望はIssueで受け付けています
- プルリクエストも歓迎します
- コードの改善案や新しいサンプルの提案も歓迎します

## 📝 ライセンス

このプロジェクトはMITライセンスの下で公開されています。

## 🔗 参考リンク

- [phidata公式ドキュメント](https://docs.phidata.com)
- [phidata GitHub](https://github.com/phidatahq/phidata)
- [コミュニティフォーラム](https://community.phidata.com/)
