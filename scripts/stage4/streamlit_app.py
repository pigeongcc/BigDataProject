import streamlit as st
import pandas as pd
import numpy as np
import io
import altair as alt

url = {
    "header_pic": "https://akket.com/wp-content/uploads/2020/04/KinoPoisk-HD-Besplatnaya-podpiska-Filmy-Serialy-5.jpg",
    "kaggle": "https://www.kaggle.com/datasets/samlearner/letterboxd-movie-ratings-data?select=movie_data.csv",
    "recsys": "https://user-images.githubusercontent.com/50820635/85274861-7e0e3b00-b4ba-11ea-8cd3-2690ec55a67a.jpg",
}


ratings = pd.read_csv("/root/BigDataProject/data/ratings_export_pd.csv")
movies = pd.read_csv("/root/BigDataProject/data/movie_data_pd.csv")

q1 = pd.read_csv("/root/BigDataProject/output/eda/q1.csv", sep='\t')
q2 = pd.read_csv("/root/BigDataProject/output/eda/q2.csv", sep='\t')
q3 = pd.read_csv("/root/BigDataProject/output/eda/q3.csv", sep='\t')
q4 = pd.read_csv("/root/BigDataProject/output/eda/q4.csv", sep='\t')
q5 = pd.read_csv("/root/BigDataProject/output/eda/q5.csv", sep='\t')


st.title("Movies RecSys - Big Data Project, S23")
st.text("Done by B20-AI-01 students: Andrey Vagin and Sergey Golubev")
st.markdown("""<style>body {
    background-color: white;
}
.fullScreenFrame > div {
    display: flex;
    justify-content: center;
}
</style>""", unsafe_allow_html=True)

st.image(url["header_pic"], caption = "Movies RecSys", width=600)

st.markdown('---')
st.header('About Recommendation Systems')
st.image(url["recsys"], caption = "RecSys Map", width=1300)
st.markdown("""- Data: user rating matrix (URM)
- Model: memory-based collaborative filtering (alternating least squares)
- Evaluation type: offline (k-Fold cross-validation)
- Evaluation metric: RMSE on rating predictions""")


st.markdown('---')
st.header('Descriptive Data Analysis')
st.markdown("To train the RecSys model, we used the Letterboxd Movie Ratings Data, freely available on Kaggle ([link](%s))" % url['kaggle'])
emps_dda = pd.DataFrame(columns = ["Table", "# of instances", "# of features"],
                        data = [["Ratings", ratings.shape[0], ratings.shape[1]],
                                ["Movies", movies.shape[0], movies.shape[1]]])
st.write(emps_dda)

st.subheader('`Ratings` Table Characteristics')
st.markdown("**Couple of examples:**")
st.write(ratings.head(3))
st.markdown("**Dataframe info, missing values:**")
buffer = io.StringIO()
ratings.info(buf=buffer)
st.text(buffer.getvalue())
st.markdown("**Ratings distribution:**")
st.write(ratings.describe())

st.subheader('`Movies` Table Characteristics')
st.markdown("**Couple of examples:**")
st.write(movies.head(3))
st.markdown("**Dataframe info, missing values:**")
buffer = io.StringIO()
movies.info(buf=buffer)
st.text(buffer.getvalue())
st.markdown("**Ratings distribution:**")
st.write(movies.describe())


st.markdown('---')
st.header("Exploratory Data Analysis")

"""
1. users table is useless as it contains false vote_count value

2. users with low real vote_count value

3. movies with low real vote_count value

4. movies genres distribution

5. movies popularity distribution
"""

st.subheader('Query #1')
st.markdown('Real `vote_count` value for a sample user differs from the given one')
st.write(q1)
st.markdown('Q1 conclusion: we may exclude `users` table from considerations, as it contains no useful data: `user_id` is already present in `ratings` table, and `vote_count` provided is incorrect.')


st.subheader('Query #2')
st.markdown('Distribution of movies by # of votes:')
q2_bins = pd.qcut(q2.vote_count, 2, duplicates='drop').value_counts()
q2_dict = {'bin':['1 to 3', '4 to 6000'], 'vote_count':q2_bins.values}
q2_df = pd.DataFrame(q2_dict).set_index('bin')
st.bar_chart(q2_df)
st.markdown('Q2 conclusion: we should try to set the vote threshold for movies and omit those which do not reach it. After this evaluate the effect on performance.')


