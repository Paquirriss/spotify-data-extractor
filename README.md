# 🎧 Proyecto de Ingeniería de Datos con Spotify

## 🚀 Descripción General

Este proyecto utiliza la API de Spotify para crear un modelo dimensional de artistas, álbumes, canciones y su popularidad. El objetivo es demostrar habilidades en ingeniería de datos y análisis de datos mediante la extracción, transformación y carga (ETL) de datos en archivos CSV, que pueden ser utilizados para análisis posteriores.

## 🗂 Estructura del Proyecto

1. **dim_artist.csv**: Contiene datos sobre los artistas.
    - `id`: Identificador único del artista.
    - `artist_name`: Nombre del artista.
    - `seguidores`: Número de seguidores del artista.

2. **dim_album.csv**: Contiene datos sobre los álbumes.
    - `id`: Identificador único del álbum.
    - `id_artist`: Identificador único del artista asociado con el álbum.
    - `name`: Nombre del álbum.

3. **dim_song.csv**: Contiene datos sobre las canciones.
    - `id`: Identificador único de la canción.
    - `song_name`: Nombre de la canción.
    - `id_artist`: Identificador único del artista asociado con la canción.
    - `id_album`: Identificador único del álbum asociado con la canción.
    - `release_date`: Fecha de lanzamiento de la canción.

4. **f_popularity.csv**: Contiene datos sobre la popularidad de las canciones.
    - `id_artist`: Identificador único del artista asociado con la canción.
    - `id_album`: Identificador único del álbum asociado con la canción.
    - `id_song`: Identificador único de la canción.
    - `popularity`: Puntuación de popularidad de la canción.

## 🛠 Requisitos

- Python 3.x
- Librería spotipy (Instalar con `pip install spotipy`)
- Cuenta de Desarrollador de Spotify (Necesitas crear una aplicación en Spotify para obtener `client_id` y `client_secret`)

## ⚙️ Configuración

1. Clona este repositorio en tu máquina local.
2. Instala las librerías de Python necesarias ejecutando:
    ```
    pip install spotipy
    ```
3. Obtén tus credenciales de la API de Spotify (`client_id` y `client_secret`) desde el Panel de Desarrolladores de Spotify.
4. Reemplaza las variables `client_id` y `client_secret` en el script con tus credenciales.

## 🏃‍♂️ Uso

1. Agrega los nombres de los artistas que deseas analizar en la variable `artists`.
2. Ejecuta el script. Los datos serán obtenidos desde la API de Spotify y guardados como archivos CSV en el directorio actual.
3. Los siguientes archivos serán generados:
    - `dim_artist.csv`
    - `dim_album.csv`
    - `dim_song.csv`
    - `f_popularity.csv`

## 📜 Ejemplo

El script está configurado actualmente para obtener datos de los siguientes artistas:
```python
artists = ['Shawn Mendes','Lady Gaga','Taylor Swift','Shakira']
```
Puedes agregar o eliminar artistas modificando la variable `artists` en el script.

## 🎯 Propósito

Este proyecto está dirigido a mostrar mis habilidades en Ingeniería de Datos y Análisis de Datos mediante la construcción de un modelo dimensional utilizando datos reales de la API de Spotify. El modelo puede ser extendido y adaptado para varios tipos de análisis.
