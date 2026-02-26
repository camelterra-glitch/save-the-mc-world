import streamlit as st

# タイトル
st.title("マイクラ×さんすう：バグから世界をすくえ！")

# スティーブの登場
st.subheader("スティーブ（Steve）")
st.write("「たいへんだ！バグの せいで つるはしが ボロボロに なっちゃった。」")
st.write("「下の さんすうの もんだい（問題）が とければ、元にもどるはずなんだ！」")

# クイズの枠
st.info("### 第一もん：つるはしを なおせ！")

# 問題文（小2までの漢字＋ふりがな）
# st.markdownでHTMLを使うと、ふりがな（ルビ）が振れます
st.markdown("""
<div style='font-size: 1.5rem; line-height: 2.5rem;'>
  ひつじが <strong>15ひき</strong> います。<br>
  あとから <strong>8ぴき</strong> やってきました。<br>
  ひつじは <ruby>全部<rt>ぜんぶ</rt></ruby>で <ruby>何引<rt>なんびき</rt></ruby> に なりましたか？
</div>
""", unsafe_allow_html=True)

# 選択肢
answer = st.radio("答えを えらんでね：", ["21ぴき", "23ぴき", "25ぴき"])

# 判定ボタン
if st.button("これで けってい！"):
    if answer == "23ぴき":
        st.success("✨ せいかい（正解）！")
        st.balloons()
        st.write("「やった！『石のつるはし』が 元どおりになったよ！ ありがとう！」")
        # ここに「石のつるはし」の画像を表示するコードを追加できます
    else:
        st.error("❌ ざんねん！")
        st.write("「うわあ！ バグが なおらない…！ もういちど 計算（けいさん）してみて！」")