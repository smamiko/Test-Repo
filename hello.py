import sys
from os import rename
import math

import requests

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = "Hej, {}".format(who_to_greet)
    return greeting


r = requests.get("https://asahi.com")
print(r.status_code)
