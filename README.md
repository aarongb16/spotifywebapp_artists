# ComparadorDeArtistasSpotify
Web App hecha en Flask que realiza endpoints a la API de Spotify para obtener información de dos artistas y compararlos.

![Peek 2024-11-14 16-18](https://github.com/user-attachments/assets/355e17ee-d9f8-4ad4-a778-296c1a3f0c23)

## Origen
La idea original de la app se inspiró en el reto de programación de MoureDev, Oasis vs Linkin Park, donde se comparan las estadísticas de estos dos artistas mediante el uso de la API de Spotify, haciendo solicitudes con Python.

Posteriormente, este servidor se encargó de desarrollar su propia versión, que consiste en una aplicación web hecha con Flask.

## Enfoque propuesto
La aplicación está diseñada para que el usuario pueda ingresar a través de un formulario los nombres de los artistas que desea comparar. Una vez introducidos los nombres y enviada la información, el programa se encarga de realizar las consultas y presentar la comparativa de las estadísticas de los artistas.

Todo esto se lleva a cabo utilizando endpoints de la API de Spotify mediante Python y su framework Flask, que crea las rutas del menú principal y la de comparación, y renderiza el HTML para mostrar la información al usuario

## Requisitos
- Conocimientos Básicos de la Línea de Comandos.
- Conocimientos Básicos de Entornos Virtuales en Python.
- Contar con `CLIENT_SECRET` y `CLIENT_ID` que proporciona la web de developer.spotify.com cuando creas un App.

## Instrucciones
1. Clonar el repositorio y dirigirse al directorio donde se encuentra el repositorio clonado
2. Crear un entorno virtual (e.g. `$ python -m venv venv`)
3. Activar el entorno virtual (e.g. `$ source venv/bin/activate`)
4. Instalar los paquetes necesarios (e.g. `(venv) $ pip install -r requirements.txt`)
5. Modificar el `CLIENT_SECRET` en el archivo `env.py` al que te haya proporcionado la web de developers de spotify
6. Modificar el `CLIENT_ID` en el archivo `functions.py` al que te haya proporcionado la web de developers de spotify
7. Corre el `app.py` y dirigirse al link que proporciona Flask para entrar a la app
8. Probar ingresando artistas y viendo los resultados.

## Implementación
- Desarrollado con Python 3.10.12 y Flask
- Y las tecnologías webs: HTML5, CSS Y JS


