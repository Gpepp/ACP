package codaImpl;

import Coda.Coda;

public class CodaCircolare implements Coda{
    private int data[];

    private int size;
    private int elem;
    private int t;
    private int c;

    public CodaCircolare(int _size){
        size = _size;
        elem = t = c = 0;
        data = new int[size];
    }

    @Override
    public int getSize() {
        // TODO Auto-generated method stub
        return size;
    }
    @Override
    public boolean empty() {
        // TODO Auto-generated method stub
        return elem == 0;
    }
    @Override
    public boolean full() {
        // TODO Auto-generated method stub
        return elem == size;
    }

    @Override
    public void inserisci(int i) {
        data[t%size] = i;
        t++;
        elem++;
        System.out.println("Elemento inserito " + i);
    }

    @Override
    public int preleva() {
        int el;
        el = data[c%size];
        c++;
        elem--;
        System.out.println("Prelevato elem: " + el);
        return el;
    }
}
