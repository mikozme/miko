from flask import Flask, render_template, request, redirect, url_for
from data import db_session
from data.nuts import Nut
from forms.users import RegisterForm, LoginForm
from data.users import User
from flask_login import login_user
import os

app = Flask('testapp')

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

counter = 0
total = {
    "Арахис": 0,
    "Бразильский": 0,
    "Грецкий": 0,
    "Кешью": 0,
    "Миндаль": 0,
    "Фисташки": 0,
    "Фундук": 0,
    "Пекан": 0,
    "Вишня": 0,
    "Изюм": 0,
    "Инжир": 0,
    "Курага": 0,
    "Финик": 0,
    "Чернослив": 0,
    "Цукаты": 0,
    "Папайя": 0,
}

def all_info():
    data0 = nut_info('Арахис')
    data1 = nut_info('Грецкий')
    data2 = nut_info('Кешью')
    data3 = nut_info('Миндаль')
    data4 = nut_info('Бразильский')
    data5 = nut_info('Фисташки')
    data6 = nut_info('Фундук')
    data7 = nut_info('Пекан')
    data8 = nut_info('Вишня')
    data9 = nut_info('Изюм')
    data10 = nut_info('Инжир')
    data11 = nut_info('Курага')
    data12 = nut_info('Финик')
    data13 = nut_info('Чернослив')
    data14 = nut_info('Цукаты')
    data15 = nut_info('Папайя')
    return data0, data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data1, data11, data12, data13,\
        data14, data15,


def nut_info(name):
    db_sess = db_session.create_session()
    conected = db_sess.query(Nut).filter(Nut.name == str(name)).first()
    price = conected.price
    mass = conected.mass
    sale = conected.discount_perc
    price_w_sale = round(price / 100 * (100 - sale) - 0.01, 2)
    return price, mass, sale, price_w_sale


@app.route("/", methods=['GET', 'POST'])
def start():
    global counter
    res = all_info()
    return render_template("main.html",
                           arah_mass=res[0][1], arah_salep=res[0][3], arah_price=res[0][0], arah_sale=res[0][2],
                           grez_mass=res[1][1], grez_salep=res[1][3], grez_price=res[1][0], grez_sale=res[1][2],
                           kesh_mass=res[2][1], kesh_salep=res[2][3], kesh_price=res[2][0], kesh_sale=res[2][2],
                           mind_mass=res[3][1], mind_salep=res[3][3], mind_price=res[3][0], mind_sale=res[3][2],
                           braz_mass=res[4][1], braz_salep=res[4][3], braz_price=res[4][0], braz_sale=res[4][2],
                           fist_mass=res[5][1], fist_salep=res[5][3], fist_price=res[5][0], fist_sale=res[5][2],
                           fund_mass=res[6][1], fund_salep=res[6][3], fund_price=res[6][0], fund_sale=res[6][2],
                           peka_mass=res[7][1], peka_salep=res[7][3], peka_price=res[7][0], peka_sale=res[7][2],
                           vish_mass=res[8][1], vish_salep=res[8][3], vish_price=res[8][0], vish_sale=res[8][2],
                           izum_mass=res[9][1], izum_salep=res[9][3], izum_price=res[9][0], izum_sale=res[9][2],
                           inzh_mass=res[10][1], inzh_salep=res[10][3], inzh_price=res[10][0], inzh_sale=res[10][2],
                           kura_mass=res[11][1], kura_salep=res[11][3], kura_price=res[11][0], kura_sale=res[11][2],
                           fini_mass=res[12][1], fini_salep=res[12][3], fini_price=res[12][0], fini_sale=res[12][2],
                           cher_mass=res[13][1], cher_salep=res[13][3], cher_price=res[13][0], cher_sale=res[13][2],
                           cuka_mass=res[14][1], cuka_salep=res[14][3], cuka_price=res[14][0], cuka_sale=res[14][2],
                           papa_mass=res[15][1], papa_salep=res[15][3], papa_price=res[15][0], papa_sale=res[15][2],
                           counter=counter)


