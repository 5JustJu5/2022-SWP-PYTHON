public class FabrikBerlin extends Pizzeria{

    @Override
    public Pizza Fabrik(String art) {
        if(art.equals("Salami")){
            return new SalamiBerlin();
        }
        if(art.equals("Calzone")){
            return new CalzoneBerlin();
        }
        if(art.equals("Hawai")){
            return new HawaiBerlin();
        }
        if(art.equals("Quattro")){
            return new QuattroBerlin();
        }
        return null;
    }
    
}
