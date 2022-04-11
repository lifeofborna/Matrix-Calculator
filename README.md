# *Ohjelmisto tekniikan harjoitustyö: Matriisilaskin*

Sovelluksen ideana on, kahden matriisin väliset matriisi operaatiot. Toiminallisuuksiin kuuluu, kahden matriisin kertominen, yhteenlasku sekä erotus. 


## Dokumentaatio
[Vaatimusmäärittely](https://github.com/lifeofborna/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Tuntikirjanpito](https://github.com/lifeofborna/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[Changelog](https://github.com/lifeofborna/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

[Arkkitehtuuri](https://github.com/lifeofborna/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

## Asennus

1. Tarvittavien riippuvuuksien asentaminen:
>**poetry install**

2. Sovelluksen käynnistäminen tapahtuu seuraavasti:
>**poetry run invoke start**


## Komentorivitoiminnot

### Sovelluksen käynnistys:
>**poetry run invoke start**

### Sovelluksen testien suoritus
>**poetry run invoke test**

### Testikattavuuden suoritus
> **poetry run invoke coverage-report** 
> 
Raportti löytyy htmlcov hakemistosta.

### Pylint tarkistukset suoritetaan:
> **poetry run invoke lint**
