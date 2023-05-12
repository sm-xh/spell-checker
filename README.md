# Wstęp

Korektor ortograficzny to narzędzie używane do identyfikowania i poprawiania błędów ortograficznych w tekście. Mimo że większość nowoczesnych edytorów tekstu ma wbudowane korektory ortograficzne, zrozumienie, jak działają i jak je stworzyć, to ciekawe zadanie z zakresu przetwarzania języka naturalnego (NLP - Natural Language Processing).

Program, który stworzyliśmy, to prosty korektor ortograficzny dla języka polskiego i angielskiego. Używa on podstawowych technik NLP do identyfikowania błędów ortograficznych i sugerowania poprawek. Mimo że jest to prosta implementacja, dobrze ilustruje podstawowe koncepcje stojące za korektorem ortograficznym.

Nasz korektor ortograficzny działa na zasadzie modelu statystycznego, który ocenia prawdopodobieństwo poszczególnych słów w tekście na podstawie ich częstości występowania w korpusie - dużym zbiorze tekstów w danym języku. Jeśli dane słowo nie występuje w korpusie, program generuje listę kandydatów na poprawki, które są "bliskie" oryginalnemu słowu (tzn. różnią się od niego o jedną lub dwie "edycje", takie jak usunięcie litery, zamiana dwóch liter miejscami, zmiana jednej litery na inną, lub dodanie litery), a następnie wybiera te, które są najbardziej prawdopodobne na podstawie ich częstości występowania w korpusie.

W tym raporcie omówimy szczegółowo, jak został zbudowany nasz korektor ortograficzny, jakie techniki NLP zostały użyte, oraz jakie są jego mocne i słabe strony.

# Rozwinięcie

Podstawą naszego podejścia do rozwiązania problemu korekcji ortograficznej jest wykorzystanie modelu statystycznego opartego na częstości występowania słów w dużym korpusie tekstów. Wykorzystanie korpusu pozwala nam na ocenę, które słowa są najbardziej prawdopodobne w danym języku.

## Przygotowanie danych

Na początku naszej pracy zaimplementowaliśmy funkcję wczytującą korpus z biblioteki NLTK. Dla języka angielskiego korzystaliśmy z korpusu Brown, natomiast dla języka polskiego skorzystaliśmy z korpusu 'polish'. Wczytane słowa z korpusu przechowywane są w strukturze danych typu `Counter`, która pozwala na szybkie zliczanie częstości występowania słów.

## Generowanie kandydatów

Następnie skupiliśmy się na generowaniu kandydatów na poprawki dla słów, które nie występują w korpusie. Wykorzystaliśmy do tego tzw. odległość edycyjną, która mierzy, jak bardzo dwa słowa różnią się od siebie poprzez liczbe operacji edycyjnych potrzebnych do przekształcenia jednego słowa w drugie. Nasz model generuje kandydatów, którzy różnią się od oryginalnego słowa o jedną lub dwie operacje edycyjne.

## Wybór najlepszego kandydata

Po wygenerowaniu listy kandydatów, model ocenia ich prawdopodobieństwo na podstawie ich częstości występowania w korpusie i wybiera najbardziej prawdopodobne słowo jako poprawkę. Jeżeli dla danego słowa nie udało się wygenerować żadnych kandydatów, model zwraca oryginalne słowo bez zmian.

Nasze podejście jest proste, ale skuteczne dla wielu typów błędów ortograficznych. Jest jednak kilka potencjalnych obszarów do dalszego rozwoju i usprawnień, takich jak uwzględnienie kontekstu słowa w zdaniu czy zastosowanie zaawansowanych technik uczenia maszynowego do oceny prawdopodobieństwa kandydatów.


## Implementacja detali

### Funkcje edycji

Nasza implementacja korzysta z czterech podstawowych operacji edycyjnych:

1. **Usuwanie** (`deletes`): usuwa każdą literę z oryginalnego słowa, tworząc nowe słowo.

2. **Zamiana** (`transposes`): zamienia miejscami każde dwie sąsiednie litery w oryginalnym słowie.

3. **Zmiana** (`replaces`): zmienia każdą literę w oryginalnym słowie na inną literę.

4. **Wstawianie** (`inserts`): wstawia każdą możliwą literę na każdą możliwą pozycję w oryginalnym słowie.

Te operacje są wykonywane na wszystkich słowach, które nie są obecne w korpusie, w celu generowania listy potencjalnych kandydatów na poprawki.

### Wybór kandydatów

Po wygenerowaniu kandydatów, nasz model ocenia ich prawdopodobieństwo na podstawie ich częstości występowania w korpusie. Jeżeli dla danego słowa nie udało się wygenerować żadnych kandydatów, model zwraca oryginalne słowo bez zmian. W przeciwnym wypadku, model zwraca trzy najbardziej prawdopodobne kandydaty na poprawki.

### Korpusy

Korzystaliśmy z korpusów dostępnych w bibliotece NLTK - korpusu Brown dla języka angielskiego i korpusu 'polish' dla języka polskiego. Te korpusy zawierają duże zbiory tekstów w odpowiednim języku, co pozwoliło nam na stworzenie modelu statystycznego oceniającego prawdopodobieństwo poszczególnych słów.

