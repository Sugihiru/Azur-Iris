"""
This file is used to initialize an empty data file with its tables
It is NOT intended to be imported or used in other files
"""
from sqlalchemy import Column, Integer, String

import db_models


class Rarity(db_models.Base):
    __tablename__ = "rarity"
    rarity_id = Column(Integer, primary_key=True)
    name = Column(String)


class ShipType(db_models.Base):
    __tablename__ = "ship_types"
    ship_type_id = Column(Integer, primary_key=True)
    name = Column(String)
    abbreviation = Column(String)


class Nation(db_models.Base):
    __tablename__ = "nations"
    nation_id = Column(Integer, primary_key=True)
    name = Column(String)
    prefix = Column(String)


def init_db():
    """Create tables in database if they doesn't exist"""
    db_models.Base.metadata.create_all(db_models.engine)


def insert_datas():
    data = list()

    # Rarity
    data.append(Rarity(name="Normal"))
    data.append(Rarity(name="Rare"))
    data.append(Rarity(name="Elite"))
    data.append(Rarity(name="Super Rare"))
    data.append(Rarity(name="Ultra Rare"))
    data.append(Rarity(name="Priority"))
    data.append(Rarity(name="Decisive"))

    # Ship type
    data.append(ShipType(name="Destroyer", abbreviation="DD"))
    data.append(ShipType(name="Light Cruiser", abbreviation="CL"))
    data.append(ShipType(name="Heavy Cruiser", abbreviation="CA"))
    data.append(ShipType(name="Large Cruiser", abbreviation="CB"))
    data.append(ShipType(name="Battleship", abbreviation="BB"))
    data.append(ShipType(name="Battlecruiser", abbreviation="BC"))
    data.append(ShipType(name="Battlecruiser", abbreviation="BC"))
    data.append(ShipType(name="Monitor", abbreviation="BM"))
    data.append(ShipType(name="Aircraft Carrier", abbreviation="CV"))
    data.append(ShipType(name="Light Aircraft Carrier", abbreviation="CVL"))
    data.append(ShipType(name="Submarine", abbreviation="SS"))
    data.append(ShipType(name="Submarine Carrier", abbreviation="SSV"))
    data.append(ShipType(name="Repair Ship", abbreviation="AR"))

    # Nations
    data.append(Nation(name="Universal", prefix="UNIV"))
    data.append(Nation(name="Eagle Union", prefix="USS"))
    data.append(Nation(name="Royal Navy", prefix="HMS"))
    data.append(Nation(name="Sakura Empire", prefix="IJN"))
    data.append(Nation(name="Iron Blood", prefix="KMS"))
    data.append(Nation(name="Eastern Radiance", prefix="ROC"))
    data.append(Nation(name="North Union", prefix="SN"))
    data.append(Nation(name="Iris Libre", prefix="FFNF"))
    data.append(Nation(name="Vichya Dominion", prefix="MNF"))
    data.append(Nation(name="Sardegna Empire", prefix="RN"))
    data.append(Nation(name="Neptunia", prefix="HDN"))
    data.append(Nation(name="Bilibili", prefix=""))
    data.append(Nation(name="Utawarerumono", prefix=""))
    data.append(Nation(name="KizunaAI", prefix=""))

    data.append(db_models.Shipfu(image=None, name="Cleveland", rarity_id=1,
                                 ship_type_id=1, nation_id=1))

    db_models.session.add_all(data)
    db_models.session.commit()


if __name__ == '__main__':
    init_db()
    insert_datas()
