package Server;

import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;

import Dispatcher.IDispatcher;

public class ServerThread extends Thread {
    private Socket s;
    private IDispatcher d;

    public ServerThread (Socket _sk, IDispatcher _d){
        s = _sk;
        d = _d;
    }

    @Override
    public void run() {
        System.out.println("[Dispatcher Thread] run Thread!!!");

        try {
            System.out.println("Sono nel try");
            DataInputStream dIN = new DataInputStream(new BufferedInputStream(s.getInputStream()));
            DataOutputStream dOUT = new DataOutputStream(new BufferedOutputStream(s.getOutputStream()));

            String method = dIN.readUTF();
            
            System.out.println("{{method ------ " + method + "}}");
            int x;
            if (method.compareTo("sendCmd") == 0){
                x = dIN.readInt();
                System.out.println("[Dispatcher Thread] method: " + method + "CMD: " + x);
                d.sendCmd(x);
                dOUT.writeUTF("ack");
            }else if (method.compareTo("getCmd")==0) {
                System.out.println("[Dispatcher Thread] method: " + method);
                x = d.getCmd();
                dOUT.writeInt(x);
            }else{
                System.out.println("[Dispatcher Thread] method unknown");
                dOUT.writeUTF("fail");
            }

            dOUT.flush();
            System.out.println();
            s.close();

        } catch (IOException e) {
            e.printStackTrace();
            // TODO: handle exception
        }
    }
}
