import threading as mt
import requests, random
data_type = ["press", "temp"]

base_url = "http://127.0.0.1:8080/"

def run_th(id):
    type = data_type[id%2]
    sensor = {
            "_id": id,
            "data_type": type
            }
    response = requests.post(base_url+"sensor",json=sensor)
    print("respnse ->", response.json())

    for i in range(5):
        data = random.randint(1,50)
        sens_data = {
            "sensor_id": id,
            "data": data
        }
        response = requests.post(base_url+"data/"+type, json=sens_data)
        print("response ->", response.json())


if __name__ == "__main__":
    ths = []
    for i in range(5):
        th = mt.Thread(target=run_th, args=(i+1,))
        th.start()
        ths.append(th)

    for t in ths:
        t.join()
    
