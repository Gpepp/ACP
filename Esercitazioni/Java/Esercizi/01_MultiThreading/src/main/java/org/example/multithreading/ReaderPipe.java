package org.example.multithreading;

import java.io.DataInputStream;
import java.io.IOException;
import java.io.PipedInputStream;
import java.io.PipedOutputStream;

public class ReaderPipe extends Thread{
    private DataInputStream dataIN;

    public ReaderPipe(PipedOutputStream Dataout){
        try {
            dataIN = new DataInputStream(new PipedInputStream(Dataout));
        }catch (IOException e) {}
    }

    public void run() {
        while (true){
            System.out.println("READER wait");
            try {
                System.out.println("\n[READER] " + dataIN.readUTF());
            }catch (IOException e){}
        }
    }
}
