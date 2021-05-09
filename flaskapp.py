from flask import Flask, request
import requests
import os
import time

app = Flask(__name__)

@app.route('/')
def home():
    country=request.args.get("c")
    path = "/home/CacheServer/countries/{}".format(country)
    if (p := requests.get("https://api.covid19api.com/total/dayone/country/{}".format(country))).ok:
        content = p.content.decode()
        count = 0
        while count < 6:
            if os.access(path, os.W_OK):
                with open(path, 'w') as f:
                    f.write(content)
                return content
            else:
                time.sleep(1)
                count += 1
    while True:
        if os.access(fnm, os.R_OK):
            with open(path, 'r') as f:
                return f.read(content)
        else:
            time.sleep(5)