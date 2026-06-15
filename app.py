import streamlit as st
import os

# ---------------- SETTINGS ----------------
PASSWORD = "16sept2010"

# ---------------- SESSION STATE ----------------
if "unlocked" not in st.session_state:
    st.session_state.unlocked = False

if "likes_me" not in st.session_state:
    st.session_state.likes_me = False

if "no_count" not in st.session_state:
    st.session_state.no_count = 0

def check_password():
    if st.session_state.password_input == PASSWORD:
        st.session_state.unlocked = True

# ---------------- COLORS ----------------
if st.session_state.unlocked:
    bg_color = "#87CEEB"      # blue background
    heart_color = "#ff69b4"   # pink hearts
else:
    bg_color = "#ffd1dc"      # pink background
    heart_color = "#4da6ff"   # blue hearts

# ---------------- STYLING ----------------
st.markdown(f"""
<style>

.stApp {{
    background-color: {bg_color};
}}

.hearts {{
    position: fixed;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    pointer-events: none;
    overflow: hidden;
}}

.heart {{
    position: absolute;
    color: {heart_color};
    font-size: 30px;
    animation: float 10s linear infinite;
}}

@keyframes float {{
    0% {{
        transform: translateY(100vh);
        opacity: 0;
    }}
    10% {{
        opacity: 1;
    }}
    100% {{
        transform: translateY(-120vh);
        opacity: 0;
    }}
}}

.big-button button {{
    font-size: 40px !important;
    padding: 20px !important;
}}

.medium-button button {{
    font-size: 25px !important;
}}

.small-button button {{
    font-size: 12px !important;
}}

.tiny-button button {{
    font-size: 8px !important;
}}

</style>

<div class="hearts">
    <div class="heart" style="left:5%; animation-delay:0s;">❤</div>
    <div class="heart" style="left:15%; animation-delay:2s;">❤</div>
    <div class="heart" style="left:25%; animation-delay:4s;">❤</div>
    <div class="heart" style="left:35%; animation-delay:1s;">❤</div>
    <div class="heart" style="left:45%; animation-delay:3s;">❤</div>
    <div class="heart" style="left:55%; animation-delay:5s;">❤</div>
    <div class="heart" style="left:65%; animation-delay:2s;">❤</div>
    <div class="heart" style="left:75%; animation-delay:4s;">❤</div>
    <div class="heart" style="left:85%; animation-delay:1s;">❤</div>
    <div class="heart" style="left:95%; animation-delay:3s;">❤</div>
</div>
""", unsafe_allow_html=True)

# ---------------- PASSWORD PAGE ----------------
if not st.session_state.unlocked:

    st.markdown(
        "<h1 style='text-align:center;'>🔒 Enter Password</h1>",
        unsafe_allow_html=True
    )

    st.text_input(
        "Password",
        type="password",
        key="password_input",
        on_change=check_password
    )

# ---------------- DO YOU LIKE ME PAGE ----------------
if not st.session_state.likes_me:

    st.markdown("""
    <h1 style='text-align:center;'>
    💖 Do You Like Me? 💖
    </h1>

    <h3 style='text-align:center;'>
    Be honest... 🥺👉👈
    </h3>
    """, unsafe_allow_html=True)

    yes_sizes = [1, 2, 3, 5]
    no_sizes = [3, 2, 1, 0]

    stage = min(st.session_state.no_count, 3)

    if stage < 3:

        col1, col2 = st.columns([yes_sizes[stage], no_sizes[stage]])

        with col1:
            if st.button("❤️ YES ❤️", use_container_width=True):
                st.session_state.likes_me = True
                st.rerun()

        with col2:
            if st.button("💙 NO 💙", use_container_width=True):
                st.session_state.no_count += 1
                st.rerun()

    else:

        st.markdown(
            """
            <h2 style='text-align:center; color:pink;'>
            💖 I think I already know the answer 💖
            </h2>
            """,
            unsafe_allow_html=True
        )

        if st.button("❤️ YES ❤️", use_container_width=True):
            st.session_state.likes_me = True
            st.rerun()

    st.stop()
# ---------------- BIRTHDAY PAGE ----------------
st.markdown(
    "<h1 style='text-align:center;'>🎉 Happy Birthday! 🎉</h1>",
    unsafe_allow_html=True
)

st.markdown(
    """
    <h3 style='text-align:center;'>
    I hope your day is filled with happiness, laughter, love and lots of cake! 🎂💖
    </h3>
    """,
    unsafe_allow_html=True
)

st.write("")
st.write("")

# ---------------- PHOTOS ----------------
st.subheader("📸 Our Memories")

images = [
    f for f in os.listdir(".")
    if f.lower().endswith((".jpg", ".jpeg", ".png"))
]

if len(images) == 0:
    st.warning("No photos found.")

else:
    cols = st.columns(2)

    for i, img in enumerate(images):
        with cols[i % 2]:
            st.image(img, use_container_width=True)
