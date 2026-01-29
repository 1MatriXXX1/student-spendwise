package logika;

import model.Rower;
import model.Pracownik;
import java.util.ArrayList;
import java.util.List;

public class Magazyn {
    private List<Rower> listaRowerow;
    private List<Pracownik> listaPracownikow;
    private List<String> listaSerwisowa; 

    public Magazyn() {
        this.listaRowerow = new ArrayList<>();
        this.listaPracownikow = new ArrayList<>();
        this.listaSerwisowa = new ArrayList<>();
    }

  
    public void dodajRower(Rower rower) {
        
        boolean istnieje = listaRowerow.stream().anyMatch(r -> r.getId() == rower.getId());
        if (istnieje) {
            System.out.println("BŁĄD: Rower o takim ID już istnieje!");
        } else {
            listaRowerow.add(rower);
            System.out.println("Dodano rower do systemu.");
        }
    }

    public boolean sprzedajRower(int id) {
        return listaRowerow.removeIf(r -> r.getId() == id);
    }

    public boolean zmienCene(int id, double nowaCena) {
        for (Rower r : listaRowerow) {
            if (r.getId() == id) {
                r.setCena(nowaCena);
                return true;
            }
        }
        return false;
    }

    public boolean przeniesDoMagazynu(int id) {
        for (Rower r : listaRowerow) {
            if (r.getId() == id) {
                r.setLokalizacja("MAGAZYN");
                return true;
            }
        }
        return false;
    }

    public void wyswietlWszystkie() {
        if (listaRowerow.isEmpty()) System.out.println("Brak rowerów.");
        else {
            System.out.println("\n--- LISTA ROWERÓW ---");
            listaRowerow.forEach(r -> System.out.println(r.getDetale()));
        }
    }

    public double pobierzWartoscMagazynu() {
        return listaRowerow.stream().mapToDouble(Rower::getCena).sum();
    }

   
    public void przyjmijDoSerwisu(String opis) {
        listaSerwisowa.add(opis);
        System.out.println("Przyjęto zgłoszenie serwisowe.");
    }

    public void wyswietlSerwis() {
        if (listaSerwisowa.isEmpty()) System.out.println("Brak rowerów w serwisie.");
        else {
            System.out.println("\n--- ROWERY W NAPRAWIE ---");
            for (int i = 0; i < listaSerwisowa.size(); i++) {
                System.out.println((i + 1) + ". " + listaSerwisowa.get(i));
            }
        }
    }

    
    public void dodajPracownika(Pracownik p) {
        listaPracownikow.add(p);
        System.out.println("Zatrudniono pracownika.");
    }

    public void wyswietlPracownikow() {
        if (listaPracownikow.isEmpty()) System.out.println("Brak pracowników.");
        else {
            System.out.println("\n--- PERSONEL ---");
            listaPracownikow.forEach(System.out::println);
        }
    }
}