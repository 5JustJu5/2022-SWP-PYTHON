public class SalamiHamburg extends Pizza{
   
    public SalamiHamburg(){
        String[] zutaten = {"Mozarella","Salami"};
        int Bewertung = 4;
        float preis = 10;
    }
    @Override
    public String backen() {
        return "wird gebackt";
    }

    @Override
    public String schneiden() {
        return "wird geschnitten";
    }

    @Override
    public String einpacken() {
        return "wird weggebracht";
    }
}
