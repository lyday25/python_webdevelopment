from flask import Flask
app = Flask(__name__)
@app.route("/")
def homepage():
    return "Welcome to our Institute"

@app.route("/about")
def about():
    return "Welcome to aboutUs Page"


@app.route("/services")
def services():
    return "These are the services offered"

@app.route("/calcpage")
def calcpage():
    a=3
    b=5
    c=10
    x=a+b+c

    return "This is the result: " + str(x)

@app.route("/multidiv")
def multidiv():
    a=14
    b=10
    c=20
    y=(a*b)/c
    
    return "Hurray, you are correct, the result is: " +str(y)



if __name__ == '__main__':
   app.run(host='127.0.0.1', port=5000, debug =True)
   