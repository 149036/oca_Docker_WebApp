from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_, or_
import os

db_uri = None
if os.getenv('DEBUG') == '0':
    from mysql_model import Human
    db_uri = os.getenv('DATABASE_URI_MYSQL')
    
elif os.getenv('DEBUG') == '1':
    from test_model import Human
    db_uri = os.getenv('DATABASE_URI_SQLITE')
   

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
app.config["PORT"] = os.getenv('PORT')

db = SQLAlchemy(app)


@app.route("/")
def inex():
    return "Response Data"


@app.route("/another")
def another():
    return "Another Response"


@app.route("/test_request")
def test_request():
    return f'test_request:{request.args.get("dummy")}'


@app.route("/exercise_request/<a>")
def exercise_request(a):
    return f"{a}"


@app.route("/show_html")
def show_html():
    return render_template("test_html.html")


@app.route("/excersize")
def excersize():
    return render_template("exercise.html")


@app.route("/exercise")
def exercise():
    return render_template("answer.html", name=request.args.get("my_name"))


@app.route("/try_rest", methods=["POST"])
def try_test():
    request_json = request.get_json()
    print(request_json)
    print(type(request_json))
    name = request_json["name"]
    print(name)
    response_json = {"response_json": request_json}

    for i in response_json["response_json"]["friends"]:
        print(i)

    return jsonify(response_json)


@app.route("/person_search")
def person_search():
    return render_template("./person_search.html")


@app.route("/person_result")
def person_result():
    search_weight = request.args.get("search_weight")
    search_height = request.args.get("search_height")
    over_under1 = request.args.get("over_under1")
    over_under2 = request.args.get("over_under2")
    andalso = request.args.get("andalso")

    andor = {
        "and": lambda a, b: and_(a, b),
        "or": lambda a, b: or_(a, b),
    }
    o_u = {
        "<=": lambda a, b: a <= b,
        ">=": lambda a, b: a >= b,
    }

    filter = andor[andalso](
        o_u[over_under1](Human.weight, search_weight),
        o_u[over_under2](Human.height, search_height),
    )

    persons = db.session.query(Human).filter((filter))

    return render_template(
        "./person_result.html",
        persons=persons,
        search_weight=search_weight,
        search_height=search_height,
        andalso=andalso,
    )


@app.route("/try_html")
def try_html():
    return render_template("./try_html.html")


@app.route("/show_data", methods=["GET", "POST"])
def show_data():
    print(request.form["submit"])
    return render_template("./try_html.html")
