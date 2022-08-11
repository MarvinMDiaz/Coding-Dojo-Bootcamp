from flask_app import app
from flask_app.controller import dojo_survey_controller
app.secret_key = 'secret'

if __name__ == "__main__":
    app.run(debug=True)