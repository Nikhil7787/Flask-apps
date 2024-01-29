from flask import Flask, render_template, request, url_for
import json
import urllib.request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def weather():
    if request.method == 'POST':
        city = request.form['city']
    else:
        # For default city name Pune
        city = 'Pune'

    # Your API key here
    api = '8e16ac60dbeb8bb10fb043f750ccfda5'

    try:
        # Source contains JSON data from API
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + api).read()

        # Converting JSON data to a dictionary
        list_of_data = json.loads(source)

        # Data for the variable list_of_data
        data = {
            "country_code": str(list_of_data['sys']['country']),
            "city_name": str(list_of_data['name']),
            "coordinate": str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + 'K',
            "temp_cel": str(round(list_of_data['main']['temp'] - 273.15, 2)) + '°C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
        }

        print(data)
        return render_template('index.html', data=data)

    except Exception as e:
        # Handle exceptions, for example, if the city is not found
        error_message = f"Error: {str(e)}"
        return render_template('index.html', error=error_message)

if __name__ == '__main__':
    app.run(debug=True)