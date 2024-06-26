package ServerDelega;

import Coda.*;
import Dispatcher.IDispatcher;
import codaImpl.*;

public class DispatcherImpl implements IDispatcher {
    private CodaWrapper codaWrapper;


    public DispatcherImpl( int size){
        CodaCircolare coda = new CodaCircolare(size);
        codaWrapper = new CodaWrapperLock(coda);


    }

    @Override
    public void sendCmd(int cmd) {
        codaWrapper.inserisci(cmd);
    }

    @Override
    public int getCmd() {
        return codaWrapper.preleva();
    }
}
