from . import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    # fullName  = db.Column(db.String(50), unique=False, nullable=True)
    firstName = db.Column(db.String(50), unique=False, nullable=True)
    lastName = db.Column(db.String(50), unique=False, nullable=True)
    userName = db.Column(db.String(50), unique=True, nullable=False) # REQUIRED
    age = db.Column(db.Integer, unique=False, nullable=True)
    
    # contact infos
    email = db.Column(db.String(100), unique=True, nullable=False) # REQUIRED
    phone = db.Column(db.String(100), unique=False, nullable=True)
    password = db.Column(db.String(250), nullable=False) # REQUIRED
    adresse = db.Column(db.String(250), nullable=True)
    
    # 0 => is not confirmed yet and 1 if the user has confirmed
    isConfirmed = db.Column(db.Integer, unique=False, nullable=False, default=0) # REQUIRED
    confirmationCode = db.Column(db.String(6), unique=True, nullable=True)

    profileImage = db.Column(db.String(255), nullable=False, default='default_profile.png') # REQUIRED
    
    
    def to_dict(self):
        """Convert the User object to a dictionary."""
        return {
            # "id": self.id,
            "firstName": self.firstName,
            "lastName": self.lastName,
            # "fullName": self.fullName,
            "userName": self.userName,
            "age": self.age,
            "email": self.email,
            "phone": self.phone,
            "password": self.password,
            "adresse": self.adresse,
            "isConfirmed": self.isConfirmed,
            "confirmationCode": self.confirmationCode,
            # "profileImage": self.profileImage
        }

    def ValidateUserData(UserData):
        if ('userName' in UserData) and ('email' in UserData) and ('password' in UserData):
            if  UserData['userName'] != '' and UserData['email'] != '' and UserData['password'] != '':
                return True
        return False

    # trying to add something for my self => check it later
class Volunteer(db.Model):
    __tablename__ = 'volunteers'  # Use double underscores and a plural table name

    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(50), unique=False, nullable=True)
    lastName = db.Column(db.String(50), unique=False, nullable=True)
    email = db.Column(db.String(100), unique=True, nullable=True)
    age = db.Column(db.Integer, unique=False, nullable=True)
    phonenumber = db.Column(db.String(100), unique=False, nullable=True)
    gender = db.Column(db.String(20), unique=False, nullable=True)
    city = db.Column(db.String(100), unique=False, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "firstName": self.firstName,
            "lastName": self.lastName,
            "gender": self.gender,
            "age": self.age,
            "email": self.email,
            "phonenumber": self.phonenumber,
            "city": self.city
        }