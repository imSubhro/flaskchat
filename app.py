from flask import Flask

app = Flask(__name__)

# @app.route('/<stream>/<section>/<year>/chat')
# def home(stream, section, year):
#     return f"Yooo!you are from {stream} {section} {year} " 

chat =[]
@app.route('/')
def homepage():
    return "Let's Go!"


@app.route('/chat/<name>/<msg>')
def home(name,msg):
    mylist= name,msg
    print(mylist)
    mylist ={"username":name,"message":msg}
    chat.append(mylist)
    return "saved"


@app.route('/view')
def view_chat():
    return {"chat_history":chat}


app.run(debug=True)
