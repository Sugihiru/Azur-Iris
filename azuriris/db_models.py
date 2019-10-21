from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.sqlite import BLOB


Base = declarative_base()
engine = create_engine("sqlite:///azuriris.data")
Session = sessionmaker(bind=engine)
session = Session()


class Shipfu(Base):
    __tablename__ = "shipfus"
    shipfu_id = Column(Integer, primary_key=True)
    image = Column(BLOB)
    name = Column(String)
    rarity_id = Column(Integer, ForeignKey("rarity.rarity_id"))
    ship_type_id = Column(Integer, ForeignKey("ship_types.ship_type_id"))
    nation_id = Column(Integer, ForeignKey("nations.nation_id"))


class Rarity(Base):
    __tablename__ = "rarity"
    rarity_id = Column(Integer, primary_key=True)
    name = Column(String)


class ShipType(Base):
    __tablename__ = "ship_types"
    ship_type_id = Column(Integer, primary_key=True)
    name = Column(String)
    abbreviation = Column(String)


class Nation(Base):
    __tablename__ = "nations"
    nation_id = Column(Integer, primary_key=True)
    name = Column(String)
    prefix = Column(String)