@app.route("/Orexoff/araxis", methods=['GET', 'POST'])
def arahis():
    global counter
    data = nut_info('Арахис')
    price, mass, sale = data[3], data[1], data[2]
    if request.method == 'POST':
        amount = request.form.get('amount')
        total["Арахис"] += int(amount)
        counter += int(amount)
        return redirect('/')
    return render_template("araxis.html", massa=f"{str(mass)}", price=f"{str(price)}")


@app.route("/Orexof/gretz", methods=['GET', 'POST'])
def gretzki():
    global counter
    data = nut_info('Грецкий')
    price, mass, sale = data[3], data[1], data[2]
    if request.method == 'POST':
        amount = request.form.get('amount')
        total["Грецкий"] += int(amount)
        counter += int(amount)
        return redirect('/')
    return render_template("gretsky.html", massa=f"{str(mass)}", price=f"{str(price)}")


@app.route("/Orexof/keshy", methods=['GET', 'POST'])
def keshy():
    global counter
    data = nut_info('Кешью')
    price, mass, sale = data[3], data[1], data[2]
    if request.method == 'POST':
        amount = request.form.get('amount')
        total["Кешью"] += int(amount)
        counter += int(amount)
        return redirect('/')
    return render_template("keshiy.html", massa=f"{str(mass)}", price=f"{str(price)}")


@app.route("/Orexof/mindal", methods=['GET', 'POST'])
def mindal():
    global counter
    data = nut_info('Миндаль')
    price, mass, sale = data[3], data[1], data[2]
    if request.method == 'POST':
        amount = request.form.get('amount')
        total["Миндаль"] += int(amount)
        counter += int(amount)
        return redirect('/')
    return render_template("mindal.html", massa=f"{str(mass)}", price=f"{str(price)}")


@app.route("/Orexof/brazil", methods=['GET', 'POST'])
def brasilski():
    global counter
    data = nut_info('Бразильский')
    price, mass, sale = data[3], data[1], data[2]
    if request.method == 'POST':
        amount = request.form.get('amount')
        total["Бразильский"] += int(amount)
        counter += int(amount)
        return redirect('/')
    return render_template("brasilski.html", massa=f"{str(mass)}", price=f"{str(price)}")


@app.route("/Orexof/fist", methods=['GET', 'POST'])
def fistash():
    global counter
    data = nut_info('Фисташки')
    price, mass, sale = data[3], data[1], data[2]
    if request.method == 'POST':
        amount = request.form.get('amount')
        total["Фисташки"] += int(amount)
        counter += int(amount)
        return redirect('/')
    return render_template("fistashki.html", massa=f"{str(mass)}", price=f"{str(price)}")


@app.route("/Orexof/fund", methods=['GET', 'POST'])
def funduk():
    global counter
    data = nut_info('Фундук')
    price, mass, sale = data[3], data[1], data[2]
    if request.method == 'POST':
        amount = request.form.get('amount')
        total["Фундук"] += int(amount)
        counter += int(amount)
        return redirect('/')
    return render_template("funduk.html", massa=f"{str(mass)}", price=f"{str(price)}")


@app.route("/Orexof/pekan", methods=['GET', 'POST'])
def pekan():
    global counter
    data = nut_info('Пекан')
    price, mass, sale = data[3], data[1], data[2]
    if request.method == 'POST':
        amount = request.form.get('amount')
        total["Пекан"] += int(amount)
        counter += int(amount)
        return redirect('/')
    return render_template("pekan.html", massa=f"{str(mass)}", price=f"{str(price)}")


@app.route("/Orexof/vishnia", methods=['GET', 'POST'])
def vishnia():
    global counter
    data = nut_info('Вишня')
    price, mass, sale = data[3], data[1], data[2]
    if request.method == 'POST':
        amount = request.form.get('amount')
        total["Вишня"] += int(amount)
        counter += int(amount)
        return redirect('/')
    return render_template("vishnya.html", massa=f"{str(mass)}", price=f"{str(price)}")


