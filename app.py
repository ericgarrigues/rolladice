import json
from random import randrange
from flask import Flask

app = Flask(__name__)

@app.route('/<dice_max>')
def index(dice_max):

    try:
        dice_value = int(dice_max)
    except:
        return json.dumps({'error': 'dice value must be an integer'})
    else:
        return_value = randrange(1, dice_value + 1)

    return json.dumps({'value': return_value})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
