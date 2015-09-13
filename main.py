from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('photovibrant/home.html')

@app.route('/portfolio')
def portfolio():
    return render_template('photovibrant/portfolio.html')

@app.route('/resume')
def resume():
    return render_template('photovibrant/resume.html')



if __name__ == '__main__':
    app.run()
