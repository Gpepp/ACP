package org.example.multithreading;

import java.io.PipedOutputStream;

public class Main {
    public static void main(String[] args) {

        PipedOutputStream p = new PipedOutputStream();
        WriterPipe wr = new WriterPipe(p);
        ReaderPipe re = new ReaderPipe(p);

        re.start();
        wr.start();
    }
}