@app.route("/Orexof/izum", methods=['GET', 'POST'])
def izum():
    global counter
    data = nut_info('Изюм')
    price, mass, sale = data[3], data[1], data[2]
    if request.method == 'POST':
        amount = request.form.get('amount')
        total["Изюм"] += int(amount)
        counter += int(amount)
        return redirect('/')
    return render_template("izym.html", massa=f"{str(mass)}", price=f"{str(price)}")


@app.route("/Orexof/inzhir", methods=['GET', 'POST'])
def inzhir():
    global counter
    data = nut_info('Инжир')
    price, mass, sale = data[3], data[1], data[2]
    if request.method == 'POST':
        amount = request.form.get('amount')
        total["Инжир"] += int(amount)
        counter += int(amount)
        return redirect('/')
    return render_template("inzhir.html", massa=f"{str(mass)}", price=f"{str(price)}")


@app.route("/Orexof/kuraga", methods=['GET', 'POST'])
def kuraga():
    global counter
    data = nut_info('Курага')
    price, mass, sale = data[3], data[1], data[2]
    if request.method == 'POST':
        amount = request.form.get('amount')
        total["Курага"] += int(amount)
        counter += int(amount)
        return redirect('/')
    return render_template("kuraga.html", massa=f"{str(mass)}", price=f"{str(price)}")


@app.route("/Orexof/finik", methods=['GET', 'POST'])
def finik():
    global counter
    data = nut_info('Финик')
    price, mass, sale = data[3], data[1], data[2]
    if request.method == 'POST':
        amount = request.form.get('amount')
        total["Финик"] += int(amount)
        counter += int(amount)
        return redirect('/')
    return render_template("finik.html", massa=f"{str(mass)}", price=f"{str(price)}")


@app.route("/Orexof/chernosliv", methods=['GET', 'POST'])
def cherno():
    global counter
    data = nut_info('Чернослив')
    price, mass, sale = data[3], data[1], data[2]
    if request.method == 'POST':
        amount = request.form.get('amount')
        total["Чернослив"] += int(amount)
        counter += int(amount)
        return redirect('/')
    return render_template("chernosliv.html", massa=f"{str(mass)}", price=f"{str(price)}")


@app.route("/Orexof/cukati", methods=['GET', 'POST'])
def cukati():
    global counter
    data = nut_info('Цукаты')
    price, mass, sale = data[3], data[1], data[2]
    if request.method == 'POST':
        amount = request.form.get('amount')
        total["Цукаты"] += int(amount)
        counter += int(amount)
        return redirect('/')
    return render_template("cukati.html", massa=f"{str(mass)}", price=f"{str(price)}")


@app.route("/Orexof/papya", methods=['GET', 'POST'])
def papya():
    global counter
    data = nut_info('Папайя')
    price, mass, sale = data[3], data[1], data[2]
    if request.method == 'POST':
        amount = request.form.get('amount')
        total["Папайя"] += int(amount)
        counter += int(amount)
        return redirect('/')
    return render_template("papya.html", massa=f"{str(mass)}", price=f"{str(price)}")


