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
# 分割線
st.divider()

# 第二もん（引き算）
st.info("### 第二もん：そばかすを なおせ！")

st.markdown("""
<div style='font-size: 1.5rem; line-height: 2.5rem;'>
  リンゴが <strong>18こ</strong> ありました。<br>
  <strong>7こ</strong> 食べました。<br>
  リンゴは あと <ruby>何個<rt>なんこ</rt></ruby> ありますか？
</div>
""", unsafe_allow_html=True)

answer2 = st.radio("答えを えらんでね：", ["10こ", "11こ", "12こ"], key="q2")

if st.button("これで けってい！", key="btn2"):
    if answer2 == "11こ":
        st.success("✨ せいかい（正解）！")
        st.balloons()
        st.image("assets/pickaxe_fixed.png", width=100, caption="そばかすが なおった！")
        st.write("「すごい！もう <ruby>一回<rt>いっかい</rt></ruby> なおった！」")
    else:
        st.error("❌ ざんねん！")
        st.write("「もう <ruby>一回<rt>いっかい</rt></ruby> チャレンジしてね！」")

st.divider()

# 第三もん（掛け算）
st.info("### 第三もん：モンスターを たおせ！")

st.markdown("""
<div style='font-size: 1.5rem; line-height: 2.5rem;'>
  <ruby>一日<rt>いちにち</rt></ruby>に <strong>3びき</strong> モンスターが あらわれます。<br>
  <strong>5日間</strong> で <ruby>全部<rt>ぜんぶ</rt></ruby> <ruby>何匹<rt>なんびき</rt></ruby> あらわれますか？
</div>
""", unsafe_allow_html=True)

answer3 = st.radio("答えを えらんでね：", ["12ぴき", "15ぴき", "18ぴき"], key="q3")

if st.button("これで けってい！", key="btn3"):
    if answer3 == "15ぴき":
        st.success("✨ せいかい（正解）！")
        st.balloons()
        st.image("assets/pickaxe_fixed.png", width=100, caption="つるはしが さらに つよくなった！")
        st.write("「すばらしい！つるはしが ダイヤモンドに なったよ！」")
    else:
        st.error("❌ ざんねん！")
        st.write("「モンスターが まだ いるよ…もう あとすこし！」")

st.divider()

# 第四もん（混合計算）
st.info("### 第四もん：すべてを なおせ！")

st.markdown("""
<div style='font-size: 1.5rem; line-height: 2.5rem;'>
  <ruby>石<rt>いし</rt></ruby>が <strong>20こ</strong> あります。<br>
  <strong>5こ</strong> あげて、あとから <strong>8こ</strong> もらいました。<br>
  <ruby>石<rt>いし</rt></ruby>は <ruby>全部<rt>ぜんぶ</rt></ruby>で <ruby>何個<rt>なんこ</rt></ruby> ですか？
</div>
""", unsafe_allow_html=True)

answer4 = st.radio("答えを えらんでね：", ["21こ", "23こ", "25こ"], key="q4")

if st.button("これで けってい！", key="btn4"):
    if answer4 == "23こ":
        st.success("✨ せいかい（正解）！")
        st.balloons()
        st.image("assets/pickaxe_fixed.png", width=100, caption="すべてが なおった！")
        st.write("「やったーーー！全てが もとどおりになったよ！キミが いたから たすかった！」")
        st.write("「さんすう、がんばってくれてありがとう！」")
    else:
        st.error("❌ ざんねん！")
        st.write("「もう <ruby>一回<rt>いっかい</rt></ruby> <ruby>頑張<rt>がんば</rt></ruby>ってみてね！」")