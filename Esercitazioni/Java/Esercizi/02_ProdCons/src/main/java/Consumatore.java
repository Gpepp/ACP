public class Consumatore extends Thread{
    Buffer b;

    public Consumatore(Buffer b, String nome) {
        super(nome);
        this.b = b;
    }
    @Override
    public void run(){
        b.consuma();
    }
}
