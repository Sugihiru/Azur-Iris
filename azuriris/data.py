import db_models


class Data():
    def __init__(self):
        self.shipfus = db_models.session.query(db_models.Shipfu).all()
        print(self.shipfus)
