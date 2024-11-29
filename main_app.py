from flask import Flask,render_template


app = Flask(__name__)
@app.route('/')
def main():
    return render_template("HomeTemplate.html")
@app.route('/PinballGame')
def PinballGame():
    return render_template("PinballGame.html")
@app.route('/PlaneWarsGame')
def FlyGame():
    return render_template("PlaneWarsGame.html")

if __name__ == '__main__':
    app.run(port = 8080, debug = True)