from flask_app import app
app.secret_key = 'secret'
from flask_app.controller import users_controller





if __name__ == "__main__":
    app.run(debug=True)