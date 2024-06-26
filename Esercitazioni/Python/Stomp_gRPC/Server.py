from MagImpl import Magazzino
import multiprocess as mp
import magazzino_pb2 as srv_msg
import magazzino_pb2_grpc as srv
import grpc, sys
from concurrent import futures


if __name__ == "__main__":

    print("Server Start")
    # Istanzio la coda
    q = mp.Queue(5)
    prodLock = mp.Lock()
    consLock = mp.Lock()

    # Istanzio il server gRPC
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    srv.add_magazzinoServicer_to_server(Magazzino(queue=q, prodLock=prodLock, consLock=consLock),server=server)
    port = server.add_insecure_port("0.0.0.0:0")
    print(f"host e port:  localhost:{port}")

    server.start()

    server.wait_for_termination()