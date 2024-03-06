

# Music Recommendation System

This project implements a music recommendation system based on natural language processing techniques and the Spotify API. It provides users with recommendations for similar songs based on a selected song using cosine similarity.

## Features

- **Data Preprocessing**: The training script preprocesses the Spotify song data, including text cleaning and tokenization.
- **TF-IDF Vectorization**: Text data is transformed into TF-IDF vectors to represent the songs.
- **Cosine Similarity**: Similarity between songs is calculated using cosine similarity on the TF-IDF vectors.
- **Spotify API Integration**: The app script utilizes the Spotify API to retrieve album cover URLs for recommended songs.
- **Command-line Interface**: Users can interact with the recommendation system through a simple command-line interface.
- **Serialization**: Trained models and data are serialized using pickle for efficient loading and reuse.

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/your-username/music-recommendation-system.git
    cd music-recommendation-system
    ```

2. Install dependencies:

    ```
    pip install -r requirements.txt
    ```

3. Obtain Spotify API credentials:
   
   - Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).
   - Create a new application and note down the client ID and client secret.

4. Update the `app.py` file with your Spotify API credentials:

    ```python
    CLIENT_ID = "your-client-id"
    CLIENT_SECRET = "your-client-secret"
    ```

## Usage

1. Run the training script to preprocess data, train the model, and serialize it:

    ```
    python train.py
    ```

2. Launch the application to interact with the recommendation system:

    ```
    python app.py
    ```

3. Follow the prompts to select a song and view recommended songs along with their album cover URLs.

## Acknowledgments

- This project utilizes the Spotipy library to interact with the Spotify API.
- Data used for training the recommendation system is sourced from [Spotify Million Playlist Dataset Challenge](https://www.aicrowd.com/challenges/spotify-million-playlist-dataset-challenge).
- This project is for educational purposes and inspired by various tutorials and resources on recommendation systems.
