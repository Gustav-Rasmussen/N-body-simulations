#!/bin/bash

echo "Starting GADGET simulation of energy exchange!"

for i in {0..20}
do
   echo "Starting GADGET run number: $i"
   eval "mpirun -np 4 ./Gadget2 Run$i.param"
   echo "Analyzing GADGET run number: $i"
   python Energy_exchange_D1.py
done

echo "GADGET simulation of energy exchange complete!"
