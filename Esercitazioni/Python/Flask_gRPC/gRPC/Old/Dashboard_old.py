import grpc, sys

import statistics_pb2 as srv_msg
import statistics_pb2_grpc as srv


if __name__ == "__main__":
    try:
        port = sys.argv[1]
    except IndexError:
        print("Insert valid port")

    url = f"127.0.0.1:{port}"

    ch = grpc.insecure_channel(url)
    print("channel create")
    stub = srv.statisticsStub(ch)
    print("stub create create")

    sens = stub.getSensors(srv_msg.Empty())
    print("sens return create")

    for s in sens:
        print(s.id)

    # for s in sens:
    #     media = stub.getMean(srv_msg.MeanRequest(id=s.id))
    #     print(f"Media sensore {s.id}/{s.data_type}: {media.media}")