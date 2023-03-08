public class QuattroBerlin extends Pizza{
   
    public QuattroBerlin(){
        String[] zutaten = {"Mozarella","diverserse Käse"};
        int Bewertung = 2;
        float preis = 5;
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
