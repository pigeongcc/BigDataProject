import streamlit as st
import pandas as pd
import numpy as np
import io

buffer = io.StringIO()
url = {
    "header_pic": "https://akket.com/wp-content/uploads/2020/04/KinoPoisk-HD-Besplatnaya-podpiska-Filmy-Serialy-5.jpg",
    "kaggle": "https://www.kaggle.com/datasets/samlearner/letterboxd-movie-ratings-data?select=movie_data.csv",
} 


ratings = pd.read_csv("/root/BigDataProject/data/ratings_export_pd.csv")
movies = pd.read_csv("/root/BigDataProject/data/movie_data_pd.csv")
movies.runtime = movies.runtime.replace(0, np.nan)
q1 = pd.read_csv("/root/BigDataProject/output/eda/q1.csv", sep='\t')



st.markdown('---')
st.title("Movies RecSys - Big Data Project, S23")
st.markdown("""<style>body {
    background-color: #eee;
}
.fullScreenFrame > div {
    display: flex;
    justify-content: center;
}
</style>""", unsafe_allow_html=True)

st.image(url["header_pic"], caption = "Movies RecSys", width=600)

st.markdown('---')
st.header('Descriptive Data Analysis')
st.text("To train the RecSys model, we used the Letterboxd Movie Ratings Data, freely available on Kaggle ([link](%s))" % url['kaggle'])
emps_dda = pd.DataFrame(columns = ["Table", "# of features", "# of instances"],
                        data = [["Ratings", ratings.shape[0], ratings.shape[1]],
                                ["Movies", movies.shape[0], movies.shape[1]]])
st.write(emps_dda)

st.subheader('`Ratings` table Characteristics')
st.markdown("**Couple of examples:**")
st.write(ratings.head(3))
st.markdown("**Dataframe info, missing values:**")
ratings.info(buf=buffer)
st.text(buffer.getvalue())
st.markdown("**Ratings distribution:**")
st.write(ratings.describe())
# TODO: bar chart of ratings

st.subheader('`Movies` table Characteristics')
st.markdown("**Couple of examples:**")
st.write(movies.head(3))
st.markdown("**Dataframe info, missing values:**")
movies.info(buf=buffer)
st.text(buffer.getvalue())
st.markdown("**Ratings distribution:**")
st.write(movies.describe())
# TODO: bar chart of vote count
# TODO: bar chart of year released

st.markdown('---')
st.header("Exploratory Data Analysis")
st.subheader('Q1')
st.text('The distribution of employees in departments')
st.bar_chart(q1)

st.markdown('---')
st.header('Predictive Data Analytics')
st.subheader('ML Model')
st.markdown('1. Linear Regression Model')
st.markdown('Settings of the model')
st.table(pd.DataFrame([['setting1', 1.0], ['setting2', 0.01], ['....','....']], columns = ['setting', 'value']))

st.markdown('2. SVC Regressor')
st.markdown('Settings of the model')
st.table(pd.DataFrame([['setting1', 1.0], ['setting2', 'linear'], ['....','....']], columns = ['setting', 'value']))

st.subheader('Results')
st.text('Here you can display metrics you are using and values you got')
st.table(pd.DataFrame([]))
st.markdown('<center>Results table</center>', unsafe_allow_html = True)
st.subheader('Training vs. Error chart')
st.write("matplotlib or altair chart")
st.subheader('Prediction')
st.text('Given a sample, predict its value and display results in a table.')
st.text('Here you can use input elements but it is not mandatory')