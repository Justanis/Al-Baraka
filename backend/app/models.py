from . import db
from sqlalchemy.orm import relationship
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    id               = db.Column(db.Integer, primary_key=True)
    firstName        = db.Column(db.String(50), nullable=True)
    lastName         = db.Column(db.String(50), nullable=True)
    userName         = db.Column(db.String(50), unique=True, nullable=False)
    age              = db.Column(db.Integer, nullable=True)
    email            = db.Column(db.String(100), unique=True, nullable=False)
    phone            = db.Column(db.String(100), nullable=True)
    password         = db.Column(db.String(250), nullable=False)
    city             = db.Column(db.String(250), nullable=True)
    street           = db.Column(db.String(250), nullable=True)
    gender           = db.Column(db.String(250), nullable=True)
    isConfirmed      = db.Column(db.Integer, default=0, nullable=False)
    confirmationCode = db.Column(db.String(6), unique=True, nullable=True)
    profileImage     = db.Column(db.String(255), default='default_profile.png', nullable=False)

    # ←– relationship
    volunteer = relationship(
        'Volunteer',
        back_populates='user',
        uselist=False
    )

    # 1-to-many relationship to ContactMessage
    messages = relationship(
        'ContactMessage', back_populates='user', lazy='dynamic'
    )

    transfers = relationship('Transfer', back_populates='user', lazy='dynamic')

    @property
    def is_volunteer(self) -> bool:
        """Return True if this user has a Volunteer record."""
        return self.volunteer is not None
    
    def ValidateUserData(UserData):
        if ('userName' in UserData) and ('email' in UserData) and ('password' in UserData):
            if  UserData['userName'] != '' and UserData['email'] != '' and UserData['password'] != '':
                return True
        return False
    
    def to_dict(self):
        return {
            "id": self.id,
            "firstName": self.firstName,
            "lastName": self.lastName,
            "userName": self.userName,
            "age": self.age,
            "email": self.email,
            "phone": self.phone,
            "city": self.city,
            "street": self.street,
            "gender": self.gender,
            "isConfirmed": self.isConfirmed,
            "confirmationCode": self.confirmationCode,
            "profileImage": self.profileImage,
        }

class Volunteer(db.Model):  
    __tablename__ = 'volunteers'

    id            = db.Column(db.Integer, primary_key=True)

    # 1-to-1 link to User
    user_id       = db.Column(
                       db.Integer,
                       db.ForeignKey('users.id'),
                       nullable=False,
                       unique=True     # ←– enforces one-to-one
                   )
    user          = relationship(
                       'User',
                       back_populates='volunteer',
                       uselist=False
                   )

    # now embed your “responses” here
    firstResponse  = db.Column(db.String(250), nullable=True)
    secondResponse = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "firstResponse": self.firstResponse,
            "secondResponse": self.secondResponse,
            # …etc… 
        }
    
class ContactMessage(db.Model):
    __tablename__ = 'contact_messages'

    id         = db.Column(db.Integer, primary_key=True)
    user_id    = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    message    = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    user       = relationship('User', back_populates='messages')

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "message": self.message,
            "created_at": self.created_at.isoformat()
        }
    
# new table for payment methods
class PaymentMethod(db.Model):
    __tablename__ = 'payment_methods'
    id    = db.Column(db.Integer, primary_key=True)
    name  = db.Column(db.String(50), unique=True, nullable=False)

    # default methods will be seeded via migration or startup script
    transfers = relationship('Transfer', back_populates='method', lazy='dynamic')

    def to_dict(self):
        return {"id": self.id, "name": self.name}
    
# transfers table linking user and payment_methods
class Transfer(db.Model):
    __tablename__ = 'transfers'
    id                = db.Column(db.Integer, primary_key=True)
    user_id           = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    method_id         = db.Column(db.Integer, db.ForeignKey('payment_methods.id'), nullable=False)
    amount            = db.Column(db.Numeric(10,2), nullable=False)
    transaction_date  = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    details           = db.Column(db.Text, nullable=True)

    user   = relationship('User', back_populates='transfers')
    method = relationship('PaymentMethod', back_populates='transfers')

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "method_id": self.method_id,
            "amount": float(self.amount),
            "transaction_date": self.transaction_date.isoformat(),
            "details": self.details
        }