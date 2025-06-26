from flask import Flask
import datetime
import random
import time


app = Flask(__name__)
def build_response(title="",description="",image=""):
    return f"""<head>
    <title>{title}</title>
    <meta name="description" content="{description}">
    <meta property="og:image" content="{image}">
    </head>
    <body>
    <h1>{title}</h1>
    <p>{description}</p>
    </body>"""

@app.route('/')
def index():
    helptext="""
    note: one response per input so certain operations require random text to change outputs 
    add: http://<domain>/add/<number>/<number>
    multiply: http://<domain>/multiply/<number>/<number>
    8ball: http://<domain>/multiply/8ball/<random text>

    """
    return build_response(title="Commands:",description=helptext)

@app.route('/add/<num1>/<num2>')
def add(num1,num2):
   return build_response(title=str(float(num1)+float(num2)))

@app.route('/multiply/<num1>/<num2>')
def multiply(num1,num2):
    return build_response(title=str(float(num1)*float(num2)))
@app.route('/8ball/<rand>') 
def eightball(rand):
    answer_list=['It is certain.', 
             'It is decidedly so.', 
             'Without a doubt.',
             'Yes definitely.', 
             'You may rely on it.', 
             'As I see it, yes.',
             'Most likely.',
             'Outlook good.', 
             'Yes.', 
             'Signs point to yes.',
             'Reply hazy, try again.', 
             'Ask again later.', 
             'Better not tell you now.',
             'Cannot predict now.', 
             'Concentrate and ask again.',
             "Don't count on it.", 
             'My reply is no.', 
             'My sources say no.', 
             'Outlook not so good.',
             'Very doubtful.']

    response=random.choice(answer_list)
    descr=f"generated on {time.strftime('%Y-%m-%d %H:%M:%S')}, add randomness to the end of the url to generate a new response"
    return build_response(title=response,description=descr )


if __name__ == '__main__':
   app.run(host="0.0.0.0",port=8080)

