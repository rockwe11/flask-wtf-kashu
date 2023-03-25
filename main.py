import os

from flask import Flask, render_template, url_for, redirect, request
from werkzeug.utils import secure_filename

from forms.load_img import LoadIMGForm
from forms.login import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html', title='Заготовка')


@app.route('/training/<prof>')
def training(prof):
    return render_template("training.html", prof=prof)


@app.route("/list_prof/<list>")
def list_prof(list):
    profs = ["инженер-исследователь", "пилот", "строитель", "экзобиолог", "врач", "инженер по терраформированию",
             "климатолог", "специалист по радиационной защите", "астрогеолог", "гляциолог", "инженер жизнеобеспечения",
             "метеоролог", "оператор марсохода", "киберинженер", "штурман", "пилот дронов"]
    return render_template("list_prof.html", type=list, list=profs)


@app.route("/answer")
@app.route("/auto_answer")
def auto_answer():
    info = {
        "title": "Анкета",
        "surname": "Watny",
        "name": "Mark",
        "education": "выше среднего",
        "profession": "штурман марсохода",
        "sex": "male",
        "motivation": "Всегда мечтал застрять на Марсе!",
        "ready": True
    }
    return render_template("auto_answer.html", title=info["title"], info=info)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


@app.route("/distribution")
def distribution():
    info = [
        "Ридли Скотт",
        "Энди Уир",
        "Марк Уотни",
        "Венката Капур",
        "Тедди Сандерс",
        "Шон Бин"
    ]
    return render_template("distribution.html", info=info)


@app.route("/table/<sex>/<int:age>")
def table(sex, age):
    return render_template("table.html", sex=sex, age=age)


@app.route("/galery", methods=['POST', 'GET'])
def galery():
    form = LoadIMGForm()
    if form.validate_on_submit():
        f = form.file.data
        filename = secure_filename(f.filename)
        f.save(os.path.join(
            os.getcwd(), 'static/img/galery', filename
        ))
        # f.save("/static/img/galery/\"" + f.filename + '\"')
        # print(f)
        # with open("/static/img/galery/" + f.name) as file:
        #     file.write(f.read())
        return redirect("/galery")
    hists = os.listdir('static/img/galery')
    hists = ['img/galery/' + file for file in hists]
    print(hists)
    return render_template("galery.html", title="Красная планета", hists=hists, form=form)


if __name__ == '__main__':
    app.run(port=8091, host='127.0.0.1')
