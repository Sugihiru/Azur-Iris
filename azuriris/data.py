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
                             .order_by(db_models.Shipfu.shipfu_id)
                             .all())

        for shipfu in self.shipfus:
            shipfu.Shipfu.set_drops()
            if shipfu.Shipfu.buyable_source:
                shipfu.Shipfu.set_shop_name()
            shipfu.Shipfu.build_obtention_method_string()

        self.rarities = (db_models.session.query(db_models.Rarity)
                                          .order_by(db_models.Rarity.rarity_id)
                                          .all())

        self.nations = (db_models.session.query(db_models.Nation)
                                         .order_by(db_models.Nation.nation_id)
                                         .all())

        self.ship_types = (
            db_models.session.query(db_models.ShipType)
                             .order_by(db_models.ShipType.ship_type_id)
                             .all())

        self.non_retrofit_shipfus = [x for x in self.shipfus
                                     if not x.Shipfu.name.endswith(" Kai")]

        self.retrofit_shipfus = [x for x in self.shipfus
                                 if x.Shipfu.name.endswith(" Kai")]


def getStatsForShipfu(shipfu_id):
    return (db_models.session.query(db_models.ShipfuStat)
                             .filter_by(shipfu_id=shipfu_id)
                             .order_by(db_models.ShipfuStat.level)
                             .all())


def getRetrofitCosts():
    return db_models.session.query(db_models.RetrofitCost).all()
