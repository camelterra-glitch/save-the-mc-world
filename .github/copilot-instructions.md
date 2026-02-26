# Copilot 指示書 — Save the MC World

## 概要
Minecraft テーマの教育用算数ゲーム（小学校低学年向け）。UI は `Streamlit` で構築されています。学習者にやさしい日本語（ふりがな）を使う点が特徴です。

## 目的（AIエージェント向け）
- 迅速に新しい問題を追加できるテンプレートを守ること
- 日本語のふりがなと視覚アセットを正しく扱うこと
- CI（構文・リンティング・起動確認）に従って安全に変更を検証すること

## 主要パターン（必読）
- クイズは「ストーリー → 問題文（ふりがな）→ 選択肢 → フィードバック」の流れで作成します。
- ふりがな（ルビ）は HTML の `<ruby>` タグを使い、必ず `st.markdown(..., unsafe_allow_html=True)` で表示します。
  例: `<ruby>全部<rt>ぜんぶ</rt></ruby>`
- 選択肢は基本的に `st.radio()`、確定は `st.button("これで けってい！")` を使います。

## 追加・編集の実例（最短テンプレ）
```python
st.info("### 第◯もん：問題タイトル")
st.markdown("""<div style='font-size:1.5rem;line-height:2.5rem;'>
  問題文（<ruby>漢字<rt>かんじ</rt></ruby>）
</div>""", unsafe_allow_html=True)
answer = st.radio("答えをえらんでね：", ["A", "B", "C"])
if st.button("これで けってい！"):
    if answer == "正解":
        st.success("✨ せいかい！")
        st.balloons()
    else:
        st.error("ざんねん！もういちど チャレンジしよう！")
```

## 実行方法（ローカル）
```bash
pip install -r requirements.txt
streamlit run app.py
```

## CI の要点（参照ファイル: `.github/workflows/ci.yml`）
- Python 3.9/3.10/3.11 で動作確認
- `python -m py_compile app.py` による構文チェック
- `flake8` による静的解析（現状は警告を出して非ブロッキング）
- Streamlit アプリの起動確認を行います（簡易的なランタイムチェック）

## 主要ファイルと役割
- `app.py` : メインの Streamlit アプリ
- `requirements.txt` : 本番依存（`streamlit`）
- `requirements-dev.txt` : 開発用依存（`flake8` 等の候補）
- `.github/workflows/ci.yml` : CI 定義（構文・lint・起動確認）
- `.streamlit/config.toml` / `.streamlit/secrets.toml` : ストリームリット設定とシークレット（`secrets.toml` はコミットしない）
- `assets/` : 画像やスプライトを置くフォルダ

## プロジェクト固有の注意点
- 日本語の可読性が最優先：漢字には必ずふりがなを付けること
- 出力は Streamlit の HTML 安全性設定を尊重する（`unsafe_allow_html=True` を明示）
- アセットは `assets/` に格納し、パスは相対で参照してください

## 変更作業のチェックリスト
1. `app.py` に新しい問題を追加
2. ローカルで `streamlit run app.py` を起動して表示確認
3. 必要に応じて `requirements-dev.txt` に依存を追加
4. プルリクを作成し、CI が通ることを確認

## 今後の提案（短め）
- スコア管理とページ遷移は `st.session_state` を使って実装すると自然です。
- 自動化された UI テスト（Playwright など）の導入を検討してください。

---
作成・更新日: 2026-02-25
