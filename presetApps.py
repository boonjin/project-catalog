"""presetApps.py: initialize categories and apps"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, App, User

engine = create_engine('sqlite:///appstorewithusers.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()


# Create dummy user
User1 = User(name="Susan Brent", email="susanbrent@alextest123.co",
             picture='https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xaf1' + 
             '/v/t1.0-1/p50x50/481902_10150980461973016_480056919_n.jpg?oh=' + 
             '2092e695168a4e4165741a5b1a0819b8&oe=5674C7A7&__gda__=' + 
             '1447372075_f2a6c0b88977be61465cc4bf95cc718b')
session.add(User1)
session.commit()



# Create Category: Games and apps for this category
category1 = Category(user_id=0, name="Games")

session.add(category1)
session.commit()


app1 = App(user_id=1, name="Fast n Furious", description="Racing Game", image_url="https://lh6.ggpht.com/gfZaWN5ttjMY_GQiqJpn9wBNKhOdD5E0hBxRR9dQCzgoP7H5uwrCCBpYidz9nlYjcBwu=w300-rw",
                     price="$1.99", category=category1)

session.add(app1)
session.commit()

app2 = App(user_id=1, name="Flying Eagle", description="War plane multiplayer fight", image_url="https://lh5.ggpht.com/jg--Q4mKlE0kBGDlZYmYh8KCsBtNn6H6kmaw6ALBDoemJ9uPb9ONdpcQEUbRvSvduFBO=w300-rw",
                     price="$0.99", category=category1)

session.add(app2)
session.commit()

app3 = App(user_id=1, name="Duck Hunt", description="Simple and fun game", image_url="https://lh5.ggpht.com/gOztZVKtu9aUPc_fSmP927mdAIySKq6bE5dlkk8kssbT4u1E7OgQxdU00rDgxKV7qO0=w300-rw",
                     price="$2.99", category=category1)

session.add(app3)
session.commit()


# Create Category: Communication and apps for this category
category1 = Category(user_id=0, name="Communication")

session.add(category1)
session.commit()


app1 = App(user_id=1, name="Facebook", description="Social Network Platform", image_url="https://lh3.googleusercontent.com/ZZPdzvlpK9r_Df9C3M7j1rNRi7hhHRvPhlklJ3lfi5jk86Jd1s0Y5wcQ1QgbVaAP5Q=w300-rw",
                     price="$1.99", category=category1)

session.add(app1)
session.commit()

app2 = App(user_id=1, name="Whatsapp", description="Messaging network", image_url="https://lh6.ggpht.com/mp86vbELnqLi2FzvhiKdPX31_oiTRLNyeK8x4IIrbF5eD1D5RdnVwjQP0hwMNR_JdA=w300-rw",
                     price="$0.99", category=category1)

session.add(app2)
session.commit()


# Create Category: Productivity and apps for this category
category1 = Category(user_id=0, name="Productivity")

session.add(category1)
session.commit()


app1 = App(user_id=1, name="Calculator", description="Simple calculator app", image_url="https://lh3.ggpht.com/qx4m0t5_uWGfjHfd-6P5lGOeI46HKGARtSWT1lncKLbtpn31fQqF3mhKBgQ6nQ8lElA=w300-rw",
                     price="$1.99", category=category1)

session.add(app1)
session.commit()




print "added preset category and apps"
