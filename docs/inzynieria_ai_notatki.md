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

W modelowaniu języka kolejny token jest etykietą, a wcześniejsze tokeny kontekstem, więc z jednej sekwencji powstaje wiele próbek treningowych. Znaczniki początku i końca sekwencji są potrzebne, by model wiedział, gdzie zacząć i kiedy zakończyć generację w pracy z wieloma sekwencjami.

Samonadzorowanie różni się od uczenia bez nadzoru: w samonadzorowaniu etykiety są wnioskowane z wejścia, w uczeniu bez nadzoru etykiety nie są wymagane w ogóle.

Konsekwencje skali:
- większe modele wymagają więcej danych i zasobów obliczeniowych,
- jakość danych bywa ważniejsza niż sama ich ilość,
- koszt i czas trenowania stają się strategicznym ograniczeniem.

Próg „wielkości” LLM jest umowny i przesuwa się w czasie; rozmiar zwykle wyraża się liczbą parametrów. Większa pojemność uczenia się oznacza zwykle większy apetyt na dane, żeby realnie wykorzystać skalę zamiast marnować moc obliczeniową na przeuczenie małym zbiorem.

## Od LLM do modeli podstawowych
Modele podstawowe obejmują zarówno duże modele językowe, jak i multimodalne. Model multimodalny przetwarza i łączy wiele typów danych, np. tekst i obraz.

Duży model multimodalny (LMM) generuje kolejny token warunkowany nie tylko tekstem, lecz także innymi modalnościami obsługiwanymi przez model.

CLIP ilustruje inną klasę modelu: uczenie z parą obraz–tekst bez ręcznego etykietowania każdego obrazu, lecz CLIP jest modelem osadzania wspólnej przestrzeni znaczeń, a nie modelem generatywnym z otwartą odpowiedzią tekstową. Takie osadzanie bywa fundamentem późniejszych systemów generatywnych łączących modalności.

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

Przykładowe metryki opóźnień w generacji obejmują czas do pierwszego tokena oraz czas na pojedynczy token w trybie autoregresyjnym; akceptowalne wartości zależą od przypadku użycia i punktu odniesienia, np. obsługi ludzkiej.

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

Mówienie o „trenowaniu” modelu przez same prompty bywa nieprecyzyjne: jeśli nie zmieniasz wag, technicznie wykonujesz inżynierię promptów, nawet gdy behawioralnie „uczysz” model w potocznym sensie.

## Trenowanie, dostrajanie i post-trening
Wstępne trenowanie buduje bazowe kompetencje modelu i jest najbardziej zasobożerne. Dostrajanie kontynuuje uczenie na modelu już wytrenowanym. Post-trening to praktycznie ta sama klasa operacji co dostrajanie, zwykle realizowana przez twórcę modelu przed udostępnieniem.

Po wstępnym treningu model potrafi generować, lecz nie musi być wygodny ani bezpieczny w użyciu; etapy dopasowania do ludzkich preferencji i zachowań użytkowych realizuje się właśnie w obszarze post-treningu lub równoważnym dostrajaniu produkcyjnym.

Nie każda zmiana wag jest „trenowaniem” w sensie produktowym: np. kwantyzacja zmienia reprezentację wag, lecz nie jest tym samym co trening uczenia nadzorowanego w rozumieniu etapów modelu językowego.

Wniosek dla zespołów produktowych: warto precyzyjnie rozróżniać pojęcia, bo od nich zależą oczekiwania dotyczące danych, kosztu i czasu.

## Agenty i automatyzacja
Agent to system planujący i wywołujący zewnętrzne narzędzia, by wykonać zadanie wykraczające poza samą generację tekstu w jednym kroku, np. wyszukanie numeru, wykonanie akcji w innym systemie, zapis w kalendarzu.

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

### Seq2seq a transformer
Klasyczny seq2seq składa się z kodera i dekodera opartych na RNN; dekoder korzystał często tylko z ostatniego stanu ukrytego wejścia, co ograniczało jakość odwołań do pełnego kontekstu, a przetwarzanie było sekwencyjne i kosztowne dla długich wejść.

Transformer eliminuje RNN i pozwala równolegle przetworzyć tokeny wejściowe w fazie wstępnego uzupełniania, a uwaga rozdziela ważność wcześniejszych tokenów przy każdym kroku dekodowania.

### Prefill i dekodowanie
Wnioskowanie w modelu autoregresyjnym ma dwa szerokie etapy: wstępne uzupełnianie, gdzie wszystkie tokeny wejściowe są przetwarzane równolegle i powstają stany pośrednie z kluczami i wartościami dla kontekstu, oraz dekodowanie, gdzie kolejne tokeny wyjściowe powstają jeden po drugim.

