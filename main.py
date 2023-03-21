from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html', title='Заготовка')


@app.route('/training/<prof>')
def training(prof):
    return render_template("training.html", prof=prof)
    # return render_template("training.html", training="Инженерные тренажеры", img=url_for('static', filename='img/mars.png'))
    # if "инженер" in prof or "строитель" in prof:
    #     return render_template("training.html", training="Инженерные тренажеры", img=url_for('static', filename='img/mars.png'))
    # else:
    #     return render_template("training.html", training="Научные симуляторы", img=url_for('static', filename='img/science.png'))


if __name__ == '__main__':
    app.run(port=8091, host='127.0.0.1')
