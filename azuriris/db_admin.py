"""
This file is used to initialize an empty data file with its tables
It is NOT intended to be imported or used in other files
"""
import db_models


def init_db():
    """Create tables in database if they doesn't exist"""
    db_models.Base.metadata.create_all(db_models.engine)


def insert_datas():
    data = list()

    # Rarity
    data.append(db_models.Rarity(rarity_id=1, name="Normal"))
    data.append(db_models.Rarity(rarity_id=2, name="Rare"))
    data.append(db_models.Rarity(rarity_id=3, name="Elite"))
    data.append(db_models.Rarity(rarity_id=4, name="Super Rare"))
    data.append(db_models.Rarity(rarity_id=5, name="Ultra Rare"))
    data.append(db_models.Rarity(rarity_id=6, name="Priority"))
    data.append(db_models.Rarity(rarity_id=7, name="Decisive"))

    # Ship type
    data.append(db_models.ShipType(ship_type_id=1,
                                   name="Destroyer", abbreviation="DD"))
    data.append(db_models.ShipType(ship_type_id=2,
                                   name="Light Cruiser", abbreviation="CL"))
    data.append(db_models.ShipType(ship_type_id=3,
                                   name="Heavy Cruiser", abbreviation="CA"))
    data.append(db_models.ShipType(ship_type_id=4,
                                   name="Large Cruiser", abbreviation="CB"))
    data.append(db_models.ShipType(ship_type_id=5,
                                   name="Battleship", abbreviation="BB"))
    data.append(db_models.ShipType(ship_type_id=6,
                                   name="Battlecruiser", abbreviation="BC"))
    data.append(db_models.ShipType(ship_type_id=7,
                                   name="Battlecruiser", abbreviation="BC"))
    data.append(db_models.ShipType(ship_type_id=8,
                                   name="Monitor", abbreviation="BM"))
    data.append(db_models.ShipType(ship_type_id=9,
                                   name="Aircraft Carrier", abbreviation="CV"))
    data.append(db_models.ShipType(ship_type_id=10,
                                   name="Light Aircraft Carrier",
                                   abbreviation="CVL"))
    data.append(db_models.ShipType(ship_type_id=11,
                                   name="Submarine", abbreviation="SS"))
    data.append(db_models.ShipType(ship_type_id=12,
                                   name="Submarine Carrier",
                                   abbreviation="SSV"))
    data.append(db_models.ShipType(ship_type_id=13,
                                   name="Repair Ship", abbreviation="AR"))

    # Nations
    data.append(db_models.Nation(nation_id=1,
                                 name="Universal", prefix="UNIV"))
    data.append(db_models.Nation(nation_id=2,
                                 name="Eagle Union", prefix="USS"))
    data.append(db_models.Nation(nation_id=3,
                                 name="Royal Navy", prefix="HMS"))
    data.append(db_models.Nation(nation_id=4,
                                 name="Sakura Empire", prefix="IJN"))
    data.append(db_models.Nation(nation_id=5,
                                 name="Iron Blood", prefix="KMS"))
    data.append(db_models.Nation(nation_id=6,
                                 name="Eastern Radiance", prefix="ROC"))
    data.append(db_models.Nation(nation_id=7,
                                 name="North Union", prefix="SN"))
    data.append(db_models.Nation(nation_id=8,
                                 name="Iris Libre", prefix="FFNF"))
    data.append(db_models.Nation(nation_id=9,
                                 name="Vichya Dominion", prefix="MNF"))
    data.append(db_models.Nation(nation_id=10,
                                 name="Sardegna Empire", prefix="RN"))
    data.append(db_models.Nation(nation_id=11,
                                 name="Neptunia", prefix="HDN"))
    data.append(db_models.Nation(nation_id=12,
                                 name="Bilibili", prefix=""))
    data.append(db_models.Nation(nation_id=13,
                                 name="Utawarerumono", prefix=""))
    data.append(db_models.Nation(nation_id=14,
                                 name="KizunaAI", prefix=""))

    # Ships
    with open("ClevelandIcon.png", "rb") as f:
        blob = f.read()
    data.append(db_models.Shipfu(image=blob, name="Cleveland", rarity_id=3,
                                 ship_type_id=2, nation_id=2))

    db_models.session.add_all(data)
    db_models.session.commit()


if __name__ == '__main__':
    init_db()
    insert_datas()
