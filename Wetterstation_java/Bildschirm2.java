public class Bildschirm2 implements Bildschirme {

    private KWetterstation konkretesSubjekt;
 
    public Bildschirm2(KWetterstation konkretesSubjekt) {
        this.konkretesSubjekt = konkretesSubjekt;
        
        // Durchführung der Registrierung beim übergebenen Subjekt
        this.konkretesSubjekt.addBeobachter(this);
    }
    
    @Override
    public void update() {
        int newState = konkretesSubjekt.getState();
        
        System.out.println("hello");
        // ...auf neuen Status reagieren
    }

    public void interessant(){
        
    }
 }