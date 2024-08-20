import csv
import codecs
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
 
# Credenciales de la aplicación Spotify
client_id = ''
client_secret = ''
 
# Inicializar el objeto Spotify
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
 
 
# Función para obtener los seguidores de un artista
def get_artist_followers(artist_id):
    artist = sp.artist(artist_id)
    return artist['followers']['total']
 
# Función para obtener los datos de los álbumes de un artista
def get_albums_data(artist_id):
    print(f"Obteniendo datos de álbumes para el artista con ID: {artist_id}")
    albums_data = []
    albums = sp.artist_albums(artist_id, album_type='album')
    for album in albums['items']:
        album_data = {
            'id': album['id'],
            'id_artist': artist_id,
            'name': album['name']
        }
        albums_data.append(album_data)
    return albums_data
 
# Función para obtener los datos de las canciones de un álbum
def get_songs_data(album_id, artist_id):
    print(f"Obteniendo datos de canciones para el álbum con ID: {album_id}")
    songs_data = []
    tracks = sp.album_tracks(album_id)
    for track in tracks['items']:
        if 'album' in track and 'release_date' in track['album']:
            release_date = track['album']['release_date'][:10]  # Tomar solo la fecha de lanzamiento en formato AAAAMMDD
        else:
            release_date = ''  # Establecer como cadena vacía si la información del álbum no está disponible
        song_data = {
            'id': track['id'],
            'song_name': track['name'],
            'id_artist': artist_id,
            'id_album': album_id,
            'release_date': release_date
        }
        songs_data.append(song_data)
    return songs_data
 
# Función para obtener los datos de popularidad de las canciones
def get_popularity_data(all_songs_data):
    popularity_data = []
    for song in all_songs_data:
        try:
            print(f"Obteniendo popularidad para la canción: {song['song_name']} - ID: {song['id']}")
            track = sp.track(song['id'])
            popularity_data.append({
                'id_artist': song['id_artist'],
                'id_album': song['id_album'],
                'id_song': song['id'],
                'popularity': track['popularity']
            })
        except spotipy.SpotifyException as e:
            print(f"Error al obtener datos de popularidad para la canción {song['id']}: {e}")
            # Manejar el error de autenticación u otros errores de Spotify
        except Exception as e:
            print(f"Error inesperado al obtener datos de popularidad para la canción {song['id']}: {e}")
            # Manejar otros errores de forma genérica
    return popularity_data
 

print("Obteniendo datos de artistas...")
# Obtener datos de artistas
artists = ['Shawn Mendes','Lady Gaga','Taylor Swift','Shakira']
artists_data = []
for artist_name in artists:
    print(f"Buscando información del artista: {artist_name}")
    results = sp.search(q='artist:' + artist_name, type='artist')
    if len(results['artists']['items']) > 0:
        artist = results['artists']['items'][0]
        artist_data = {
            'id': artist['id'],
            'artist_name': artist['name'],
            'seguidores': get_artist_followers(artist['id'])
        }
        artists_data.append(artist_data)
 
# Obtener datos de álbumes y canciones
print("Obteniendo datos de álbumes y canciones...")
albums_data = []
all_songs_data = []
for artist_data in artists_data:
    albums_data.extend(get_albums_data(artist_data['id']))
    for album_data in albums_data:
        all_songs_data.extend(get_songs_data(album_data['id'], artist_data['id']))
 
# Obtener datos de popularidad
print("Obteniendo datos de popularidad...")
popularity_data = get_popularity_data(all_songs_data)
 
# Escribir datos en archivos CSV
print("Escribiendo datos en archivos CSV...")
with codecs.open('dim_artist.csv', 'w', 'utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['id', 'artist_name', 'seguidores'])
    writer.writeheader()
    writer.writerows(artists_data)
 
with codecs.open('dim_album.csv', 'w', 'utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['id', 'id_artist', 'name'])
    writer.writeheader()
    writer.writerows(albums_data)
 
with codecs.open('dim_song.csv', 'w', 'utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['id', 'song_name', 'id_artist', 'id_album', 'release_date'])
    writer.writeheader()
    writer.writerows(all_songs_data)
 
with codecs.open('f_popularity.csv', 'w', 'utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['id_artist', 'id_album', 'id_song', 'popularity'])
    writer.writeheader()
    writer.writerows(popularity_data)
 
print("Proceso completado. Archivos CSV creados exitosamente.")