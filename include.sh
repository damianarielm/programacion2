#!/bin/bash

while read -r line; do
    read -a words <<< $line
    if [[ ${words[0]} == "!include" ]]; then
        cat ${words[1]}
    else
        echo "$line"
    fi
done < $1
