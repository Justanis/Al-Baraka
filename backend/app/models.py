from . import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    # fullName  = db.Column(db.String(50), unique=False, nullable=True)
    firstName = db.Column(db.String(50), unique=False, nullable=True) # REQUIRED
    lastName = db.Column(db.String(50), unique=False, nullable=True) # REQUIRED
    userName = db.Column(db.String(50), unique=True, nullable=False) # REQUIRED
    age = db.Column(db.Integer, unique=False, nullable=True)
    
    # contact infos
    email = db.Column(db.String(100), unique=True, nullable=False)# REQUIRED
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
            "id": self.id,
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
            "profileImage": self.profileImage
        }

    def ValidateUserData(UserData):
        if ('userName' in UserData) and ('email' in UserData) and ('password' in UserData):
            if  UserData['userName'] != '' and UserData['email'] != '' and UserData['password'] != '':
                return True
        return False
         
