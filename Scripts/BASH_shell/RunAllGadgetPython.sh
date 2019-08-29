#!/bin/bash
for i in 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
do
   # echo "Welcome $i times"
   mpirun -np 4 ./Gadget2 Run$i.param
   python Energy_exchange_D1.py
done



/*
mpirun -np 4 ./Gadget2 Run0.param
python Energy_exchange_D1.py
mpirun -np 4 ./Gadget2 Run1.param
python Energy_exchange_D1.py
mpirun -np 4 ./Gadget2 Run2.param
python Energy_exchange_D1.py
mpirun -np 4 ./Gadget2 Run3.param
python Energy_exchange_D1.py
mpirun -np 4 ./Gadget2 Run4.param
python Energy_exchange_D1.py
mpirun -np 4 ./Gadget2 Run5.param
python Energy_exchange_D1.py
mpirun -np 4 ./Gadget2 Run6.param
python Energy_exchange_D1.py
mpirun -np 4 ./Gadget2 Run7.param
python Energy_exchange_D1.py
mpirun -np 4 ./Gadget2 Run8.param
python Energy_exchange_D1.py
mpirun -np 4 ./Gadget2 Run9.param
python Energy_exchange_D1.py
mpirun -np 4 ./Gadget2 Run10.param
python Energy_exchange_D1.py
mpirun -np 4 ./Gadget2 Run11.param
python Energy_exchange_D1.py
mpirun -np 4 ./Gadget2 Run12.param
python Energy_exchange_D1.py
mpirun -np 4 ./Gadget2 Run13.param
python Energy_exchange_D1.py
mpirun -np 4 ./Gadget2 Run14.param
python Energy_exchange_D1.py
mpirun -np 4 ./Gadget2 Run15.param
python Energy_exchange_D1.py
mpirun -np 4 ./Gadget2 Run16.param
python Energy_exchange_D1.py
mpirun -np 4 ./Gadget2 Run17.param
python Energy_exchange_D1.py
mpirun -np 4 ./Gadget2 Run18.param
python Energy_exchange_D1.py
mpirun -np 4 ./Gadget2 Run19.param
python Energy_exchange_D1.py
mpirun -np 4 ./Gadget2 Run20.param
python Energy_exchange_D1.py
*/
