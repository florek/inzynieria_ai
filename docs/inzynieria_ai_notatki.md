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

### Post-trening — cele i typowy pipeline
Post-trening dotyczy modelu już wstępnie wytrenowanego. Samonadzorowane wstępne trenowanie optymalizuje głównie przewidywanie kolejnego tokenu, więc model zachowuje się jak uzupełniacz tekstu, a nie jak rozmówca — na pytanie może kontynuować zdanie pytaniem pomocniczym zamiast udzielić instrukcji. Drugi problem wynika z losowych danych internetowych: model może generować treści obraźliwe, stronnicze lub błędne.

Typowy pipeline produkcyjny obejmuje zwykle dwa etapy:
- dostrajanie nadzorowane na wysokiej jakości parach instrukcja–odpowiedź, by nauczyć formatu rozmowy i wykonywania zadań,
- dostrajanie preferencji, by odpowiedzi lepiej odpowiadały ludzkim oczekiwaniom — często przez uczenie przez wzmacnianie, np. RLHF, bezpośrednią optymalizację preferencji lub opinie modelu jako sędziego.

Wstępne trenowanie optymalizuje jakość na poziomie pojedynczego tokenu; użytkownikom zależy na jakości całej odpowiedzi — post-trening przesuwa optymalizację na poziom użytecznej, bezpiecznej odpowiedzi. Można to porównać do zdobywania wiedzy (pre-trening) versus umiejętności jej stosowania (post-trening).

Post-trening zużywa zwykle ułamek mocy obliczeniowej wstępnego treningu — w opisywanym przykładzie InstructGPT około dwa procent obliczeń poszło na post-trening i około dziewięćdziesięciu ośmiu na pre-trening, więc traktuje się go jako odblokowanie kompetencji już obecnych w modelu bazowym, trudnych do wyciągnięcia samymi promptami.

Termin „dostrajanie instrukcji” bywa niejednoznaczny: czasem oznacza wyłącznie SFT, czasem SFT razem z dostrajaniem preferencji — w notatkach rozdzielamy te etapy explicite.

Metafora „Shoggoth z uśmiechniętą maską” oddaje intuicję: surowy model wytrenowany na internecie jest trudny w użyciu, SFT cywilizuje zachowanie na lepszych danych dialogowych, a dostrajanie preferencji nakłada warstwę dopasowaną do użytkownika końcowego. Żaden z kroków nie jest obowiązkowy — każdy można pominąć w zależności od produktu.

### Dostrajanie nadzorowane — dane i koszt
Model po samym wstępnym treningu optymalizuje uzupełnianie tekstu, nie rozmowę: na pytanie może dodać kontekst, zadać pytanie pomocnicze albo — właściwie dla użytkownika — podać instrukcję. SFT pokazuje modelowi pary instrukcja–odpowiedź (dane demonstracyjne); to klonowanie zachowań: model naśladuje jakość i format odpowiedzi z przykładów.

Dane demonstracyjne muszą obejmować różne typy zadań (pytania, streszczenia, tłumaczenia itd.), bo różne prompty wymagają różnych stylów odpowiedzi. Etykietowanie bywa droższe niż proste etykiety obrazów: jedna para może zająć do około trzydziestu minut przy długim kontekście; przy koszcie rzędu dziesięciu dolarów za parę tysiące par to setki tysięcy dolarów samych etykiet, bez projektowania zadań, rekrutacji i kontroli jakości. Wysokiej klasy zespoły etykietujące często mają wykształcenie wyższe.

Źródła danych dialogowych obejmują m.in. wysokiej jakości korpusy Q&A, ręczne adnotacje oraz heurystyki filtrujące rozmowy z internetu (np. wykrywanie wzorca wymiany krótkich akapitów między rolami). Crowdsourcing na dużą skalę obniża koszt, lecz ryzykuje stronniczość: przy masowej mobilizacji wolontariuszy reprezentacja etykietujących może mocno odbiegać od populacji (np. dominacja jednej płci w ankiecie), co przekłada się na preferencje wbudowane w model. Zespoły coraz częściej sięgają po dane syntetyczne generowane przez AI, by ograniczyć zależność od drogich etykiet ludzkich.

Technicznie można trenować model od zera wyłącznie na danych demonstracyjnych i pominąć wstępny krok samonadzorowany, ale ścieżka z pre-treningiem zwykle daje lepsze wyniki przy porównywalnym budżecie.

### Dostrajanie preferencji — RLHF, DPO i model nagradzania
Dane demonstracyjne uczą formatu rozmowy, ale nie mówią, jakich treści unikać ani jak odpowiadać na kontrowersyjne tematy (aborcja, broń, polityka itd.), gdzie ludzie się nie zgadzają. Zbyt cenzura odstrasza użytkowników; brak guardrailów blokuje wdrożenie u klientów. Celem dostrajania preferencji jest dopasowanie do ludzkich oczekiwań — cel ambitny, bo zakłada możliwość ujednolicenia preferencji w modelu.

