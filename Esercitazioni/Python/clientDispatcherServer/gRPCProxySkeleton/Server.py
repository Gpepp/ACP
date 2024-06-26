from Skeleton import Skeleton
from SkeletonImpl import SkeletonImpl


if __name__=="__main__":

    impl = SkeletonImpl(5)
    sk = Skeleton(impl=impl, ip="localhost", port=50501)

    print("[SERVER] Start")
    sk.run()
