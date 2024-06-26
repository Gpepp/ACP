package org.example.multithreading;

import java.io.*;

public class WriterPipe extends Thread {
    private final DataOutputStream dataOut;


    public WriterPipe (PipedOutputStream pipeOut){
        dataOut = new DataOutputStream( pipeOut );
    }
    @Override
    public void run(){
        BufferedReader keyboardBuffer = new BufferedReader(new InputStreamReader(System.in));
        String s;
        while (true){
            try {
                System.out.print("[Writer] Inserire un nuovo testso: ");

                s = keyboardBuffer.readLine();
                System.out.println(s);
                dataOut.writeUTF(s);
            }catch (IOException e){
                e.printStackTrace();
            }
        }
    }
}
