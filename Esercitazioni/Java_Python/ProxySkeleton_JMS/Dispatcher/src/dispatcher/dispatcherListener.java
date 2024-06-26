package dispatcher;



import javax.jms.Message;
import javax.jms.MessageListener;
import javax.jms.QueueConnection;
import javax.jms.TextMessage;

public class dispatcherListener implements MessageListener{

    private QueueConnection qConnection;
    private int port;

    public dispatcherListener(QueueConnection _QueueConnection, int _port){
        qConnection = _QueueConnection;
        port = _port;
    }


    
    public void onMessage(Message arg0) {
        // TODO Auto-generated method stub
        TextMessage msg = (TextMessage) arg0;

        dispatcherThread th = new dispatcherThread(port, qConnection, msg);
        th.start();
        
    }
}
