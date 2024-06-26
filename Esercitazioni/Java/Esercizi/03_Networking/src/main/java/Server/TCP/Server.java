package Server.TCP;

import java.io.IOException;
import java.net.*;

public class Server {
    public static void main(String[] args) {
        try{
            ServerSocket server = new ServerSocket(8050);

            while (true){
                Socket s = server.accept();
                System.out.println("Nuovo client connesso");

                Worker w = new Worker(s);
                w.start();
            }
        }catch (IOException e){
            e.printStackTrace();
        }
    }
}
