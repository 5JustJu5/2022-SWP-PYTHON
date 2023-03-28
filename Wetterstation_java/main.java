public class main {
 
	public static void main(String[] args) {
		
		// Erzeugung des Subjektes
		KWetterstation konkretesSubjekt = new KWetterstation();
		
		// Erzeugung des Beobachters. Dabei wird
		// das Subjekt übergeben und registriert.
		Bildschirm1 konkreterBeobachter = new Bildschirm1(konkretesSubjekt);
				
		// Zustandsänderung, Subjekt benachrichtigt
		// daraufhin die Beobachter
		konkretesSubjekt.setState(4);
	}
}