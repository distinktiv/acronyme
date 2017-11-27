from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	#return "Hello World"
	#render template
	return render_template("hello Seubayne!!!!!!")

@app.route('/acronym')
def acronym():
	#traitement	
	return dict()

if __name__ == "__main__":
	app.run(debug=True)
