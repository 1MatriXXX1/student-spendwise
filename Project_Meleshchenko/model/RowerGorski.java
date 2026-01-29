package model;

public class RowerGorski extends Rower {
    private int rozmiarKol;
    private String typZawieszenia;

    public RowerGorski(int id, String marka, String model, double cena, int rozmiarKol, String typZawieszenia) {
        super(id, marka, model, cena);
        this.rozmiarKol = rozmiarKol;
        this.typZawieszenia = typZawieszenia;
    }

    @Override
    public String getDetale() {
        return super.toString() + " | Koła: " + rozmiarKol + "\" | Typ: " + typZawieszenia;
    }
}