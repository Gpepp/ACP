import socket
import sys
from Mag_Proxy import MagProxy as px

try:
    host = sys.argv[1].split(':')[0]
    port = int(sys.argv[1].split(':')[1])
except:
    print("err")
    sys.exit(-1)

proxy = px(host, port)

print("connesso")

# msg = '-'.join(['deposita-smartphone-10']).encode('utf-8')

# response = proxy.deposita('smartphone', 10)
response = proxy.deposita('laptop', 10)
# response = proxy.preleva('smartphone')

print(response)


