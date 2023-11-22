from flask import Flask, render_template, request, make_response, session
# noinspection PyUnresolvedReferences
from data import db_session
# noinspection PyUnresolvedReferences
from data.users import User


from forms.users import RegisterForm
from werkzeug.utils import redirect


def main():
    app = Flask ( __name__ )

    app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
    db_session.global_init("db/orehoff.db")

    user = User ()
    user.name = "Пользователь 1"
    user.email = "email1@email.ru"
    db_sess = db_session.create_session ()
    db_sess.add ( user )
    db_sess.commit ()
    # #
    # user2 = User ()
    # user2.name = "Пользователь 2"
    # user2.about = "биография пользователя 2"
    # user2.email = "email2@email.ru"
    # db_sess = db_session.create_session ()
    # db_sess.add ( user2 )
    # db_sess.commit ()
    #
    # user3 = User ()
    # user3.name = "Пользователь 3"
    # user3.about = "биография пользователя 3"
    # user3.email = "email1@email.ru"
    # db_sess = db_session.create_session ()
    # db_sess.add ( user3 )
    # db_sess.commit ()
    #
    db_sess = db_session.create_session()
    user = db_sess.query ( User ).first ()
    print ( user.name )

    for user in db_sess.query ( User ).all ():
        print ( user )
    #
    # print ('AND')
    # for user in db_sess.query ( User ).filter ( User.id > 1, User.email.notilike ( "%1%" ) ):
    #     print ( user )
    # print('OR')
    # for user in db_sess.query ( User ).filter ( (User.id > 1) | (User.email.notilike ( "%1%" )) ):
    #     print ( user )
    #
    # user = db_sess.query ( User ).filter ( User.id == 1 ).first ()
    # print ( user )
    #
    # user.name = "Измененное имя пользователя"
    # user.created_date = datetime.datetime.now ()
    # db_sess.commit ()
    #
    # db_sess.query ( User ).filter ( User.id >= 3 ).delete ()
    # db_sess.commit ()
    #
    # db_sess.query ( User ).filter ( User.id >= 2 ).delete ()
    # db_sess.commit ()
    #
    # news = News ( title="Первая новость", content="Привет блог!",
    #               user_id=1, is_private=False )
    # db_sess.add ( news )
    # db_sess.commit ()
    #
    # user = db_sess.query ( User ).filter ( User.id == 1 ).first ()
    # news = News ( title="Вторая новость", content="Уже вторая запись!",
    #               user=user, is_private=False )
    # db_sess.add ( news )
    # db_sess.commit ()
    #
    # user = db_sess.query ( User ).filter ( User.id == 1 ).first ()
    # news = News ( title="Личная запись", content="Эта запись личная",
    #               is_private=True )
    # user.news.append ( news )
    #  db_sess.commit ()
    #
    #  print("Новости")
    #  for news in user.news:
    #      print ( news )
    #
    #  @app.route ( "/" )
    #  def index():
    #      db_sess = db_session.create_session ()
    #      news = db_sess.query ( News ).filter ( News.is_private != True )
    #      print(news)
    #      return render_template ( "index0.html", news=news )
    #
    #  @app.route ( '/register', methods=['GET', 'POST'] )
    #  def reqister():
    #      form = RegisterForm ()
    #     if form.validate_on_submit ():
    #          if form.password.data != form.password_again.data:
    #              return render_template ( 'register.html', title='Регистрация',
    #                                       form=form,
    #                                       message="Пароли не совпадают" )
    #          db_sess = db_session.create_session ()
    #          if db_sess.query ( User ).filter ( User.email == form.email.data ).first ():
    #              return render_template ( 'register.html', title='Регистрация',
    #                                       form=form,
    #                                       message="Такой пользователь уже есть" )
    #          user = User (
    #              name=form.name.data,
    #              email=form.email.data,
    #              about=form.about.data
    #          )
    #          user.set_password ( form.password.data )
    #          db_sess.add ( user )
    #          db_sess.commit ()
    #          return redirect ( '/login' )
    #      return render_template ( 'register.html', title='Регистрация', form=form )
    #
    # app.run(port=8080, host='127.0.0.1')

if __name__ == '__main__':
    main()