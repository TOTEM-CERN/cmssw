## Configuration files:
- eliza_final.py which has same settings as Eliza Melo simulation
- test_sw.py where simwhatcher is tested
- eliza_sw.py where simwhatcher is added to eliza configuration file

## Particle Generator file
- Pythia8MBR_generated_cfi.py which was used in eliza simulation

## CC files for plotting results

For simulation:

- rps2.cc
- plotti-patryk.cc

For reconstruction:

- recoHits.cc

To plot desired plots adjust settings in .cc file and call:

- root *.cc
