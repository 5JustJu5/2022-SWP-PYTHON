public class CalzoneBerlin extends Pizza{
   
    public CalzoneBerlin(){
        String[] zutaten = {"Mozarella","Schinken","Mushrooms"};
        int Bewertung = 4;
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
