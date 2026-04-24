# Inżynieria AI — notatki (strony 1–54)

## Kontekst i cel materiału

Materiał wyjaśnia, dlaczego budowa aplikacji na modelach podstawowych stała się masową dyscypliną inżynierską: rosnąca skala modeli, model jako usługa oraz niższy próg wejścia dla twórców aplikacji. Podkreśla też ciągłość z dobrymi praktykami klasycznego uczenia maszynowego: systematyczne eksperymenty, rygorystyczna ocena i ciągła optymalizacja kosztów oraz opóźnień.

## Skala i „model jako usługa”

Po roku 2020 pojęcie **skali** jest centralne: duże modele zużywają znaczące zasoby energii, a do treningu brakuje już wprost publicznie dostępnych danych z internetu. Trening dużych modeli językowych wymaga danych, mocy obliczeniowej i ekspertyzy dostępnej tylko niewielu organizacjom, co prowadzi do **modelu jako usługi**: gotowe modele są udostępniane innym podmiotom bez konieczności samodzielnego budowania ich od zera. W efekcie popyt na aplikacje AI rośnie, a wymagania wobec samodzielnego budowania modeli od podstaw maleją.

## Wstęp do książki: co czytelnik może z niej wynieść

Tekst wstępny formułuje pytania praktyczne, m.in.: czy warto budować daną aplikację AI, jak ją oceniać (także z użyciem AI jako oceniającego), skąd biorą się halucynacje, jakie są dobre praktyki promptowania, dlaczego działa RAG i jak go stosować, czym jest agent i jak go oceniać, kiedy dostrajać model i kiedy nie, ile danych potrzeba i jak oceniać ich jakość, jak obniżyć koszt i opóźnienia oraz zwiększyć bezpieczeństwo, jak zaprojektować pętlę informacji zwrotnej od użytkowników.

Inżynieria AI jest zestawiana z tradycyjną inżynierią ML: ta druga częściej oznacza **opracowywanie i trenowanie** modeli; inżynieria AI częściej **wykorzystuje już istniejące modele podstawowe** (m.in. przez prompty, kontekst, RAG, dostrajanie). W systemach produkcyjnych często współistnieją oba podejścia.

## Co książka jest, a czym nie jest

To nie jest samouczek po konkretnych narzędziach ani podręcznik teorii ML od zera (np. od definicji sieci neuronowej i treningu własnego modelu od podstaw). To praktyczny przewodnik po **doprowadzaniu aplikacji opartych na modelach podstawowych do sensownego działania** w realnych problemach. Znajomość podstaw probabilistyki i ML (próbkowanie, gradient, propagacja wsteczna, funkcja straty, metryki typu precyzja czy entropia krzyżowa) ułatwia czytanie, ale tekst daje też skrótowe przypomnienia lub odesłania.

## Jak autor dobierał trwałe treści

Przy ocenie trwałości rozwiązań autor stosuje m.in.: rozróżnienie problemów wynikających z **fundamentalnych ograniczeń** działania AI od problemów, które mogą zniknąć przy lepszych modelach; konsultacje z praktykami; oraz intuicję **efektu Lindy’ego** — im dłużej dane podejście trwa, tym dłużej może przetrwać. Pojawiają się też świadomie **tymczasowe** koncepcje, przydatne w danym momencie lub jako ilustracja podejścia.

## Struktura logiczna opracowania (wiedza merytoryczna)

Typowy proces: zrozumienie modeli podstawowych, **ewaluacja** (dwa bloki tematyczne), następnie optymalizacja **instrukcji (promptów)**, **kontekstu** (m.in. RAG i wzorce agentowe) oraz **samego modelu** (dostrajanie, dane), potem **optymalizacja wnioskowania**, na końcu **architektura całego systemu** i informacja zwrotna od użytkowników.

Dla jednego zdania jakości odpowiedzi (poza ustawieniami generowania) istotne są: **instrukcje** dotyczące zachowania modelu, **kontekst**, którego model może użyć, oraz **sam model**.

