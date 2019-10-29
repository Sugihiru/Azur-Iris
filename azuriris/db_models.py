import enum

from sqlalchemy import (Column, Integer, String, create_engine,
                        ForeignKey, Enum, Boolean)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.sqlite import BLOB


Base = declarative_base()
engine = create_engine("sqlite:///azuriris.data")
Session = sessionmaker(bind=engine)
session = Session()


class Shipfu(Base):
    __tablename__ = "shipfus"
    shipfu_id = Column(String, primary_key=True)
    image = Column(BLOB)
    name = Column(String, nullable=False)
    rarity_id = Column(Integer, ForeignKey("rarity.rarity_id"), nullable=False)
    ship_type_id = Column(Integer, ForeignKey("ship_types.ship_type_id"),
                          nullable=False)
    nation_id = Column(Integer, ForeignKey("nations.nation_id"),
                       nullable=False)
    retrofit_shipfu_id = Column(String)
    is_in_cn = Column(Boolean, nullable=False)
    is_in_jp = Column(Boolean, nullable=False)
    is_in_en = Column(Boolean, nullable=False)
    is_in_light_build = Column(Boolean, nullable=False)
    is_in_heavy_build = Column(Boolean, nullable=False)
    is_in_special_build = Column(Boolean, nullable=False)
    is_event_ship = Column(Boolean, nullable=False)
    buyable_source = Column(Integer, ForeignKey("shops.shop_id"))

    def __repr__(self):
        return ("<Shipfu({}, rarity_id={}, ship_type_id={},"
                " nation_id={})>".format(
                    self.name, self.rarity_id,
                    self.ship_type_id, self.nation_id))


class ShipfuDrop(Base):
    __tablename__ = "shipfu_drops"
    shipfu_drop_id = Column(Integer, primary_key=True)
    shipfu_id = Column(String, ForeignKey("shipfus.shipfu_id"), nullable=False)
    world = Column(Integer, nullable=False)
    subworld = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<ShipfuDrop({self.world}-{self.subworld})>"


class ShipfuWeaponSlot(Base):
    __tablename__ = "shipfu_weapon_slots"
    shipfu_weapon_slot_id = Column(Integer, primary_key=True)
    shipfu_id = Column(String, ForeignKey("shipfus.shipfu_id"), nullable=False)
    weapon_slot_nb = Column(Integer, nullable=False)
    min_efficiency = Column(Integer, nullable=False)
    max_efficiency = Column(Integer, nullable=False)
    weapon_type_id = Column(Integer, ForeignKey("weapon_types.weapon_type_id"),
                            nullable=False)

    def __repr__(self):
        return ("<ShipfuWeaponSlot(Slot={}, weapon_type_id={}, "
                "min_eff={}, max_eff={})>".format(
                    self.weapon_slot_nb, self.weapon_type_id,
                    self.min_efficiency, self.max_efficiency))


class ArmorTypeEnum(enum.Enum):
    Light = 0
    Medium = 1
    Heavy = 2


class ShipfuStat(Base):
    __tablename__ = "shipfu_stats"
    shipfu_stat_id = Column(Integer, primary_key=True)
    shipfu_id = Column(String, ForeignKey("shipfus.shipfu_id"), nullable=False)
    level = Column(Integer)
    health = Column(Integer, nullable=False)
    armor_type = Column(Enum(ArmorTypeEnum), nullable=False)
    firepower = Column(Integer, nullable=False)
    torpedo = Column(Integer, nullable=False)
    evasion = Column(Integer, nullable=False)
    reload = Column(Integer, nullable=False)
    antiair = Column(Integer, nullable=False)
    aviation = Column(Integer, nullable=False)
    luck = Column(Integer, nullable=False)
    speed = Column(Integer, nullable=False)
    accuracy = Column(Integer, nullable=False)
    antisub = Column(Integer, nullable=False)
    cost = Column(Integer, nullable=False)
    oxygen = Column(Integer)
    ammunition = Column(Integer)

    def __repr__(self):
        return f"<ShipfuStat(shipfu_id={self.shipfu_id}, level={self.level})>"


class Rarity(Base):
    __tablename__ = "rarity"
    rarity_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


class ShipType(Base):
    __tablename__ = "ship_types"
    ship_type_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    abbreviation = Column(String)


class Nation(Base):
    __tablename__ = "nations"
    nation_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    prefix = Column(String)


class WeaponType(Base):
    __tablename__ = "weapon_types"
    weapon_type_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


class Shop(Base):
    __tablename__ = "shops"
    shop_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
