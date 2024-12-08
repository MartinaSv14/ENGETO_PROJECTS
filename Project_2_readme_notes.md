### TEST_1

Cílem testu je zjistit, zda se na stránce https://engeto.cz/absolventi/ po zaškrnutí každého políčka ve filtru _Současná pozice_ objeví alespoň jeden příspěvek/příběh absolventa, každá z položek ve filtru by měla návštěvníkovi zobrazit alespoň jeden příspěvek/příběh. Jednotlivé kroky zakliknutí každého políčka ve filtru mám rozepsané zvlášť, přičemž na konci každého tohoto kroku užívám ke kontrole funkci _assert_ (počet zobrazených elementů > 0).

### TEST_2

Cílem testu je ověřit znění Page title na stránce https://engeto.cz/absolventi/. Test obsahuje invalidní hodnotu na řádku 13, pokud se test spustí s tímto řádkem, neměl by passnout.

### TEST_3

Cílem testu je ověřit, zda se na stránce https://engeto.cz/terminy/ vyskytuje alespoň jeden termín kurzu. Test si skrze lokátor najde tlačítko _Termín kurzu_, které spočítá a funkcí _assert_ zkontroluje, zda je počet tlačítek větší než 0.

