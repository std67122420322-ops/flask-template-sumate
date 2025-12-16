from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  title = 'Home Page'
  return render_template('index.html', title=title)

@app.route('/about')
def about():
  title = 'About Page'
  neme = 'Sumate'
  email = 'std.67122420322@ubru.ac.th'
  mobile = '0933825645'
  age = 20
  return render_template('about.html', title=title, neme=neme, email=email, mobile=mobile, age=age)

@app.route('/food')
def food():
  title = 'Favorite Food Page'
  Foods = ['หมูกระทะ', 'ชาบู', 'ไก่ต้ม', 'ก๋วยเตี๋ยวเรือ']
  return render_template('food.html', title=title, Foods=Foods)

@app.route('/sport')
def sport():
  title = 'Favorite Sport Page'
  sport = ['ฟุตบอล', 'บาสเกตบอล', 'ฟุตซอล', 'ปั่นจักรยาน']
  return render_template('sport.html', title=title, sport=sport)