public class FabrikHamburg extends Pizzeria {

    @Override
    public Pizza Fabrik(String art) {
        if(art.equals("Salami")){
            return new SalamiHamburg();
        }else if(art.equals("Calzone")){
            return new CalzoneHamburg();
        }
        if(art.equals("Hawai")){
            return new HawaiHamburg();
        }
        if(art.equals("Quattro")){
            return new QuattroHamburg();
        }
        return null;
    }
    
}