**RAG** jest opisany jako lepiej zrozumiany i sprawdzony w produkcji; **wzorzec agentowy** jest postrzegany jako potężniejszy, ale bardziej złożony i wciąż intensywnie badany.

## Rozwój od modeli językowych do inżynierii AI

Ewolucja: **modele językowe** → **duże modele językowe (LLM)** → **modele podstawowe** (także multimodalne). Pierwsze modele językowe sięgają lat 50. XX wieku; rozwój do dzisiejszej skali był możliwy m.in. dzięki **samonadzorowaniu**.

**Model językowy** koduje statystyki języka (lub wielu języków): jak prawdopodobne jest słowo w danym kontekście. Podstawowa jednostka to **token** (znak, słowo lub podwyraz, np. sufiks). **Tokenizacja** dzieli tekst na tokeny; zbiór dopuszczalnych tokenów to **słownik** modelu. Metoda tokenizacji i rozmiar słownika są decyzją twórców modelu. Dla części modeli średnio jeden token odpowiada około trzech czwartych długości słowa (przykładowo około sto tokenów to około siedemdziesiąt pięć słów).

Powody użycia tokenów zamiast samych znaków lub słów: tokeny pozwalają **rozbijać słowa na znaczące części**; jest zwykle **mniej unikalnych tokenów niż unikalnych słów**, co ogranicza rozmiar słownika; tokeny pomagają **obsługiwać neologizmy i rzadkie formy** przez podział na znane fragmenty. Token jest krótszy od pełnego słowa, ale niesie więcej informacji niż pojedynczy znak.

## Maskowane i autoregresyjne modele językowe

**Maskowany model językowy** przewiduje **brakujące tokeny** wewnątrz sekwencji, korzystając z kontekstu **przed i po** luce (np. BERT). Typowo stosuje się go do zadań **niegeneratywnych** (klasyfikacja, analiza sentymentu) lub tam, gdzie potrzebne jest pełne „otoczenie” (np. debugowanie kodu z rozumieniem kodu przed i po).

**Autoregresyjny model językowy** przewiduje **następny token** na podstawie **wcześniejszych** tokenów; może generować kolejne tokeny w pętli. W omawianym materiale, jeśli nie powiedziano inaczej, zwrot „model językowy” oznacza **autoregresyjny** model. Autoregresyjne modele bywają też nazywane **przyczynowymi** modelami językowymi.

Wyniki modeli językowych są **otwarte**: ze skończonego słownika można złożyć nieograniczoną liczbę wariacji wyjścia. Model generujący takie otwarte wyniki jest **generatywny**, stąd mowa o generatywnej sztucznej inteligencji.

Intuicja **uzupełniania**: z promptu model kontynuuje tekst. Uzupełnianie można przeformułować na tłumaczenie, klasyfikację spamu itd., lecz **uzupełnianie nie jest tożsame z konwersacją** — model może „dokleić” kolejne pytanie zamiast odpowiedzi, dopóki nie nadano mu zachowania konwersacyjnego w treningu lub systemie.

## Samonadzorowanie i nadzorowanie

**Nadzorowanie** wymaga **jawnych etykiet** (np. oszustwo / brak oszustwa) — zbieranie etykiet jest kosztowne i ogranicza skalę. Klasyczny przełom głębokiego uczenia w wizji (AlexNet) opierał się na nadzorowanym zbiorze z milionami etykietowanych obrazów.

**Samonadzorowanie** pozwala **ominąć wąskie gardło etykiet**: etykiety są **wnioskowane z danych wejściowych** (np. następny token jest „etykietą” dla poprzedniego kontekstu). W **uczeniu bez nadzoru** etykiety w ogóle nie są wymagane — to odrębna relacja.

W modelowaniu języka sekwencja wejściowa dostarcza zarówno **kontekstów**, jak i **prognozowanych tokenów**. Stosuje się znaczniki początku i końca sekwencji; znacznik końca pozwala modelowi **zakończyć generację**.

