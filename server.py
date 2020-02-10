from flask import Flask, render_template
# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
app = Flask(__name__)
@app.route('/')
def index():
    mysql = connectToMySQL("busdb")
    busdb = mysql.query_db("SELECT * FROM busdb")
    print(busdb)
    return render_template("index.html", busdb=busdb)


if __name__ == "__main__":
    app.run(debug=True)
