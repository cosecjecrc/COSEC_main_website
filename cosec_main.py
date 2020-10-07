from flask import Flask, render_template, url_for, request,redirect

app = Flask(__name__)

@app.route('/home' , methods=[ 'GET' , 'POST' ])
def index():
    return render_template('index.html')

@app.route('/home/Memo', methods=['GET','POST'] )
def MEMO():
    return render_template('MEMOIR.html')

@app.route('/home/Memo/act' , methods=['GET','POST'] )
def act():
    return render_template('google_act.html')

@app.route('/home/Memo/ind2018' , methods=['GET','POST'] )
def IND():
    return render_template('ind_2018.html')

@app.route('/home/Memo/cyber' , methods=['GET','POST'] )
def cyber():
    return render_template('cyber.html')

@app.route('/home/team', methods=['GET'])
def team():
     return render_template('team.html')

@app.route('/home/hof')
def hof():
     return render_template('HOF.html')



if __name__ == "__main__":
    app.run(debug=True)
