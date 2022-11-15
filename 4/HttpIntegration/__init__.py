import logging
import azure.functions as func

import math


#Code from numpy
def linspace(start, stop, num=50, endpoint=True):
    num = int(num)
    start = start * 1.
    stop = stop * 1.

    if num == 1:
        yield stop
        return
    if endpoint:
        step = (stop - start) / (num - 1)
    else:
        step = (stop - start) / num

    for i in range(num):
        yield start + step * i


def linspace(start, stop, num=50, endpoint=True):
    num = int(num)
    start = start * 1.
    stop = stop * 1.

    if num == 1:
        yield stop
        return
    if endpoint:
        step = (stop - start) / (num - 1)
    else:
        step = (stop - start) / num

    for i in range(num):
        yield start + step * i

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    nums = req.params.get('nums')
    if not nums:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            nums = req_body.get('nums')

    if nums:
        N = 1000
        FUN =  lambda x : abs(math.sin(x))
        LOWER = float(nums.split('/')[0])
        UPPER =  float(nums.split('/')[1])
        xx = list(linspace(LOWER, UPPER, num=N))
        step = xx[1]-xx[0]

        sum = 0

        for i in xx:
            sum += (FUN(i) * step)

        return func.HttpResponse(f"Hello, {sum}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )