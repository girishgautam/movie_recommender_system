import streamlit as st
import pickle
import pandas as pd
import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY')


def fetch_poster(movie_id):
    '''
    fetching posters for the movies from TMDB website using an api
    '''
    url = 'https://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US'.format(movie_id, api_key)
    response = requests.get(url)
    data = response.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    movie_poster = []
    for i in movies_list:
        movie_id = movies_df.iloc[i[0]]['id']
        recommended_movies.append(movies_df.iloc[i[0]]['title'])
        movie_poster.append(fetch_poster(movie_id))

    return recommended_movies, movie_poster

movie_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies_df = pd.DataFrame(movie_dict)


similarity = pickle.load(open('similarity.pkl', 'rb'))


st.title('Movie Recommender System')
selected_movie = st.selectbox('Type or select a movie from the dropdown', movies_df['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])



