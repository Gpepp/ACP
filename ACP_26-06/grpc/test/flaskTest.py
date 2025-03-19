import requests as rq


data = {"id": 1}

rq.post("http://localhost:8080/",data=data)