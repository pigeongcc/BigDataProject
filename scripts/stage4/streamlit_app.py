import streamlit as st
import pandas as pd
import numpy as np
import io
import altair as alt

buffer = io.StringIO()
url = {
    "header_pic": "https://akket.com/wp-content/uploads/2020/04/KinoPoisk-HD-Besplatnaya-podpiska-Filmy-Serialy-5.jpg",
    "kaggle": "https://www.kaggle.com/datasets/samlearner/letterboxd-movie-ratings-data?select=movie_data.csv",
    "users_useless": "https://doc-0k-34-docs.googleusercontent.com/docs/securesc/6vgfqgfhgmfl6ia38c4bpaq0c20ebc3m/dlnqliih0m8v523178ddpmass4vkvkvh/1683747975000/04388380893538145158/04388380893538145158/1Qn2plL6QEKM9DWiemEgLftajfV8Yryut?e=download&ax=ADWCPKCzpNeqVNIAMrnExUEQeXKhTHdnEefUXXPFe5m8NIoQVz68u7j_mMzPVjFJU-__pplY7LL_l-CPxa6ubE4N3900krO01nQAan_WJQUvKAzKsksZeGSJeHVggFF-2Ryr6ytHEmmR4mOjx8BrLQsAEUtJcmhGA3b8z5TawjT8XODuc3BQcOQkmjTm9OBjWeQngSiabQJK55S0zXsxmu3Su5iufwv4_ViJtu9pop8mKTcT3VQoIn5VqJi5ZaHb9qCQ1euBBOdjjnPTtl3mROrMX3R215172uvabvpezj8wd6NlB3Uw-J3EmY-LFDMF90pPCmb-s1ZUdskmZ4Cpq93RlInFIMY9T5gUIK-pMOTdguJN5K77on68_yR7wkySN8GOcLIjSBKAYnsbfEizfebuKQXPn7pY50fzmsut0bD7spFHxuIhswYFh-D_C1rTmNvdcvsBNYMPe_wAciFRi2rM0bX-GLjKMG_-CLt_iVv2UmXfs3VHnXRdmH0FBSVoyijgZqPutSc0wwban8TO4QMZmTaZT-WHcoNWYU_5GHHxKSdBF5DRWhu4FwRrIqeTM4Gh0aCjoJodUmm_5S5ud5l52YQ6U7bhI3Zr1Rb750aCB4FhrPC1tIrUWsA564_kU8Gfq9BQ2eoIru4yK1YJE-loLKzTp2o8TXdoifkqvrolwxARFREVbbX4DmVqwJDSerniBt2bTZGLvodrEPGV3gMbATCn6eqF_iO7eHxsKbjXRBRSiMMT7VMHjj7AVzvtV0wDzHSNyc7TIlsUPbSxsUALsgu_9-7a1PSkIuQ-wZGhU1FK9pNUK3ECs8vY69ijkw3CMvz75vIDMvqdicZrePjCEgg0dvCKwsYPkXEd01jtzTtkTWHOKaCG_ObSufYCiSVxR9ZehjNY-jN_JV34YzR94rKgUwUZnWmW&uuid=2436eadc-8146-433b-aa8c-be17df15a764&authuser=0&nonce=so6q8fuj9l4po&user=04388380893538145158&hash=qch9i62pvfgev6bfsdaviip9g43hdhlr",
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
    background-color: white;
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

"""
1. users table is useless as it contains false vote_count value

2. users with low real vote_count value

3. movies with low real vote_count value

4. movies genres distribution

5. movies popularity distribution
"""

st.subheader('Query #1')
st.text('Real `vote_count` value for a sample user differs from the given one')
st.write(q1)
st.image(url["users_useless"], caption = "Incorrect value in Users table", width=300)
st.text('Q1 conclusion: we may exclude `users` table from considerations, as it contains no useful data: `user_id` is already present in `ratings` table, and `vote_count` provided is incorrect.')

st.subheader('Query #5')
st.text('Distribution of `popularity` feature:')
q5.popularity = q5.popularity.replace({'\N': 0.6})
q5.popularity = q5.popularity.astype('float16')
q5_bins = pd.qcut(q5.popularity, 2, duplicates='drop').value_counts()
q5_bins = q5_bins.reindex([0.84, 6024.0])
print("bins:")
print(q5_bins)
print("dtype:")
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
