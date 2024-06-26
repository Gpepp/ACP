package Client;

public class Client {
    private static final int NUM_THREAD = 5;
    public static void main(String[] args) {
        
        String host = "localhost";// args[0];
        int port = 5080; // Integer.valueOf(args[1]);

        ClientThread ths[] = new ClientThread[NUM_THREAD];

        for (int i = 0; i < NUM_THREAD; i++) {
            ths[i] = new ClientThread(host, port);
            ths[i].start();
        }
    }
}