Nasza implementacja jest prosta, ale efektywna dla wielu rodzajów błędów ortograficznych. Jednakże, jest kilka możliwych obszarów do dalszego rozwoju i usprawnienia, jak uwzględnienie kontekstu słowa w zdaniu czy zastosowanie bardziej zaawansowanych technik NLP i uczenia maszynowego.

## Implementacja detali

### Funkcje edycji

Nasza implementacja korzysta z czterech podstawowych operacji edycyjnych:

1. **Usuwanie** (`deletes`): usuwa każdą literę z oryginalnego słowa, tworząc nowe słowo.

2. **Zamiana** (`transposes`): zamienia miejscami każde dwie sąsiednie litery w oryginalnym słowie.

3. **Zmiana** (`replaces`): zmienia każdą literę w oryginalnym słowie na inną literę.

4. **Wstawianie** (`inserts`): wstawia każdą możliwą literę na każdą możliwą pozycję w oryginalnym słowie.

Te operacje są wykonywane na wszystkich słowach, które nie są obecne w korpusie, w celu generowania listy potencjalnych kandydatów na poprawki.

### Wybór kandydatów

Po wygenerowaniu kandydatów, nasz model ocenia ich prawdopodobieństwo na podstawie ich częstości występowania w korpusie. Jeżeli dla danego słowa nie udało się wygenerować żadnych kandydatów, model zwraca oryginalne słowo bez zmian. W przeciwnym wypadku, model zwraca trzy najbardziej prawdopodobne kandydaty na poprawki.

### Korpusy

Korzystaliśmy z korpusów dostępnych w bibliotece NLTK - korpusu Brown dla języka angielskiego i korpusu 'polish' dla języka polskiego. Te korpusy zawierają duże zbiory tekstów w odpowiednim języku, co pozwoliło nam na stworzenie modelu statystycznego oceniającego prawdopodobieństwo poszczególnych słów.

Nasza implementacja jest prosta, ale efektywna dla wielu rodzajów błędów ortograficznych. Jednakże, jest kilka możliwych obszarów do dalszego rozwoju i usprawnienia, jak uwzględnienie kontekstu słowa w zdaniu czy zastosowanie bardziej zaawansowanych technik NLP i uczenia maszynowego.


## Obszary do dalszego rozwoju

### Kontekstualne sprawdzanie pisowni

Aktualna implementacja nie bierze pod uwagę kontekstu, w jakim występuje dane słowo. To oznacza, że jeśli dane słowo jest pisowniowo poprawne, ale użyte jest w niewłaściwym kontekście, nasz model tego nie wykryje. Przykładem może być pomyłka "morze" zamiast "może". Obie formy są poprawne językowo, ale ich użycie zależy od kontekstu zdania.

Rozwiązaniem tego problemu może być zastosowanie modelu języka, który ocenia prawdopodobieństwo sekwencji słów, a nie pojedynczych słów. Takie modele, zwane często modelami n-gramów, są powszechnie stosowane w NLP.

### Zaawansowane techniki NLP i uczenia maszynowego

Innym obszarem do dalszego rozwoju jest zastosowanie zaawansowanych technik NLP i uczenia maszynowego, takich jak sieci neuronowe, które mogą być w stanie lepiej modelować złożoność języka naturalnego i dokonywać bardziej precyzyjnych poprawek.

Na przykład, model zwany BERT, opracowany przez firmę Google, jest w stanie dokonywać kontekstualnej korekcji pisowni, oceniając prawdopodobieństwo poszczególnych słów na podstawie ich kontekstu w zdaniu, a nie tylko na podstawie ich pojedynczych częstości występowania.

Jednakże, implementacja takiego modelu jest znacznie bardziej złożona i wymaga dużej ilości danych do treningu, a także znacznej mocy obliczeniowej.

Podsumowując, nasza aktualna implementacja korektora ortograficznego jest prosta, ale skuteczna dla wielu typów błędów ortograficznych. Jest jednak wiele obszarów do dalszego rozwoju i usprawnienia, które mogą znacznie poprawić jakość korekcji.

# Podsumowanie

Nasza implementacja korektora ortograficznego oparta jest na statystycznym modelu języka, który ocenia prawdopodobieństwo poszczególnych słów na podstawie ich częstości występowania w korpusie. Nasze podejście jest skuteczne dla wielu typów błędów ortograficznych, ale ma też swoje ograniczenia.

Nie uwzględnia kontekstu słowa w zdaniu, co może prowadzić do niepoprawnej korekty w przypadku słów, które są ortograficznie poprawne, ale użyte są w niewłaściwym kontekście. Ponadto, nasza implementacja opiera się na relatywnie prostych technikach NLP i nie wykorzystuje zaawansowanych technik uczenia maszynowego, które mogą zwiększyć precyzję korekty.

Mimo tych ograniczeń, nasz korektor ortograficzny jest dobrym punktem wyjścia do dalszego rozwoju i eksploracji w dziedzinie przetwarzania języka naturalnego. Przez rozszerzenie naszego modelu o kontekstualne sprawdzanie pisowni lub zastosowanie zaawansowanych technik uczenia maszynowego, moglibyśmy stworzyć jeszcze bardziej precyzyjny i skuteczny korektor ortograficzny.


