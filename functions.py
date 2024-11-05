import requests
import base64
import env

CLIENT_SECRET = env.CLIENT_SECRET


# CLIENT ID que la SPOTIFY API Proporciona
CLIENT_ID = "SPOTIFY_CLIENT_ID"

# Funcion para obtener token de validacion del Spotify API
def get_token() -> str:
        url = "https://accounts.spotify.com/api/token"
        headers = {
                "Authorization": "Basic " + base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode(),
                "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {"grant_type": "client_credentials"}
        response = requests.post(url, headers=headers, data=data)

        if response.status_code != 200:
                raise Exception(f"Error obteniendo el token: {response.json()}")

        else:
                return response.json()["access_token"]
token = get_token()

# Funcion para obtener fecha de lanzamiento de su ultimo album
def get_lastalbum(token: str, id: str):
	url = f"https://api.spotify.com/v1/artists/{id}/albums"
	headers = {"Authorization": F"Bearer {token}"}
	response = requests.get(url, headers=headers)
	if response.status_code != 200:
		raise Exception(
			f"Error obteniendo la fecha del lanzamiento del ultimo album: {response.json()}"
		)
	results = response.json()
	return results["items"][0]['release_date']

# Obtenemos el track mas escuchado del artista
def top_tracks(token: str, id: str):
	url = f"https://api.spotify.com/v1/artists/{id}/top-tracks?country=GB"
	headers = {"Authorization": F"Bearer {token}"}
	response = requests.get(url, headers=headers)
	if response.status_code != 200:
		raise Exception(
			f"Error obteniendo la cancion mas escuchada: {response.json()}"
		)
	results = response.json()
	return results['tracks'][0]['name']

#Funcion para obtener la data del artista {Nombre, Seguidores, Generos, Imagen, etc}
# Hacemos un endpoint de la data del artista y esa data la guardamos en un dict
def get_artist_data(artist_name, token):
    headers = {
        'Authorization': f'Bearer {token}'
    }
    # Buscar el artista por nombre
    search_url = f'https://api.spotify.com/v1/search?q={artist_name}&type=artist&limit=1'
    response = requests.get(search_url, headers=headers)
    results = response.json().get('artists', {}).get('items', [])
    
    if not results:
        return None  # En caso de que el artista no se encuentre
    
    artist = results[0]
    artist_data = {
        'name': artist['name'],
        'followers': artist['followers']['total'],
        'popularity': artist['popularity'],
        'genres': artist['genres'][:3],
        'image': artist['images'][0]['url'] if artist['images'] else None,
        'top_track': top_tracks(token, artist['id']),
        'releasedate_lastalbum': get_lastalbum(token, artist['id'])
    }
    return artist_data