@app.route("/Orexof/korzina")
def korzina():
    global counter, total
    data0 = nut_info('Арахис')
    data1 = nut_info('Грецкий')
    data2 = nut_info('Кешью')
    data3 = nut_info('Миндаль')
    data4 = nut_info('Бразильский')
    data5 = nut_info('Фисташки')
    data6 = nut_info('Фундук')
    data7 = nut_info('Пекан')
    data8 = nut_info('Вишня')
    data9 = nut_info('Изюм')
    data10 = nut_info('Инжир')
    data11 = nut_info('Курага')
    data12 = nut_info('Финик')
    data13 = nut_info('Чернослив')
    data14 = nut_info('Цукаты')
    data15 = nut_info('Папайя')
    totals = data0[0]*total['Арахис'] + data1[0]*total['Грецкий'] + data2[0]*total['Кешью'] + data3[0]*total['Миндаль']\
             + data4[0]*total['Бразильский'] + data5[0]*total['Фисташки'] + data6[0]*total['Фундук']\
             + data7[0]*total['Пекан'] + data8[0]*total['Вишня'] + data9[0]*total['Изюм'] + data10[0]*total['Инжир']\
             + data11[0]*total['Курага'] + data12[0]*total['Финик'] + data13[0]*total['Чернослив']\
             + data14[0]*total['Цукаты'] + data15[0]*total['Папайя']
    total_ws = data0[3]*total['Арахис'] + data1[3]*total['Грецкий'] + data2[3]*total['Кешью'] + data3[3]*total['Миндаль']\
             + data4[3]*total['Бразильский'] + data5[3]*total['Фисташки'] + data6[3]*total['Фундук']\
             + data7[3]*total['Пекан'] + data8[3]*total['Вишня'] + data9[3]*total['Изюм'] + data10[3]*total['Инжир']\
             + data11[3]*total['Курага'] + data12[3]*total['Финик'] + data13[3]*total['Чернослив']\
             + data14[3]*total['Цукаты'] + data15[3]*total['Папайя']
    sales = totals - total_ws
    return render_template("korzina.html",
                           arah_mass=data0[1], ar_am=total['Арахис'], arah_price=data0[0]*total['Арахис'],
                           grez_mass=data1[1], gr_am=total['Грецкий'], grez_price=data1[0]*total['Грецкий'],
                           kesh_mass=data2[1], ks_am=total['Кешью'], kesh_price=data2[0*total['Кешью']],
                           mind_mass=data3[1], mi_am=total['Миндаль'], mind_price=data3[0]*total['Миндаль'],
                           braz_mass=data4[1], br_am=total['Бразильский'], braz_price=data4[0]*total['Бразильский'],
                           fist_mass=data5[1], fs_am=total['Фисташки'], fist_price=data5[0]*total['Фисташки'],
                           fund_mass=data6[1], fu_am=total['Фундук'], fund_price=data6[0]*total['Фундук'],
                           peka_mass=data7[1], pe_am=total['Пекан'], peka_price=data7[0]*total['Пекан'],
                           vish_mass=data8[1], vi_am=total['Вишня'], vish_price=data8[0]*total['Вишня'],
                           izum_mass=data9[1], iz_am=total['Изюм'], izum_price=data9[0]*total['Изюм'],
                           inzh_mass=data10[1], in_am=total['Инжир'], inzh_price=data10[0]*total['Инжир'],
                           kura_mass=data11[1], ku_am=total['Курага'], kura_price=data11[0]*total['Курага'],
                           fini_mass=data12[1], fi_am=total['Финик'], fini_price=data12[0]*total['Финик'],
                           cher_mass=data13[1], ch_am=total['Чернослив'], cher_price=data13[0]*total['Чернослив'],
                           cuka_mass=data14[1], cu_am=total['Цукаты'], cuka_price=data14[0]*total['Цукаты'],
                           papa_mass=data15[1], pa_am=total['Папайя'], papa_price=data15[0]*total['Папайя'],
                           counter=counter, total=round(totals, 2), sale=round(sales, 2), total_s=round(total_ws, 2))


@app.route("/Orexof/register", methods=["GET", "POST"])
def reggs():
    forma = RegisterForm()
    if request.method == "POST":
        db_sess = db_session.create_session()
        user = User(
            surname=forma.surname.data,
            name=forma.name.data,
            email=forma.email.data,
            hashed_password=forma.password.data
        )
        db_sess.add(user)
        db_sess.commit()
        return redirect('/')
    return render_template("register.html", form=forma, title='reg')


@app.route("/Orexof/login", methods=["GET", "POST"])
def logges():
    registration = False
    forma = LoginForm()
    print(0)
    if forma.validate():
        print(1)
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == forma.email.data).first()
        if user and user.check_password(forma.password.data):
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=forma)
    return render_template('login.html', title='Авторизация', form=forma, registration=registration)


if __name__ == '__main__':
    db_session.global_init("db/orehoff.db")
    app.run(debug=True)
