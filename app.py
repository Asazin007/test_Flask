from flask import Flask, render_template, request,redirect,url_for,jsonify

##simple flask application
app = Flask(__name__)

@app.route('/')
def welcome():
    return "<h1>Welcome to page</h1>"

@app.route('/index',methods=['GET'])
def index():
    return "This is index page"
#variable rule
@app.route('/success/<score>')
def success(score):
    return f'the person has passed and score is: {score}'
@app.route('/fail/<score>')
def fail(score):
    return f'the person has failed and score is: {score}'

@app.route('/form',methods=["GET","POST"])
def form():
    if request.method=="GET":
        return render_template('form.html')
    else:
        maths= float(request.form['maths'])
        science= float(request.form['science'])
        history= float(request.form['history'])

        average_mrks= (maths+science+history)/3
        score = average_mrks
        res=""
        if(average_mrks>=50):
            res="success"
        else:
            res="fail"
        # render_template('form.html',score=average_mrks)   
        return redirect(url_for(res,score=score))
        # return render_template('form.html',score=average_mrks)
@app.route('/api',methods=["POST"])
def calculate_sum():
    data=request.get_json()   
    a_val= float(dict(data)['a'])
    b_val= float(dict(data)['b'])
    return jsonify(a_val+b_val)
    
    
if __name__== "__main__":
    app.run(debug=True) 