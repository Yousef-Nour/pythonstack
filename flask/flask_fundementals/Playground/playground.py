from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play/')
def play():
    return render_template("index.html")

@app.route('/play/<num>/')
def repeating(num):
    print(num)
    return render_template("index.html",repeating=int(num))

@app.route('/play/<num>/<color>')
def color(num,color):
    return render_template("index.html", repeating=int(num),backgroundColor= color)




if __name__=="__main__":
    app.run(debug=True)