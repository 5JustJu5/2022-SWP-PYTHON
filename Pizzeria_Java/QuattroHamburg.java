public class QuattroHamburg extends Pizza{
   
    public QuattroHamburg(){
        String[] zutaten = {"Mozarella","diverserse Käse"};
        int Bewertung = 5;
        float preis = 8;
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
