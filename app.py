import streamlit as st
import os

# ---------------- SETTINGS ----------------
PASSWORD = "1234"
PHOTO_FOLDER = "photos"

# ---------------- SESSION STATE ----------------
if "unlocked" not in st.session_state:
    st.session_state.unlocked = False

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

    st.stop()

# ---------------- BIRTHDAY PAGE ----------------
st.markdown(
    "<h1 style='text-align:center;'>🎉 Happy Birthday! 🎉</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<h3 style='text-align:center;'>I hope your day is filled with happiness, laughter and lots of cake! 🎂💖</h3>",
    unsafe_allow_html=True
)

st.write("")
st.write("")

# ---------------- PHOTOS ----------------
st.subheader("📸 Our Memories")

if os.path.exists(PHOTO_FOLDER):

    images = [
        f for f in os.listdir(PHOTO_FOLDER)
        if f.lower().endswith((".jpg", ".jpeg", ".png"))
    ]

    if len(images) == 0:
        st.warning("No photos found in the photos folder.")

    else:
        cols = st.columns(2)

        for i, img in enumerate(images):
            with cols[i % 2]:
                st.image(
                    os.path.join(PHOTO_FOLDER, img),
                    use_container_width=True
                )

else:
    st.error("Photos folder not found!")