from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html", num1=8, num2=8, color1="white", color2="black")

@app.route('/<int:num1>/<int:num2>')
def numbers(num1, num2):
    return render_template("index.html", num1=num1, num2=num2,color1="white", color2="black")

@app.route('/<int:num1>/<int:num2>/<color1>/<color2>/')
def colors(num1,num2,color1,color2):
    return render_template("index.html", num1=num1, num2=num2, color1=color1, color2= color2)







if __name__ == "__main__":
    app.run(debug=True)