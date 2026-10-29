from flask import Flask

app = Flask(__name__)


@app.get("/")
def hello() -> str:
    return """
Hello, world!\n
1
"""


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