Najdłużej stosowany schemat to uczenie przez wzmacnianie z ludzką opinią (RLHF) w dwóch krokach: najpierw trenuje się model nagradzania, który ocenia parę prompt–odpowiedź, potem optymalizuje się model bazowy, by maksymalizować nagrodę. Nowsze metody, np. bezpośrednia optymalizacja preferencji (DPO), upraszczają pipeline — w nowszych wersjach rodzin modeli często rezygnuje się z pełnego RLHF na rzecz DPO ze względu na mniejszą złożoność operacyjną, choć RLHF bywa uznawane za bardziej elastyczne przy trudnych celach preferencji.

Dane do modelu nagradzania są trudne: ocena punktowa (niezależna skala dla każdej odpowiedzi) bywa niespójna między i wewnątrz etykietujących. Łatwiej poprosić o porównanie dwóch odpowiedzi na ten sam prompt i wskazać lepszą — powstają dane porównawcze (prompt, zwycięzca, przegrany). Nawet wtedy zbieżność z subiektywnymi preferencjami bywa niska.

Intensywniejsze treningi „wyrównania” preferencji mogą paradoksalnie pogorszyć zgodność z oczekiwanymi wartościami — większy model nie zawsze jest lepszy we wszystkich wymiarach produktowych.

### Wąskie gardła skalowania modeli
Wzrost rozmiaru modeli napędzał postęp, lecz pojawiają się twarde ograniczenia:
- dane treningowe — tempo wzrostu korpusów przewyższa tempo powstawania nowych danych ludzkich w internecie; treści publikowane online trafiają do przyszłych korpusów jak indeksowanie w wyszukiwarce, co umożliwia celowe zasilanie przyszłych modeli lub ataki przez zatrucie danych. Po wyczerpaniu danych publicznych przewaga przesuwa się na dane zastrzeżone (np. książki, kontrakty, dane medyczne). Restrykcje dostępu do źródeł internetowych mogą unieważniać dużą część popularnych korpusów oczyszczonych.
- energia — centra danych zużywają rosnący ułamek globalnej energii; bez tańszej produkcji energii skala centrów danych ma górny limit wzrostu, co podnosi koszty i ryzyko niedoborów.

Trenowanie kolejnych modeli na treściach generowanych przez AI komplikuje jakość — modele mogą uczyć się wzorców syntetycznych i stopniowo tracić kontakt z oryginalnym rozkładem danych ludzkich, choć efekt zależy od proporcji i filtrowania.

### Hiperparametry i ekstrapolacja skalowania
Parametr to wartość uczona w trakcie treningu (wagi). Hiperparametr ustawia człowiek: liczba warstw, wymiar modelu, rozmiar słownika, rozmiar batcha, liczba epok, współczynnik uczenia itd.

Przy wielkich modelach rzadko można wielokrotnie trenować pełną skalę tylko po to, by dobrać hiperparametry — stąd ekstrapolacja skalowania: trenuje się mniejsze warianty, obserwuje wpływ hiperparametrów i przenosi wnioski na docelowy rozmiar. Metoda działa częściowo, lecz jest trudna z powodu liczby hiperparametrów i ich interakcji oraz zdolności emergentnych, które ujawniają się dopiero w dużych modelach i mogą być niewidoczne na małych.

Zdolności emergentne to zachowania pojawiające się dopiero po przekroczeniu skali modelu lub danych, niewidoczne w mniejszych eksperymentach używanych do strojenia hiperparametrów.

## Agenty i automatyzacja
Agent to system planujący i wywołujący zewnętrzne narzędzia, by wykonać zadanie wykraczające poza samą generację tekstu w jednym kroku, np. wyszukanie numeru, wykonanie akcji w innym systemie, zapis w kalendarzu.

## Dane treningowe i ich jakość
Model jest tak dobry, jak dane, na których był uczony. Dane internetowe są skalowalne, ale zawierają szum, dezinformację i treści niskiej jakości. Heurystyki filtracji pomagają, lecz nie rozwiązują problemu całkowicie.

Popularne repozytoria typu Common Crawl i oczyszczone warianty, np. C4, są szeroko wykorzystywane przy wstępnym treningu wielu modeli podstawowych, mimo że zawierają m.in. clickbait, dezinformację i treści niskiej wiarygodności. Strategia „bierzemy to, co jest dostępne, zamiast tego, czego potrzebujemy” często daje modele silne na wzorcach obecnych w danych treningowych, lecz niekoniecznie na Twoim przypadku użycia.

