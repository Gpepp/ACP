from flask import Flask, request
import json


app = Flask(__name__)


@app.post('/')
def productManager():
    print(request.get_json())
    req = request.get_json()
    msg_req = []
    for v in req.values():
        msg_req.append(str(v))
    msg = '-'.join(msg_req)
    

    with open("./history.txt", mode="a") as file:
        file.write(msg+'\n')

    return request.get_json()


if __name__ == "__main__":
    app.run( port="8080", debug=True)