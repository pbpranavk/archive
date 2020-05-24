from flask import  Flask
app = Flask(__name__)

@app.route('/')
def hello_from_heroku():
	return "Hello from Heroku"

if __name__ == '__main__':
	app.run()
