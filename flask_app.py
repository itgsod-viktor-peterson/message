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
    if request.method == "GET":
        return "Try to make a post instead"
    try:
        message = request.form['message']
        name = request.form.get("name", "dude")

        enail = request.form.get("email", "None")



    except:
        return abort(400)

    if name == "jobs":
        return abort(501)
    elif name == "bill":
        return abort(403)
    messages.insert(0, Message(name,enail,message))
    return redirect('/')


#error pages

@app.errorhandler(404)
def page_not_found(e):
    return "Halla sidan funkar ej bosse"




@app.errorhandler(501)
def all_is_steves_fault(e):
    return "blame steve"

@app.errorhandler(403)
def bill_is_not_welcome(e):
    return "sorry bill try another operating system"


@app.errorhandler(405)
def method_not_allowed(e):
    return render_template("405.html"), 405




if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
