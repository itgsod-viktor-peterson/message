from flask import Flask, render_template, request, redirect, abort


app = Flask(__name__)

messages=[]


class Message(object):
    def __init__(self, name,email,message):
        self.name = name
        self.email= email
        self.message = message


@app.route('/')
def welcome():


    return render_template('index.html',title="hackerspace",messages=messages[:100])


@app.route("/message", methods=['POST'])
def message():


    try:
        message = request.form['message']
        name = request.form.get("name", "dude")
        enail = request.form.get("email", "None")

        messages.insert(0, Message(name,enail,message))

    except:
        return abort(400)

    return redirect('/')








if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
