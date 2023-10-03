from flask import Flask,render_template,request
import pickle
import pandas as pd

app = Flask(__name__)

@app.route('/')
def entered():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def process_form():
    cab_type = request.form['cab_type']
    destination = request.form['destination']
    type = request.form['type']
    source = request.form['source']
    
    sources = ['Financial District', 'Theatre District', 'Back Bay', 'Boston University', 'North End', 'Fenway', 'Northeastern University', 'South Station', 'Haymarket Square', 'West End', 'Beacon Hill', 'North Station']
    destinations = ['Financial District', 'Theatre District', 'Back Bay', 'Boston University', 'North End', 'Fenway', 'Northeastern University', 'South Station', 'Haymarket Square', 'West End', 'Beacon Hill', 'North Station']
    types = ['UberXL', 'WAV', 'Black SUV', 'Black', 'Taxi', 'UberX', 'UberPool', 'Lux', 'Lyft', 'Lux Black XL', 'Lyft XL', 'Lux Black', 'Shared']

    cab_type = 0 if cab_type == 'Uber' else 1
    type_idx = types.index(type) + 1
    source_idx = sources.index(source) + 1
    destination_idx = destinations.index(destination) + 1

    data = {
        'name': [type_idx],
        'cab_type': [cab_type],
        'destination': [destination_idx],
        'source_x': [source_idx]
    }

    df = pd.DataFrame(data)
    model = pickle.load(open('finalized_model.sav', 'rb'))
    predicted_price = model.predict(df)

    return render_template('succesfull.html', price=predicted_price[0])
if __name__ == '__main__':
    app.run(debug=True)