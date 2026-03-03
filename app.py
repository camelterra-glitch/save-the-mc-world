import streamlit as st

# モバイル対応用のカスタムスタイル
st.markdown("""
<style>
/* マイクラ風フォントのインポート */
@import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@400;700&display=swap');

/* Minecraft テーマカラー定義 */
:root {
  --mc-dark-green: #2d5016;
  --mc-orange: #ff9900;
  --mc-yellow: #ffcc00;
  --mc-dark-gray: #3a3a3a;
  --mc-white: #ffffff;
}

/* マイクラ風フォント全体に適用 */
* {
  font-family: 'Roboto Mono', 'Courier New', monospace !important;
  letter-spacing: 0.05em;
}

/* マイクラ風背景パターン */
html, body, [data-testid="stAppViewContainer"] {
  background: linear-gradient(135deg, #2a2a2a 0%, #1a1a1a 100%);
  background-attachment: fixed;
}

/* ブロック状のテクスチャ背景 */
[data-testid="stAppViewContainer"]::before {
  content: '';
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: 
    repeating-linear-gradient(0deg, transparent, transparent 2px, rgba(255, 255, 255, 0.05) 2px, rgba(255, 255, 255, 0.05) 4px),
    repeating-linear-gradient(90deg, transparent, transparent 2px, rgba(255, 255, 255, 0.05) 2px, rgba(255, 255, 255, 0.05) 4px);
  pointer-events: none;
  z-index: 0;
}

/* タイトルスタイル */
[data-testid="stTitle"] {
  background: linear-gradient(135deg, #2d5016, #3a7a2d);
  color: #ffcc00;
  padding: 20px;
  border-radius: 10px;
  text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
  font-family: 'Roboto Mono', 'Courier New', monospace !important;
  letter-spacing: 0.1em !important;
  font-weight: 700 !important;
}

/* 問題タイトル（st.info） */
.stMarkdown div p:has(+ [data-testid="stMarkdownContainer"]) {
  font-size: 1.2em !important;
  font-weight: bold !important;
}

/* 情報ボックス（つるはしタイトル） */
.stAlert > div {
  background: url('data:image/svg+xml,<svg></svg>');
  border-left: 5px solid #2d5016;
}

[data-testid="stException"] {
  border-left: 5px solid #ff9900 !important;
}

/* 正解メッセージ */
[data-testid="stAlert"][role="alert"] {
  background-color: #d4f1d4 !important;
  border-left: 5px solid #2d5016 !important;
}

/* 不正解メッセージ */
[data-testid="stAlert"][role="status"] {
  background-color: #ffe4cc !important;
  border-left: 5px solid #ff9900 !important;
}

/* ボタンを幅いっぱい義テムカラー20pxパディング */
.stButton>button {
  width: 100% !important;
  background-color: #ff9900 !important;
  color: #111111 !important;
  font-weight: bold !important;
  font-size: 1.1em !important;
  padding: 12px 20px !important;
  border-radius: 8px !important;
  border: 2px solid #ffcc00 !important;
  letter-spacing: 0.08em !important;
}

.stButton>button:hover {
  background-color: #ffaa00 !important;
  box-shadow: 0 4px 8px rgba(255, 153, 0, 0.4) !important;
}

/* ラジオボタンの選択肢を縦並びに */
.stRadio > div {
  flex-direction: column !important;
}

/* ラジオボタンの選択肢間隔 */
.stRadio > div > label {
  margin-bottom: 12px !important;
  padding: 10px 15px !important;
  border-radius: 6px !important;
  background-color: #4a4a4a !important;
  border-left: 4px solid #ffcc00 !important;
  color: #ffffff !important;
  font-weight: 600 !important;
}

/* ラジオボタンホバーエフェクト */
.stRadio > div > label:hover {
  background-color: #5a5a5a !important;
  box-shadow: 0 2px 6px rgba(255, 153, 0, 0.3) !important;
}

/* ラジオボタンチェック時のスタイル */
.stRadio > div > label [data-testid="stCheckbox"] {
  accent-color: #ffcc00 !important;
}

/* 答えの語文コンテナ */
[data-testid="stMarkdownContainer"] {
  line-height: 1.8 !important;
}

/* プログレスバー */
[role="progressbar"] {
  background-color: #2d5016 !important;
}

/* カラムが自動で横並びになる場合、狭い画面では縦積みに */
@media (max-width: 600px) {
  .css-1d391kg, .css-1oebfis {
    flex-direction: column !important;
  }
  [data-testid="stTitle"] {
    font-size: 1.5em !important;
  }
}
</style>
""", unsafe_allow_html=True)

# セッション状態の初期化
if "current_question" not in st.session_state:
    st.session_state.current_question = 1
