import db_models


class Data():
    def __init__(self):
        self.shipfus = (db_models.session.query(db_models.Shipfu,
                                                db_models.Rarity,
                                                db_models.ShipType,
                                                db_models.Nation)
                                         .join(db_models.Rarity)
                                         .join(db_models.ShipType)
                                         .join(db_models.Nation)
                                         .all())
