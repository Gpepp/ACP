import grpc
from concurrent import futures
import magazzino_pb2 as mag_msg
import magazzino_pb2_grpc as mag
from server_impl import Maagazzino


if __name__=='__main__':
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), options=(('grpc.so_reuseport',0),))
    mag.add_gestioneMagazzinoServicer_to_server(Maagazzino(), server)

    port = 0;
    port = server.add_insecure_port('[::]:' + str(port))
    print(f"server start on localhost:{port}")

    server.start()
    server.wait_for_termination()