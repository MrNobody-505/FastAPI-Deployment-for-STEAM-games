from fastapi import FastAPI

app = FastAPI()

#http://127.0.0.1:8000

@app.get("/")

def index():
    return "esto es la prueba # 1"

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    options = ['Action', 'Casual', 'Indie', 'Simulation', 'Strategy',
       'Free to Play', 'RPG', 'Sports', 'Adventure', 'Racing',
       'Early Access', 'Massively Multiplayer',
       'Animation &amp; Modeling', 'Web Publishing', 'Education',
       'Software Training', 'Utilities', 'Design &amp; Illustration',
       'Audio Production', 'Video Production', 'Photo Editing']  # Generate a list of 21 options
    return render_template('index.html', options=options)

if __name__ == '__main__':
    app.run(debug=True)