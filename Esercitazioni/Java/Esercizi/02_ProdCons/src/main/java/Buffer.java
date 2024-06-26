import sun.lwawt.macosx.CSystemTray;

import java.io.IOException;

public class Buffer {
    private long content;
    private boolean full;

    public Buffer (){
        content = 0;
        full = false;
    }

    public synchronized void produci (){
        System.out.println(Thread.currentThread().getName() + " Invocazione Produzione");

        while (full){
            System.out.println(Thread.currentThread().getName() + " In attesa che ci sia posto nel buffer");
            try {
                wait();
            }catch (InterruptedException e){
                e.printStackTrace();
            }

        }

        content = System.currentTimeMillis();
        System.out.println("prodotto: " + content);
        full = true;
        notifyAll();
    }

    public synchronized void consuma(){
        System.out.println(Thread.currentThread().getName() + " Consuma");
        while (!full){
            System.out.println(Thread.currentThread().getName() + "Attesa che venga prodotto");
            try {
                wait();
            }catch (InterruptedException e){
                e.printStackTrace();
            }
        }
        System.out.println(Thread.currentThread().getName() + " Elemento consumato: " + content);
        full = false;
        notifyAll();
    }
}
