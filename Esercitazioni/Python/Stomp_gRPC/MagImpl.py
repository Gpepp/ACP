import magazzino_pb2 as srv_msg
import magazzino_pb2_grpc as srv


class Magazzino(srv.magazzinoServicer):
    def __init__(self, queue, prodLock, consLock):
        self.q = queue
        self.pLock = prodLock
        self.cLock = consLock

    def deposita(self, req, ctx):
        id = req.id
        prod = req.prod
        art = (id, prod)
        with self.pLock:
       		self.q.put(art)
        msg = srv_msg.msg_ack(ack="True")
        return msg

    def preleva(self, req, ctx):
        with self.cLock:
            art = self.q.get()
        msg = srv_msg.msg_articolo(id=art[0], prod=art[1])
        return msg

    def svuota(self, req, ctx):
        self.pLock.acquire()
        self.cLock.acquire()
        while self.q.empty():
            self.q.get()
        msg = srv_msg.msg_ack(ack="True")
        self.pLock.release()
        self.cLock.release()
        return msg
