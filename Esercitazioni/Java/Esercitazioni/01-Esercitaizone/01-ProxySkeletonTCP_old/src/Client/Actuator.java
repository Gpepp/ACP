package Client;

import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.PrintStream;

import Dispatcher.IDispatcher;


public class Actuator {
    public static void main(String[] args) {

        String host = "localhost";// args[0];
        int port = 5080; // Integer.valueOf(args[1]);

        System.out.println("[Actuator] Start... ");
        IDispatcher proxy = new DispatcherProxy(host, port);

        try{
            FileOutputStream file = new FileOutputStream("./out.txt");
            PrintStream outStream = new PrintStream(file);
            while (true) {
                System.out.println("[Actuator] getCmd ");
                int el = proxy.getCmd();
                System.out.println("[Actuato] cmd Response: " + el);
                outStream.println(el);

                Thread.sleep(1000);
            } 
        }catch (FileNotFoundException e) {
            e.printStackTrace();
        }catch (InterruptedException e1){
            e1.printStackTrace();
        }
    }
}
