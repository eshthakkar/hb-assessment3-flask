from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

@app.route("/")
def index_page():
  """Show an index page."""

  return render_template("index.html")


@app.route("/application-form")
def show_app_form():
  """Show the application form page."""

  return render_template("application-form.html")
  

@app.route("/application",methods=["POST"])
def show_app_response():
  """Show the application response page."""

  first_name = request.form.get("firstname")
  last_name = request.form.get("lastname")
  salary = request.form.get("salary")
  jobtitle = request.form.get("jobtitle")


  return render_template("application-response.html",
                        first_name=first_name,
                        last_name=last_name,
                        salary=salary,
                        jobtitle=jobtitle)  


if __name__ == "__main__":
  # We have to set debug=True here, since it has to be True at the
  # point that we invoke the DebugToolbarExtension
  app.debug = True

  # Use the DebugToolbar
  DebugToolbarExtension(app)

  app.run(host="0.0.0.0")

