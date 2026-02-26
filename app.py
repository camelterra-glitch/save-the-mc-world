import streamlit as st

# タイトル
st.title("マイクラ×さんすう：バグから世界をすくえ！")

# スティーブの登場
st.subheader("スティーブ（Steve）")
col1, col2 = st.columns([1, 2])
with col1:
    st.image("assets/steve.png", width=120)
with col2:
    st.write("「たいへんだ！バグの せいで つるはしが ボロボロに なっちゃった。」")
    st.write("「下の さんすうの もんだい（問題）が とければ、元にもどるはずなんだ！」")

# クイズの枠
st.info("### 第一もん：つるはしを なおせ！")

# 壊れたつるはしの画像
st.image("assets/pickaxe_broken.png", width=100, caption="ボロボロの つるはし")

# 問題文（小2までの漢字＋ふりがな）
# st.markdownでHTMLを使うと、ふりがな（ルビ）が振れます
st.markdown("""
<div style='font-size: 1.5rem; line-height: 2.5rem;'>
  <ruby>羊<rt>ひつじ</rt></ruby>が <strong>15ひき</strong> います。<br>
  あとから <strong>8ぴき</strong> やってきました。<br>
  <ruby>羊<rt>ひつじ</rt></ruby>は <ruby>全部<rt>ぜんぶ</rt></ruby>で <ruby>何引<rt>なんびき</rt></ruby> に なりましたか？
</div>
""", unsafe_allow_html=True)

# ひつじの画像
st.image("assets/sheep.png", width=100, caption="ひつじたち")

# 選択肢
answer = st.radio("答えを えらんでね：", ["21ぴき", "23ぴき", "25ぴき"])

# 判定ボタン
if st.button("これで けってい！"):
    if answer == "23ぴき":
        st.success("✨ せいかい（正解）！")
        st.balloons()
        
        # 修復されたつるはしの画像を表示
        st.image("assets/pickaxe_fixed.png", width=100, caption="ピカピカに なおった！")
        
        st.write("「やった！『石のつるはし』が 元どおりになったよ！ ありがとう！」")
    else:
        st.error("❌ ざんねん！")
        st.write("「うわあ！ バグが なおらない…！ もういちど 計算（けいさん）してみて！」")