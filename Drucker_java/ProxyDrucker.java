public class ProxyDrucker implements Drucker {
    
    private Drucker drucker;

    public ProxyDrucker(boolean color){

        if (color == true){
            drucker = new CDrucker();
        }else
        {
            drucker = new SWDrucker();
        }
    }

    public void switchTo(){
        if(this.drucker instanceof CDrucker){
            this.drucker = new SWDrucker();
        }else
        {
            this.drucker = new CDrucker();
        }
    }

    @Override
    public void druck(String content) {
        if(this.drucker instanceof CDrucker){
            this.drucker.druck(content);
        }else
        {
            this.drucker.druck(content);
        }
    }
    
}