## Od LLM do modeli podstawowych i multimodalności

**LLM** nie jest ścisłym terminem naukowym: to, co „duże”, jest **względne w czasie** (np. 117 mln parametrów kiedyś uznawane za duże, później mniejsze modele za małe w zestawieniu z nowszymi; w tekście punkt odniesienia to rząd setek miliardów parametrów). Rozmiar zwykle mierzy się liczbą **parametrów** (zmiennych uczonej w treningu). Większy model ma większą zdolność uczenia się i **potrzebuje więcej danych**, aby wykorzystać tę zdolność — trening dużego modelu na zbyt małym zbiorze to **marnotrawstwo zasobów** w porównaniu z mniejszym modelem na tych samych danych.

Modele ograniczone do tekstu są rozszerzane o obrazy, wideo, dźwięk itd. **Model multimodalny** obsługuje więcej niż jeden typ danych. **Duży model multimodalny (LMM)** to generatywny model multimodalny: następny token może być warunkowany **tekstem i innymi modalnościami** (np. obrazem).

W tekście **modele podstawowe** obejmują zarówno duże LLM, jak i duże LMM. Termin „podstawowy” oddaje **szerokie zastosowanie** i rolę fundamentu pod wiele zadań — w przeciwieństwie do epoki silnego podziału na osobne modele tylko do NLP, tylko do wizji itd.

**CLIP** jest przykładem: trenowany z **nadzorem języka naturalnego** na parach (obraz, tekst) z internetu, bez ręcznego etykietowania każdego obrazu; powstał ogromny zbiór par w porównaniu do skali ImageNet. CLIP **nie jest modelem generatywnym** — jest modelem **osadzania** (wspólna przestrzeń wektorowa tekstu i obrazu). Takie modele osadzania bywają podstawą późniejszych generatywnych systemów multimodalnych.

Modele podstawowe są często **ogólnego przeznaczenia**: jeden model może obsłużyć wiele zadań (np. analiza sentymentu i tłumaczenie), choć **dostrajanie** pod konkretne zadanie może maksymalizować wydajność. Dostosowanie mocnego gotowego modelu bywa znacznie tańsze w czasie i danych niż budowa dedykowanego modelu od zera — w tekście pojawia się zestawienie rzędu **dziesięciu przykładów i weekendu** kontra **milion przykładów i pół roku** w zależności od podejścia. Nadal istnieje klasyczny kompromis **kupić czy zbudować** model.

## Trzy czynniki rozwoju inżynierii AI

Po pierwsze, **szerokie możliwości** modeli ogólnego przeznaczenia otwierają nowe klasy aplikacji. Po drugie, **rosnące inwestycje** w AI. Po trzecie, **łatwiejsze tworzenie aplikacji** dzięki API modeli (proste wywołania zamiast własnej infrastruktury serwowania dużych modeli) oraz możliwość tworzenia z minimalnym kodem lub z językiem naturalnym jako „interfejsem”.

## Techniki dopasowania modelu (zapowiedź)

Do dopasowania modelu do potrzeb wymienia się m.in. **inżynierię promptów**, **RAG** (baza wiedzy uzupełniająca instrukcję) oraz **dostrajanie** na danych domenowych — trzy powszechne ścieżki, rozwinięte później w materiale.

## Strony 31–40: od technik dopasowania do przykładów branżowych

### Trzy techniki i koszt adaptacji

**Inżynieria promptów** to m.in. szczegółowe instrukcje z przykładami pożądanych wyników (np. opisy produktów). **RAG** łączy model z bazą (np. opinii klientów), z której pobierany jest kontekst uzupełniający polecenie. **Dostrajanie** to dodatkowe trenowanie na danych domenowych wysokiej jakości. Te trzy podejścia są w tekście wymieniane jako bardzo powszechne w adaptacji modelu.

