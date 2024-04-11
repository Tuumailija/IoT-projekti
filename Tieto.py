from flask import Flask, jsonify, render_template
import requests
import json

app = Flask(__name__)

API_KEY = 'Z9HL1JG0Y6TPT1BI'
CHANNEL_ID = '2504141'

@app.route('/')
def get_data_from_thingspeak():
    try:
        response = requests.get(f'https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.json?api_key={API_KEY}&results=1')
        data = response.json()

        latest_entry = data['feeds'][0]

        formatted_data = {
            'Sisalampotila': latest_entry.get('field1'),
            'Ulkolampotila': latest_entry.get('field2'),
            'Ilmankosteus sisalla': latest_entry.get('field3'),
            'Ilmankosteus ulkona': latest_entry.get('field4'),
        }

        return jsonify(formatted_data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)