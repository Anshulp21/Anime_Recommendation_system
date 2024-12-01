
# Anime Recommendation System

This project is a REST API built with FastAPI for an Anime Recommendation System. It allows users to search for anime by name or genre, view recommendations based on their preferences, and manage their preferences and authentication using JWT.

## Features
- **User Registration and Login:** Secure authentication with JWT.
- **Anime Search:** Search for anime by name or genre.
- **Recommendations:** Fetch recommended anime based on the user's preferences.
- **User Preferences:** Store and manage user preferences (e.g., favorite genres).

## Setup

### Prerequisites
- Python 3.11
- PostgreSQL (for the database)

### Installation Steps

1. Clone the repository:

    ```bash
    https://github.com/Anshulp21/Anime_Recommendation_system.git
    cd anime-recommendation-system
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file to store your environment variables:

    ```
    DATABASE_URL=postgresql://user:password@localhost:5432/anime_db
    SECRET_KEY=your_secret_key
    ANILIST_API_URL=https://graphql.anilist.co
    ```

4. Set up the database:

    ```bash
    uvicorn app.main:app --reload
    ```

    You can now access the FastAPI documentation at `http://localhost:8000/docs`.


### API Endpoints

- `/auth/register`: Register a new user.
- `/auth/login`: Login and retrieve a JWT token.
- `/anime/search`: Search anime by name or genre.
- `/anime/anime/recommendations` :search anime by preferences.
- `/user/preferences`: Manage user preferences (e.g., favorite genres).

