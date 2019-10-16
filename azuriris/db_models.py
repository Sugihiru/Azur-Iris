from sqlalchemy import Column, Integer, String, create_engine
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
    rarity_id = Column(Integer)
    ship_type_id = Column(Integer)
    nation_id = Column(Integer)
