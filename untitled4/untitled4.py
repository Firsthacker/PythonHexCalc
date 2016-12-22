from flask import Flask
import jinja2       # for html templates
import os

app = Flask(__name__)

@app.route('/')
def index():
    return """
    <!doctype html>
    <html lang="en">
        <head>
            <meta charset="utf-8"/>
            <title>HexCalc</title>
        </head>

        <body>
            <h1>Hex to Dec converter</h1>

            <form method="post">
                <lable for="hexValue">Value:</label>
                <input name="hexValue" type="text" value=""><br>

                <input name="convert" type="submit" value="Convert"><br>
            </form>
	    <br>
        </body>
    </html>"""

@app.route('/page2')
def hello():
    return """
        <!doctype html>
        <html lang="en">
            <head>
                <meta charset="utf-8"/>
                <title>HexCalc Page2 =)</title>
            </head>

            <body>
                <h1>Hex to Dec converter Page2 =)</h1>

                <form method="post">
                    <lable for="hexValue">Value:</label>
                    <input name="hexValue" type="text" value=""><br>

                    <input name="convert" type="submit" value="Convert"><br>
                </form>
    	    <br>
            </body>
        </html>"""

if __name__ == '__main__':
    app.run()