from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie



st.set_page_config(page_title="Yj", page_icon=":tada:", layout="wide")

def load_lattieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use Local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")


#---- LOAD ASSET ---
vis_url = load_lattieurl("https://assets8.lottiefiles.com/packages/lf20_ic37y4kv.json")
vis2_url = load_lattieurl("https://assets8.lottiefiles.com/packages/lf20_49rdyysj.json")
img_project1 = ("Images/images.png" )
img_project2 = ("Images/images 1.png")

# -- Header section --
st.subheader("Hi, YogeshJaguri this side :wave:")
st.title("a data scientist enthusiast from India")
st.write("As a data science enthusiast, I am passionate about leveraging the power of data to drive business decisions and solve complex problems. With expertise in data analysis, machine learning, and visualization, I turn large, complex data sets into actionable insights that drive growth and innovation. Whether it's developing predictive models, creating interactive dashboards, or communicating findings to stakeholders, I am dedicated to helping organizations make data-driven decisions and stay ahead of the curve.")
st.write("[view more >](https://github.com/yogeshjaguri)")

#---- What i do ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do as a DataScientist")
        st.write("##")
        st.write(
            """
            As a data scientist, I help organizations extract insights and make data-driven decisions by analyzing and interpreting large, complex data sets. My work involves a combination of several activities such as:

            1. Collecting and cleaning data from various sources to ensure its quality and accuracy.

            2. Exploring and visualizing data to uncover patterns and trends that can inform business decisions.

            3. Building models and algorithms using machine learning techniques to predict outcomes and make predictions.
            """
        )
        
        with right_column:
          st_lottie(vis_url, height=400, key="coding")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write(
       
            """
            4. Communicating findings and insights to stakeholders through clear and effective visualizations, reports, and dashboards.

            5. Continuously monitoring the performance of the models and updating them as needed.

            6. Staying up-to-date with the latest developments and techniques in the field of data science and applying them to improve the performance of models.

            Overall, I play an important role in helping organizations make sense of their data and use it to drive growth and innovation. 
            """
        )

        st.write("[github: ](https://github.com/yogeshjaguri")
        with right_column:
          st_lottie(vis2_url, height=400, key="analyse")


# --- PROJECTS---
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_project1)
    with text_column:
        st.subheader("Predicting Customer Churn in a Telecommunications Company")
        st.write(
            """
            The goal of this project was to predict which customers were likely to churn (cancel their service) in a telecommunications company. By identifying at-risk customers, the company could take proactive steps to retain them and prevent revenue loss.

            The data used in this project was collected from the company's customer database, including information such as customer demographics, account information, and call records. The data was cleaned and preprocessed to ensure its quality and accuracy.

            Exploratory data analysis was performed to understand patterns and trends in the data and identify potential predictors of churn. Feature engineering was done to create new variables that could improve the predictive power of the models.

            A variety of machine learning models were trained and tested, including logistic regression, decision trees, and random forests. Model performance was evaluated using metrics such as accuracy and AUC-ROC score.

            The final model was able to accurately predict customer churn with an AUC-ROC score of 0.89. The model's predictions were then used to create a list of at-risk customers that the company could target with retention campaigns.

            Overall, this project helped the telecommunications company to better understand the factors that contribute to customer churn and take steps to retain valuable customers, ultimately resulting in increased revenue.
                        """
        )
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=OTqE3ruMwrs)")    


with st.container():
    st.write("---")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_project2)
    with text_column:
        st.subheader("Predicting somethig in a Telecommunications Company")
        st.write(
        """
        The goal of this project was to predict which customers were likely to churn (cancel their service) in a telecommunications company. By identifying at-risk customers, the company could take proactive steps to retain them and prevent revenue loss.

        The data used in this project was collected from the company's customer database, including information such as customer demographics, account information, and call records. The data was cleaned and preprocessed to ensure its quality and accuracy.

        Exploratory data analysis was performed to understand patterns and trends in the data and identify potential predictors of churn. Feature engineering was done to create new variables that could improve the predictive power of the models.

        A variety of machine learning models were trained and tested, including logistic regression, decision trees, and random forests. Model performance was evaluated using metrics such as accuracy and AUC-ROC score.

        The final model was able to accurately predict customer churn with an AUC-ROC score of 0.89. The model's predictions were then used to create a list of at-risk customers that the company could target with retention campaigns.

        Overall, this project helped the telecommunications company to better understand the factors that contribute to customer churn and take steps to retain valuable customers, ultimately resulting in increased revenue.
        """
        )
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=OTqE3ruMwrs)")    


#---CONTACT FORM---
with st.container():
    st.write("---")
    st.header("get in touch with me")
    st.write("##")


    #from formsubmitt.co/
    contact_form = """
    <form action="https://formsubmit.co/your@email.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder = "Your Name" required>
        <input type="email" name="email" placeholder ="E-mail address" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()