from flask import Flask, Response, render_template, request
import json
from wtforms import TextField, Form

app = Flask(__name__)

class SearchForm(Form):
    autocomp = TextField('Insert City', id='city_autocomplete')


@app.route('/_autocomplete', methods=['GET'])
def autocomplete():
    cities = ["Olongapo City",
          "Angeles City",
          "Manila",
          "Makati",
          "Pasig",
          "Davao",
          "Cebu",
          "Quezon City",
          "Taguig"]
    print(cities)    
    return Response(json.dumps(cities), mimetype='application/json')



def getUserInput():
    """
    1. Get City User Input when he submits (see "Confirm" in search.html)
    2. Store in "city" variable

    Not mandatory to have a function like this, it's just illustrative.
    Point is just to get user input stored in a python variable so that I can reuse it after in the code as a string
    """

    # city = variable
    # print(city)
    pass 


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm(request.form)

    return render_template("search.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)
