from Mag_Implement import MagImplement
import sys
import logging as log
log.basicConfig(filename='info.log',format='%(levelname)s - %(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

if __name__ == "__main__":
    try:
        host = sys.argv[1]
    except:
        print('Insert valid host')
        log.critical('[SERVER] Insert valid host')

        sys.exit(-1)

    mag = MagImplement(host,0)
    log.warning('[SERVER] MagImplement create')
    mag.run_skeleton()
