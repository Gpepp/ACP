package dispatcher;

import java.util.Hashtable;

import javax.jms.*;
import javax.naming.InitialContext;

public class dispatcher {
    public static void main(String[] args) {
        if (args.length != 1) {
            System.out.println("Insert a valid port");
            System.exit(-1);
        }

        Hashtable<String, String> properties = new Hashtable<String, String>();
        properties.put("java.naming.factory.initial","org.apache.activemq.jndi.ActiveMQInitialContextFactory");
        properties.put("java.naming.provider.url","tcp://127.0.0.1:61616");

        properties.put("queue.request", "request");
        properties.put("queue.response", "response");
        
        try {
            InitialContext ctx = new InitialContext(properties);
            QueueConnectionFactory queueConnectionFactory = (QueueConnectionFactory) ctx.lookup("QueueConnectionFactory");

            Queue request = (Queue) ctx.lookup("request");
            QueueConnection cQueueConnection = queueConnectionFactory.createQueueConnection();
            cQueueConnection.start();

            QueueSession qSession = cQueueConnection.createQueueSession(false, Session.AUTO_ACKNOWLEDGE);
            QueueReceiver qReceiver = qSession.createReceiver(request);

            int port = Integer.valueOf( args[1]);
            dispatcherListener listener = new dispatcherListener(cQueueConnection, port);

            qReceiver.setMessageListener(listener);
            



        } catch (Exception e) {
            // TODO: handle exception
        }

    }
}
