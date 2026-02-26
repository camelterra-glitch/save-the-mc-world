# Save the MC World 🌍

教育的なインタラクティブ数学ゲーム。Minecraftのテーマを使用した日本の小学1~2年生向けの数学学習アプリです。Streamlitで構築されており、迅速にデプロイできます。

## 🚀 クイック開始

### 1. 依存関係のインストール
```bash
pip install -r requirements.txt
```

### 2. アプリの実行
```bash
streamlit run app.py
```

ブラウザが自動的に `http://localhost:8501` で開きます。

### 3. 開発モード（オプション）
コード品質チェックのための開発依存関係をインストール：
```bash
pip install -r requirements-dev.txt
```

Flake8でコードをチェック：
```bash
flake8 app.py
```

## 📁 プロジェクト構造

```
save-the-mc-world/
├── app.py                          # メインアプリケーション
├── requirements.txt               # 実運用の依存関係
├── requirements-dev.txt           # 開発時の依存関係
├── .streamlit/
│   ├── config.toml               # Streamlit設定
│   └── secrets.toml              # API キー（非公開）
├── .github/
│   ├── copilot-instructions.md   # AIエージェント向けガイド
│   └── workflows/
│       └── ci.yml                # CI/CDパイプライン
├── assets/                        # 画像やアイコン置き場
└── .gitignore                     # Git無視リスト
```

## 🎮 アプリの特徴

- **ストーリー駆動**：Minecraftのキャラクターがくり返して登場
- **ルビ振り対応**：小学生が読める日本語テキスト
- **複数選択肢**：4択の数学問題
- **ポジティブフィードバック**：成功時に風船アニメーション
- **ホットリロード**：ファイル保存で自動リロード

## 🔧 CI/CD パイプライン

GitHub Actions（`.github/workflows/ci.yml`）を使用して、すべてのプッシュとプルリクエストに対して以下を実施：

1. **構文チェック**：Python コンパイル確認
2. **コード品質チェック**：flake8でのリント（non-blocking）
3. **ランタイムテスト**：Streamlit アプリの起動確認
4. **マルチバージョンテスト**：Python 3.9、3.10、3.11 に対応

## 📦 Streamlit Cloud へのデプロイ

### 準備
1. [Streamlit Cloud](https://streamlit.io/cloud) でアカウント作成
2. リポジトリをGitHubに接続
3. `.streamlit/secrets.toml` を作成（ローカルのみ、Gitでは無視）

### デプロイ
メインブランチへのプッシュで自動デプロイ：
```bash
git push origin main
```

## 📝 開発ガイド

新しい問題を追加する場合は、[AIエージェント向けガイド](./github/copilot-instructions.md)の「拡張パターン」を参照してください。

### 例：新しい問題の追加
```python
st.info("### 第二もん：新しいクエスト")
st.markdown("""<div style='font-size: 1.5rem; line-height: 2.5rem;'>
  <ruby>何<rt>なん</rt></ruby>かの問題文
</div>""", unsafe_allow_html=True)
answer = st.radio("選択肢:", ["A", "B", "C", "D"])
if st.button("これで けってい！"):
    if answer == "正解":
        st.success("✨ せいかい！")
        st.balloons()
```

## 🌐 サポートOSと環境

- **対応OS**：Windows, macOS, Linux
- **必須Python**：3.9 以上
- **ブラウザ**：最新のChrome、Firefox、Safari、Edge

## 📚 参考資料

- [Streamlit ドキュメント](https://docs.streamlit.io)
- [日本語チュートリアル](https://docs.streamlit.io/library/get-started/multipage-apps)

## 📄 ライセンス

MIT License - 詳細は LICENSE ファイルを参照

---

**作成日**：2026年2月25日  
**最終更新**：2026年2月25日
