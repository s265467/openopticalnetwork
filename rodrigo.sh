#caricamento interprete bash
#!/bin/bash

#accesso a directory passata da linea di comando
cd $1
#finchè non ho raggiunto la root sto nel ciclo
#il comando pwd restituisce il percorso assoluto fino alla cartella corrente
while [ "$(pwd)" != "/" ]
do
	pwd # stampo il precorso della cartella in cui sono
	ls | wc -l # stampo il numero di file/cartelle nella cartella in cui sono
	cd ".." #vado al livello superiore
done;
#rieseguo questi due comandi perchè quando arrivo alla / esco dal ciclo
pwd 
ls |wc -l
