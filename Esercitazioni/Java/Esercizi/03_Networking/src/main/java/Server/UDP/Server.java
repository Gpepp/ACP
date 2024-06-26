package Server.UDP;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;

public class Server {
    public static void main(String[] args) {

        try {
            byte[] data = new byte[65508];
            DatagramPacket pack = new DatagramPacket(data, data.length);

            DatagramSocket sock = new DatagramSocket(8050);

            System.out.println("Server start on port 8050");
            sock.receive(pack);

            String s = new String(pack.getData(), 0, pack.getLength());
            System.out.println("Stringa ricevuta: " + s);

            String resp = new String("OK contentu ricecevuto");
            DatagramPacket response = new DatagramPacket(resp.getBytes(), resp.getBytes().length, pack.getAddress(), pack.getPort());

            Thread.sleep(2000);
            System.out.println("Invio risposta");
            sock.send(response);
            System.out.println("Inviatao");


            sock.close();
        }catch (IOException e){
            e.printStackTrace();
        }catch (InterruptedException e){
            e.printStackTrace();
        }
    }
}
