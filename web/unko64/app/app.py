from flask import Flask, render_template, request, redirect, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/finder/")
def finder():
    filename = request.args.get('filename')

    if filename == None:
        print("a")
        return redirect(url_for("main"))

    if filename == "flag":
        return "flag not found. can't you find it?LOL"
    try:
        f = open(filename,encoding='utf-8')
    except Exception as e:
        return "ERROR!..maybe file could not found.."

    data = f.readline()
    return f"{data}"


@app.errorhandler(404)
def error_404(error):
    return '''
        <h1>404</h1>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0")
