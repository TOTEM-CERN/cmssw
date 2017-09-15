import FWCore.ParameterSet.Config as cms

TotemNtuplizer = cms.EDAnalyzer("TotemNtuplizer",
    # caution: if set to 0, you might miss important error messages
    verbosity = cms.untracked.uint32(1),

    outputFileName = cms.untracked.string("totem_ntuple.root"),

    # available modules: raw, trigger, rp, rp-timing, t1, t2
    modules = cms.vstring("raw", "trigger", "rp", "t1", "t2"),
    
    # raw metadata part
    RawEventLabel = cms.InputTag("source"),

    # RP part
    includeDigi = cms.bool(False),
    includePatterns = cms.bool(False),

    ModulLabelSimu = cms.string('Raw2DigiProducer'),

    ProductLabelSimu = cms.string('rpCCOutput'),
    RPFittedTrackCollectionLabel = cms.InputTag("RPSingleTrackCandCollFit"),
    RPMulFittedTrackCollectionLabel = cms.InputTag("RPMulTrackCandCollFit"),
    RPStripDigiSetLabel = cms.InputTag("RPSiDetDigitizer"),
    RPDigClusterLabel = cms.InputTag("RPClustProd"),

    RPReconstructedProtonCollectionLabel = cms.InputTag("ElasticReconstruction"),
    RPReconstructedProtonPairCollectionLabel = cms.InputTag("ElasticReconstruction"),

    # T1 part
    RoadLabel = cms.InputTag('NewRoadFinder'),
    T1TrackLabel = cms.string('t1tracks2'),
    T1DigiWireCollectionLabel = cms.InputTag("T1Digis", "T1DigiWire"),
    T1DigiVfatCollectionLabel= cms.InputTag("T1Digis", "T1DigiVfat"),
    T1RecHit2DCollectionLabel = cms.InputTag("t1rechit"),

    # T2 part
    T2IncludePadAndStripDigi = cms.bool(False),
    T2PadClusterCollectionLabel = cms.InputTag("T2MCl", "T2PadClusters"),
    T2StripClusterCollectionLabel = cms.InputTag("T2MCl", "T2StripClusters"),
    HitLabel = cms.InputTag("T2Hits", "T2Hits"),
    T2PadDigiCollectionLabel = cms.InputTag("T2Digis", "T2PadDigi"),
    T2StripDigiCollectionLabel = cms.InputTag("T2Digis", "T2StripDigi"),
    TrackLabel = cms.InputTag("T2TrackColl3", "T2TrackColl")
)

