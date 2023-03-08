public class SalamiBerlin extends Pizza{
   
    public SalamiBerlin(){
        String[] zutaten = {"Mozarella","scharfe Salami"};
        int Bewertung = 5;
        float preis = 9;
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
