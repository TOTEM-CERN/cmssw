## Configuration files:
- test_simwatcher_6500GeV_0p4_185.py with first test of simwhatcher
- test_6500GeV_90p0_50.py which has same settings as Eliza Melo simulation file
- test_simwatcher_6500GeV_90p0_50.py with added simwatcher to above configuration file

Mind the fact that due to multithreading introduced to Geant4 you could be forced to run start simulation several times before simwatcher would start to work.

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
