# Inżynieria AI — notatki kursowe

## Fundamenty inżynierii AI
Inżynieria AI koncentruje się na adaptowaniu modeli podstawowych do realnych problemów produktowych, a nie tylko na trenowaniu modeli od zera. Przełom wynika ze skali modeli oraz ich dostępności jako usługi, co obniża próg wejścia i skraca czas budowy pierwszych wersji aplikacji.

Kluczowa różnica względem klasycznego podejścia ML polega na przesunięciu środka ciężkości z budowy modelu na jego adaptację, ewaluację i integrację z produktem. Nadal obowiązują zasady inżynierskie: systematyczne eksperymenty, mierzalne cele, iteracyjne doskonalenie i kontrola kosztu.

## Model językowy i tokenizacja
Model językowy estymuje prawdopodobieństwo kolejnego elementu sekwencji na podstawie kontekstu. Jednostką operacyjną jest token, który może być znakiem, słowem lub częścią słowa. Tokenizacja wpływa bezpośrednio na koszt, opóźnienie i zdolność modelu do pracy z różnymi językami.

Dlaczego tokeny zamiast pełnych słów?
- pozwalają lepiej uchwycić strukturę słowotwórczą,
- redukują rozmiar słownika modelu,
- wspierają obsługę rzadkich i nowych słów.

Znaczniki początku i końca sekwencji są istotne, bo model musi wiedzieć, kiedy rozpocząć i zakończyć generację.

## Maskowane vs autoregresyjne modele językowe
Maskowane modele językowe przewidują brakujące elementy, korzystając z kontekstu po obu stronach luki. Sprawdzają się w zadaniach wymagających rozumienia całego kontekstu.

Autoregresyjne modele językowe przewidują kolejne tokeny tylko na bazie wcześniejszych elementów sekwencji. To one dominują w zastosowaniach generatywnych, ponieważ naturalnie wspierają generowanie krok po kroku.

Wniosek praktyczny: generowanie jest probabilistyczne, więc nawet poprawnie zaprojektowany system musi uwzględniać możliwość niespójności i halucynacji.

## Samonadzorowanie i skala
Samonadzorowanie umożliwia uczenie bez ręcznego etykietowania każdej próbki, bo etykiety są wyprowadzane z samych danych wejściowych. To kluczowy mechanizm, który pozwolił modelom językowym skalować się do poziomu LLM.

Konsekwencje:
- większe modele wymagają więcej danych i zasobów obliczeniowych,
- jakość danych bywa ważniejsza niż sama ich ilość,
- koszt i czas trenowania stają się strategicznym ograniczeniem.

## Od LLM do modeli podstawowych
Modele podstawowe obejmują zarówno duże modele językowe, jak i multimodalne. Model multimodalny przetwarza i łączy wiele typów danych, np. tekst i obraz.

To oznacza przejście od modeli pojedynczego zastosowania do modeli ogólnego przeznaczenia, które adaptuje się przez:
- inżynierię promptów,
- rozszerzanie kontekstu (np. RAG),
- dostrajanie.

## Najczęstsze wzorce zastosowań
Powtarzalne wzorce użycia obejmują:
- programowanie i wsparcie pracy deweloperskiej,
- generowanie i edycję treści wizualnych,
- tworzenie i redakcję tekstu,
- edukację i personalizację nauki,
- boty konwersacyjne,
- agregację informacji,
- organizowanie danych nieustrukturyzowanych,
- automatyzację procesów.

Wspólny mianownik: AI najczęściej zwiększa produktywność, ale wartość biznesowa zależy od jakości, niezawodności i dopasowania do konkretnego przepływu pracy.

## Planowanie aplikacji AI
Łatwo zbudować demo, trudniej dowieźć stabilny produkt. Dlatego planowanie zaczyna się od pytań:
- jakie ryzyko i jaka szansa biznesowa uzasadniają wdrożenie,
- czy budować samodzielnie, czy korzystać z gotowego rozwiązania,
- jaka rola AI jest krytyczna, a jaka uzupełniająca,
- gdzie konieczny jest człowiek w pętli decyzyjnej.

Praktyczny model dojrzewania automatyzacji:
- etap kontrolowany przez człowieka,
- etap częściowej autonomii w środowisku wewnętrznym,
- etap szerszej automatyzacji dla użytkowników końcowych.

## Kryteria sukcesu i metryki
Sama liczba odpowiedzi modelu nie wystarczy. Trzeba mierzyć jednocześnie:
- metryki jakości odpowiedzi,
- metryki opóźnień,
- metryki kosztu na zapytanie,
- metryki biznesowe i satysfakcję użytkowników.

Kluczowa pułapka: szybki postęp na początku projektu nie skaluje się liniowo do jakości produkcyjnej. Ostatnie procenty jakości zwykle kosztują najwięcej.

## Utrzymanie i ryzyko długoterminowe
Ekosystem AI zmienia się szybko: modele, ceny, interfejsy, regulacje i dostępność mocy obliczeniowej. Decyzje architektoniczne trzeba regularnie rewidować przez analizę kosztów i korzyści.

