#!/bin/bash
OUT=`mysql -N -u seanconnery eggdrop -e  "SELECT phrase FROM mfw-phrases ORDER BY RAND() limit 1;"`;
echo $OUT;
