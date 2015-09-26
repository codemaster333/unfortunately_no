from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('message.html')

@app.route('/signup', methods = ['POST'])
def signup():
    relationship = request.form['Relationship']
    family = request.form['Family']
    work = request.form['Work']
    print(relationship, family, work)
    return relationship, family, work


if __name__ == '__main__':
    app.run()