### Blok transformera
Typowy blok łączy podmoduł uwagi oraz wielowarstwowy perceptron. Moduł uwagi używa zwykle czterech macierzy wag: zapytania, klucza, wartości i rzutu wyjściowego. MLP składa się z warstw liniowych rozdzielonych nieliniowością; pojedyncza warstwa liniowa wewnątrz bloku bywa nazywana warstwą ze sprzężeniem wyprzedzającym.

Typowe nieliniowości w LLM to m.in. ReLU i GELU; prostsze funkcje bywają preferowane, bo wprowadzają nieliniowość przy niskim koszcie obliczeń w porównaniu do bardziej złożonych aktywacji, które nie dają proporcjonalnej korzyści jakościowej.

### Osadzanie wejścia i wyjścia
Przed blokami transformera działa moduł osadzania tokenów oraz osadzania pozycyjnego; liczba indeksów pozycji wiąże się z maksymalnym kontekstem, choć istnieją metody wydłużania kontekstu bez liniowego zwiększania liczby indeksów pozycji.

Po blokach transformera warstwa wyjściowa mapuje stany ukryte na logity słownika; bywa nazywana warstwą odwrotnego osadzania lub „wierzchołkiem” modelu, bo jest ostatnia przed próbkowaniem.

### Rozmiar modelu a kontekst
Rozmiar modelu transformer zależy m.in. od wymiaru modelu, liczby bloków, wymiaru warstwy ze sprzężeniem wyprzedzającym i rozmiaru słownika. Wydłużenie okna kontekstu zwiększa zapotrzebowanie na pamięć w fazie wnioskowania, ale nie musi zwiększać całkowitej liczby parametrów w tej samej architekturze wag.

### Liczba parametrów, kolejne generacje i koszt pamięciowy
W obrębie jednej rodziny modeli większa liczba parametrów zwykle poprawia zdolność uczenia, ale porównania między generacjami pokazują, że nowszy mniejszy model może przewyższyć starszy znacznie większy na tym samym benchmarku, jeśli trening i dane są lepsze.

Do dolnego, orientacyjnego oszacowania pamięci potrzebnej na same wagi przy wnioskowaniu można pomnożyć liczbę parametrów przez liczbę bajtów na wagę; przykładowo rząd 7 miliardów parametrów przy reprezentacji 16-bitowej sugeruje co najmniej około 14 gigabajtów magazynu wag, przy czym w praktyce zużycie pamięci jest wyższe z powodu narzutu środowiska i dodatkowych buforów.

W modelach rzadkich duży ułamej wag o wartości zerowej zmniejsza efektywną liczbę parametrów, które trzeba realnie przechowywać i mnożyć, więc nominalnie większy, lecz mocno rzadki model może być tańszy obliczeniowo niż mniejszy model gęsty.

Architektura MoE dzieli parametry na wielu ekspertów i przy przetwarzaniu pojedynczego tokena aktywuje tylko część ekspertów, co zmienia relację między liczbą wszystkich wag w checkpointcie a kosztem pojedynczego kroku. W opisywanym przykładzie ośmiu ekspertów z rzędu 7 miliardów parametrów każdy daje naiwnie 56 miliardów parametrów przy braku współdzielenia, natomiast przy częściowym współdzieleniu wag łączna liczba parametrów wynosi około 46,7 miliarda w tej samej konfiguracji.

### Alternatywy i konkurencja architektur
Choć transformer dominuje, pojawiały się wcześniej inne fale architektur, m.in. wokół AlexNet, seq2seq i GAN; transformer jest intensywnie optymalizowany od 2017 roku pod sprzęt masowo równoległy, więc konkurent musi nie tylko być lepszy jakościowo, lecz także sensowny ekonomicznie na realnym sprzęcie.

RWKV łączy motyw RNN z możliwością równoległości treningu; teoretycznie nie wymusza twardego limitu długości kontekstu jak klasyczny obraz transformera, lecz w praktyce bardzo długie sekwencje nadal bywają trudne jakościowo i obliczeniowo.

Modele przestrzeni stanów (SSM) i ich rozwinięcia, np. S4 i H3, celują w wydajniejsze modelowanie długich sekwencji; H3 łączy pamiętanie wcześniejszych tokenów z porównywaniem informacji między sekwencjami w sposób funkcjonalnie zbliżony do idei uwagi, lecz bardziej ekonomicznie w niektórych ustawieniach.

### Ewaluacja a prompty
Porównywanie modeli wymaga kontroli nad protokołem ewaluacji: ta sama architektura scoringu może dać odwrócony ranking, jeśli modele dostaną inną liczbę przykładów w promptowaniu wielokrokowym albo inną strategię agregacji prób.

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
