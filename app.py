import numpy as np
import pickle
import streamlit as st
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=39e2c68b80d80aa722abf450aedca470&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


st.header('Movie Recommender System')
movies = pickle.load(open('movie_list.pkl','rb'))
similarity_0 = pickle.load(open('chunk_0.pkl','rb'))
similarity_1 = pickle.load(open('chunk_1.pkl','rb'))
similarity_2 = pickle.load(open('chunk_2.pkl','rb'))
similarity_3 = pickle.load(open('chunk_3.pkl','rb'))
similarity_4 = pickle.load(open('chunk_4.pkl','rb'))
similarity_5 = pickle.load(open('chunk_5.pkl','rb'))
similarity_6 = pickle.load(open('chunk_6.pkl','rb'))
similarity_7 = pickle.load(open('chunk_7.pkl','rb'))
similarity_8 = pickle.load(open('chunk_8.pkl','rb'))

similarity = np.concatenate((similarity_0, similarity_1, similarity_2, similarity_3,
                            similarity_4, similarity_5, similarity_6, similarity_7, similarity_8), axis=0)

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])