if "correct_count" not in st.session_state:
    st.session_state.correct_count = 0
if "answered" not in st.session_state:
    st.session_state.answered = False
if "is_correct" not in st.session_state:
    st.session_state.is_correct = False
if "counted" not in st.session_state:
    st.session_state.counted = False

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

# プログレス表示
st.progress(st.session_state.current_question / 4)

# クイズセクション
if st.session_state.current_question == 1:
    st.markdown("""<div style='background: linear-gradient(135deg, #2d5016, #3a7a2d); color: #ffcc00; padding: 15px; border-radius: 8px; text-align: center; font-size: 1.3em; font-weight: bold; margin-bottom: 15px;'>⛏️ 第一もん：つるはしを なおせ！</div>""", unsafe_allow_html=True)
    st.image("assets/pickaxe_broken.png", width=100, caption="ボロボロの つるはし")
    
    st.markdown("""
    <div style='font-size: 1.5rem; line-height: 2.5rem;'>
      <ruby>羊<rt>ひつじ</rt></ruby>が <strong>15ひき</strong> います。<br>
      あとから <strong>8ぴき</strong> やってきました。<br>
      <ruby>羊<rt>ひつじ</rt></ruby>は <ruby>全部<rt>ぜんぶ</rt></ruby>で <ruby>何匹<rt>なんぴき</rt></ruby> に なりましたか？
    </div>
    """, unsafe_allow_html=True)
    
    st.image("assets/sheep.png", width=100, caption="ひつじたち")
    
    answer = st.radio("答えを えらんでね：", ["21ぴき", "23ぴき", "25ぴき"], key="q1")
    
    if st.button("これで けってい！", key="btn1"):
        st.session_state.answered = True
        st.session_state.is_correct = (answer == "23ぴき")
        if st.session_state.is_correct and not st.session_state.counted:
            st.session_state.correct_count += 1
            st.session_state.counted = True
    
    if st.session_state.answered:
        if st.session_state.is_correct:
                st.success("✨ せいかい（正解）！")
                st.balloons()
                st.image("assets/pickaxe_fixed.png", width=100, caption="ピカピカに なおった！")
                st.write("「やった！『石のつるはし』が 元どおりになったよ！ありがとう！」")
                
                if st.button("次の もんだいへ →", key="next1"):
                    # increment score when moving forward
                    st.session_state.correct_count += 1
                    st.session_state.current_question += 1
                    st.session_state.answered = False
                    st.rerun()
        else:
            st.error("❌ ざんねん！")
            st.write("「うわあ！ バグが なおらない…！ もういちど 計算（けいさん）してみて！」")
            if st.button("もう いっかい チャレンジ", key="retry1"):
                st.session_state.answered = False
                st.rerun()

elif st.session_state.current_question == 2:
    st.markdown("""<div style='background: linear-gradient(135deg, #2d5016, #3a7a2d); color: #ffcc00; padding: 15px; border-radius: 8px; text-align: center; font-size: 1.3em; font-weight: bold; margin-bottom: 15px;'>🐟 第二もん：そばかすを なおせ！</div>""", unsafe_allow_html=True)
    
    st.markdown("""
    <div style='font-size: 1.5rem; line-height: 2.5rem;'>
      リンゴが <strong>18こ</strong> ありました。<br>
      <strong>7こ</strong> 食べました。<br>
      リンゴは あと <ruby>何個<rt>なんこ</rt></ruby> ありますか？
    </div>
    """, unsafe_allow_html=True)
    
    answer = st.radio("答えを えらんでね：", ["10こ", "11こ", "12こ"], key="q2")
    
    if st.button("これで けってい！", key="btn2"):
        st.session_state.answered = True
        st.session_state.is_correct = (answer == "11こ")
        if st.session_state.is_correct and not st.session_state.counted:
            st.session_state.correct_count += 1
            st.session_state.counted = True
    
    if st.session_state.answered:
        if st.session_state.is_correct:
                st.success("✨ せいかい（正解）！")
                st.balloons()
                st.image("assets/pickaxe_fixed.png", width=100, caption="そばかすが なおった！")
                st.write("「すごい！もう <ruby>一回<rt>いっかい</rt></ruby> なおった！」")
                
                if st.button("次の もんだいへ →", key="next2"):
                    st.session_state.correct_count += 1
                    st.session_state.current_question += 1
                    st.session_state.answered = False
                    st.rerun()
        else:
            st.error("❌ ざんねん！")
            st.markdown("""「もう <ruby>一回<rt>いっかい</rt></ruby> チャレンジしてね！」""", unsafe_allow_html=True)
            if st.button("もう いっかい チャレンジ", key="retry2"):
                st.session_state.answered = False
                st.rerun()

