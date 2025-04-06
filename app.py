from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        batting_team = request.form['batting_team']
        bowling_team = request.form['bowling_team']
        city = request.form['city']
        current_score = request.form['current_score']
        overs = request.form['overs']
        wickets = request.form['wickets']
        last_five = request.form['last_five']
        # Process the data here
        return f"Received data: {batting_team}, {bowling_team}, {city}, {current_score}, {overs}, {wickets}, {last_five}"
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
