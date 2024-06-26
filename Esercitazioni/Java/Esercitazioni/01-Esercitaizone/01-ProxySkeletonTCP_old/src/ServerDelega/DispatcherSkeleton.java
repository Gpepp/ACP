package ServerDelega;

import java.io.IOException;
import java.net.*;

import Dispatcher.*;
import Server.ServerThread;
public class DispatcherSkeleton implements IDispatcher{
    private IDispatcher dispatcher;
    private int port;


    public DispatcherSkeleton( IDispatcher d, int p){
        dispatcher = d;
        port = p;
    }

    public void run(){
        try {
            ServerSocket server = new ServerSocket(port);
            System.out.println("[Dispatcher] Server start...");
            while (true) {
                Socket s = server.accept();
                ServerThread th = new ServerThread(s, this);
                th.start();
            }
        } catch (IOException e) {
            // TODO: handle exception
            e.printStackTrace();
        }
    }

    public void sendCmd (int cmd){
        dispatcher.sendCmd(cmd);
    }
    @Override
    public int getCmd() {
        // TODO Auto-generated method stub
        return dispatcher.getCmd();
    }
}
