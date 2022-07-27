# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from model import budget_calc
from model import images_calc
# -- Initialization section --
app = Flask(__name__)

# -- Routes section --
@app.route('/')
@app.route('/home')
def home():
  return render_template("home.html")

@app.route('/map')
def map():
  return render_template("map.html")
  
@app.route('/ourmission')
def ourmission():
  return render_template("ourmission.html")

# @app.route('/birthstone',methods=['GET','POST'])
# def birthstone():
#   if request.method == 'POST':
#     user_info = request.form
#     print(user_info)
#     birth_message = calc_birthstone((user_info))

@app.route('/recipes',methods=['GET','POST'])
def recipes():
  if request.method == "POST":
    user_info = request.form
    print(int(user_info["budget"]))
    answer = budget_calc(int(user_info["budget"]))
    images = images_calc()
    print(answer)
    return render_template('results.html',answer=answer, images=images)
  else:
    return render_template('recipes.html')

#propose something within user budget and preferences
  #use household income as a filter 
  #number of people in the household 
  # ask how many people are in their household
  #units of food multiplied by how many people there are
  #give them a general idea for budget

app.run(host='0.0.0.0', port=81, debug=True)