elif st.session_state.current_question == 3:
    st.markdown("""<div style='background: linear-gradient(135deg, #2d5016, #3a7a2d); color: #ffcc00; padding: 15px; border-radius: 8px; text-align: center; font-size: 1.3em; font-weight: bold; margin-bottom: 15px;'>🤮 第三もん：モンスターを たおせ！</div>""", unsafe_allow_html=True)
    
    st.markdown("""
    <div style='font-size: 1.5rem; line-height: 2.5rem;'>
      <ruby>一日<rt>いちにち</rt></ruby>に <strong>3びき</strong> モンスターが あらわれます。<br>
      <strong>5日間</strong> で <ruby>全部<rt>ぜんぶ</rt></ruby> <ruby>何匹<rt>なんびき</rt></ruby> あらわれますか？
    </div>
    """, unsafe_allow_html=True)
    
    answer = st.radio("答えを えらんでね：", ["12ぴき", "15ぴき", "18ぴき"], key="q3")
    
    if st.button("これで けってい！", key="btn3"):
        st.session_state.answered = True
        st.session_state.is_correct = (answer == "15ぴき")
        if st.session_state.is_correct and not st.session_state.counted:
            st.session_state.correct_count += 1
            st.session_state.counted = True
    
    if st.session_state.answered:
        if st.session_state.is_correct:
                st.success("✨ せいかい（正解）！")
                st.balloons()
                st.image("assets/pickaxe_fixed.png", width=100, caption="つるはしが さらに つよくなった！")
                st.write("「すばらしい！つるはしが ダイヤモンドに なったよ！」")
                
                if st.button("次の もんだいへ →", key="next3"):
                    st.session_state.correct_count += 1
                    st.session_state.current_question += 1
                    st.session_state.answered = False
                    st.rerun()
        else:
            st.error("❌ ざんねん！")
            st.write("「モンスターが まだ いるよ…もう あとすこし！」")
            if st.button("もう いっかい チャレンジ", key="retry3"):
                st.session_state.answered = False
                st.rerun()

elif st.session_state.current_question == 4:
    st.markdown("""<div style='background: linear-gradient(135deg, #2d5016, #3a7a2d); color: #ffcc00; padding: 15px; border-radius: 8px; text-align: center; font-size: 1.3em; font-weight: bold; margin-bottom: 15px;'>⚠️ 第四もん：すべてを なおせ！</div>""", unsafe_allow_html=True)
    
    st.markdown("""
    <div style='font-size: 1.5rem; line-height: 2.5rem;'>
      <ruby>石<rt>いし</rt></ruby>が <strong>20こ</strong> あります。<br>
      <strong>5こ</strong> あげて、あとから <strong>8こ</strong> もらいました。<br>
      <ruby>石<rt>いし</rt></ruby>は <ruby>全部<rt>ぜんぶ</rt></ruby>で <ruby>何個<rt>なんこ</rt></ruby> ですか？
    </div>
    """, unsafe_allow_html=True)
    
    answer = st.radio("答えを えらんでね：", ["21こ", "23こ", "25こ"], key="q4")
    
    if st.button("これで けってい！", key="btn4"):
        st.session_state.answered = True
        st.session_state.is_correct = (answer == "23こ")
        if st.session_state.is_correct and not st.session_state.counted:
            st.session_state.correct_count += 1
            st.session_state.counted = True
    
    if st.session_state.answered:
        if st.session_state.is_correct:
            st.success("✨ せいかい（正解）！")
            st.balloons()
            st.image("assets/pickaxe_fixed.png", width=100, caption="すべてが なおった！")
            st.write("「やったーーー！全てが もとどおりになったよ！キミが いたから たすかった！」")
            st.write("「さんすう、がんばってくれてありがとう！」")
            
            # 最終結果表示
            st.divider()
            st.markdown("""🎉 <ruby>完成<rt>かんせい</rt></ruby>！""", unsafe_allow_html=True)
            st.write(f"\n**{st.session_state.correct_count}/4** もん、 せいかい！")
            
            if st.button("もう いっかい プレイする"):
                st.session_state.current_question = 1
                st.session_state.correct_count = 0
                st.session_state.answered = False
                st.session_state.counted = False
                st.rerun()
        else:
            st.error("❌ ざんねん！")
            st.markdown("""「もう <ruby>一回<rt>いっかい</rt></ruby> <ruby>頑張<rt>がんば</rt></ruby>ってみてね！」""", unsafe_allow_html=True)
            if st.button("もう いっかい チャレンジ", key="retry4"):
                st.session_state.answered = False
                st.rerun()