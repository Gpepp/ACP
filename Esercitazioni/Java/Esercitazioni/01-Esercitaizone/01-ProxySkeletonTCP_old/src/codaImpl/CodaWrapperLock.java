package codaImpl;

import java.util.concurrent.locks.*;

import Coda.*;

public class CodaWrapperLock extends CodaWrapper {
    private Lock lock;
    private Condition empty;
    private Condition full;


    public CodaWrapperLock (Coda coda){
        super(coda);
        lock = new ReentrantLock();
        empty = lock.newCondition();
        full = lock.newCondition();

    }
    @Override
    public void inserisci(int i) {
        // TODO Auto-generated method stub
        lock.lock();
        try {
            while (coda.full() ) {
                try {
                    empty.await();
                } catch (InterruptedException e) {
                    e.printStackTrace();// TODO: handle exception
                }
            }

            coda.inserisci(i);
            full.signal();
        } finally {
            lock.unlock();
        }
    }
    @Override
    public int preleva() {
        // TODO Auto-generated method stub
        int el = 0;
        lock.lock();
        try {
            while (coda.empty()) {
                try {
                    full.await();
                } catch (InterruptedException e) {
                    e.printStackTrace();// TODO: handle exception
                }

            }

            el = coda.preleva();
            empty.signal();
            
        }finally{
            lock.unlock();
        }
        return el;
    }
}
