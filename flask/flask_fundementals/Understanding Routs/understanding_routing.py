from flask import Flask
app = Flask(__name__)

#Create a root route ("/") that responds with "Hello World!"
@app.route('/')
def hello():
    return 'Hello_world'

#Create a route that responds with "Dojo!"
@app.route('/dojo')
def Dojo():
    return 'Dojo!'
#Create a route that responds with "Hi" and whatever name is in the URL after /say/
@app.route("/say/<name>")
def say(name):
    return "Hi {}".format(name)

#Create a route that responds with the given word repeated as many times as specified in the URL
@app.route("/repeat/<num>/<word>")
def repeating(num,word):
    return f"{word} "*int(num)
    
#NINJA Bonus
@app.route("/repeat/<int:num>/<word>")
def repeated(num,word):
    return f"{word} "*num   

#SENSEI BONUS
@app.route("/<anyword>")
def sorry(anyword):
    return "Sorry no response. Try Again!"



if __name__=="__main__": 
    app.run(debug=True) 