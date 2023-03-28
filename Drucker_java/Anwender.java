public class Anwender {
    public static void main(String[] args) {
        ProxyDrucker printerProxy = new ProxyDrucker(true);
        //printerProxy.switchTo();
        printerProxy.druck("hello");
    }
}