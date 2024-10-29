from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)  

@app.route('/')
def hello():
    return '''
    <p>Hello, World!</p>
    <p>Rayan Hamid : LOL</p>
    '''

# New route using template
@app.route('/rayan')
def show_acronym():
    return render_template('my_template.html')

if __name__ == '__main__':
    app.run(debug=True)