st.subheader('Query #3')
st.markdown('Distribution of users by # of votes:')
q3_vc = q3.vote_count.value_counts()
q3_ctr = 0
for i in range(1, 11):
    q3_ctr += q3_vc[i]
q3_dict = {'bin':['<= 10', '11 to 90k'], 'vote_count':[q3_ctr, len(q3)-q3_ctr]}
q3_df = pd.DataFrame(q3_dict).set_index('bin')
st.bar_chart(q3_df)
st.markdown('Q3 conclusion: we should try to set the vote threshold for users and omit those who do not reach it. After this evaluate the effect on performance.')


st.subheader('Query #4')
st.markdown('Distribution of movies by genres:')
st.write(alt.Chart(q4.sort_values('count', ascending=False)).mark_bar().encode(
    x=alt.X('genre', sort=None),
    y='count',
))
st.markdown('Q4 conclusion: we are capable of building bar charts.')


st.subheader('Query #5')
st.markdown('Distribution of `popularity` feature:')
q5.popularity = q5.popularity.replace({'\N': 0.6})
q5.popularity = q5.popularity.astype('float16')
q5_bins = pd.qcut(q5.popularity, 2, duplicates='drop').value_counts()
q5_bins = q5_bins.reindex([0.84, 6024.0])
st.bar_chart(q5_bins)
st.markdown("Q5 conclusion: we may divide the rating in the user rating matrix (URM) into two components.")
st.latex("Score_{final} = W_{orig} * Score_{orig} + W_{popular} * Score_{popular}")
st.markdown("""1. The original rating from `ratings` table (the term with the weight W_orig ~ 0.8)
2. The movie popularity. We may try binary format for the baseline solution: a movie is either popular, or not (weight W_popular = 1 - W_orig)""")



st.markdown('---')
st.header('Predictive Data Analisys')
st.subheader('Models Configurations')
st.table(pd.DataFrame([
            [1, 'ALS', 10, 10, 0.05, 1.41]],
            columns = ['Index', 'Model', 'Rank', 'MaxIter', 'RegParam', 'Rating RMSE'],
            ).set_index('Index'))
st.markdown('<center>Models configurations we trained and evaluated</center>', unsafe_allow_html = True)

# st.subheader('Evaluation')
# st.table(pd.DataFrame([
#             [1, '-', '-', 1.4, 0.9, 1.0],
#             [1, '-', '+', 1.4, 0.9, 1.0],
#             [1, '+', '-', 1.4, 0.9, 1.0],
#             [1, '+', '+', 1.4, 0.9, 1.0],
#             [2, '-', '-', 1.4, 0.9, 1.0],
#             [2, '-', '+', 1.4, 0.9, 1.0],
#             [2, '+', '-', 1.4, 0.9, 1.0],
#             [2, '+', '+', 1.4, 0.9, 1.0]],
#             columns = ['Model Index', 'Users Vote Limit', 'Movies Vote Limit', 'Rating RMSE', 'MAP', 'NDCG'],
#             ).set_index('Model Index')
# )

st.header('Inference')
st.markdown('Given a sample, predict its value and display results in a table.')

st.text("""+------------+-----------+----------+
|movie_id_enc|user_id_enc|prediction|
+------------+-----------+----------+
|       148.0|      471.0|  7.902857|
|       463.0|      471.0|  7.220045|
|       471.0|      471.0| 6.9887342|
|       496.0|      471.0|  6.625198|
|       833.0|      471.0| 7.3281274|
|      1088.0|      471.0| 7.5984254|
|      1238.0|      471.0| 7.5677934|
|      1342.0|      471.0|    4.2058|
|      1580.0|      471.0| 7.3103867|
|      1591.0|      471.0|  5.739383|
|      1645.0|      471.0| 6.8555117|
|      1829.0|      471.0|  7.620226|
|      1959.0|      471.0|  7.487306|
|      2122.0|      471.0| 6.5442185|
|      2142.0|      471.0| 7.1860785|
|      2366.0|      471.0|  6.768844|
|      2659.0|      471.0|  7.575165|
|      2866.0|      471.0|  7.089205|
|      3175.0|      471.0| 6.0085006|
|      3749.0|      471.0| 6.2505913|
+------------+-----------+----------+""")