# Historia wyników

| Data | Wynik | % | Braki | Link |
|------|-------|---|-------|------|
| 14.05.2026 | 8/10 | 80% | 8, 10 | [14.05.2026_results.md](14.05.2026_results.md) |
| 13.05.2026 | 9/10 | 90% | 9 | [13.05.2026_results.md](13.05.2026_results.md) |
| 12.05.2026 | 17/20 | 85% | 10, 13, 17 | [12.05.2026_results.md](12.05.2026_results.md) |
| 11.05.2026 | 15/20 | 75% | 6, 12, 14, 18 | [11.05.2026_results.md](11.05.2026_results.md) |
| 09.05.2026 | 17/20 | 85% | 9, 15, 16 | [09.05.2026_results.md](09.05.2026_results.md) |
| 08.05.2026 | 20/20 | 100% | brak | [08.05.2026_results.md](08.05.2026_results.md) |
| 07.05.2026 | 20/20 | 100% | brak | [07.05.2026_results.md](07.05.2026_results.md) |
| 05.05.2026 | 20/20 | 100% | brak | [05.05.2026_results.md](05.05.2026_results.md) |
| 29.04.2026 | 18/20 | 90% | 15 | [29.04.2026_results.md](29.04.2026_results.md) |
| 27.04.2026 | 17/20 | 85% | 13, 19 | [27.04.2026_results.md](27.04.2026_results.md) |
| 25.04.2026 | 19/20 | 95% | 5 | [25.04.2026_results.md](25.04.2026_results.md) |
| 24.04.2026 | 20/20 | 100% | brak | [24.04.2026_results.md](24.04.2026_results.md) |
| 21.04.2026 | 18/20 | 90% | 6 | [21.04.2026_results.md](21.04.2026_results.md) |
| 20.04.2026 | 19/20 | 95% | brak | [20.04.2026_results.md](20.04.2026_results.md) |
| 19.04.2026 | 20/20 | 100% | brak | [19.04.2026_results.md](19.04.2026_results.md) |

## Statystyki

- Najlepszy wynik: 20/20 (100%) — 19.04.2026, 24.04.2026, 05.05.2026, 07.05.2026, 08.05.2026
- Najgorszy wynik: 15/20 (75%) — 11.05.2026
- Średnia ze wszystkich prób: 91,33% (średnia procentowa z piętnastu quizów; quizy 13.05.2026 i 14.05.2026 mają po 10 pytań, pozostałe po 20)
- Ostatnie 5 wyników (malejąco po dacie): 14.05.2026 — 8/10 (80%); 13.05.2026 — 9/10 (90%); 12.05.2026 — 17/20 (85%); 11.05.2026 — 15/20 (75%); 09.05.2026 — 17/20 (85%)

## Najczęstsze obszary do poprawy

Na podstawie sekcji „Szczegóły błędów” we wszystkich plikach `*_results.md` (łącznie **23** zapisane pomyłki w **piętnastu** quizach). **Top 5 kategorii** według liczby błędów:

| Kategoria | Liczba błędów |
|-----------|----------------|
| [Architektura] | 3 |
| [ML] | 2 |
| [Inżynieria AI] | 2 |
| [Modele podstawowe] | 2 |
| [Rozmiar modelu] | 1 |

Pozostałe kategorie z dokładnie jednym błędem (remis o miejsca 4–5 w sensie częstości): [Alternatywy architektury], [Agregacja], [Aktywacje], [Badania], [Ewaluacja], [Ewaluacja kodu], [Feedback], [Generacja], [Kwantyzacja], [MoE], [Multimodalność], [Wnioskowanie].

## Notatki (z wcześniejszej wersji dashboardu)

W pierwszej zapisanej próbie (19.04.2026) nie było błędów; po dodaniu 20.04.2026 pojedynczy błąd w kategorii [Inżynieria AI] pozwala uzupełniać ranking powyżej na podstawie sekcji „Szczegóły błędów” w plikach `*_results.md`.

Quiz 21.04.2026 dodał błędy w [Agregacji] (brak poprawnej litery przy pytaniu o Salesforce) oraz w [Badaniach] (pomyłka 40% vs 18% z badania MIT). Sugerowane obszary dalszej nauki (z pełnego pokrycia quizów): [Badania] (rozdzielenie metryk czasu i jakości w badaniu MIT), [Agregacja] (liczby z Salesforce), [Inżynieria AI] (definicja „inżynieria ML” vs specyfika modeli podstawowych — błąd z 20.04), oraz utrwalenie [Modele językowe], [Tokenizacja], [LLM], [Samonadzorowanie], [Modele podstawowe], [Architektura], [Metodologia], [Branża i rynek], [Zastosowania], [Programowanie] wg kolejnych quizów.

Quiz 24.04.2026 (strony 1–54): wynik bez błędów; warto kontynuować materiał rozdziału 2 i utrwalać metryki opóźnień oraz planowanie produktu AI z notatek o stronach 51–54.

Quiz 29.04.2026 (notatki do str. 67): dwa błędy — brak odpowiedzi przy **pass@k** oraz pomyłka przy rozróżnieniu uzupełniania od konwersacji; przy sprawdzaniu skorygowano literówki w kluczu odpowiedzi dla pytań 11 i 19 tak, by zgadzały się z uzasadnieniami w pliku odpowiedzi (inżynieria promptów bez zmiany wag; start praktyki od warstwy aplikacji).

Quiz 05.05.2026 (notatki do str. 70): wynik 20/20; przed sprawdzeniem skorygowano pytanie 12 w kluczu (`docs/quiz/answers/05.05.2026_answers.md`) — „rosnące zapotrzebowanie na dane” to kolejność od najmniej do najbardziej kosztownej danymi ścieżki (prompting → dostrajanie → trening od zera), a nie odwrotna.

Quiz 07.05.2026 (notatki do str. 73): wynik 20/20; pełna zgodność odpowiedzi z kluczem i brak nowych kategorii błędów.

Quiz 08.05.2026 (notatki do str. 75): wynik 20/20; pełna zgodność odpowiedzi z kluczem, brak braków w tabeli `my_answers`.

Quiz 11.05.2026: wynik 15/20; cztery braki („X”) oraz jedna pomyłka przy definicji LMM vs model osadzania; warto utrwalić seq2seq/uwagę, prefill/dekodowanie, protokół ewaluacji benchmarków oraz kwantyzację względem treningu.

Quiz 12.05.2026: wynik 17/20; trzy braki („X”) przy pytaniach o **seq2seq**, **RWKV** oraz **liczbę parametrów MoE** — warto domknąć różnicę „jeden stan ukryty vs wielokrotna uwaga”, opis RWKV oraz różnicę między 56 mld a ~46,7 mld przy współdzieleniu wag ekspertów.

Quiz 13.05.2026: wynik 9/10; jeden brak („X”) przy **tokenach treningowych i epokach** — warto utrwalić, że liczba tokenów treningowych to rozmiar korpusu pomnożony przez liczbę epok, a nie sama wielkość zbioru ani liczba parametrów modelu.

Quiz 14.05.2026: wynik 8/10; dwa braki („X”) przy **wykorzystaniu sprzętu w szacunku kosztu treningu** oraz **wyborze mniejszego modelu w produkcji** — warto utrwalić rolę współczynnika wykorzystania w formule kosztowej oraz różnicę między optymalnością obliczeniową a kosztem inferencji.
