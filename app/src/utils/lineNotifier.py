# -*- coding: utf-8 -*-

import requests
import getEnvValue as env


def lineNotifier(message):
    url = "https://notify-api.line.me/api/notify"
    token = env.get_token()
    headers = {"Authorization": "Bearer " + token}

    payload = {"message": message}

    r = requests.post(url, headers=headers, params=payload,)

    return r


def lineNotifierWithFiles(message, files):
    url = "https://notify-api.line.me/api/notify"
    token = env.get_token()
    headers = {"Authorization": "Bearer " + token}

    payload = {"message": message}

    r = requests.post(url, headers=headers, params=payload, file=files)

    return r
