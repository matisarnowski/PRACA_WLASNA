"""Module PIL providing functions for opening the image. 
Module os providing functions for opening path to files. 
Module streamlit is basic module in this code."""
import os
from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Moja stronka", page_icon=":open_book:", layout="wide")


def load_lottieurl(url):  # sourcery skip: assign-if-exp, reintroduce-else
    """**load_lottieurl(url)**

    Loads and returns the JSON data from a given URL.

    Args:
        url (str): The URL to load the JSON data from.

    Returns:
        dict or None: The JSON data loaded from the URL, or None if the request fails.

    Examples:
        ```python
        data =
        load_lottieurl("https://lottie.host/5627c703-4224-48ab-a721-e650f35c3c0f/FrnjXWGhia.json")
        ```"""
    r = requests.get(url, timeout=10)
    return None if r.status_code != 200 else r.json()


# Use local CSS
def local_css(file_name):
    """ "**local_css(file_name)**

    Loads and applies local CSS styles to the Streamlit app.

    Args:
        file_name (str): The name of the CSS file to load.

    Returns:
        None

    Examples:
        ```python
        local_css("styles/style.css")
        ```"""
    with open(file_name, encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css(os.path.join("styles", "style.css"))

# ---- Load Assets ----
lottie_coding = load_lottieurl(
    "https://lottie.host/5627c703-4224-48ab-a721-e650f35c3c0f/FrnjXWGhia.json"
)
image_code = Image.open(os.path.join("images", "moja_stronka_1.jpg"))

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
                 - Zazwyczaj po prostu uczę się programować. 
                 Piszę proste programiki w języku programowania Python, 
                 lub proste strony Internetowe z użyciem JavaScript, CSS i HTML.
                 - Poza tym sporo do niedawna siedziałem nad matematyką po prostu musiałem to zrobić. 
                 Było to wymagane na studiach. Ale nie sprawiło mi to trudności. 
                 Już od dawna lubię tą dziedzinę nauki.
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
    st.image(image_code)
with text_column:
    st.subheader("Oto projekt tejże stronki Internetowej oraz moje CV...")
    st.write(
        """
             Z Netlify nauczyłem się korzystać podczas krótkiego kursu, 
             na którym tworzyłem stronkę ze swoim CV.
             Na codzień po prostu wrzucam coś tylko na Facebooka.
             No i oczywiście zamieszczam na GitHub. 
             Ale z nowym Visual Studio Code, 
             który jest programem open source, 
             to wszystko jest zautomatyzowane.
             """
    )
    st.write("* Oto link do CV z Netlify.")
    st.markdown("[Moje CV >](https://sarnowskimateusz.netlify.app/)")
    st.write("* A po lewej stronie kod tej stronki.")
    st.write(
        """
        Ostatnio przeczytane książki przeze mnie, które serdecznie polecam to: \n
        ** Racjonalność Steven Pickling \n
        ** Potęga Nieskończoności Steven Strogatz \n
        ** Deep Learning Głęboka Rewolucja Terrens Sejnowski \n
        ** Demon w Maszynie Paul Davies \n
        ** Umysł matematyczny Bartosz Brożek, Mateusz Hohold \n
        """
    )

with st.container():
    st.write("---")
    st.header("Wyślij mi tu swój adres email, abym się z Tobą skontaktował!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    CONTACT_FORM = """
    <form action="https://formsubmit.co/matsarnow@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Twoje imię" required>
        <input type="email" name="email" placeholder="Twój email" required>
        <textarea name="message" placeholder="Twoja wiadomość do mnie: " required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(CONTACT_FORM, unsafe_allow_html=True)
    with right_column:
        st.empty()
