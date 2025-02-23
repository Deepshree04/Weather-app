from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        api_key = '074ec2fa8c5804e567e76ecc57090115'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        weather_data = response.json()

        if weather_data.get('cod') != 200:
            message = weather_data.get('message', 'City not found')
            return render_template('index.html', message=message)

        weather = {
            'city': city,
            'temperature': weather_data['main']['temp'],
            'description': weather_data['weather'][0]['description'],
            'icon': weather_data['weather'][0]['icon']
        }
        return render_template('index.html', weather=weather)

    return render_template('index.html')

if __name__ == '_main_':
    app.run(debug=True)