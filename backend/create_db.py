from app import app, db, User

# Ensure the app context is pushed
with app.app_context():
    # db.create_all()
    # print("Tables created successfully")
    user = User.query.first()
    print(user.phonenum)
    # db.drop_all()