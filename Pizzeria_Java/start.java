public class start{
    public static void main(String[] args){
        Pizzeria pHamburg = new FabrikHamburg();
        Pizzeria pBerlin = new FabrikBerlin();
        Pizza p = pHamburg.bestellung("Calzone");
        Pizza p2 = pBerlin.bestellung("Salami");

        


    }
}
