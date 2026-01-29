package model;

public abstract class Rower {
    private int id;
    private String marka;
    private String model;
    private double cena;
    private String lokalizacja; 

    public Rower(int id, String marka, String model, double cena) {
        this.id = id;
        this.marka = marka;
        this.model = model;
        this.cena = cena;
        this.lokalizacja = "EKSPOZYCJA"; 
    }

    public int getId() { return id; }
    public String getMarka() { return marka; }
    public double getCena() { return cena; }
    public String getLokalizacja() { return lokalizacja; }

    public void setCena(double cena) {
        this.cena = cena;
    }

    public void setLokalizacja(String lokalizacja) {
        this.lokalizacja = lokalizacja;
    }

    public abstract String getDetale();

    @Override
    public String toString() {
        return "ID: " + id + " | " + marka + " " + model + 
               " | Cena: " + cena + " PLN | Lok: " + lokalizacja;
    }
}