Adaptacja istniejącego silnego modelu do zadania bywa porównywana rzędem wielkości do **kilkunastu przykładów i około weekendu pracy** w zestawieniu z **około milionem przykładów i wieloma miesiącami** przy budowie dedykowanego modelu od zera — dokładne liczby zależą od metody. Modele zadaniowo wąskie nadal mogą być **mniejsze, szybsze i tańsze w eksploatacji**.

### Trzy czynniki rozwoju inżynierii AI (rozwinięcie)

**Czynnik 1 — możliwości ogólne:** modele podstawowe nie tylko poprawiają istniejące zadania, ale umożliwiają **więcej klas aplikacji**; to, co wcześniej wydawało się niemożliwe do zbudowania, staje się osiągalne.

**Czynnik 2 — inwestycje:** sukces ChatGPT przyspieszył inwestycje VC i przedsiębiorstw w AI. Przykładowo podano **spadek kosztu użycia AI w projektach o dwa rzędy wielkości** w jednym roku między dwoma punktami czasowymi w 2022–2023. Szacunki makroekonomiczne i dane o **wzmiankach o AI w raportach dużych firm** ilustrują szeroką presję konkurencyjną; jednocześnie zaznacza się, że **wyższy wzrost cen akcji** u firm wspominających o AI w raportach **nie musi być związkiem przyczynowym** — może to być korelacja z szybką adaptacją technologii.

**Czynnik 3 — łatwiejsze budowanie aplikacji:** **model usługowy** i **API** zamieniają potrzebę własnej ciężkiej infrastruktury serwowania na proste wywołania. AI umożliwia też tworzenie przy **minimalnym programowaniu** (generowanie kodu, interfejs w języku naturalnym). Trening modeli podstawowych pozostaje domeną **wielkich firm, rządów i dobrze finansowanych startupów**; publicznie cytowany głos sugeruje, że **adaptacja** gotowych modeli do konkretnych zastosowań jest rozsądną ścieżką. **Narzędzia open source** z ekosystemu inżynierii AI zyskiwały w opisywanym okresie **gwiazdki na GitHubie szybciej** niż niektóre wcześniejsze wzorce popularności oprogramowania.

### Dlaczego „inżynieria AI”, a nie tylko „ML” lub „Ops”

Samo określenie **inżynieria ML** nie oddaje w pełni specyfiki pracy z **modelami podstawowymi** względem tradycyjnych modeli ML — choć jest szersze i obejmuje oba światy. Nazwy kończące się na **„Ops”** kładą nacisk operacyjny, podczas gdy w tej książce akcent pada na **dopasowywanie (inżynierię)** modeli podstawowych do celów. **Ankieta wśród praktyków** miała wskazywać preferencję terminu zbliżonego do „inżynierii AI”.

### Klasyfikacje przypadków użycia

Różne organizacje stosują **różne podziały**: np. trzy grupy skupione na **doświadczeniu klienta, produktywności pracowników i optymalizacji procesów**; inne badanie — **osiem kategorii** obejmujących m.in. programowanie, analizę danych, obsługę klienta, teksty marketingowe, badania, projektowanie stron i sztukę; inne podejścia grupują według **wartości biznesowej** (koszt, efektywność, wzrost, innowacje) lub **ciągłości biznesowej** (zagrożenie trwałości firmy bez adopcji). Pełne wylistowanie wszystkich pomysłów na aplikacje jest uznawane za nierealne ze względu na rozmiar przestrzeni rozwiązań.

### Podatność zawodów na AI (badanie Eloundou i in.)

Zadanie uznaje się za **podatne**, jeśli AI może skrócić czas wykonania o **co najmniej około połowę**. Zawody z bardzo wysokim udziałem zadań podatnych to m.in. **tłumaczenia**, **podatkowe biura rachunkowe**, **projektanci stron**, **pisarze**; za **mało podatne** podano m.in. **kucharzy**, **kamieniarzy**, **sportowców**. Wyniki mają charakter **orientacyjny**, ale wspierają myślenie o realnych zastosowaniach.

