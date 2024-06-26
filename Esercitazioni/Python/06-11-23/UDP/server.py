from skeleton import Skeleton
from implSkeleton import ImplSkeleton
import threading as mt
from consumerThread import ConsumerThread


if __name__ == "__main__":
    lcok = mt.Lock()
    cvCons = mt.Condition(lock=lcok)
    queue = []

    consumer = ConsumerThread(queue,lcok,cvCons)
    consumer.start()

    delegate = ImplSkeleton(queue=queue,lock= lcok, cvCons=cvCons)
    sk = Skeleton(delegate)
    sk.run()
