from flask import Flask

# create and configure the app
app = Flask(__name__, instance_relative_config=True) 
app.app_context().push()

if __name__ == "__main__":
    app.run(debug=True)
