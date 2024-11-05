import requests
import functions
from flask import Flask, render_template, request

app = Flask(__name__)

# Cargamos el menu principal
@app.route('/')
def index():
    return render_template('compare.html')

#creamos la ruta de comparacion
# Obtenemos los nombre ingresados por el usuario en el html
# Los usamos como parametro para la funcion que obtiene la data del artista
# Renderizamos el HTMl y le pasamos la data de los dos artistas.
@app.route('/compare', methods=['POST'])
def compare_artists():
    artist1_name = request.form.get('artist1')
    artist2_name = request.form.get('artist2')
    token = functions.get_token()
    # Call the function to get artist data
    artist1_data = functions.get_artist_data(artist1_name, token)
    artist2_data = functions.get_artist_data(artist2_name, token)
    return render_template('compare.html', artist1 = artist1_data, artist2 = artist2_data)

if __name__ == "__main__":
    app.run(debug=True)