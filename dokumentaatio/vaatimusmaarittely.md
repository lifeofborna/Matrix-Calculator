# Vaatimusmäärittely

## Sovelluksen tarkoitus
Sovelluksen tarkoituksena on mahdollistaa käyttäjän antamaan matriisiin tiettyjä laskuoperaatioita. Sovelluksen on myös tarkoitus 
pitää historiaa tapahtuneista laskuista/tuloksista.

## Käyttäjät
Sovellus on suunniteltu siten, että se koostuu yhdestä käyttäjäroolista. 

## Perusversion tarjoama toiminnallisuus

### Ennen kirjautumista
- Käyttäjällä on mahdollisuus luoda käyttäjätunnuksen
- Käyttäjällä on mahdollisuus kirjautua sovellukseen.
- Jos käyttäjätunnus on väärin tai sitä ei löydy niin sovellus antaa selkeän virheilmoituksen.

### Kirjautumisen jälkeen
- Käyttäjä näkee vanhat suoritetut laskut.
- Käyttäjä voi luoda uuden laskun ja valita laskuoperaation. (Tehty)
  - Laskuoperaatiot ovat ( - + * ) (Tehty)
  - Jos käyttäjä syöttää laittoman laskuoperaation niin sovellus antaa virheilmoituksen. (Tehty) 
- Käyttäjä antaa matriisin, johon tehdän laskuoperaatio ja toinen matriisi, jolla laskuoperaatio suoritetaan. (Tehty) 
  - Sovellus tarkistaa, että matriisi ei sisällä ei sallittuja merkkejä, jos löytyy heittää virheilmoituksen. (Tehty)
  - Sovellus myös tarkistaa jos kertolasku operaatio on valittu niin matriisien rivit ja sarakkeet ovat salittuja tähän operaatioon.(Tehty)
- Käyttäjä voi tyhjentää historiansa
- Käyttäjä voi kirjautua ulos

## Jatkokehitysideoita

Perusversion jälkeen järjestelmää on mahdollista parantaa seuraavilla toiminnallisuuksilla: 

- Matriisien ominaisarvojen/vektoreiden laskeminen.
- Matriisin determinattien laskeminen.
- Matriisien transpoosien laskeminen. 
- Matriisien vieminen porrasmuotoon tai supistettuun porrasmuotoon. 
- Onko matriisi lineaarisesti riippumaton.
- Matriisin kertominen skalaareilla. 
- Matriisin dimension näyttäminen aina laskutoimituksen jälkeen.
- Käyttäjän historiasta on mahdollista kopioda vanha laskutoimitus ja tehdä uusia operaatioita siihen. 
- Poistaa jo tehty käyttäjä.
