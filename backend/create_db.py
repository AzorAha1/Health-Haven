from app import app, db, User

# Set up an application context
with app.app_context():
    # db.create_all()
    # user_1 = User(username='Faisal', email='wizfaiz@icloud.com', password='123456')
    # db.session.add(user_1)
    # db.session.commit()
    # users = User.query.all()
    # for user in users:
    #     print(f"User ID: {user.user_id}, Username: {user.username}, Email: {user.email}")
    db.drop_all()
   
