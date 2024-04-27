from mag_impl import MagImpl

if __name__=="__main__":
    ip = 'localhost'
    port = 0

    test = MagImpl(ip,port,1024)
    test.super().run_skeleton()
    #MagImpl.run_skeleton(ip, port, 1024)
    print("hello")
