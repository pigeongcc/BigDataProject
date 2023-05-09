import streamlit as st
import pandas as pd
import numpy as np
import io
import altair as alt

buffer = io.StringIO()
url = {
    "header_pic": "https://akket.com/wp-content/uploads/2020/04/KinoPoisk-HD-Besplatnaya-podpiska-Filmy-Serialy-5.jpg",
    "kaggle": "https://www.kaggle.com/datasets/samlearner/letterboxd-movie-ratings-data?select=movie_data.csv",
} 


ratings = pd.read_csv("/root/BigDataProject/data/ratings_export_pd.csv")
movies = pd.read_csv("/root/BigDataProject/data/movie_data_pd.csv")
movies.runtime = movies.runtime.replace(0, np.nan)
q1 = pd.read_csv("/root/BigDataProject/output/eda/q1.csv", sep='\t')
q2 = pd.read_csv("/root/BigDataProject/output/eda/q2.csv", sep='\t')
q3 = pd.read_csv("/root/BigDataProject/output/eda/q3.csv", sep='\t')
q4 = pd.read_csv("/root/BigDataProject/output/eda/q4.csv", sep='\t')
q5 = pd.read_csv("/root/BigDataProject/output/eda/q5.csv", sep='\t')



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

st.subheader('`Ratings` Table Characteristics')
st.markdown("**Couple of examples:**")
st.write(ratings.head(3))
st.markdown("**Dataframe info, missing values:**")
ratings.info(buf=buffer)
st.text(buffer.getvalue())
st.markdown("**Ratings distribution:**")
st.write(ratings.describe())
# TODO: bar chart of ratings

st.subheader('`Movies` Table Characteristics')
st.markdown("**Couple of examples:**")
st.write(movies.head(3))
st.markdown("**Dataframe info, missing values:**")
movies.info(buf=buffer)
st.text(buffer.getvalue())
st.markdown("**Ratings distribution:**")
st.write(movies.describe())
# TODO: bar chart of real vote count
# TODO: bar chart of year released


st.markdown('---')
st.header("Exploratory Data Analysis")

st.subheader('Query #1')
st.text('Distribution of employees in departments')
st.write(q1)
# TODO: show screenshot from kaggle

st.subheader('Query #5')
st.text('Distribution of `popularity` feature:')
q5.popularity = q5.popularity.replace({'\N': 0.6})
q5.popularity = q5.popularity.astype('float16')
q5_bins = pd.qcut(q5.popularity, 6, duplicates='drop').value_counts()
print("bins:")
print(q5_bins)
print("dtype:")
q5_bins = q5_bins.reindex([0.6, 6024.0, 1.4, 2.795, 0.84])
print(q5_bins.dtype)
st.bar_chart(q5_bins)



st.markdown('---')
st.header('Predictive Data Analisys')
st.subheader('Models Configurations')
st.table(pd.DataFrame([
            [1, 'ALS', 'setting1', 1.0],
            [2, 'CF', 'setting2', 0.01]],
            columns = ['Model Index', 'Model', 'Param1', 'Param2'],
            ).set_index('Model Index'))
st.markdown('<center>Models configurations we trained and evaluated</center>', unsafe_allow_html = True)

st.subheader('Evaluation')
st.table(pd.DataFrame([
            [1, '-', '-', 1.4, 0.9, 1.0],
            [1, '-', '+', 1.4, 0.9, 1.0],
            [1, '+', '-', 1.4, 0.9, 1.0],
            [1, '+', '+', 1.4, 0.9, 1.0],
            [2, '-', '-', 1.4, 0.9, 1.0],
            [2, '-', '+', 1.4, 0.9, 1.0],
            [2, '+', '-', 1.4, 0.9, 1.0],
            [2, '+', '+', 1.4, 0.9, 1.0]],
            columns = ['Model Index', 'Users Vote Limit', 'Movies Vote Limit', 'Rating RMSE', 'MAP', 'NDCG'],
            ).set_index('Model Index')
)
st.markdown('<center>Evaluation results</center>', unsafe_allow_html = True)
st.subheader('Training vs. Error chart')
st.write("matplotlib or altair chart")

st.header('Inference')
st.text('Given a sample, predict its value and display results in a table.')
