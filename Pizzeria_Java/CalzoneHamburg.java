public class CalzoneHamburg extends Pizza{
   
    public CalzoneHamburg(){
        String[] zutaten = {"Mozarella","Schinken","Mushrooms", "oliven"};
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
