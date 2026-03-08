Online Sales Analysis - E-shop korpa sistem

## Opis projekta

Ovaj projekat implementira jednostavan e-shop sistem za upravljanje proizvodima i korisničkom korpom. Projekat koristi objektno-orijentisano programiranje (OOP) u Pythonu.

## Struktura projekta

online_sales_analysis/ ├── README.md ← Ovaj fajl ├── product.py ← Product klasa ├── product_manager.py ← ProductManager klasa ├── cart.py ← Cart klasa ├── main.py ← Glavni program ├── config.json ← Konfiguracija (ignorisano u Gitu) └── .gitignore ← Git ignore rules


## Klase i funkcionalnosti

### Product klasa (`product.py`)
- Predstavlja jedan proizvod u e-shopu
- Atributi: naziv, cena, količina, kategorija
- Funkcionalnost:
  - Prikaz informacija o proizvodu
  - Pristup atributima (naziv, cena, količina, kategorija)

### ProductManager klasa (`product_manager.py`)
- Upravlja kolekcijom proizvoda
- Funkcionalnost:
  - Dodavanje novi proizvodi
  - Prikaz svih proizvoda
  - Izračunavanje ukupne vrednosti zaliha
  - Pretraga proizvoda po nazivu

### Cart klasa (`cart.py`)
- Predstavlja korisničku korpu
- Funkcionalnost:
  - Dodavanje proizvoda u korpu sa količinom
  - Uklanjanje proizvoda iz korpe
  - Prikaz svih itema u korpi
  - Izračunavanje ukupne cene korpe
  - Provera da li je korpa prazna

### Glavni program (`main.py`)
- Demonstrira upotrebu svih klasa
- Funkcionalnost:
  - Kreiranje ProductManager instance
  - Dodavanje proizvodi (Laptop, miš, tastatura, monitor)
  - Prikaz svih proizvoda
  - Kreiranje korpe
  - Dodavanje itema u korpu
  - Izračunavanje ukupne cene korpe

## Korišćenje

### Prerequisites
- Python 3.6+
- Git (za verzionisanje)

### Instalacija i pokretanje

1. Klonirajte repozitorijum:
```bash
git clone [GITHUB_REPO_URL]
cd online_sales_analysis/online_sales_analysis
