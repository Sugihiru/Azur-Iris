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
    is_collection_ship = Column(Boolean, nullable=False)
    is_login_reward_ship = Column(Boolean, nullable=False)
    buyable_source = Column(Integer, ForeignKey("shops.shop_id"))

    def __repr__(self):
        return ("<Shipfu({}, rarity_id={}, ship_type_id={},"
                " nation_id={})>".format(
                    self.name, self.rarity_id,
                    self.ship_type_id, self.nation_id))

    def set_drops(self):
        self.drops = (session.query(ShipfuDrop)
                             .filter_by(shipfu_id=self.shipfu_id)
                             .order_by(ShipfuDrop.world,
                                       ShipfuDrop.subworld).all())

    def set_shop_name(self):
        self.shop_name = (session.query(Shop.name)
                                 .filter_by(shop_id=self.buyable_source)
                                 .first())[0]

    def build_obtention_method_string(self):
        """
        Build a string stored in self.obtention_methods that contains
        human-readable informations about how to obtain the shipfu
        """
        obtention_methods = list()

        # Builds
        build_sources = list()
        if self.is_in_light_build:
            build_sources.append("Light build")
        if self.is_in_heavy_build:
            build_sources.append("Heavy build")
        if self.is_in_special_build:
            build_sources.append("Special build")
        if build_sources:
            obtention_methods.append(
                "Buildable in " + ", ".join(build_sources))

        # Drops
        if self.drops:
            drop_msg = list()
            for drop in self.drops:
                drop_msg.append(f"{drop.world}-{drop.subworld}")
            drop_msg = "Droppable in " + ", ".join(drop_msg)
            obtention_methods.append(drop_msg)

        # Event
        if self.is_event_ship:
            obtention_methods.append("Event")

        # Shop
        if self.buyable_source:
            obtention_methods.append(f"Buyable in {self.shop_name}")

        # Research shipfus
        if self.is_pr_ship():
            obtention_methods.append("Research")

        # Collection
        if self.is_collection_ship:
            obtention_methods.append("Collection")

        # Login reward
        if self.is_login_reward_ship:
            obtention_methods.append("Monthly login reward")

        self.obtention_methods = "\n".join(obtention_methods)

    def is_buildable(self):
        return (self.is_in_light_build or
                self.is_in_heavy_build or
                self.is_in_special_build)

    def is_buyable(self):
        return self.buyable_source is not None

    def is_pr_ship(self):
        return self.rarity_id in (6, 7)


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
    min_efficiency = Column(Integer)
    max_efficiency = Column(Integer)
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


class RetrofitCost(Base):
    __tablename__ = "retrofit_costs"
    retrofit_cost_id = Column(Integer, primary_key=True)
    shipfu_id = Column(String, ForeignKey("shipfus.shipfu_id"), nullable=False)
    bp_type_id = Column(Integer, ForeignKey("ship_types.ship_type_id"),
                        nullable=False)
    t1_bp = Column(Integer, nullable=False)
    t2_bp = Column(Integer, nullable=False)
    t3_bp = Column(Integer, nullable=False)
    gold = Column(Integer, nullable=False)
    gun_plates = Column(Integer)
    torpedo_plates = Column(Integer)
    aircraft_plates = Column(Integer)
    antiair_plates = Column(Integer)
    aux_plates = Column(Integer)

    def hasPlatesReq(self):
        return (self.gun_plates or self.torpedo_plates or
                self.aircraft_plates or self.antiair_plates or self.aux_plates)

    def shipTypeIdToName(self):
        if self.bp_type_id == 1:
            return "Destroyer"
        if self.bp_type_id == 2:
            return "Cruiser"
        if self.bp_type_id == 5:
            return "Battleship"
        if self.bp_type_id == 9:
            return "Aircraft Carrier"
        return "Unknown"


class ResearchShip(Base):
    __tablename__ = "research_ships"
    research_ship_id = Column(Integer, primary_key=True)
    shipfu_id = Column(String, ForeignKey("shipfus.shipfu_id"), nullable=False)
    season = Column(Integer, nullable=False)


class EventBuyable(Base):
    __tablename__ = "event_buyables"
    event_buyable_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    image = Column(BLOB)
    price_per_unit = Column(Integer, nullable=False)
    usual_max_per_event = Column(Integer)
