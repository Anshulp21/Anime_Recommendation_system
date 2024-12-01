import requests

def search_anime(name, genre):
    url = "https://graphql.anilist.co"
    query = """
    query ($name: String, $genre: [String]) {
      Page(page: 1, perPage: 10) {
        media(search: $name, genre_in: $genre) {
          id
          title {
            romaji
            english
          }
          genres
        }
      }
    }
    """
    variables = {
        'name': name,
        'genre': genre.split(',') if genre else []
    }

    response = requests.post(url, json={'query': query, 'variables': variables})
    print(f"Sending request to Anilist with variables: {variables}")  # Debugging line
    if response.status_code == 200:
        data = response.json()
        print(f"Received data: {data}")  # Debugging line
        return data['data']['Page']['media']
    else:
        return []
