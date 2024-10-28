### 1_TEST

Cílem testu je zjistit, zda se na stránce https://engeto.cz/absolventi/ po zaškrnutí každého políčka ve filtru _Současná pozice_ objeví alespoň jeden příspěvek/příběh absolventa, každá z položek ve filtru by měla návštěvníkovi zobrazit alespoň jeden příspěvek/příběh. Jednotlivé kroky zakliknutí každého políčka ve filtru mám rozepsané zvlášť, přičemž na konci každého tohoto kroku užívám ke kontrole funkci _assert_ (počet zobrazených elementů > 0).

_Note: Tady si myslím, že by určitě šel test více optimalizovat, je zbytečně rozepsaný na jednotlivé kroky, ale to už je bohužel nad moje dosavadní znalosti :-). Taky by možná stálo za to se zamyslet nad tím, jakou nejlepší metodu zvolit k zaklikávání jednotlivých políček ve filtru, protože jakmile by developer změnil název jednolitlivých položek, už by test nefungoval._

### 2_TEST

Cílem testu je ověřit znění Page title na stránce https://engeto.cz/absolventi/. Test obsahuje invalidní hodnotu na řádku 13.

### 3_TEST

Cílem testu je ověřit, zda se na stránce https://engeto.cz/terminy/ vyskytuje alespoň jeden termín kurzu.