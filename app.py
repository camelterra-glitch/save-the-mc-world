import streamlit as st

# セッション状態の初期化
if "current_question" not in st.session_state:
    st.session_state.current_question = 1
if "correct_count" not in st.session_state:
    st.session_state.correct_count = 0
if "answered" not in st.session_state:
    st.session_state.answered = False
if "is_correct" not in st.session_state:
    st.session_state.is_correct = False

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
    st.info("### 第一もん：つるはしを なおせ！")
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
    
    if st.session_state.answered:
        if st.session_state.is_correct:
            st.success("✨ せいかい（正解）！")
            st.balloons()
            st.image("assets/pickaxe_fixed.png", width=100, caption="ピカピカに なおった！")
            st.write("「やった！『石のつるはし』が 元どおりになったよ！ありがとう！」")
            st.session_state.correct_count += 1
            
            if st.button("次の もんだいへ →", key="next1"):
                st.session_state.current_question += 1
                st.session_state.answered = False
                st.rerun()
        else:
            st.error("❌ ざんねん！")
            st.write("「うわあ！ バグが なおらない…！ もういちど 計算（けいさん）してみて！」")
            if st.button("もう <ruby>一回<rt>いっかい</rt></ruby> チャレンジ", key="retry1"):
                st.session_state.answered = False
                st.rerun()

elif st.session_state.current_question == 2:
    st.info("### 第二もん：そばかすを なおせ！")
    
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
    
    if st.session_state.answered:
        if st.session_state.is_correct:
            st.success("✨ せいかい（正解）！")
            st.balloons()
            st.image("assets/pickaxe_fixed.png", width=100, caption="そばかすが なおった！")
            st.write("「すごい！もう <ruby>一回<rt>いっかい</rt></ruby> なおった！」")
            st.session_state.correct_count += 1
            
            if st.button("次の もんだいへ →", key="next2"):
                st.session_state.current_question += 1
                st.session_state.answered = False
                st.rerun()
        else:
            st.error("❌ ざんねん！")
            st.write("「もう <ruby>一回<rt>いっかい</rt></ruby> チャレンジしてね！」")
            if st.button("もう <ruby>一回<rt>いっかい</rt></ruby> チャレンジ", key="retry2"):
                st.session_state.answered = False
                st.rerun()

elif st.session_state.current_question == 3:
    st.info("### 第三もん：モンスターを たおせ！")
    
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
    
    if st.session_state.answered:
        if st.session_state.is_correct:
            st.success("✨ せいかい（正解）！")
            st.balloons()
            st.image("assets/pickaxe_fixed.png", width=100, caption="つるはしが さらに つよくなった！")
            st.write("「すばらしい！つるはしが ダイヤモンドに なったよ！」")
            st.session_state.correct_count += 1
            
            if st.button("次の もんだいへ →", key="next3"):
                st.session_state.current_question += 1
                st.session_state.answered = False
                st.rerun()
        else:
            st.error("❌ ざんねん！")
            st.write("「モンスターが まだ いるよ…もう あとすこし！」")
            if st.button("もう <ruby>一回<rt>いっかい</rt></ruby> チャレンジ", key="retry3"):
                st.session_state.answered = False
                st.rerun()

elif st.session_state.current_question == 4:
    st.info("### 第四もん：すべてを なおせ！")
    
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
    
    if st.session_state.answered:
        if st.session_state.is_correct:
            st.success("✨ せいかい（正解）！")
            st.balloons()
            st.image("assets/pickaxe_fixed.png", width=100, caption="すべてが なおった！")
            st.write("「やったーーー！全てが もとどおりになったよ！キミが いたから たすかった！」")
            st.write("「さんすう、がんばってくれてありがとう！」")
            st.session_state.correct_count += 1
            
            # 最終結果表示
            st.divider()
            st.success(f"🎉 <ruby>完成<rt>かんせい</rt></ruby>！")
            st.write(f"\n**{st.session_state.correct_count}/4** もん、 せいかい！")
            
            if st.button("もう <ruby>一回<rt>いっかい</rt></ruby> プレイする"):
                st.session_state.current_question = 1
                st.session_state.correct_count = 0
                st.session_state.answered = False
                st.rerun()
        else:
            st.error("❌ ざんねん！")
            st.write("「もう <ruby>一回<rt>いっかい</rt></ruby> <ruby>頑張<rt>がんば</rt></ruby>ってみてね！」")
            if st.button("もう <ruby>一回<rt>いっかい</rt></ruby> チャレンジ", key="retry4"):
                st.session_state.answered = False
                st.rerun()