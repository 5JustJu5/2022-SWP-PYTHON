public class Bildschirm1 implements Bildschirme {

   private KWetterstation konkretesSubjekt;

   public Bildschirm1(KWetterstation konkretesSubjekt) {
       this.konkretesSubjekt = konkretesSubjekt;
       
       // Durchführung der Registrierung beim übergebenen Subjekt
       this.konkretesSubjekt.addBeobachter(this);
   }
   
   @Override
   public void update() {
       int newState = konkretesSubjekt.getState();
       System.out.println(newState);
       // ...auf neuen Status reagieren
   }
}