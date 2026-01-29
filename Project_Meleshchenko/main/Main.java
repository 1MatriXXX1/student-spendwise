package main;

import logika.Magazyn;
import model.RowerGorski;
import model.Pracownik;
import java.util.Scanner;
import java.util.InputMismatchException;

public class Main {
    public static void main(String[] args) {
        Magazyn sklep = new Magazyn();
        Scanner skaner = new Scanner(System.in);
        boolean czyDziala = true;

       
        sklep.dodajPracownika(new Pracownik("Jan", "Kowalski", "Sprzedawca"));
        sklep.dodajRower(new RowerGorski(1, "Kross", "Level 1", 1999.00, 29, "Hardtail"));

        while (czyDziala) {
            System.out.println("\n========================================");
            System.out.println("   SYSTEM SALONU ROWERÓW GÓRSKICH");
            System.out.println("========================================");
            System.out.println("1. Wyświetl listę rowerów");
            System.out.println("2. Dodaj nowy rower");
            System.out.println("3. Sprzedaj rower (usuń z bazy)");
            System.out.println("4. Zmień cenę roweru");
            System.out.println("5. Przenieś rower do magazynu (z ekspozycji)");
            System.out.println("6. SERWIS: Przyjmij rower do naprawy");
            System.out.println("7. SERWIS: Lista napraw");
            System.out.println("8. KADRY: Dodaj pracownika");
            System.out.println("9. KADRY: Lista pracowników");
            System.out.println("10. Raport finansowy (wartość towaru)");
            System.out.println("0. Wyjdź");
            System.out.print("Wybierz opcję: ");

            try {
                int opcja = skaner.nextInt();
                skaner.nextLine(); 

                switch (opcja) {
                    case 1:
                        sklep.wyswietlWszystkie();
                        break;
                    case 2:
                        System.out.print("Podaj ID: ");
                        int id = skaner.nextInt();
                        skaner.nextLine();
                        System.out.print("Podaj Markę: ");
                        String marka = skaner.nextLine();
                        System.out.print("Podaj Model: ");
                        String model = skaner.nextLine();
                        System.out.print("Podaj Cenę (np. 2500,00): ");
                        double cena = skaner.nextDouble();
                        System.out.print("Rozmiar kół (cal): ");
                        int kola = skaner.nextInt();
                        skaner.nextLine();
                        System.out.print("Typ zawieszenia: ");
                        String typ = skaner.nextLine();
                        sklep.dodajRower(new RowerGorski(id, marka, model, cena, kola, typ));
                        break;
                    case 3:
                        System.out.print("Podaj ID sprzedawanego roweru: ");
                        int idSprzedaz = skaner.nextInt();
                        if (sklep.sprzedajRower(idSprzedaz)) System.out.println("Sprzedano pomyślnie.");
                        else System.out.println("Nie znaleziono takiego ID.");
                        break;
                    case 4:
                        System.out.print("Podaj ID roweru do zmiany ceny: ");
                        int idCena = skaner.nextInt();
                        System.out.print("Podaj nową cenę: ");
                        double nowaCena = skaner.nextDouble();
                        if (sklep.zmienCene(idCena, nowaCena)) System.out.println("Cena zaktualizowana.");
                        else System.out.println("Błąd: Nie ma roweru o takim ID.");
                        break;
                    case 5:
                        System.out.print("Podaj ID roweru do przeniesienia na zaplecze: ");
                        int idMag = skaner.nextInt();
                        if (sklep.przeniesDoMagazynu(idMag)) System.out.println("Status zmieniony na MAGAZYN.");
                        else System.out.println("Nie znaleziono roweru.");
                        break;
                    case 6:
                        System.out.print("Opis usterki/modelu (np. Giant - pęknięta rama): ");
                        String usterka = skaner.nextLine();
                        sklep.przyjmijDoSerwisu(usterka);
                        break;
                    case 7:
                        sklep.wyswietlSerwis();
                        break;
                    case 8:
                        System.out.print("Imię: ");
                        String imie = skaner.next();
                        System.out.print("Nazwisko: ");
                        String nazwisko = skaner.next();
                        System.out.print("Stanowisko: ");
                        String stanowisko = skaner.next();
                        sklep.dodajPracownika(new Pracownik(imie, nazwisko, stanowisko));
                        break;
                    case 9:
                        sklep.wyswietlPracownikow();
                        break;
                    case 10:
                        System.out.printf("Łączna wartość magazynu: %.2f PLN%n", sklep.pobierzWartoscMagazynu());
                        break;
                    case 0:
                        czyDziala = false;
                        System.out.println("Zamykanie systemu...");
                        break;
                    default:
                        System.out.println("Nieznana opcja.");
                }
            } catch (InputMismatchException e) {
                System.out.println("Błąd: Wprowadzono niepoprawne dane (np. literę zamiast liczby). Spróbuj ponownie.");
                skaner.nextLine(); 
            }
        }
        skaner.close();
    }
}