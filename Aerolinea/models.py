from database import db


class Aviones(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    airportentry = db.Column(db.String(250))
    departureairport = db.Column(db.String(250))
    status = db.Column(db.String(250))

    def __str__(self):
        return (
            f'id: {self.id}, '
            f'name: {self.name}, '
            f'airportentry: {self.airportentry}, '
            f'departureairport: {self.departureairport}, '
            f'status: {self.status}, '
        )