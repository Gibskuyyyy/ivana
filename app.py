import streamlit as st
import time
import random

st.set_page_config(page_title="Untuk Kamu 🤍", layout="wide")

# ================= STATE =================
if "authorized" not in st.session_state:
    st.session_state.authorized = False
if "loading" not in st.session_state:
    st.session_state.loading = False
if "slide" not in st.session_state:
    st.session_state.slide = 1

# ================= CSS =================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500&display=swap');

html, body, [class*="css"] {
    font-family: 'Playfair Display', serif;
    background: linear-gradient(180deg, #fff0f5, #ffe4e1);
    overflow: hidden;
}

/* Fade transition */
.fade {
    animation: fadein 1.5s;
}
@keyframes fadein {
    from { opacity: 0; }
    to { opacity: 1; }
}

/* Full screen center */
.full {
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
}

/* Text styles */
.big {
    font-size: 72px;
    letter-spacing: 3px;
}
.mid {
    font-size: 26px;
    margin-top: 15px;
}
.text {
    max-width: 760px;
    text-align: center;
    font-size: 22px;
    line-height: 1.9;
}

/* Falling hearts */
.heart {
    position: fixed;
    top: -10%;
    font-size: 30px;
    animation: fall linear infinite;
    opacity: 0.5;
}
@keyframes fall {
    to {
        transform: translateY(120vh);
        opacity: 0;
    }
}

button {
    margin-top: 40px !important;
    font-size: 20px !important;
}
</style>
""", unsafe_allow_html=True)

# ================= FALLING HEARTS =================
hearts_html = ""
for _ in range(15):
    left = random.randint(0, 100)
    duration = random.randint(8, 15)
    delay = random.randint(0, 5)
    hearts_html += f"""
    <div class="heart" style="left:{left}%; animation-duration:{duration}s; animation-delay:{delay}s;">💗</div>
    """
st.markdown(hearts_html, unsafe_allow_html=True)

# ================= PASSWORD GATE =================
if not st.session_state.authorized:
    st.markdown("""
    <div class="full fade">
        <div class="big">Sebelum masuk…</div>
        <div class="mid">pakai tanggal yang penting buat kita 🤍</div>
    </div>
    """, unsafe_allow_html=True)

    password = st.text_input("Tanggal jadian (DDMMYYYY)", type="password")

    if st.button("Masuk"):
        if password == "11062024":  # ⬅️ GANTI DENGAN TANGGAL JADIAN KAMU
            st.session_state.loading = True
            st.session_state.authorized = True
            st.rerun()
        else:
            st.error("Bukan itu… tapi kamu pasti tahu jawabannya 🤍")

    st.stop()

# ================= FAKE LOADING =================
if st.session_state.loading:
    with st.spinner("Please wait…"):
        time.sleep(2.5)
    st.session_state.loading = False
    st.rerun()

# ================= SLIDES =================

# SLIDE 1 — OPENING
if st.session_state.slide == 1:
    st.markdown("""
    <div class="full fade">
        <div class="big">Aku salah.</div>
        <div class="mid">aku minta maaf.</div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Lanjut"):
        st.session_state.slide = 2
        st.rerun()

# SLIDE 2 — CALM
elif st.session_state.slide == 2:
    st.markdown("""
    <div class="full fade">
        <div class="text">
        Aku tahu,  
        di momen itu kamu lagi serius,  
        dan kamu berharap direspon dengan serius juga.
        Dan ketika itu nggak kamu dapetin, responku terasa bercanda,  
        itu bisa bikin kamu ngerasa  
        nggak dihargai perasaannya. 
        wajar kalau kamu ngerasa sakit hati.   
        aku minta maaf karena nggak cukup peka.
        </div>
    </div>

    """, unsafe_allow_html=True)

    if st.button("Lanjut"):
        st.session_state.slide = 3
        st.rerun()

# SLIDE 3 — MUSIC
elif st.session_state.slide == 3:
    audio = open("iwannabeyours.mp3", "rb").read()
    st.audio(audio, format="audio/mp3")

    st.markdown("""
    <div class="full fade">
        <div class="text">
        Lagu ini aku pilih  
        karena aku pengen kamu tahu satu hal:
        aku pengen jadi tempat kamu pulang,
        aku pengen jadi tempat kamu keluh kesah,
        segalanya tentang kamu buat kamu buat kita
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Lanjut"):
        st.session_state.slide = 4
        st.rerun()

# SLIDE 4 — PHOTO
elif st.session_state.slide == 4:
    st.markdown('<div class="full fade">', unsafe_allow_html=True)
    st.image("foto.jpeg", width=380 )
    st.markdown("""
    <div class="full fade">
        <div class="text">
        Ini aku.  
        Masih belajar,  
        masih sering salah,  
        tapi lagi berusaha jadi lebih peka, 
        belajar buat ngerti kondisi untuk bercanda
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Lanjut"):
        st.session_state.slide = 5
        st.rerun()

# SLIDE 5 — CONFESSION
elif st.session_state.slide == 5:
    st.markdown("""
    <div class="full fade">
        <div class="text">
        Waktu kamu bilang <b>I love you</b>,  
        aku jawab bercanda.
        Bukan karena perasaanku main-main,  
        tapi karena aku salah baca momen.
        Aku ngerti sekarang,  
        itu bukan momen buat bercanda.
        Dan aku minta maaf  
        karena bikin kamu ngerasa sendirian  
        di momen yang seharusnya hangat.
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Lanjut"):
        st.session_state.slide = 6
        st.rerun()

# SLIDE 6 — ENDING
elif st.session_state.slide == 6:
    st.markdown("""
    <div class="full fade">
        <div class="text">
        Aku nggak minta kamu langsung maafin aku.
        Aku cuma pengen kamu tahu,  
        aku dengerin,  
        aku belajar,  
        dan aku nggak mau ngulangin hal yang sama.
        Karena aku cuma punya kamu.
        Terima kasih  
        kalau kamu masih mau baca sampai sini.
        </div>
    </div>

    """, unsafe_allow_html=True)

    if st.button("Lanjut"):
        st.session_state.slide = 7
        st.rerun()

# SLIDE 7 — VIDEO
elif st.session_state.slide == 7:
    st.markdown("""
    <div class="full fade">
        <div class="text">
        aku sayang sekali sama kamu.
        aku sayang sama cewek kecilkuu yang imut ini.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.video("video.mp4")

    st.markdown("""
    <div class="text" style="margin-top:30px;">
    Aku cuma pengen kamu ngerasa
    ditemani. wa aku kalau kamu sudah merasa lebih baik
    </div>
    """, unsafe_allow_html=True)

    st.caption("aku di sini, kalau kamu butuh 🤍")
