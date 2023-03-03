from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")

    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    user.hashed_password = "cap"
    session = db_session.create_session()
    session.add(user)
    session.commit()

    user = User()
    user.surname = "Andrew"
    user.name = "Walker"
    user.age = 39
    user.position = "soldier"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "andrew_chief@mars.org"
    user.hashed_password = "cap"
    session = db_session.create_session()
    session.add(user)
    session.commit()

    user = User()
    user.surname = "Paul"
    user.name = "Brown"
    user.age = 25
    user.position = "soldier"
    user.speciality = "cooker"
    user.address = "module_2"
    user.email = "paul_chief@mars.org"
    user.hashed_password = "cap"
    session = db_session.create_session()
    session.add(user)
    session.commit()

    user = User()
    user.surname = "Joe"
    user.name = "Winston"
    user.age = 45
    user.position = "soldier"
    user.speciality = "teacher"
    user.address = "module_4"
    user.email = "joe_chief@mars.org"
    user.hashed_password = "cap"
    session = db_session.create_session()
    session.add(user)
    session.commit()

    app.run()


if __name__ == '__main__':
    main()
