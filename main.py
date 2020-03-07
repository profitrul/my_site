from flask import Flask , render_template,url_for,redirect
app = Flask(__name__)

@app.route("/")
@app.route("/<text>")
def hello_world(text = None):
    if text == None:

        return render_template('index.html',name = 'world')
    else:
        # text = text.split(',')
        # return render_template('index.html', name=text)
        return redirect(url_for('hello_world'))



if __name__ == '__main__':
    app.run()