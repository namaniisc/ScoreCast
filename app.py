from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load the model
pipe = pickle.load(open('pipe.pkl', 'rb'))

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    if request.method == 'POST':
        batting_team = request.form['batting_team']
        bowling_team = request.form['bowling_team']
        city = request.form['city']
        current_score = int(request.form['current_score'])
        overs = float(request.form['overs'])
        wickets = int(request.form['wickets'])
        last_five = int(request.form['last_five'])

        balls_left = 120 - (overs * 6)
        wickets_left = 10 - wickets
        crr = current_score / overs

        input_df = pd.DataFrame(
            {'batting_team': [batting_team], 'bowling_team': [bowling_team], 'city': [city], 
            'current_score': [current_score], 'balls_left': [balls_left], 
            'wicket_left': [wickets_left], 'current_run_rate': [crr], 'last_five': [last_five]}
        )

        result = pipe.predict(input_df)
        prediction = int(result[0])

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
