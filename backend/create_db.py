from app import app, db, User, Doctor

# Ensure the app context is pushed
with app.app_context():
    # db.create_all()
    # print("Tables created successfully")
    user = User.query.all()
    print(user)
    # db.drop_all()