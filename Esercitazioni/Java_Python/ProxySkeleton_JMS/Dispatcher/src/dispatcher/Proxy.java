package dispatcher;


import java.io.*;
import java.net.Socket;

import javax.jms.*;

public class Proxy implements Idisptcher {

    private String addr;
    private int port;
    private QueueConnection qConnection;
    private Queue qResponse;

    public Proxy (String _addr, int _port, QueueConnection _qConn, Queue _queue){
        addr = _addr;
        port = _port;
        qConnection = _qConn;
        qResponse = _queue;
    }
    
    public void deposita(int id) {
        try {
            Socket s = new Socket(addr,port);
            System.out.println("[Proxy] socket start...");
            DataOutputStream dOUT = new DataOutputStream(s.getOutputStream());

            BufferedReader dIN = new BufferedReader(new InputStreamReader(s.getInputStream()));
            dOUT.writeUTF("deposita-"+String.valueOf(id));
            System.out.println("[Proxy] Deposit: " + id);

            String response = dIN.readLine();
            System.out.println("[Proxy] response = " + response);

            dOUT.close();
            dIN.close();
            s.close();

            QueueSession qSession = qConnection.createQueueSession(false, Session.AUTO_ACKNOWLEDGE);
            TextMessage msg = qSession.createTextMessage("Depositato resp: " + response);
            QueueSender qSender = qSession.createSender(qResponse);
            qSender.send(msg);
        } catch (Exception e) {
            e.printStackTrace();
            // TODO: handle exception
        }
    }
    
    public int preleva() {
        int el = -1;
        try {
            System.out.println("[Proxy] Socket start...");
            Socket s = new Socket(addr,port);
            DataOutputStream dOUT = new DataOutputStream(new BufferedOutputStream(s.getOutputStream()));
            BufferedReader dIN = new BufferedReader(new InputStreamReader(s.getInputStream()));

            dOUT.writeUTF("preleva");
            el = Integer.valueOf(dIN.readLine());

            dOUT.close();
            dIN.close();
            s.close();

            QueueSession qs = qConnection.createQueueSession(false, Session.AUTO_ACKNOWLEDGE);
            TextMessage tx = qs.createTextMessage("Prelevato: " + el);
            QueueSender qsend = qs.createSender(qResponse);
            qsend.send(tx);

        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }
        return el;
    }
}
