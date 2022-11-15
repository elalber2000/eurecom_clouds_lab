from flask import Flask
import math
import numpy as np

app = Flask(__name__)


@app.route('/integral/<lower>/<upper>')
def integrate(lower, upper):
    N = 1000
    FUN =  lambda x : abs(math.sin(x))
    LOWER = float(lower)
    UPPER =  float(upper)
    xx = np.linspace(LOWER, UPPER, num=N)
    step = xx[1]-xx[0]

    sum = 0

    for i in xx:
        sum += (FUN(i) * step)

    return f"The integration is {sum}"

if __name__=="__main__":
    app.run()