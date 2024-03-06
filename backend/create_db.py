from app import app, db, User, Doctor

# Set up an application context
with app.app_context():
    db.create_all()
    # doctor_2 = Doctor(name='Faisal', specialty='Neurology', yearsofexperience=1)
    # db.session.add(doctor_2)
    # db.session.commit()
    # for user in User.query.all():
    #     print(user)
    print(User.query.all())

    # for doctor in Doctor.query.all():
    #     print(doctor)
    # db.drop_all()
    
   
