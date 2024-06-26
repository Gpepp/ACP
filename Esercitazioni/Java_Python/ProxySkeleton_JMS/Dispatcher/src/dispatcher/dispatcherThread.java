package dispatcher;

import javax.jms.Queue;
import javax.jms.QueueConnection;
import javax.jms.TextMessage;

public class dispatcherThread extends Thread {

    private int port;
    private QueueConnection qConnection;
    private TextMessage textMessage;


    public dispatcherThread(int _port, QueueConnection _QueueConnection, TextMessage _TextMessage){
        port = _port;
        qConnection = _QueueConnection;
        textMessage = _TextMessage;
    }
    @Override
    public void run() {
        try {
            String msg = textMessage.getText();
            Queue qResponse = (Queue) textMessage.getJMSReplyTo();

            Idisptcher disp = new Proxy(msg, port, qConnection, qResponse);
            if (msg.contains("deposita")) {
                String [] msg_split = msg.split("-");
                System.out.println("[Thread] deposita " + msg_split[1]);
                disp.deposita(Integer.valueOf(msg_split[1]));
            } else if (msg.equalsIgnoreCase("preleva")) {
                System.out.println("[Thread] Preleva");
                disp.preleva();
            } else {
                System.out.println("[Thread] Unknown command");
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
