#!/bin/sh
clear

str="[???]: Ecco qui il nuovo arrivato..."

while IFS= read -r -n1 var
do
    printf '%s' "$var"
    sleep 0.015
done <<< "$str"

echo
sleep 0.3
echo

str="[???]: Io sono San Pietro bot, il custode di tutte le chiavi SSH utilizzate per il trasferimento dei dati all'interno del laboratorio."

while IFS= read -r -n1 var
do
    printf '%s' "$var"
    sleep 0.015
done <<< "$str"

echo
sleep 0.3
echo


str="[San_Pietro_bot]: Visto che non abbiamo molto tempo andiamo subito alla spiegazione del test."

while IFS= read -r -n1 var
do
    printf '%s' "$var"
    sleep 0.015
done <<< "$str"

echo
sleep 0.3
echo

str="[San_Pietro_bot]: Tutto quello che dovrai fare in questo test è creare una chiave SSH."

while IFS= read -r -n1 var
do
    printf '%s' "$var"
    sleep 0.015
done <<< "$str"

echo
sleep 0.3
echo

str="[San_Pietro_bot]: Nel caso non conoscessi il protocollo SSH ti ho lasciato della documentazione a riguardo nel file doc.txt. Troverai anche altre risorse utili."

while IFS= read -r -n1 var
do
    printf '%s' "$var"
    sleep 0.015
done <<< "$str"

echo
sleep 0.3
echo

str="[San_Pietro_bot]: Per questo test puoi usare quelle oppure cercare da solo informazioni a riguardo, ma nota che per questo test non avrai bisogno di usare nessuna flag assieme al comando per generare la chiave SSH."

while IFS= read -r -n1 var
do
    printf '%s' "$var"
    sleep 0.015
done <<< "$str"

echo
echo
