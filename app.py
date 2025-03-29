import pickle
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = "97d9aa743b294555b4165c2d53d75952"
CLIENT_SECRET = "4fafce982f094f79b6eed84f7321820c"

# Initialize the Spotify client
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_song_info(song_name, artist_name):
    search_query = f"track:{song_name} artist:{artist_name}"
    results = sp.search(q=search_query, type="track")

    if results and results["tracks"]["items"]:
        track = results["tracks"]["items"][0]
        album_cover_url = track["album"]["images"][0]["url"]
        song_url = track["external_urls"]["spotify"]
        return album_cover_url, song_url
    else:
        return "https://shorturl.at/HYaaJ", None
    
def recommend(song):
    index = music[music['song'] == song].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_music_names = []
    recommended_music_posters = []
    recommended_music_links = []

    for i in distances[1:6]:
        # fetch the album cover and song URL from Spotify
        artist = music.iloc[i[0]].artist
        album_cover_url, song_url = get_song_info(music.iloc[i[0]].song, artist)
        
        recommended_music_posters.append(album_cover_url)
        recommended_music_names.append(music.iloc[i[0]].song)
        recommended_music_links.append(song_url)

    return recommended_music_names, recommended_music_posters, recommended_music_links



# Streamlit UI
st.header('Music Recommender System')
music = pickle.load(open('data.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

music_list = music['song'].values
selected_song = st.selectbox(
    "Type or select a song from the dropdown",
    music_list
)

if st.button('Show Recommendation'):
    recommended_music_names, recommended_music_posters, recommended_music_links = recommend(selected_song)
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.text(recommended_music_names[0])
        st.image(recommended_music_posters[0])
        st.markdown(f"[Listen on Spotify]({recommended_music_links[0]})")
    
    with col2:
        st.text(recommended_music_names[1])
        st.image(recommended_music_posters[1])
        st.markdown(f"[Listen on Spotify]({recommended_music_links[1]})")

    with col3:
        st.text(recommended_music_names[2])
        st.image(recommended_music_posters[2])
        st.markdown(f"[Listen on Spotify]({recommended_music_links[2]})")

    with col4:
        st.text(recommended_music_names[3])
        st.image(recommended_music_posters[3])
        st.markdown(f"[Listen on Spotify]({recommended_music_links[3]})")

    with col5:
        st.text(recommended_music_names[4])
        st.image(recommended_music_posters[4])
        st.markdown(f"[Listen on Spotify]({recommended_music_links[4]})")
