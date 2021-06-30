import os
from itertools import cycle
from time import sleep

from flask import Flask, redirect, request, stream_with_context
from termcolor import colored

app = Flask(__name__)


@app.route("/")
def kekw():
    if not "curl" in request.headers["User-Agent"]:
        return redirect("https://github.com/seriousm4x/kekw-as-a-service")

    colors = cycle(["red", "green", "blue", "white",
                   "cyan", "magenta", "yellow"])

    def generate():
        while True:
            for file_ in os.listdir("frames"):
                with open(os.path.join("frames", file_), "r", encoding="utf-8") as f:
                    sleep(0.08)
                    yield "\033[2J\033[3J\033[H" + colored(f.read(), next(colors))

    return app.response_class(stream_with_context(generate()))


app.run(host="0.0.0.0", port=5000, debug=False)
