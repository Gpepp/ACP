package Server.TCP;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;

public class Worker extends Thread{
    private Socket s;

    public Worker(Socket skt) {
        this.s = skt;
    }

    @Override
    public void run() {
        try {
            DataInputStream fromClient = new DataInputStream(s.getInputStream());
            DataOutputStream toClient = new DataOutputStream(s.getOutputStream());

            System.out.println("[SERVER-Worker]: Attesa dal client...");
            String dataFromClient = fromClient.readUTF();
            System.out.println("[SERVER-Worker]: Client -> " + dataFromClient);
            System.out.println("[SERVER-Worker]: Invio risposta");
            toClient.writeUTF("Ricevuto: " + dataFromClient);

            fromClient.close();
            toClient.close();
            s.close();

        }catch (IOException e){
            e.printStackTrace();
        }
    }
}
