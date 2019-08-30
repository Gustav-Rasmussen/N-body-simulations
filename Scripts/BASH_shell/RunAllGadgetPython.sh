#!/bin/bash
for i in {0..20}
do
   # echo "mpirun -np 4 ./Gadget2 Run$i.param"
   eval "mpirun -np 4 ./Gadget2 Run$i.param"
   python Energy_exchange_D1.py
done


: <<'END'
Multi-line
comment
END
