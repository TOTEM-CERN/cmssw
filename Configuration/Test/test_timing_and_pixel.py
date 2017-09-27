from SimG4Core.Application.hectorParameter_cfi import *
import FWCore.ParameterSet.Config as cms
import copy

# Summer 2017 Maciej Kocot
# Used for simulation of strips, pixels and timing (diamond+UFSD)

process = cms.Process("TestFlatGun")

# Specify the maximum events to simulate
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)

# Configure the output module (save the result in a file)
process.o1 = cms.OutputModule("PoolOutputModule",
                              outputCommands = cms.untracked.vstring('keep *'),
                              fileName = cms.untracked.string('file:test.root')
                              )
process.outpath = cms.EndPath(process.o1)


process.load("Configuration.StandardSequences.Services_cff")
process.load("Configuration.Generator.FlatLogKsiLogT_pp_13TeV_cfi")
process.load("Configuration.StandardSequences.MagneticField_cff")

process.load("SimG4Core.Application.g4SimHits_cfi")

process.BeamProtTransportSetup = cms.PSet(
    Verbosity = cms.bool(False),
    ModelRootFile = cms.string('Geometry/VeryForwardProtonTransport/data/parametrization_6500GeV_0p4_185_reco_beam1.root'),
    # ModelRootFile = cms.string('Geometry/VeryForwardProtonTransport/data/parametrization_6500GeV_90_transp_75.root'),
    Model_IP_150_R_Name = cms.string('ip5_to_beg_150_station_lhcb1'),
    Model_IP_150_L_Name = cms.string('ip5_to_beg_150_station_lhcb1'),

    # in m, should be consistent with geometry xml definitions
    Model_IP_150_R_Zmin = cms.double(0.0),
    Model_IP_150_R_Zmax = cms.double(202.769),
    Model_IP_150_L_Zmax = cms.double(-202.769),
    Model_IP_150_L_Zmin = cms.double(0.0),
)

# Generate a GDML file for geometry visualisation (for example using SWAN)
# Set process.maxEvents to 1 in order to make the running time short.
# process.g4SimHits.FileNameGDML = cms.untracked.string('geometry.gdml')

process.g4SimHits.Physics.BeamProtTransportSetup = process.BeamProtTransportSetup
process.g4SimHits.G4TrackingManagerVerbosity = cms.untracked.int32(0)
process.g4SimHits.OverrideUserStackingAction = cms.bool(True)   # HINT: TOTEM specific
process.g4SimHits.TransportParticlesThroughWholeBeampipe = cms.bool(True)
process.g4SimHits.UseMeasuredGeometryRecord = cms.untracked.bool(False)  # HINT: TOTEM specific
process.g4SimHits.SteppingVerbosity = cms.int32(5)
process.g4SimHits.G4EventManagerVerbosity = cms.untracked.int32(0)
process.g4SimHits.G4StackManagerVerbosity = cms.untracked.int32(0)
process.g4SimHits.Watchers = cms.VPSet()
process.g4SimHits.HepMCProductLabel = cms.InputTag("generator")
process.g4SimHits.Physics.DefaultCutValue = cms.double(100.0)
process.g4SimHits.Generator = cms.PSet(
    HectorEtaCut,
    HepMCProductLabel=cms.string('SmearingGenerator'),
    ApplyPCuts=cms.bool(False),
    ApplyPtransCut=cms.bool(False),
    MinPCut=cms.double(0.04),  ## the cut is in GeV
    MaxPCut=cms.double(99999.0),  ## the pmax=99.TeV
    ApplyEtaCuts=cms.bool(False),
    MinEtaCut=cms.double(-5.5),
    MaxEtaCut=cms.double(5.5),
    RDecLenCut=cms.double(2.9),  ## (cm) the cut on vertex radius
    LDecLenCut=cms.double(30.0),  ## (cm) decay volume length
    ApplyPhiCuts=cms.bool(False),
    MinPhiCut=cms.double(-3.14159265359),  ## (radians)
    MaxPhiCut=cms.double(3.14159265359),  ## according to CMS conventions
    ApplyLumiMonitorCuts=cms.bool(False),  ## primary for lumi monitors
    Verbosity=cms.untracked.int32(0),
    LeaveScatteredProtons=cms.untracked.bool(True),
    ## HINT: TOTEM specific - Leave intact protons after scattering for further near beam transport
    LeaveOnlyScatteredProtons=cms.untracked.bool(False)
    ## HINT: TOTEM specific - Leave only intact protons and reject all the other particles
)

