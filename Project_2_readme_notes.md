### 1_TEST

Cílem testu je zjistit, zda se na stránce https://engeto.cz/absolventi/ po zaškrnutí každého políčka ve filtru _Současná pozice_ objeví alespoň jeden příspěvek/příběh absolventa, každá z položek ve filtru by měla návštěvníkovi zobrazit alespoň jeden příspěvek/příběh. Jednotlivé kroky zakliknutí každého políčka ve filtru mám rozepsané zvlášť, přičemž na konci každého tohoto kroku užívám ke kontrole funkci _assert_ (počet zobrazených elementů > 0).

_Note: Tady si myslím, že by určitě šel test více optimalizovat, je zbytečně rozepsaný na jednotlivé kroky, ale to už je bohužel nad moje dosavadní znalosti :-). Taky by možná stálo za to se zamyslet nad tím, jakou nejlepší metodu zvolit k zaklikávání jednotlivých políček ve filtru, protože jakmile by developer změnil název jednolitlivých položek, už by test nefungoval._

### 2_TEST

Cílem testu je ověřit znění Page title na stránce https://engeto.cz/absolventi/. Test obsahuje invalidní hodnotu na řádku 13, pokud se test spustí s tímto řádkem, neměl by passnout.

### 3_TEST

Cílem testu je ověřit, zda se na stránce https://engeto.cz/terminy/ vyskytuje alespoň jeden termín kurzu. Test si skrze lokátor najde tlačítko _Termín kurzu_, které spočítá a funkcí _assert_ zkontroluje, zda je počet tlačítek větší než 0.

_Note: Musela jsem si pomoct funkcí timeout na řádku 16, bez ní mi automaticky spuštěný test pokaždé vracel jiný součet (jako by vždy záleželo, jak rychle se stránka stihla načíst a jaký počet tlačítek test zachytil). Teprve až když jsem test procházela v Playwright Inspectoru a chvíli na stránce s termíny počkala, vypadalo to, že měl test dost času tlačítka spočítat a vrátil mi správný součet._
