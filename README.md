# Owocowy zbiór

Prototyp gry, w której gracz steruje koszykiem, aby łapać spadające owoce i unikać bomb. Gra staje się coraz trudniejsza w miarę zdobywania punktów.

## Instrukcje uruchomienia prototypu

1. **Wymagane biblioteki i wersja Pythona:**
    Upewnij się, że masz zainstalowanego Pythona w wersji 3.6 lub wyższej.
    Potrzebne biblioteki to:
   - pygame

     **Instalacja pygame**
     ```bash
     pip install pygame
     ```

3. **Uruchomienie gry:**
    ```bash
    python main.py
    ```

## Instrukcje użytkowania

### Sterowanie

- Strzałka w lewo: Przesuń koszyk w lewo.
- Strzałka w prawo: Przesuń koszyk w prawo.
- Spacja: Wstrzymaj/Wznow grę.

### Zasady gry

1. **Zbieranie owoców:** 
   - Gracz steruje niebieskim prostokątem, który musi łapać spadające czerwone owoce.
   - Za każdy złapany owoc gracz otrzymuje punkt.
   - Co 5 punktów zwiększany jest poziom:
    - przy wyniku podzielnym przez 5, zwiększana jest szansa na pojawienie się owoców i bomb, oraz zwiekszana jest ich prędkość spadania.
    - przy wyniku podzielnym przez 10 dodatkowo zwiekszana jest maksymalna liczba owoców i bomb na ekranie.
2. **Unikanie bomb:**
   - Gracz musi unikać spadających czarnych bomb.
   - Jeśli gracz dotknie bombę, gra kończy się.

3. **Życia:**
   - Gracz na start posiada 3 życia.
   - Każdy owoc który nie zostanie złapany, zmniejsza liczbę żyć o 1.
   - Jeśli liczba żyć spadnie do zera, gra się kończy.

Baw się dobrze!
