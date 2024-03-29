from flask import Flask

app = Flask(__name__)



# @app.route('/')
# def hello_world():  # put application's code here
#     return '<h1>Hello World :)</h1>'
#
#
# @app.route('/greet')
# @app.route('/greet/<name>')
# def greet(name=""):
#     return f"Hello {name}"
#

def celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32


@app.route('/f/<float:celsius>')
def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = celsius_to_fahrenheit(celsius)
    return f'{fahrenheit:.2f}'


if __name__ == '__main__':
    app.run()