### Osiem kategorii zastosowań (konsument vs firma)

W jednym zestawieniu aplikacje dzieli się na m.in.: **programowanie**, **obrazy i wideo**, **projektowanie/reklamy**, **tworzenie tekstów** (e-maile, SEO, dokumenty), **edukację**, **boty konwersacyjne** (w tym wsparcie klienta i asystenci), **agregację informacji** (streszczenia, analiza dokumentów, badania rynku), **organizację danych** (wyszukiwanie obrazów, zarządzanie wiedzą, przetwarzanie dokumentów), **automatyzację procesów** (planowanie, ekstrakcja danych, leady). Modele są **uniwersalne**, więc jedna aplikacja może **należeć do wielu kategorii** jednocześnie.

### Aplikacje open source vs enterprise

Analiza setek repozytoriów z otwartym kodem na GitHubie pokazuje **rozkład przypadków użycia** — niska reprezentacja niektórych obszarów (np. część zastosowań edukacyjnych czy organizacji danych) **nie oznacza małej popularności tematu w ogóle**: autorzy mogli celować w **zastosowania firmowe** zamiast w OSS. **Przedsiębiorstwa** częściej i szybciej wdrażają narzędzia **wewnętrzne** (np. zarządzanie wiedzą) niż **zewnętrzne** (np. chatboty dla klienta), bo **mniejsze ryzyko** dotyczące prywatności, zgodności i poważnych awarii; wdrożenia wewnętrzne budują też kompetencje zespołu. Wiele aplikacji nadal ma **zamknięty** charakter — **klasyfikacja** jest **łatwiejsza do oceny**, co obniża ryzyko wdrożenia.

### Programowanie jako wiodący przypadek użycia

**Programowanie** bywa najczęściej wskazywane w badaniach generatywnego AI. **Copilot** jest przykładem wczesnego sukcesu komercyjnego (skala przychodu w krótkim czasie od startu). Zakres narzędzi obejmuje m.in. ekstrakcję struktury z PDF, **angielski → kod** (SQL, pandas), **kod z layoutu / zrzutu ekranu**, migrację między językami, dokumentację, testy, opisy commitów.

**McKinsey** podaje m.in. **ok. dwukrotny wzrost produktywności przy dokumentacji** oraz **ok. 25–50% przy generowaniu kodu i refaktoryzacji**, przy **minimalnym wzroście przy bardzo złożonych zadaniach**. Twórcy narzędzi zauważają, że AI **lepiej radzi sobie często z warstwą wizualną niż serwerową**. Pojawiają się sprzeczne publiczne wizje: od **pełnej automatyzacji roli programisty** po przekonanie, że **zastąpienie ludzi nie nastąpi** — spójny wątek mówi, że **rola się zmienia**, a nie że zawód znika wprost. **Outsourcing** jest narażony, bo zlecane bywa **prostsze** i rzadziej strategiczne. **Produktywniejsi programiści** mogą oznaczać, że firma osiąga cele przy **mniejszej liczbie etatów** deweloperskich.

## Strony 41–42: tworzenie obrazów, wideo i tekstów

**Probabilistyczna natura AI** sprzyja zadaniom kreatywnym; przykłady komercyjne to m.in. generowanie obrazów (np. Midjourney), edycja zdjęć (np. Adobe Firefly), wideo (np. Runway, Pika Labs, Sora). Pod koniec 2023 roku znaczna część czołowych darmowych aplikacji graficznych w sklepie mobilnym miała w nazwie słowo „AI”. **Zdjęcia profilowe** generowane przez AI są powszechne w mediach społecznościowych; postrzeganie takich zdjęć zmieniło się — kiedyś platformy blokowały konta z powodów bezpieczeństwa, później coraz częściej same aplikacje oferują generowanie awatarów. **Reklama i marketing** szybko adoptują AI: bezpośrednie generowanie materiałów, wsparcie koncepcji dla ekspertów, wiele wariantów do testów A/B, sezonowe dostosowania (np. kolory, śnieg).

