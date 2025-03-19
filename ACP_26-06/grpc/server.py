import grpc, sys
import productM_pb2 as srv_msg
import productM_pb2_grpc as srv
from concurrent import futures
from productMangaer import ProductManager


if __name__ == "__main__":
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    srv.add_ProductManagerServicer_to_server(ProductManager(5), server)

    port = server.add_insecure_port('localhost:0')

    server.start()

    print(f"Server start at: localhost:{port}")

    server.wait_for_termination()