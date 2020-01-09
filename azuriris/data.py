import sqlalchemy

import db_models


class Data():
    _version = None
    _shipfus = None
    _rarities = None
    _nations = None
    _ship_types = None
    _retrofit_costs = None
    _research_ships = None
    _event_shop_items = None

    @classmethod
    def getVersion(cls):
        if not cls._version:
            try:
                cls._version = db_models.session.query(
                    db_models.Version).first()
            except sqlalchemy.exc.OperationalError:
                cls._version = None
        return cls._version

    @classmethod
    def getShipfus(cls):
        if not cls._shipfus:
            cls._shipfus = (
                db_models.session.query(db_models.Shipfu,
                                        db_models.Rarity,
                                        db_models.ShipType,
                                        db_models.Nation)
                                 .join(db_models.Rarity)
                                 .join(db_models.ShipType)
                                 .join(db_models.Nation)
                                 .order_by(db_models.Shipfu.shipfu_id)
                                 .all())
            for shipfu in cls._shipfus:
                shipfu.Shipfu.set_drops()
                if shipfu.Shipfu.buyable_source:
                    shipfu.Shipfu.set_shop_name()
                shipfu.Shipfu.build_obtention_method_string()

        return cls._shipfus

    @classmethod
    def getShipfuFromId(cls, shipfu_id):
        return next(
            x for x in cls.getShipfus() if x.Shipfu.shipfu_id == shipfu_id)

    @classmethod
    def getNonRetrofitShipfus(cls):
        return [
            x for x in cls.getShipfus() if not x.Shipfu.name.endswith(" Kai")]

    @classmethod
    def getRetrofitShipfus(cls):
        return [
            x for x in cls.getShipfus() if x.Shipfu.name.endswith(" Kai")]

    @classmethod
    def getRarities(cls):
        if not cls._rarities:
            cls._rarities = (
                db_models.session.query(db_models.Rarity)
                                 .order_by(db_models.Rarity.rarity_id)
                                 .all())
        return cls._rarities

    @classmethod
    def getNations(cls):
        if not cls._nations:
            cls._nations = (
                db_models.session.query(db_models.Nation)
                                 .order_by(db_models.Nation.nation_id)
                                 .all())
        return cls._nations

    @classmethod
    def getShipTypes(cls):
        if not cls._ship_types:
            cls._ship_types = (
                db_models.session.query(db_models.ShipType)
                                 .order_by(db_models.ShipType.ship_type_id)
                                 .all())
        return cls._ship_types

    @classmethod
    def getRetrofitCosts(cls):
        if not cls._retrofit_costs:
            cls._retrofit_costs = db_models.session.query(
                db_models.RetrofitCost).order_by(
                db_models.RetrofitCost.shipfu_id).all()
        return cls._retrofit_costs

    @staticmethod
    def getStatsForShipfu(shipfu_id):
        return (db_models.session.query(db_models.ShipfuStat)
                                 .filter_by(shipfu_id=shipfu_id)
                                 .order_by(db_models.ShipfuStat.level)
                                 .all())

    @classmethod
    def getResearchShips(cls):
        if not cls._research_ships:
            cls._research_ships = (
                db_models.session.query(db_models.ResearchShip,
                                        db_models.Shipfu)
                                 .join(db_models.Shipfu)
                                 .order_by(db_models.ResearchShip.shipfu_id)
                                 .all())
        return cls._research_ships

    @classmethod
    def getShopEventItems(cls):
        if not cls._event_shop_items:
            cls._event_shop_items = (
                db_models.session.query(db_models.EventBuyable)
                                 .order_by(db_models.EventBuyable.event_buyable_id)
                                 .all())
        return cls._event_shop_items