**Generowanie tekstów** jest naturalnym zastosowaniem, bo LLM są trenowane do uzupełniania tekstu; użytkownicy bywają tolerancyjni na błędy. Badanie MIT (Noy i Zhang, 2023) na grupie profesjonalistów: połowa z dostępem do ChatGPT — **średni czas pisania −40%**, **jakość +18%**; narzędzie **wyrównuje poziom** (większy zysk dla słabszych pisarzy); po dwóch tygodniach **dwukrotnie wyższa skłonność** do użycia, po dwóch miesiącach **1,6×**. Przykłady nadużyć: niskiej jakości przewodniki na marketplace’ach z fikcyjnymi biografiami i recenzjami. W firmach: sprzedaż, marketing, komunikacja wewnętrzna, raporty ocen pracowniczych; CRM oferują generowanie treści na strony i maile.

## Strony 43–44: SEO, edukacja, boty

**SEO:** modele trenowane na tekstach z internetu dobrze naśladują treści pod wyszukiwarki; to napędza **farmy treści** niskiej jakości; w 2023 **NewsGuard** wskazał setki reklam marek na stronach z treścią generowaną przez AI, jedna strona produkowała rzędu **tysiąca artykułów dziennie** — bez regulacji wizja treści w sieci jest pesymistyczna.

**Edukacja:** szkoły najpierw **zakazywały** ChatGPT, potem część **cofała decyzję**. AI może personalizować format (audio, wizualizacje, tłumaczenie matematyki na kod). Według **Pajaka i Bicknella (Duolingo, 2022)** spośród etapów tworzenia kursu **największy potencjał ma personalizacja** (ilustracja w materiale). **Chegg** jako ostrzeżenie: spadek wartości akcji gdy uczniowie masowo przeszli na AI. Metoda **„wypracowanie z błędami”**: model generuje tekst, uczeń znajduje i poprawia błędy.

**Boty konwersacyjne:** wyszukiwanie, wyjaśnianie, pomysły, towarzyszenie, symulacja osobowości; badania z **grupami botów symulującymi społeczeństwo**. W biznesie dominuje **obsługa klienta** (koszt, szybkość), asystenci produktowi przy złożonych procesach. Sukces ChatGPT otworzył wiele botów tekstowych; **tekst nie jest jedynym kanałem** (np. głos, 3D).

## Strony 45–46: głos, agregacja, organizacja danych, automatyzacja

**Asystenci głosowi** (np. asystenci w telefonach) istnieją od lat; **boty 3D** w grach i handlu; postacie niezależne w grach dzięki AI mogą być **inteligentniejsze niż skrypty** — wpływ na dynamikę gier i nowe gatunki.

**Agregacja informacji** (streszczenia, „talk-to-your-docs”): badanie **Salesforce (2023)** — **74%** użytkowników AI do **upraszczania złożonych idei i podsumowań**. W firmie **Instacart** wewnętrzny rynek promptów — popularny szablon **„Fast Breakdown”** do notatek ze spotkań, maili, Slacka z faktami, tematami i zadaniami.

**Organizowanie danych:** rośnie wolumen zdjęć, filmów, PDF, umów; potrzeba **wyszukiwania i strukturyzacji**. AI: opisy multimediów, dopasowanie zapytań tekstowych do wizualiów, **Google Photos**; możliwość **generowania obrazu**, gdy brak gotowego. Analiza: wizualizacje, anomalie, prognozy. **IDP (inteligentne przetwarzanie dokumentów)** — szacunki rynkowe na przyszłość w materiale rzędu **miliardów USD** i **wysokiego tempa wzrostu rocznego**. Ekstrakcja pól z dokumentów od prostych (paragony) po złożone (umowy, wykresy).

