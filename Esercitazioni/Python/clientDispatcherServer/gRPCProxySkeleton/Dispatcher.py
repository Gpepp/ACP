from SkeletonProxy import SkeletonProxy as skProxy
import client_pb2 as srv_msg
import client_pb2_grpc as srv
import grpc
from concurrent import futures


class DispatcherAct(srv.commandServicer):

    def __init__(self,proxy):
        self.px = proxy


    def deposita(self, rqst, ctx):
        print("deposita chiamata")
        req = rqst.id
        response = self.px.deposita(rqst)
        return srv_msg.msg_response(response="deposited")

    def preleva (self, rqst, ctx):
        print("preleva Chiamata")
        response = self.px.preleva()
        return srv_msg.msg_response(response=str(response))



if __name__ == "__main__":
    proxy = skProxy('localhost', 50501)
    server = grpc.server(futures.ThreadPoolExecutor(10))
    srv.add_commandServicer_to_server(DispatcherAct(proxy=proxy), server)
    port = server.add_insecure_port("0.0.0.0:0")
    print(f"Server port: localhost:{port}")
    server.start()
    server.wait_for_termination()
