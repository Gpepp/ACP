import java.io.IOException;
import java.io.*;
public class main {
    public static void main(String[] args) {
        Buffer b = new Buffer();
        /*
        Produttore p = new Produttore(b, "produttore");
        Consumatore c = new Consumatore(b, "consumatore");

        p.start();
        c.start();*/
        BufferedReader stdin = new BufferedReader(new InputStreamReader(System.in));
        int choise=0; int id=1;
        while (choise!=9){
            System.out.print("0 (C)/1 (P): ");

            try{
                choise = Integer.parseInt(stdin.readLine());
            }catch (IOException e){
                e.printStackTrace();
            }
            if (choise==0){
                Consumatore c = new Consumatore(b, "Consumer_"+id);
                c.start();
            }
            if (choise == 1
            ) {
                Produttore p = new Produttore(b,"Produttore_"+id);
                p.start();
            }else{
                System.out.println("choise = " + choise);
            }
            id ++;
        }

    }
}