process.g4SimHits.StackingAction.SaveFirstLevelSecondary = cms.untracked.bool(True)
process.g4SimHits.Totem_RP_SD = cms.PSet(  # HINT: TOTEM specific
    Verbosity=cms.int32(0)
)
process.g4SimHits.PPS_Timing_SD = cms.PSet(
    Verbosity = cms.int32(0)
)
#
# # Use particle table
process.g4SimHits.PPSSD = cms.PSet(
    Verbosity = cms.untracked.int32(0)
)

# Use particle table
process.load("SimGeneral.HepPDTESSource.pdt_cfi")
process.load("SimTotem.RPDigiProducer.RPSiDetConf_cfi")

process.load("RecoCTPPS.Configuration.recoCTPPS_cff")
process.totemRPClusterProducer.tagDigi = cms.InputTag("RPSiDetDigitizer")

process.load("Geometry.VeryForwardGeometry.geometryRP_cfi")
process.load("Configuration.Test.test_cfi")
process.prefer("magfield")

ctppsUFSDGeomXMLFiles = cms.vstring(
    'Geometry/VeryForwardData/data/CTPPS_UFSD_Segments/CTPPS_UFSD_Pattern1.xml',
    'Geometry/VeryForwardData/data/CTPPS_UFSD_Segments/CTPPS_UFSD_Pattern2_SegmentA.xml',
    'Geometry/VeryForwardData/data/CTPPS_UFSD_Segments/CTPPS_UFSD_Pattern2_SegmentB.xml',
    'Geometry/VeryForwardData/data/CTPPS_UFSD_Planes/CTPPS_UFSD_Plane4.xml',
    'Geometry/VeryForwardData/data/CTPPS_UFSD_Parameters.xml',
    'Geometry/VeryForwardData/data/CTPPS_UFSD_Sensitive_Dets.xml',
)

process.XMLIdealGeometryESSource = copy.deepcopy(process.XMLIdealGeometryESSource_CTPPS)
process.XMLIdealGeometryESSource.geomXMLFiles += ctppsUFSDGeomXMLFiles
process.XMLIdealGeometryESSource.geomXMLFiles.remove('Geometry/VeryForwardData/data/CTPPS_Diamond_Planes/CTPPS_Diamond_Plane4.xml')
process.XMLIdealGeometryESSource.geomXMLFiles.append('Geometry/VeryForwardData/data/CTPPS_Diamond_Sensitive_Dets.xml')

# position of RPs
process.XMLIdealGeometryESSource.geomXMLFiles.append("Geometry/VeryForwardData/data/2017_07_08_fill5912/RP_Dist_Beam_Cent.xml")


#from SimGeneral/MixingModule/python/mix_Objects_cfi.py
process.mix.mixObjects.mixSH.input =  cms.VInputTag(  # note that this list needs to be in the same order as the subdets
    cms.InputTag("g4SimHits","TotemHitsRP"),
    cms.InputTag("g4SimHits","CTPPSHitsDiamond"),
    cms.InputTag("g4SimHits","CTPPSHitsUFSD"),
    cms.InputTag("g4SimHits","CTPPSHitsPixel"))

process.mix.mixObjects.mixSH.subdets = cms.vstring(
    'TotemHitsRP',
    'CTPPSHitsDiamond',
    'CTPPSHitsUFSD',
    'CTPPSHitsPixel'
)

process.mix.mixObjects.mixSH.crossingFrames = cms.untracked.vstring(
    'TotemHitsRP',
    'CTPPSHitsDiamond',
    'CTPPSHitsUFSD',
    'CTPPSHitsPixel'
)

process.p1 = cms.Path(
    process.generator
    *process.SmearingGenerator
    *process.g4SimHits
    *process.mix
)
