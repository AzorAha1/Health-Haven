from app import app, db, User, Doctor, Appointment

# Ensure the app context is pushed
with app.app_context():
    # db.create_all()
    # print("Tables created successfully")
    # user = User.query.all()
    # print(user)
    # doctor = Doctor(name='Jon Snow', specialty='General Medicine', yearsofexperience=5)
    # db.session.add(doctor)
    # db.session.commit()
    doctors = Doctor.query.all()
    for doctor in doctors:
        print(doctor)
    # db.drop_all()