**Automatyzacja przepływu** w firmach: leady, faktury, rozliczenia, prośby klientów, wprowadzanie danych. **Synteza danych** do doskonalenia zbiorów i **etykietowanie wspomagane przez AI** (ludzie tylko korygują) — rozwinięcie w rozdziale o danych. Zadania wymagające **narzędzi zewnętrznych** (wyszukiwarka, telefon, kalendarz) prowadzą do pojęcia **agentów** (planowanie + narzędzia), omówionych w dalszej części książki.

## Strony 47–50: planowanie aplikacji i przewaga konkurencyjna

**Ocena przypadku użycia** jako decyzja **ryzyka i szansy** (przykładowe poziomy w tekście): (1) **zagrożenie dla ciągłości biznesu** jeśli konkurencja wyprzedzi — cytowane badanie **Gartnera (2023)**: **7%** wskazań **ciągłości działalności** jako powodu wdrożenia AI; szczególnie branże od dokumentów i agregacji; odniesienie do pracy **Eloundou i in. (GPTs are GPTs, 2023)**; (2) **nie wykorzystana szansa** na zyski i produktywność; (3) **niepewność modelu biznesowego**, ale potrzeba nie zostać w tyle — przykłady firm, które spóźniły się na rewolucje technologiczne. Przy **egzystencjalnym ryzyku** rozważać **rozwój wewnętrzny** zamiast outsourcingu do konkurentów; przy szansach na wzrost często dostępne są **gotowe produkty**.

**Role AI w produkcie (m.in. dokument Apple):** **krytyczna vs uzupełniająca** — np. rozpoznawanie twarzy bez AI nie działa, a edytor maila bez podpowiedzi tak; im bardziej AI krytyczne, tym wyższe wymagania co do **niezawodności**; użytkownicy **bardziej wyrozumiali**, gdy AI dodatkiem. **Reaktywna vs proaktywna** — chatbot **reaktywny**, powiadomienia o ruchu **proaktywne**; reaktywne zwykle wymagają **niskich opóźnień**; proaktywne mogą być liczone wcześniej; zła jakość proaktywnych treści może irytować. **Dynamiczna vs statyczna** — np. twarz wymaga aktualizacji przy zmianie wyglądu; wykrywanie obiektów może aktualizować się rzadziej z wersją aplikacji; dynamicznie możliwy **model per użytkownik** lub **pamięć preferencji**; statycznie jeden model dla grupy. **Rola ludzi:** warianty od podpowiedzi dla agentów, przez AI tylko do prostych spraw, po pełną automatyzację — **human-in-the-loop**. **Microsoft (2023) Crawl–Walk–Run:** **Crawl** — człowiek obowiązkowy; **Walk** — AI z pracownikami wewnętrznymi; **Run** — większa automatyzacja, także wobec klientów zewnętrznych. Wraz ze wzrostem jakości i **akceptacji sugestii** (np. bardzo wysoki odsetek na prostych zapytaniach) można przejść do **bezpośredniej interakcji klient–AI**.

**Przewaga konkurencyjna:** łatwy start to też **łatwe skopiowanie**; produkt jako **warstwa nad modelem podstawowym** ryzykuje **wchłonięciem** przez rozwój samego modelu (np. lepsza obsługa PDF w modelu). Sensowne pozycje to m.in. **modele otwarte i lokalne** dla określonych użytkowników. Trzy filary przewagi wskazane w tekście: **technologia, dane, dystrybucja** — przy modelach podstawowych **technologie firm często zbliżone**, **dystrybucję** często mają **duże firmy**; **dane** są złożone: duże organizacje mają wolumen, startupy mogą uczyć się z **zachowań użytkowników** i **sygnałów użycia** nawet gdy bezpośrednie trenowanie na danych użytkowników jest ograniczone.

## Strony 51–54: oczekiwania, kamienie milowe, utrzymanie, wstęp do stosu

**Historia produktów a nisza:** wiele trwałych firm zaczynało od rozwiązań, które mogłyby wyglądać jak „składowa” większego ekosystemu (np. planowanie spotkań, newslettery, edycja zdjęć w obrębie gigantów). Startupy często wygrywają, gdy budzą kategorię, którą **więksi konkurenci przeoczyli** — to argument motywacyjny przy planowaniu własnej aplikacji.

