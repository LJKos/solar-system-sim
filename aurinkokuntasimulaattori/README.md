# Aurinkokuntasimulaattori

Ohjelma on projekti, joka kuului Python-kurssin suoritukseen.

## Esittely

Ohjelmalla voi simuloida aurinkokunnan taivaankappaleita, sekä satelliitteja. Kappaleita voi lisätä aloitustiedostoon tai simulaation aikana. Ohjelma mallintaa aurinkokunnan liikkeitä kunnes tapahtuu törmäys tai käyttäjän määrittämä ajanjakso loppuu.

## Tiedosto- ja kansiorakenne

Kaikki ohjelman Python tiedostot ovat sim-kansiossa, joka taas on src-kansiossa. Sim-kansiossa on files kansio, joka sisältää aloitustiedoston, start_file.txt, ja tallennustiedoston, save.txt. Dokumentti ja suunnitelmat löytyvät doc-kansiosta.
  
## Asennusohje

Ohjelma tarvitsee PyQt5 kirjaston toimiakseen.

## Käyttöohje

Ohjelma ajetaan avaamalla main.py tiedosto Python tulkilla, jolloin käyttöliittymä aukeaa. Simulaatio lähtee liikkeelle painamalla "pause"-näppäintä. Aika-askelta voi vaihtaa "Change dt:"-näppäimillä ja ajanjakson voi asettaa kirjoittamalla aika tekstikenttään sekunteina. Taivaankappaleita voi skaalata "Scale"-näppäimillä ja keskellä näkyvän kappaleen voi vaihtaa "Center object"-näppäimillä. Tarkemmat ohjeet löytyvät dokumentin käyttöohje kohdasta.


# Solar System simulator

This program is project that was part of a Python course.

## Introduction

This program simulates celestial bodies like planets and satellites. Objects can be added to the starting file or during the simulation. The simulator tracks objects' movements until collision occures or a time span that the user has set ends.

## File structure

All Python files are located in /src/sim folder. There is a files folder which includes a file that is used to initialize simulation, start_file.txt, and a file where simulation information is saved, save.txt. Documents (in Finnish) are in doc folder.
  
## Downloads

PyQt5 library is needed to run this program.

## Instructions

The program can be executed by opening the main.py file in Python interpreter, which opens up the graphical user interface. Simulation starts by pressing the "pause" button. Simulation speed can be altered with "Change dt" and the time span can be entered to the text field in seconds. "Scale" buttons are for changing objects' sizes and distances and "Center object" selects the object to be in the center of the screen.
