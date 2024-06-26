package Client;

import java.util.Random;

public class ClientThread extends Thread{
    private DispatcherProxy proxy;
    private static final int NUM_REQ = 3;


    public ClientThread(String _host, int _port){
        proxy = new DispatcherProxy(_host, _port);

    }
    @Override
    public void run() {
        // TODO Auto-generated method stub
        Random rand = new Random();

        for (int i = 0; i < NUM_REQ; i++) {
            int wait_time = rand.nextInt(3);
            try {
                Thread.sleep(wait_time * 1000);

            } catch (InterruptedException e) {
                // TODO: handle exception
                e.printStackTrace();
            }

            int command = rand.nextInt(4);
            System.out.println("[Client Thread] sendCommand: " + command);

            proxy.sendCmd(command);

        }
    }
}