Najważniejsze obserwacje:
- nadmiar danych niskiej jakości może przegrywać z mniejszym zbiorem danych wysokiej jakości,
- rozkład danych determinuje zachowanie modelu,
- dane domenowe bywają kluczowe dla wysokiej jakości w specjalistycznych zastosowaniach,
- większy model trenowany na zbyt małym lub zbyt wąskim zbiorze może działać gorzej niż mniejszy model na bogatszych danych.

## Wielojęzyczność i niedoreprezentowanie języków
Dominacja języka angielskiego w danych treningowych przekłada się na przewagę jakościową modeli w tym języku. Języki niedoreprezentowane mają zwykle gorsze wyniki, większy koszt i większe opóźnienia z powodu mniej efektywnej tokenizacji.

W popularnych korpusach internetowych angielski bywa wielokrotnie częstszy niż kolejne języki; dla języków słabo obecnych w danych treningowych relacja udziału w populacji światowej do udziału w korpusie powyżej jeden sygnalizuje niedobór danych. Niedoreprezentowanie nie wyjaśnia jednak wszystkich różnic jakościowych — struktura języka i kontekst kulturowy też wpływają na trudność uczenia.

Tłumaczenie pośrednie do angielskiego nie zawsze rozwiązuje problem, bo może:
- tracić niuanse semantyczne i kulturowe,
- utrwalać błędy bezpieczeństwa i jakości,
- zwiększać koszt całego przepływu,
- wymagać modelu, który i tak rozumie język źródłowy na tyle, by poprawnie go przetłumaczyć.

Ta sama treść w językach o gorszej efektywności tokenizacji może wymagać znacznie więcej tokenów niż w angielskim, co przy rozliczaniu API podnosi koszt i opóźnienie generacji. Zachowania bezpieczeństwa i jakości mogą różnić się między językami nawet przy tym samym modelu ogólnego przeznaczenia.

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

Architektura MoE dzieli parametry na wielu ekspertów i przy przetwarzaniu pojedynczego tokena aktywuje tylko część ekspertów, co zmienia relację między liczbą wszystkich wag w checkpointcie a kosztem pojedynczego kroku. W opisywanym przykładzie ośmiu ekspertów z rzędu 7 miliardów parametrów każdy daje naiwnie 56 miliardów parametrów przy braku współdzielenia, natomiast przy częściowym współdzieleniu wag łączna liczba parametrów wynosi około 46,7 miliarda w tej samej konfiguracji. Gdy na każdym kroku aktywni są tylko dwaj eksperci, efektywny koszt i prędkość wnioskowania bywają zbliżone do modelu gęstego o rząd 12,9 miliarda parametrów, mimo znacznie większej liczby wag w całym checkpointcie.

### Skala danych treningowych a epoki
Rozmiar zbioru danych dla modeli językowych sensowniej mierzyć liczbą tokenów niż liczbą „próbek”, bo jedna próbka może być zdaniem, stroną lub całą książką. Liczba tokenów w zbiorze danych nie jest tym samym co liczba tokenów treningowych: druga mnoży wielkość korpusu przez liczbę epok, czyli pełnych przejść przez dane podczas uczenia. Współczesne LLM bywają trenowane na korpusach liczących biliony tokenów, przy czym kolejne generacje rodzin modeli często korzystają z coraz większych zbiorów, o ile jakość i budżet obliczeniowy na to pozwalają.

### FLOP, wykorzystanie sprzętu i trzy liczby skali
Wymagania obliczeniowe wstępnego treningu opisuje się często liczbą operacji zmiennoprzecinkowych FLOP dla całego zadania, a nie samą liczbą maszyn GPU, CPU czy TPU, bo różne układy mają różną wydajność i koszt. FLOP/s oznacza operacje zmiennoprzecinkowe na sekundę, czyli maksymalną przepustowość sprzętu; angielska liczba mnoga FLOPs bywa mylona z FLOP/s, a niektórzy podają budżet w FLOP/s-day, gdzie jeden dzień to 86 400 sekund pracy przy jednej operacji na sekundę.

Pełne wykorzystanie deklarowanej wydajności przez cały trening jest mało prawdopodobne; wskaźnik wykorzystania mówi, jaka część szczytowej mocy faktycznie pracuje i zależy od modelu, obciążenia i sprzętu. Około połowy deklarowanej wydajności bywa już dobrym wynikiem, a powyżej około siedemdziesięciu procent uznaje się za bardzo dobre, choć nie zwalnia to z dalszej optymalizacji.

Skalę modelu w praktyce opisują trzy liczby: liczba parametrów jako pojemność uczenia, liczba tokenów, na których model był trenowany, jako miara tego, ile wiedzy wyciągnął ze danych, oraz liczba FLOP jako koszt obliczeniowy treningu. Większy model i większy korpus zwykle wymagają większej mocy obliczeniowej, a moc obliczeniowa kosztuje pieniądze, więc planowanie zaczyna się od budżetu, a nie od losowo dużego rozmiaru modelu i dopiero potem od szacunku rachunku.

