from flask import Flask

app=Flask(__name__)

@app.route("/")
def start():
    return "<h1>Welcome Have to finitsh...</h1>"

if __name__=='__main__':
    app.run(debug=True)