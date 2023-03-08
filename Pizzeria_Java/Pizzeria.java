public abstract class Pizzeria{

    public Pizza bestellung(String art){
        Pizza Pizza = Fabrik(art);
        System.out.println(Pizza.backen());
        System.out.println(Pizza.schneiden());
        System.out.println(Pizza.einpacken());
        Pizza.backen();
        Pizza.schneiden();
        return Pizza;
        
    }

    public abstract Pizza Fabrik(String art);
}