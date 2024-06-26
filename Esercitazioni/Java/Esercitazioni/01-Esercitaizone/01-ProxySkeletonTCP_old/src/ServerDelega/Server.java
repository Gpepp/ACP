package ServerDelega;

public class Server {
public static void main(String[] args) {
    System.out.println("Server start...");
    DispatcherImpl d = new DispatcherImpl( 5);
    DispatcherSkeleton sk = new DispatcherSkeleton(d, 5080);
    sk.run();
}
}
