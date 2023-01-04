import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_cmaqoazd.json")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I'm Shawn Oliver :wave:")
    st.title("A Senior Business Analyst From Montreal, Canada")
    st.write(
        """
        I'm a markets/tech nerd with a knack for problem solving and a passion for creating innovative and engaging user experiences. 
        """
    )

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("##")
        st.write(
            """
            What I've accomplished and what I like to do:
            - Possesses over a decade of unique and diverse experience in Fintech and asset management
            - Has proven track record of taking projects from idea, to market success in both the software and financial management space
            - Previously a member of the launch team that brought the first Robo Advisor offering to Canada, helping it grow into a multi billion dollar market leader
            - Currently a very proud member of the team at Equisoft building innovative tools in the wealth management space that solve the real world problems facing financial professionals
            - Is a Chartered Investment Manager (CIM) and holds a Bachelor of Commerce (Finance w/ distinction) from the John Molson School of Business at Concordia University
            - Has completed the Software Product Management Specialization at the University of Alberta
            - Dabbles in macroeconomics, computer networking, crypto and likes to ride bikes in the Summer and snowboards in the Winter
            """
        )
        st.write("[LinkedIn >](https://www.linkedin.com/in/shawnoliver85/)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/shawn@shawnoliver.ca" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()