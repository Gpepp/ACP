package Client;

import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.net.UnknownHostException;

import Dispatcher.IDispatcher;

public class DispatcherProxy implements IDispatcher{
    private String addr;
    private int port;

    public DispatcherProxy(String _addr, int _port){
        addr = new String(_addr);
        port = _port;
    }
    
    @Override
    public int getCmd() {
        int el = 0;
        try {
            Socket s = new Socket(addr, port);
            DataInputStream dIN = new DataInputStream(s.getInputStream());
            DataOutputStream dOUT = new DataOutputStream(s.getOutputStream());

            dOUT.writeUTF("getCmd");
            el = dIN.readInt();
            System.out.println("[Proxy] Read getCmd: " + el);

            dOUT.close();
            dIN.close();
            s.close();

        } catch (UnknownHostException e) {
            e.printStackTrace();
        }catch (IOException e1){
            e1.printStackTrace();
        }
        return el;
    }


    @Override
    public void sendCmd(int cmd) {
        try {
            Socket s = new Socket(addr, port);
            DataInputStream dIN = new DataInputStream(new BufferedInputStream(s.getInputStream()));
            DataOutputStream dOUT = new DataOutputStream(new BufferedOutputStream(s.getOutputStream()));

            System.out.println("[Proxy] sendCommand " + cmd);
            dOUT.writeUTF("sendCmd");
            dOUT.writeInt(cmd);
            dOUT.flush();

            String respnse = dIN.readUTF();

            System.out.println("[Proxy] Response: " + respnse);

            dIN.close();
            dOUT.close();
            s.close();


        } catch (UnknownHostException e) {
            e.printStackTrace();
        } catch (IOException e1){
            e1.printStackTrace();
        }
        
    }
}
