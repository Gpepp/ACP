public class Produttore extends Thread{
    private Buffer buffer;

    public Produttore(Buffer buffer, String name) {
        super(name);
        this.buffer = buffer;
    }

    public void run(){
        buffer.produci();
    }
}
