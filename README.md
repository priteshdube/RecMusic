# RecMusic

A personalized music recommendation system that enhances music discovery by analyzing user listening behavior and track similarities. Built using Python, the Spotify API, and NLP techniques, RecMusic provides real-time, tailored song suggestions through an interactive Streamlit interface.

## Features
- **Personalized Recommendations**: Suggests songs based on user listening habits and track content similarity.
- **NLP-Based Matching**: Utilizes TF-IDF Vectorization and Cosine Similarity for song recommendation.
- **Interactive UI**: A Streamlit-powered web application for seamless user experience.
- **Spotify API Integration**: Fetches real-world track metadata for more accurate suggestions.

## Technologies Used
- **Python**
- **Spotify API & Spotipy**
- **TF-IDF Vectorizer & Cosine Similarity**
- **Pandas, NLTK (PorterStemmer)**
- **Streamlit**

## Installation & Setup

### Prerequisites
Ensure you have the following installed:
- Python (>=3.7)
- pip (Python package manager)

### Clone the Repository
```sh
git clone https://github.com/yourusername/RecMusic.git
cd RecMusic
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

### Set Up Spotify API Credentials
1. Create a Spotify Developer account: [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)
2. Register an application and get your **Client ID** and **Client Secret**.
3. Create a `.env` file in the project root and add:
   ```sh
   SPOTIPY_CLIENT_ID='your_client_id'
   SPOTIPY_CLIENT_SECRET='your_client_secret'
   SPOTIPY_REDIRECT_URI='http://localhost:8888/callback'
   ```

### Run the Application
```sh
streamlit run app.py
```

## Usage
1. Launch the Streamlit app as described above.
2. Log in with your Spotify credentials.
3. Enter a song or playlist to receive personalized recommendations.
4. Explore recommended tracks and refine suggestions based on your preferences.

## Contributing
Feel free to submit issues or fork the repository to enhance the project.