**Ustalenie oczekiwań:** po decyzji o budowie aplikacji kolejny krok to **kryteria sukcesu**; nadrzędnie liczy się **wpływ na działalność** (biznes), nie sama technologia dla niej samej. Dla chatbota obsługi przykładowe kierunki myślenia to: jaki **odsetek** spraw ma być zautomatyzowany, **wolumen** dodatkowych spraw, **czas reakcji** względem linii bazowej ludzkiej, **oszczędność pracy** ludzi. **Większa liczba obsłużonych wiadomości** nie implikuje wyższej satysfakcji — warto łączyć metryki jakości odpowiedzi z **badaniem satysfakcji** i opinią o produkcie.

**Progi użyteczności przed wypuszczeniem do klientów:** poza metrykami jakości odpowiedzi istotne są **opóźnienia** (w tekście pojawiają się skróty **TTFT** — czas do pierwszego tokena, **TPOT** — czas na token w generacji oraz opóźnienie całkowite), **koszt zapytania** do modelu oraz ewentualnie **interpretowalność** i **sprawiedliwość**. Akceptowalne opóźnienie jest **zależne od przypadku użycia** (np. jeśli ludzie odpowiadają średnio w godzinach, szybsza odpowiedź modelu może już być wystarczająca).

**Kamienie milowe i pułapka demo:** po ustawieniu mierzalnych celów potrzebny jest plan osiągnięcia z uwzględnieniem **stanu gotowych modeli** — im lepszy punkt startowy, tym mniej pracy do celu; analiza może **zmienić cele** lub doprowadzić do rezygnacji, gdy koszt przekroczy korzyść. Wczesny sukces z modelem podstawowym bywa **mylący**: demo bywa szybkie, produkt produkcyjny — **znacznie dłuższy**. W przytoczonych źródłach pojawia się obraz „łatwego” skoku początkowego i **trudnego domykania ostatnich procentów** jakości (praca nad błędami i halucynacjami, spadek motywacji przy marginalnych przyrostach).

**Konserwacja i zmienność środowiska:** utrzymanie produktu AI wiąże się z **szybką ewolucją** dziedziny. Zmiany bywają korzystne (maleją ograniczenia modeli, **dłuższe okna kontekstu**, wyższa jakość odpowiedzi, **tańsze i szybsze wnioskowanie**), ale też **zakłócają procesy** — wymagają ciągłej **analizy kosztów i korzyści** inwestycji; to, co dziś optymalne, jutro może przestać się opłacać (np. zmiana cen u dostawców, upadłość dostawcy). **Ujednolicone API** ułatwiają migrację między modelami, lecz **każdy model ma swoje cechy** — bez **wersjonowania** i **ewaluacji** adaptacja bywa uciążliwa. **Regulacje** (w tym traktowanie AI jako kwestii bezpieczeństwa, kontrola zasobów obliczeniowych, handel) mogą zmieniać dostępność infrastruktury **z dnia na dzień**; pojawiają się też ryzyka **własności intelektualnej** przy modelach trenowanych na cudzych danych — część branż **ogranicza użycie AI** ze względu na niepewność prawną.

**Stos technologiczny — wejście:** rosnący szum i **FOMO** sprzyjają gonitwie za narzędziami; zamiast tego materiał kładzie nacisk na **fundamenty** inżynierii AI. Dyscyplina **wywodzi się z inżynierii ML**; organizacje albo **łączą role** AI i ML, albo je **rozdzielają** — obowiązki bywają silnie pokrywające się, a inżynier ML może rozszerzać kompetencje o AI. Dalsza część opracowania rozwija **trzy warstwy stosu** (projektowanie aplikacji, projektowanie modelu, infrastruktura) oraz porównania z tradycyjną inżynierią ML i pełnym stackiem aplikacji.
