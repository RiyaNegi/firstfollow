from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/homepage")
def index():
    pass

@app.route("/",methods = ['POST','GET'])
def savekeywords():
    msg = ""
    # global product_keys
    if request.method == 'POST':
        user = request.form['user']
        keywords = request.form['keywords']
        # product_keys = p_k
        msg = "data added"
        return redirect('/homepage')
        
    # print()
    return render_template("result.html",msg = msg)

if __name__ == "__main__":
    app.run()