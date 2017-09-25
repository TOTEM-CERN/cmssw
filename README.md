In order to run CTPPS simulation in CMSSW_9_2_6 follow these steps in terminal:
~~~~
source /cvmfs/cms.cern.ch/cmsset_default.sh
cmsrel CMSSW_9_2_6
cd CMSSW_9_2_6/src
cmsenv
git cms-merge-topic mackoo13:simulation_9_2_6
scram b -j 8
cmsRun Configuration/Test/test_timing_and_pixel.py
~~~~
The code is based on official CMS 9_2_6 release and Marcin Ziaber's fork (ziaber/simulation)
