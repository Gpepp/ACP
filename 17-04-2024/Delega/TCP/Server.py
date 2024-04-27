from Mag_Implement import MagImplement
from Mag_Skeleton import MagSkeleton

if __name__ == '__main__':
    
    mag = MagImplement(5)
    sk = MagSkeleton('localhost', 0, mag)
    sk.run()
    
