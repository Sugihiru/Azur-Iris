import os

import requests

API_BASE_URL = os.environ.get("AZURIRIS_API_BASE_URL")
API_BASE_URL = "http://localhost:5000"
APP_VERSION = "0.0.0"


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
