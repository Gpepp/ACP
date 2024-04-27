from Mag_Implement import MagImplement
import sys

if __name__ == "__main__":
    try:
        host = sys.argv[1]
    except:
        print('Insert valid host')
        sys.exit(-1)

    mag = MagImplement(host,0)
    mag.run_skeleton()
