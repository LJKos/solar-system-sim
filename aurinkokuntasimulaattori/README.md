# Aurinkokuntasimulaattori

## Esittely

Ohjelmalla voi simuloida aurinkokunnan taivaankappaleita, sekä satelliitteja. Kappaleita voi lisätä aloitustiedostoon tai simulaation aikana. Ohjelma mallintaa aurinkokunnan liikkeitä kunnes tapahtuu törmäys tai käyttäjän määrittämä ajanjakso loppuu.

## Tiedosto- ja kansiorakenne

Kaikki ohjelman Python tiedostot ovat sim-kansiossa, joka taas on src-kansiossa. Sim-kansiossa on files kansio, joka sisältää aloitustiedoston, start_file.txt, ja tallennustiedoston, save.txt. Dokumentti ja suunnitelmat löytyvät doc-kansiosta.
  
## Asennusohje

Ohjelma tarvitsee PyQt5 kirjaston toimiakseen.

## Käyttöohje

Ohjelma ajetaan avaamalla main.py tiedosto Python tulkilla, jolloin käyttöliittymä aukeaa. Simulaatio lähtee liikkeelle painamalla "pause"-näppäintä. Aika-askelta voi vaihtaa "Change dt:"-näppäimillä ja ajanjakson voi asettaa kirjoittamalla aika tekstikenttään sekunteina. Taivaankappaleita voi skaalata "Scale"-näppäimillä ja keskellä näkyvän kappaleen voi vaihtaa "Center object"-näppäimillä. Tarkemmat ohjeet löytyvät dokumentin käyttöohje kohdasta.