import FWCore.ParameterSet.Config as cms

generator = cms.EDFilter("Pythia8GeneratorFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(0),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.0),
    PythiaParameters = cms.PSet(
        processParameters = cms.vstring(
            #'SoftQCD:minBias = on',
            'Diffraction:PomFlux = 5',
            'SoftQCD:singleDiffractive = on',
            'SoftQCD:doubleDiffractive = on',
            'SoftQCD:centralDiffractive = on',
            'PDF:PomSet = 4.', #H1 2006 Fit B NLO Q^2-dependent parametrization  
            'PDF:pHardSet =  7', #CTEQ6L1, NLO
            'Tune::pp = 5'),
        parameterSets = cms.vstring(
            'processParameters'
        )
    )
)

