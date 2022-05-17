from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)
    password = db.Column(db.String(200), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "email": self.email,
            "password": self.password,
            # do not serialize the password, its a security breach
        }

class Personajes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), unique=True, nullable=False)
    poder = db.Column(db.String(120), unique=False, nullable=False)
    tipo = db.Column(db.String(120), unique=False, nullable=False)
   

    def __repr__(self):
        return '<Personajes %r>' % self.username

    def serialize(self):
        return {
            "nombre": self.nombre,
            "poder": self.poder,
            "tipo": self.tipo,

        }
        
class Planeta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), unique=True, nullable=False)
    habitable = db.Column(db.String(120), unique=False, nullable=False)
    clima = db.Column(db.String(120), unique=False, nullable=False)


    def __repr__(self):
        return '<Planeta %r>' % self.username

    def serialize(self):
        return {
            "nombre": self.nombre,
            "habitale": self.habitable,
            "clima": self.clima,

        }