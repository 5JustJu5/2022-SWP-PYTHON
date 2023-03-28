import javax.print.event.PrintEvent;

public class SWDrucker implements Drucker {

    @Override
    public void druck(String content) {
        System.out.println("SchwarzWeiß: " + content);
    }
    
}
