from flask import Flask

app = Flask(__name__)

app.router.add_rule('/')
def index():
  return 'Mi Microservicio!'

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0', port=5000)
