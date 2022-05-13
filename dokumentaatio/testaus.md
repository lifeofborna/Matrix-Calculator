# Testausdokumentti
Sovellusta on testattu erilaisilla unittesteillä sekä yksikkö että integraatiotestein. 

## Yksikkö ja integraatiotestaus
Testejä on luotu jokaiselle matriisi operaatioille. +-* testit toteutuvat tekemällä testi matriisin ja testaamalla 
tuottaako se halutun vastauksen kun valittu operaatio suoritetaan testattavalla matriisilla. Nämä testit ovat vain yksikkötestejä eli siinä 
testataan vain MatrixLogic luokan funktioita. 

Testattavana on myös UserService luokka joka siis hallitsee käyttäjän hallinnasta. Tässä tapauksessa UserService;lle annetaan default parametrin
sijaan "test.db" joka siis luo uuden testi tietokannan jota käytämme testeissä. Testit testaavat miten UserService luokka hyödyntää UserRepositorya
ja sen tietokantaoperaatioita. Testeissä kokeillaan eri arvoilla käyttäjän kirjautumista ja rekisteröitymistä ja katsotaan palautuuko haluttu arvo.
Jokaisella testikierroksella myös tyhjennetään testitietokanta ennenkuin mitään operaatioita testataan.

## Testauskattavuus
Ohjelman haarautumakattavuus on 96 % kun käyttäjäliittymä kerrosta ei testata.

![Kuva](https://github.com/lifeofborna/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/coveragereport.png)
