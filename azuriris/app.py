import os

import requests

from data import Data
import db_models

API_BASE_URL = os.environ.get("AZURIRIS_API_BASE_URL")
API_BASE_URL = "http://localhost:5000"
APP_VERSION = "0.0.0"


def get_server_data_version():
    res = requests.get(API_BASE_URL + "/get_data_version")
    if res.status_code == 200:
        return res.text
    return None


def check_and_update_data():
    """
    Checks the current data version and compare it with the server version
    If there's a version mismatch, update the data file
    """
    version = Data.getVersion()
    if not version:  # Data file does not exist
        res = requests.get(API_BASE_URL + "/get_data")
        if res.status_code == 200:
            with open("azuriris.data", "wb+") as f:
                f.write(res.content)
        return

    server_data_version = get_server_data_version()
    if not server_data_version:  # Unable to retrieve server's version
        return

    if server_data_version != version:
        res = requests.get(API_BASE_URL + "/get_data")
        if res.status_code == 200:
            # In case user interrupts the program here, write to another file
            # instead of overwriting directly the data file
            with open("azuriris.data.new", "wb+") as f:
                f.write(res.content)
            if os.path.isfile("azuriris.data"):
                db_models.session.close()
                os.remove("azuriris.data")
                print("remove")
                os.rename("azuriris.data.new", "azuriris.data")


def get_update_url():
    res = requests.get(API_BASE_URL + "/get_installer_url")
    if res.status_code == 200:
        return res.text
    return None


def check_app_version():
    ret = dict()

    res = requests.get(API_BASE_URL + "/get_app_version")
    if res.status_code == 200:
        if res.text != APP_VERSION:
            ret["error"] = False
            ret["up_to_date"] = False
            ret["update_url"] = get_update_url()
        else:
            ret["error"] = False
            ret["up_to_date"] = True
    else:
        ret["error"] = True
        ret["status_code"] = res.status_code
    return ret
