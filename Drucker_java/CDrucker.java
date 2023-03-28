public class CDrucker implements Drucker {

    @Override
    public void druck(String content) {
            System.out.println("Farbiger Druck: " + content);
       
    }
    
}
