# Arkkitehtuurikuvaus

## Rakenne

*Pakkausrakenne:* 

![Pakkausrakenne](./kuvat/arkkitehtuuri.png)

Pakkaus ui sisältää graafisen käyttöliittymän koodin joka hyödyntää pakkausta matrixcalculator jossa on matriisi operaatioiden sovelluslogiikka.

## Päätoiminnallisuudet
*Yhteenlaskuoperaatio:* 

![sekvenssikaavio](./kuvat/Addition.png)

Kun graafiseen käyttöliittymään asetetaan matriisien arvot ja tämän jälkeen painetaan yhteenlasku näppäintä, niin tapahtumakäsittelijä kutsuu funktiota addtion. Tämän jälkeen funktiossa otetaan vastaan käyttäjän syöttämät matriisit ja suoritetaan yhteenlasku operaatio hyödyntäen matrixlogic luokkaa. Jonka jälkeen palautuu matriisi johon yhteenlasku operaatio on suoritettu tämän jälkeen UI luokka asettaa tämän matriisin näkyville UI funktiolla resultant_matrix. 
