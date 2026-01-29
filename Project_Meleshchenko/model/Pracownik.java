package model;

public class Pracownik {
    private String imie;
    private String nazwisko;
    private String stanowisko;

    public Pracownik(String imie, String nazwisko, String stanowisko) {
        this.imie = imie;
        this.nazwisko = nazwisko;
        this.stanowisko = stanowisko;
    }

    @Override
    public String toString() {
        return stanowisko.toUpperCase() + ": " + imie + " " + nazwisko;
    }
}