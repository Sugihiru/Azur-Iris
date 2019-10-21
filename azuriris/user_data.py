import json


USER_DATA_FILENAME = "user_data.json"


class UserData():
    def __init__(self):
        try:
            with open(USER_DATA_FILENAME, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.set_default_data()

    def set_default_data(self):
        self.data = dict()
        self.data["shipfus"] = dict()
        self.data["pr"] = dict()
        self.data["shop_event"] = dict()

    def save(self):
        if self.data:
            with open(USER_DATA_FILENAME, 'w') as f:
                json.dump(self.data, f, sort_keys=True, indent=4)


def init_shipfu_data():
    """Default values for a shipfu in the user data file"""
    return {
        "owned": False,
        "mlb": False,
        "max_level": False,
        "max_affection": False
    }
