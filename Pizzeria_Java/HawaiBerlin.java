public class HawaiBerlin extends Pizza{
   
    public HawaiBerlin(){
        String[] zutaten = {"Mozarella","Schinken", "Ananas"};
        int Bewertung = 6;
        float preis = 7;
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
