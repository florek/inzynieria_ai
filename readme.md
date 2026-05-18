# Repozytorium szkoleniowe — Inżynieria AI

W repozytorium znajduje się materiał do nauki z pozycji *Inżynieria AI. Tworzenie aplikacji z wykorzystaniem modeli bazowych* (Chip Huyen) w formie **HTML** (eksport z PDF; treść jest podzielona na sekcje z nagłówkami **Strona 1**, **Strona 2** itd.) oraz **ściągi i quizy** utrwalające treść kursu.

- **Notatki z kursu:** katalog `docs/` — spójne podsumowania wiedzy (bez odwołań do struktury plików w treści notatek).
- **Quiz:** `docs/quiz/` — pytania wyłącznie na podstawie notatek w `docs/` (bez katalogu `docs/quiz/` jako źródła treści merytorycznej przy generowaniu pytań).
- **Kod ćwiczeniowy:** katalog `src/` — zwięzłe przykłady ilustrujące pojęcia z notatek (np. etapy treningu), bez zastępowania pełnej treści książki.

Aktualny zakres notatek obejmuje m.in. **wstęp, rozdział 1 w całości oraz rozszerzony fragment rozdziału 2** opracowania w materiale źródłowym (paginacja jak w podglądzie **Strona N** w pliku HTML wygenerowanym z PDF), zsynchronizowany z eksporterem PDF do **linii 1615** w tym pliku HTML, tj. m.in. dane treningowe, wielojęzyczność, architekturę transformera i alternatywy, rozmiar modelu, MoE, FLOP i prawo skalowania Chinchilli, wąskie gardła skalowania (dane i energia), hiperparametry i ekstrapolację skalowania, post-trening (SFT, dane demonstracyjne, koszty etykietowania), dostrajanie preferencji (RLHF, DPO, model nagradzania, ocena punktowa vs porównawcza).
