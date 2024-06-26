import multiprocessing as mp
from SkeletonImpl import SkeletonImpl


if __name__ == "__main__":

    q = mp.Queue(5)
    server = SkeletonImpl(queue=q)
    server.run()