Ryzyka strategiczne:
- zależność od zewnętrznych dostawców,
- ryzyko zmian prawnych i regulacyjnych,
- kwestie własności intelektualnej,
- utrata przewagi, gdy dostawca modelu wchłonie funkcjonalność produktu.

## Trzy warstwy stosu AI
Każda aplikacja AI działa na trzech warstwach:
- projektowanie aplikacji,
- projektowanie modelu,
- infrastruktura.

W praktyce największa dynamika zmian dotyczy warstwy aplikacyjnej i adaptacji modelu, podczas gdy część infrastrukturalna ewoluuje wolniej, ale pozostaje krytyczna operacyjnie.

## Inżynieria AI a inżynieria ML
Najważniejsze różnice:
- częściej adaptujemy model, zamiast trenować od zera,
- większą wagę mają opóźnienie i koszt wnioskowania,
- ewaluacja jest trudniejsza przez otwarty charakter wyników.

Techniki adaptacji:
- bez zmiany wag: inżynieria promptów i kontekst,
- ze zmianą wag: dostrajanie.

Wiele aplikacji osiąga dobry efekt samą inżynierią promptów, ale wymagania wysokiej jakości, niskiego kosztu i specyficznych zachowań często prowadzą do dostrajania.

## Trenowanie, dostrajanie i post-trening
Wstępne trenowanie buduje bazowe kompetencje modelu i jest najbardziej zasobożerne. Dostrajanie kontynuuje uczenie na modelu już wytrenowanym. Post-trening to praktycznie ta sama klasa operacji co dostrajanie, zwykle realizowana przez twórcę modelu przed udostępnieniem.

Wniosek dla zespołów produktowych: warto precyzyjnie rozróżniać pojęcia, bo od nich zależą oczekiwania dotyczące danych, kosztu i czasu.

## Dane treningowe i ich jakość
Model jest tak dobry, jak dane, na których był uczony. Dane internetowe są skalowalne, ale zawierają szum, dezinformację i treści niskiej jakości. Heurystyki filtracji pomagają, lecz nie rozwiązują problemu całkowicie.

Najważniejsze obserwacje:
- nadmiar danych niskiej jakości może przegrywać z mniejszym zbiorem danych wysokiej jakości,
- rozkład danych determinuje zachowanie modelu,
- dane domenowe bywają kluczowe dla wysokiej jakości w specjalistycznych zastosowaniach.

## Wielojęzyczność i niedoreprezentowanie języków
Dominacja języka angielskiego w danych treningowych przekłada się na przewagę jakościową modeli w tym języku. Języki niedoreprezentowane mają zwykle gorsze wyniki, większy koszt i większe opóźnienia z powodu mniej efektywnej tokenizacji.

Tłumaczenie pośrednie do angielskiego nie zawsze rozwiązuje problem, bo może:
- tracić niuanse semantyczne i kulturowe,
- utrwalać błędy bezpieczeństwa i jakości,
- zwiększać koszt całego przepływu.

## Modele domenowe
Modele ogólnego przeznaczenia mają szeroki zakres, ale w zadaniach specjalistycznych często wygrywają modele trenowane lub dostrajane na danych domenowych.

Dane domenowe są trudne i kosztowne do pozyskania, jednak mogą radykalnie poprawić trafność w obszarach takich jak medycyna, biotechnologia czy zastosowania przemysłowe.

## Architektura transformer
Transformer zdominował modele podstawowe, bo rozwiązał kluczowe ograniczenia starszych podejść sekwencyjnych:
- lepiej modeluje zależności przez mechanizm uwagi,
- umożliwia równoległe przetwarzanie wejścia na etapie prefill.

Wciąż pozostaje ograniczenie autoregresyjnego dekodowania, które jest sekwencyjne i wpływa na latencję.

Mechanizm uwagi opiera się na wektorach zapytania, klucza i wartości. Model waży, które elementy kontekstu są istotne dla kolejnego tokenu. Wielogłowicowa uwaga pozwala równolegle modelować różne relacje w sekwencji.

Koszt pamięci i obliczeń rośnie wraz z długością kontekstu, ponieważ trzeba utrzymywać stany związane z kluczami i wartościami dla wielu tokenów.

## Dobre praktyki produktowe
- Startuj od prostszej ścieżki adaptacji i mierz efekt przed eskalacją złożoności.
- Traktuj ewaluację jako proces ciągły, nie jednorazowy test przed wdrożeniem.
- Projektuj interfejs i pętlę feedbacku równolegle z logiką modelu.
- Pilnuj relacji jakości do kosztu i czasu odpowiedzi, nie tylko surowej jakości.
- Buduj przewagę przez dane, integrację z procesem i dystrybucję, a nie samą warstwę modelową.

## Pytania kontrolne do samodzielnej weryfikacji
- Kiedy sama inżynieria promptów wystarcza, a kiedy konieczne jest dostrajanie?
- Jakie metryki jakości i opóźnienia są krytyczne dla Twojego przypadku użycia?
- Czy w Twoim produkcie AI pełni rolę krytyczną czy wspierającą?
- Jakie ryzyko regulacyjne i zależności od dostawcy modelu wpływają na strategię?
- Czy rozkład językowy i domenowy Twoich danych odpowiada realnym użytkownikom?
