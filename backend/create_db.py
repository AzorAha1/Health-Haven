from app import app, db, User, Doctor, Appointment

# Ensure the app context is pushed
with app.app_context():
    db.create_all()
    print("Tables created successfully")
    # user = User.query.all()
    # print(user)
    # doctor = Doctor(name='David Ornstein', specialty='Physiotherapy', yearsofexperience=15)
    # db.session.add(doctor)
    # db.session.commit()
    # doctors = Appointment.query.all()
    # for doctor in doctors:
    #     print(doctor)
    # db.drop_all()
