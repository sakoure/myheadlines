from flask import Flask

app = Flask(__name__)

@app.route("/")
def get_news():
  return "it is what it is"

if __name__ == '__main__':
  app.run(port=5000, debug=True)
