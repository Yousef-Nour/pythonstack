from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return render_template ('index.html')  # Return the string 'Hello World!' as a response
# import statements, maybe some other routes
    
# @app.route('/yousef')
# def success():
#     return "success" 

# @app.route('/amer')
# def amer():
#     return "success" 

@app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    return render_template ('index.html',name ="Yousef")

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)