### Prawo skalowania Chinchilli i skalowanie odwrotne
Przy ustalonym budżecie FLOP model optymalny obliczeniowo wynika z równoczesnego skalowania rozmiaru modelu i liczby tokenów treningowych; prawo skalowania Chinchilli, wyprowadzone na setkach modeli, sugeruje około dwudziestokrotnie więcej tokenów niż parametrów, więc model rzędu trzech miliardów parametrów potrzebuje rzędu sześćdziesięciu miliardów tokenów treningowych, a podwojenie parametrów powinno iść w parze z podwojeniem tokenów. Reguła zakłada głównie gęste modele trenowane na danych generowanych przez ludzi i niski koszt danych względem obliczeń; dostosowanie do modeli rzadkich, takich jak MoE, oraz do danych syntetycznych jest aktywnym obszarem badań.

Prawo skalowania optymalizuje jakość w ramach budżetu obliczeniowego, lecz w produkcji liczy się też użyteczność: mniejszy model może być tańszy i wygodniejszy w inferencji niż większy, bardziej wydajny na benchmarku, więc twórcy czasem świadomie rezygnują z maksymalnej wydajności obliczeniowej na rzecz adopcji. Koszt osiągnięcia danego poziomu jakości na benchmarkach bywa coraz niższy w czasie, ale podnoszenie jakości z wysokiego poziomu nadal jest drogie, podobnie jak ostatnie procenty jakości w produkcie.

Większy model nie zawsze jest lepszy we wszystkich wymiarach: intensywniejszy trening wyrównania preferencji może paradoksalnie pogorszyć zgodność z oczekiwanymi wartościami, a konkursy typu Inverse Scaling Prize szukały zadań, w których większe LLM radzą sobie gorzej, np. przy zapamiętywaniu lub silnych priorytetach w treści; część zgłoszeń pokazywała regresję na małym zbiorze testowym, ale nie utrzymywała się na danych rzeczywistych w skali wymaganej do najwyższych nagród.

### Alternatywy i konkurencja architektur
Choć transformer dominuje, pojawiały się wcześniej inne fale architektur, m.in. wokół AlexNet, seq2seq i GAN; transformer jest intensywnie optymalizowany od 2017 roku pod sprzęt masowo równoległy, więc konkurent musi nie tylko być lepszy jakościowo, lecz także sensowny ekonomicznie na realnym sprzęcie.

RWKV łączy motyw RNN z możliwością równoległości treningu; teoretycznie nie wymusza twardego limitu długości kontekstu jak klasyczny obraz transformera, lecz w praktyce bardzo długie sekwencje nadal bywają trudne jakościowo i obliczeniowo.

Modele przestrzeni stanów (SSM) i ich rozwinięcia, np. S4 i H3, celują w wydajniejsze modelowanie długich sekwencji; H3 łączy pamiętanie wcześniejszych tokenów z porównywaniem informacji między sekwencjami w sposób funkcjonalnie zbliżony do idei uwagi, lecz bardziej ekonomicznie w niektórych ustawieniach. Rozwinięcia takie jak Mamba skalują SSM do miliardów parametrów i w części zadań oferują inferencję o koszcie rosnącym liniowo względem długości sekwencji, podczas gdy klasyczna uwaga w transformatorze bywa kwadratowa względem długości kontekstu. Hybrydy łączące warstwy transformera z warstwami SSM, np. Jamba, dążą do większej skali i lepszej pracy z bardzo długim kontekstem (np. setki tysięcy tokenów) przy niższym narzucie pamięciowym niż czysty transformer o porównywalnej jakości; warianty MoE w tej rodzinie mogą mieć dziesiątki miliardów parametrów w checkpointcie przy aktywacji tylko części ekspertów na token.

Przy wstępnym treningu liczy się nie tylko liczba tokenów w korpusie, lecz liczba tokenów treningowych (korpus × epoki). Kolejne generacje popularnych rodzin modeli często trenuje się na coraz większych korpusach (np. od około jednego biliona tokenów do kilkunastu bilionów w nowszych wersjach), o ile budżet i jakość danych na to pozwalają. Spadek entropii krzyżowej z około 3,4 do 2,8 natów może wymagać około dziesięciokrotnie więcej danych — drobna zmiana metryki na benchmarku bywa kosztowna w skali treningu.

Ograniczenia dostępu do źródeł internetowych szybko unieważniają część popularnych korpusów oczyszczonych: znaczący odsetek kluczowych źródeł może stać się niedostępny dla kolejnych crawlów, co podnosi wagę umów na dane zastrzeżone i zmiany regulaminów platform.

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
