import pickle
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Spotify API credentials
CLIENT_ID = "97d9aa743b294555b4165c2d53d75952"
CLIENT_SECRET = "4fafce982f094f79b6eed84f7321820c"

client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Load preprocessed data and similarity matrix
music = pickle.load(open('data.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Helper function to get album art and Spotify URL
def get_song_info(song_name, artist_name):
    search_query = f"track:{song_name} artist:{artist_name}"
    results = sp.search(q=search_query, type="track", limit=1)

    if results["tracks"]["items"]:
        track = results["tracks"]["items"][0]
        album_cover_url = track["album"]["images"][0]["url"]
        song_url = track["external_urls"]["spotify"]

        # Get artist ID and use it to fetch genre
        artist_id = track["artists"][0]["id"]
        artist_info = sp.artist(artist_id)
        genres = artist_info.get("genres", [])

        # If genre list is empty, show "Unknown"
        genre = genres[0] if genres else "Unknown"

        return album_cover_url, song_url, genre

    return "https://shorturl.at/HYaaJ", None, "Unknown"


def recommend(song):
    if song not in music['song'].values:
        return None, [], [], [], [], [], []

    index = music[music['song'] == song].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    # Current song info
    current_artist = music.iloc[index].artist
    current_album, current_url, current_genre = get_song_info(song, current_artist)

    # Recommendations (excluding the song itself)
    recommended_names, recommended_artists = [], []
    recommended_posters, recommended_links, recommended_scores, recommended_genres = [], [], [], []

    for i in distances[1:6]:  # Top 5 similar songs
        song_name = music.iloc[i[0]].song
        artist_name = music.iloc[i[0]].artist
        score = distances[i[0]][1]

        album_cover, song_url, genre = get_song_info(song_name, artist_name)

        recommended_names.append(song_name)
        recommended_artists.append(artist_name)
        recommended_posters.append(album_cover)
        recommended_links.append(song_url)
        recommended_scores.append(score)
        recommended_genres.append(genre)

    return (
        song, current_artist, current_album, current_url, current_genre
    ), recommended_names, recommended_artists, recommended_posters, recommended_links, recommended_scores, recommended_genres


# Streamlit UI
st.set_page_config(page_title="Music Recommender", layout="wide")
st.title("🎶 Music Recommender System")

selected_song = st.selectbox("🎧 Select a song to get recommendations:", music['song'].values)

if st.button("Show Recommendations"):
    current, names, artists, posters, links, scores, genres = recommend(selected_song)

    if current:
        st.subheader("🎵 Currently Selected Song")
        st.image(current[2], width=200)
        st.markdown(f"**{current[0]}** by *{current[1]}*")
        st.caption(f"🎼 Genre: {current[4]}")
        if current[3]:
            st.markdown(f"[🔗 Listen on Spotify]({current[3]})")

        st.subheader("🎯 Top 5 Recommendations")

        cols = st.columns(5)
        for i in range(5):
            with cols[i]:
                st.image(posters[i], use_column_width=True)
                st.markdown(f"**{names[i]}**")
                st.caption(f"👤 {artists[i]}")
                st.caption(f"🎼 Genre: {genres[i]}")
                st.caption(f"🔁 Similarity Score: {scores[i]:.3f}")
                if links[i]:
                    st.markdown(f"[▶️ Spotify]({links[i]})")
                else:
                    st.markdown("🔗 Link not available")
    else:
        st.error("❌ Song not found in the database. Please try another.")
