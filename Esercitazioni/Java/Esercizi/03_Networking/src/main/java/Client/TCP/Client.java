package Client.TCP;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;

public class Client {
    public static void main(String[] args) {
        try {
            Socket s = new Socket("127.0.0.1", 8050);
            System.out.println("Socket Creata");
            DataOutputStream toServer = new DataOutputStream(s.getOutputStream());
            DataInputStream fromServer = new DataInputStream(s.getInputStream());

            toServer.writeUTF("Hello Server");
            System.out.println("Messaggio inviato");
            String resp = fromServer.readUTF();
            System.out.println("Messaggio ricevuto: " + resp);
        }catch (IOException e){
            e.printStackTrace();
        }
    }
}
