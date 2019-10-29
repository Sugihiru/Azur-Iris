import db_models


class Data():
    def __init__(self):
        self.shipfus = (
            db_models.session.query(db_models.Shipfu,
                                    db_models.Rarity,
                                    db_models.ShipType,
                                    db_models.Nation)
                             .join(db_models.Rarity)
                             .join(db_models.ShipType)
                             .join(db_models.Nation)
                             .filter(
                                 ~db_models.Shipfu.name.endswith(" Kai"))
                             .order_by(db_models.Shipfu.shipfu_id)
                             .all())

        self.retrofit_shipfus = (
            db_models.session.query(db_models.Shipfu,
                                    db_models.Rarity,
                                    db_models.ShipType,
                                    db_models.Nation)
                             .join(db_models.Rarity)
                             .join(db_models.ShipType)
                             .join(db_models.Nation)
                             .filter(db_models.Shipfu.name.endswith(" Kai"))
                             .order_by(db_models.Shipfu.shipfu_id)
                             .all())
