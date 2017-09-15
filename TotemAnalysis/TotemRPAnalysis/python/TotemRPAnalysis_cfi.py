import FWCore.ParameterSet.Config as cms

TotemRPAnalysis = cms.PSet(
    # caution: if set to 0, you might miss important error messages
    verbosity = cms.untracked.uint32(1),

    # RP part

    primaryProtons = cms.bool(True),
    includeDigi = cms.bool(True),
    includePatterns = cms.bool(True),

    ModulLabelSimu = cms.string('RPDataCCProducer'),

    ProductLabelSimu = cms.string('RPCCRawBits'),
    RPFittedTrackCollectionLabel = cms.InputTag("RPSingleTrackCandCollFit"),
    RPMulFittedTrackCollectionLabel = cms.InputTag("RPMulTrackNonParallelCandCollFit"),
    RPStripDigiSetLabel = cms.InputTag("RPSiDetDigitizer"),
    RPDigClusterLabel = cms.InputTag("RPClustProd"),

    RPReconstructedProtonCollectionLabel = cms.InputTag("RP220Reconst"),
    RPReconstructedProtonPairCollectionLabel = cms.InputTag("RP220Reconst")

)
