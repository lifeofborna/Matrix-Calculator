# Vaatimusmäärittely

## Sovelluksen tarkoitus
Sovelluksen tarkoituksena on mahdollistaa käyttäjän kirjautumisen ja antamaan 3x3 matriisiin tiettyjä laskuoperaatioita. Sovellus myös toteuttaa erilaisia matriisi operaatioita. 

## Käyttäjät
Sovellus on suunniteltu siten, että se koostuu yhdestä käyttäjäroolista. 

## Perusversion tarjoama toiminnallisuus

### Ennen kirjautumista
- Käyttäjällä on mahdollisuus luoda käyttäjätunnuksen
- Käyttäjällä on mahdollisuus kirjautua sovellukseen.
- Jos käyttäjätunnus on väärin tai sitä ei löydy niin sovellus antaa selkeän virheilmoituksen.

### Kirjautumisen jälkeen
- Käyttäjä voi luoda uuden laskun ja valita laskuoperaation. 
  - Laskuoperaatiot ovat ( - + * )
  - Jos käyttäjä syöttää laittoman laskuoperaation niin sovellus antaa virheilmoituksen. 
- Käyttäjä antaa matriisin, johon tehdän laskuoperaatio ja toinen matriisi, jolla laskuoperaatio suoritetaan. 
  - Sovellus tarkistaa, että matriisi ei sisällä ei sallittuja merkkejä, jos löytyy heittää virheilmoituksen. 
- Käyttäjä voi kirjautua ulos 
- Matriisin determinantin laskeminen.
- Matriisien transpoosien laskeminen. 
- Käänteismatriisin laskeminen. 
- Tyhjentää matriisi syötteet

## Jatkokehitysideoita

Perusversion jälkeen järjestelmää on mahdollista parantaa seuraavilla toiminnallisuuksilla: 

- Matriisien ominaisarvojen/vektoreiden laskeminen.
- Käyttäjän historiasta on mahdollista kopioda vanha laskutoimitus ja tehdä uusia operaatioita siihen. 
- Poistaa jo tehty käyttäjä.
- Tallentaa käyttäjän tehdyt laskut
