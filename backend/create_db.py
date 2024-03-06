from app import app, db, User

# Ensure the app context is pushed
with app.app_context():
    print(User.query.all())
