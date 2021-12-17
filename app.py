from flack import Flask
app = Flask(_name_)

@app.route('/')
def hello_world():
    return 'Helo World! (from a docker container)'
if _name_ == '_main_':
    app.run(debug = True, host = '0.0.0.0')
