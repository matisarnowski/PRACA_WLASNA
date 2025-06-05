import requests
import streamlit as st
from streamlit_lottie import st_lottie

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Moja stronka", page_icon=":open_book:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url, timeout=10)
    if r.status_code != 200:
        return None
    return r.json()


# ---- Load Assets ----
lottie_coding = load_lottieurl(
    "https://lottie.host/5627c703-4224-48ab-a721-e650f35c3c0f/FrnjXWGhia.json"
)

# ---- Header Section ----
st.subheader("Cześć jestem Mateusz :wave:")
st.title("Junior Developer z Torunia. ")
with st.container():
    st.write(
        "Pasjonuje się nauką matematyki i informatyki. Szczególnie lubię takie działy jak algorytmika, teoria mnogości, analiza matematyczna."
    )
    st.write(
        "[Mój LinkedIn to: >](https://www.linkedin.com/in/mateusz-sarnowski-67327a285/)"
    )
    st.write("[Mój GitHub to: >](https://github.com/matisarnowski)")
    st.write("[Mój Facebook to: >](https://www.facebook.com/mateusz.sarnowski.503)")

# ---- What I do ----
with st.container():
    st.write("Tutaj opisuję, czym zajmuje się na codzień.")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Na codzień: ")
        st.write(
            """
                 - Zazwyczaj po prostu uczę się programować. Piszę proste programiki w języku programowania Python, lub proste strony Internetowe z użyciem JavaScript, CSS i HTML.
                 - Poza tym sporo do niedawna siedziałem nad matematyką po prostu musiałem to zrobić. Było to wymagane na studiach. Ale nie sprawiło mi to trudności. Już od dawna lubię tą dziedzinę nauki.
                 - W ogóle to bardzo lubię się uczyć.
                 """
        )
        st.write("")
        st.write("")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- Projects ----
with st.container():
    st.write("---")
    st.header("Ten Projekt:")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
with image_column:
    # insert the image
with text_column:
    st.subheader("Oto projekt tejże stronki Internetowej wrzucony przy użyciu Netlify...")
    st.write("""
             Z Netlify nauczyłem się korzystać podczas krótkiego kursu, na którym tworzyłem stronkę ze swoim CV.
             Na codzień po prostu wrzucam coś tylko na Facebooka.
             No i oczywiście zamieszczam na GitHub. Ale z nowym Visual Studio Code, który jest programem open source, to wszystko jest zautomatyzowane.
             """)
    st.write("* Oto link do CV z Netlify.")
    st.write("[Moje CV >](https://sarnowskimateusz.netlify.app/)")
    st.write("* Oto link do tej stronki.")
    st.write("[Ten projekt >]()")