package Client.UDP;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;

public class Client {
    public static void main(String[] args) {
        try{
            String s = new String("Stringa da inviare");

            DatagramSocket sock = new DatagramSocket();
            DatagramPacket pack = new DatagramPacket(s.getBytes(), s.getBytes().length, InetAddress.getLocalHost(), 8050);
            System.out.println("Invio pacchetto");
            sock.send(pack);
            System.out.println("PacchettoInviato");

            byte[] data = new byte[65508];
            DatagramPacket response = new DatagramPacket(data, data.length);
            sock.receive(response);

            s = new String(response.getData(), 0, response.getLength());
            System.out.println("Server Response: " + s);

            sock.close();
        }catch (IOException e){
            e.printStackTrace();
        }
    }
}
