import cloudpickle
from flask import Flask, render_template, request

with open('model.pkl', 'rb') as file_in:
  model = cloudpickle.load(file_in)

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', nome='Análise de RH')

@app.route('/predicao', methods=['POST'])
def predicao():
  age= request.form['age']
  length_of_service = request.form['length_of_service']
  awards_won = request.form['awards_won']
  avg_training_score = request.form['avg_training_score']
  department = request.form['department']
  region = request.form['region']
  previous_year_rating = request.form['previous_year_rating']
  education = request.form['education']

  array=[[str(age), str(length_of_service), str(awards_won), str(avg_training_score), str(department), str(region), str(previous_year_rating), str(education)]]

  predicao = model.predict(array)

  return render_template('resposta.html', predicao=predicao[0])

app.run(debug=True)

# pip install -r requirements.txt (instala as bibliotecas)
# python app.py (para executar)
