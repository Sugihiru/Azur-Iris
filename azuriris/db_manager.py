import db_models


def get_shipfu_obtention_method(shipfu):
    obtention_methods = list()

    # Builds
    build_sources = list()
    if shipfu.is_in_light_build:
        build_sources.append("Light build")
    if shipfu.is_in_heavy_build:
        build_sources.append("Heavy build")
    if shipfu.is_in_special_build:
        build_sources.append("Special build")
    if build_sources:
        obtention_methods.append("Buildable in " + ", ".join(build_sources))

    # Drops
    drops = (db_models.session.query(db_models.ShipfuDrop)
                              .filter_by(shipfu_id=shipfu.shipfu_id)
                              .order_by(db_models.ShipfuDrop.world,
                                        db_models.ShipfuDrop.subworld).all())
    if drops:
        drop_msg = list()
        for drop in drops:
            drop_msg.append(f"{drop.world}-{drop.subworld}")
        drop_msg = "Droppable in " + ", ".join(drop_msg)
        obtention_methods.append(drop_msg)

    # Event
    if shipfu.is_event_ship:
        obtention_methods.append("Event")

    # Shop
    if shipfu.buyable_source:
        shop = (db_models.session.query(db_models.Shop)
                                 .filter_by(shop_id=shipfu.buyable_source)
                                 .first())
        obtention_methods.append(f"Buyable in {shop.name}")

    # Research shipfus
    if shipfu.rarity_id == 6 or shipfu.rarity_id == 7:
        obtention_methods.append("Research")
    return "\n".join(obtention_methods)
