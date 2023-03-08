public class HawaiHamburg extends Pizza{
   
    public  HawaiHamburg(){
        String[] zutaten = {"Mozarella","Schinken","Ananas"};
        int Bewertung = 2;
        float preis = 15;
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
