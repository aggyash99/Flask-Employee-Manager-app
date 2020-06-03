from flaskwebapp import db

class Employees (db.Model) :
    id = db.Column(db.Integer, primary_key = True )
    name = db.Column (db.String(30), nullable=False)
    designation = db.Column (db.String(20), nullable=False)
    address = db.Column (db.String(120), nullable=False)
    phone = db.Column (db.String(20), nullable=False)

    def __repr__(self) :
        return f"Employees('{self.name}', '{self.designation}', '{self.address}', '{self.phone}')"

