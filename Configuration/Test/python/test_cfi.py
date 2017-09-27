from SimG4Core.Application.hectorParameter_cfi import *
import FWCore.ParameterSet.Config as cms

# Summer 2017 Maciej Kocot & Patryk Lawski
# Base config used for simulation

'''
MessageLogger = cms.Service("MessageLogger",
                            destinations = cms.untracked.vstring('warnings',
                                                                 'errors',
                                                                 'infos',
                                                                 'debugs'),
                            categories = cms.untracked.vstring('ForwardSim',
                                                               'TotemRP'),
                            debugModules = cms.untracked.vstring('*'),
                            errors = cms.untracked.PSet(
                                threshold = cms.untracked.string('ERROR')
                            ),
                            warnings = cms.untracked.PSet(
                                threshold = cms.untracked.string('WARNING')
                            ),
                            infos = cms.untracked.PSet(
                                threshold = cms.untracked.string('INFO')
                            ),
                            debugs = cms.untracked.PSet(
                                threshold = cms.untracked.string('DEBUG'),
                                INFO = cms.untracked.PSet(
                                    limit = cms.untracked.int32(0)
                                ),
                                DEBUG = cms.untracked.PSet(
                                    limit = cms.untracked.int32(0)
                                ),
                                TotemRP = cms.untracked.PSet(
                                    limit = cms.untracked.int32(1000000)
                                ),
                                ForwardSim = cms.untracked.PSet(
                                    limit = cms.untracked.int32(1000000)
                                )
                            )
                            )
                            '''

################## STEP 1 - generator
source = cms.Source("EmptySource")

RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService",
                                                   g4SimHits = cms.PSet(initialSeed = cms.untracked.uint32(9876)),
                                                   SimG4Object = cms.PSet(initialSeed =cms.untracked.uint32(9876)),
                                                   RPSiDetDigitizer = cms.PSet(initialSeed =cms.untracked.uint32(137137)),
                                                   DiamondSiDetDigitizer = cms.PSet(initialSeed =cms.untracked.uint32(137137)),
                                                   UFSDSiDetDigitizer = cms.PSet(initialSeed =cms.untracked.uint32(137137)),
                                                   sourceSeed = cms.PSet(initialSeed =cms.untracked.uint32(98765)),
                                                   generator = cms.PSet(initialSeed = cms.untracked.uint32(98766)),
                                                   SmearingGenerator = cms.PSet(initialSeed =cms.untracked.uint32(3849)),
                                                   # T2Digis = cms.PSet(initialSeed =cms.untracked.uint32(98765)),
                                                   # T2MCl = cms.PSet(initialSeed =cms.untracked.uint32(24141)),
                                                   RPFastStationSimulation = cms.PSet(initialSeed =cms.untracked.uint32(12)),
                                                   RPFastFullSimulation = cms.PSet(initialSeed =cms.untracked.uint32(13)),
                                                   mix = cms.PSet(initialSeed = cms.untracked.uint32(24141)),
                                                   LHCTransport = cms.PSet(initialSeed = cms.untracked.uint32(24143), engineName = cms.untracked.string('TRandom3')
                                                                           )

                                                   )
################# STEP 2 SmearingGenerator
SmearingGenerator = cms.EDProducer("GaussEvtVtxEnergyGenerator",
                                           src   = cms.InputTag("generator"),
                                           MeanX = cms.double(0.0),
                                           MeanY = cms.double(0.0),
                                           MeanZ = cms.double(0.0),
                                           SigmaX = cms.double(0.000001),
                                           SigmaY = cms.double(0.000001),
                                           SigmaZ = cms.double(0.000001),
                                           TimeOffset = cms.double(0.0)
                                           )
# declare optics parameters
BeamOpticsParamsESSource = cms.ESSource("BeamOpticsParamsESSource",
                                                BeamEnergy = cms.double(6500.0), # Gev
                                                ProtonMass = cms.double(0.938272029), # Gev
                                                LightSpeed = cms.double(300000000.0),
                                                NormalizedEmittanceX = cms.double(3.75e-06),
                                                NormalizedEmittanceY = cms.double(3.75e-06),
                                                BetaStarX = cms.double(0.4), # m
                                                BetaStarY = cms.double(0.4), # m
                                                CrossingAngleX = cms.double(150e-6),
                                                CrossingAngleY = cms.double(0.0),
                                                BeamDisplacementX = cms.double(0.0), # m
                                                BeamDisplacementY = cms.double(0.0), # m
                                                BeamDisplacementZ = cms.double(0.0), # m
                                                BunchSizeZ = cms.double(0.07), # m
                                                MeanXi = cms.double(0.0), # energy smearing
                                                SigmaXi = cms.double(0.0001)
                                                )

ProtonTransportFunctionsESSource = cms.ESProducer("ProtonTransportFunctionsESSource",
                                                          opticsFile = cms.string(''), # automatic
                                                          maySymmetrize = cms.bool(True), # this optic is assymmetric
                                                          verbosity = cms.untracked.uint32(0)
                                                          )

# ################## STEP 3 process.g4SimHits
# g4SimHits properties to be defined in actual config file

ctppsGeometryESModule = cms.ESProducer("CTPPSGeometryESModule",
                                                 verbosity = cms.untracked.uint32(1),
                                               compactViewTag = cms.string('XMLIdealGeometryESSource_CTPPS')
                                                 )

# ################## Step 4 - Magnetic field configuration
magfield = cms.ESSource("XMLIdealGeometryESSource",
                                geomXMLFiles = cms.vstring('Geometry/CMSCommonData/data/normal/cmsextent.xml',
                                                           'Geometry/CMSCommonData/data/cms.xml',
                                                           'Geometry/CMSCommonData/data/cmsMagneticField.xml',
                                                           'MagneticField/GeomBuilder/data/MagneticFieldVolumes_1103l.xml',
                                                           'Geometry/CMSCommonData/data/materials.xml'),
                                rootNodeName = cms.string('cmsMagneticField:MAGF')
                                )
ParametrizedMagneticFieldProducer = cms.ESProducer("ParametrizedMagneticFieldProducer",
                                                           version = cms.string('OAE_1103l_071212'),
                                                           parameters = cms.PSet(
                                                               BValue = cms.string('3_8T')
                                                           ),
                                                           label = cms.untracked.string('parametrizedField')
                                                           )

VolumeBasedMagneticFieldESProducer = cms.ESProducer("VolumeBasedMagneticFieldESProducer",
                                                            scalingVolumes = cms.vint32(14100, 14200, 17600, 17800, 17900,
                                                                                        18100, 18300, 18400, 18600, 23100,
                                                                                        23300, 23400, 23600, 23800, 23900,
                                                                                        24100, 28600, 28800, 28900, 29100,
                                                                                        29300, 29400, 29600, 28609, 28809,
                                                                                        28909, 29109, 29309, 29409, 29609,
                                                                                        28610, 28810, 28910, 29110, 29310,
                                                                                        29410, 29610, 28611, 28811, 28911,
                                                                                        29111, 29311, 29411, 29611),
                                                            scalingFactors = cms.vdouble(1, 1, 0.994, 1.004, 1.004,
                                                                                         1.005, 1.004, 1.004, 0.994, 0.965,
                                                                                         0.958, 0.958, 0.953, 0.958, 0.958,
                                                                                         0.965, 0.918, 0.924, 0.924, 0.906,
                                                                                         0.924, 0.924, 0.918, 0.991, 0.998,
                                                                                         0.998, 0.978, 0.998, 0.998, 0.991,
                                                                                         0.991, 0.998, 0.998, 0.978, 0.998,
                                                                                         0.998, 0.991, 0.991, 0.998, 0.998,
                                                                                         0.978, 0.998, 0.998, 0.991),
                                                            useParametrizedTrackerField = cms.bool(True),
                                                            label = cms.untracked.string(''),
                                                            version = cms.string('grid_1103l_090322_3_8t'),
                                                            debugBuilder = cms.untracked.bool(False),
                                                            paramLabel = cms.string('parametrizedField'),
                                                            geometryVersion = cms.int32(90322),
                                                            gridFiles = cms.VPSet(cms.PSet(
                                                                path = cms.string('grid.[v].bin'),
                                                                master = cms.int32(1),
                                                                volumes = cms.string('1-312'),
                                                                sectors = cms.string('0')
                                                            ),
                                                                cms.PSet(
                                                                    path = cms.string('S3/grid.[v].bin'),
                                                                    master = cms.int32(3),
                                                                    volumes = cms.string('176-186,231-241,286-296'),
                                                                    sectors = cms.string('3')
                                                                ),
                                                                cms.PSet(
                                                                    path = cms.string('S4/grid.[v].bin'),
                                                                    master = cms.int32(4),
                                                                    volumes = cms.string('176-186,231-241,286-296'),
                                                                    sectors = cms.string('4')
                                                                ),
                                                                cms.PSet(
                                                                    path = cms.string('S9/grid.[v].bin'),
                                                                    master = cms.int32(9),
                                                                    volumes = cms.string('14,15,20,21,24-27,32,33,40,41,48,49,56,57,62,63,70,71,286-296'),
                                                                    sectors = cms.string('9')
                                                                ),
                                                                cms.PSet(
                                                                    path = cms.string('S10/grid.[v].bin'),
                                                                    master = cms.int32(10),
                                                                    volumes = cms.string('14,15,20,21,24-27,32,33,40,41,48,49,56,57,62,63,70,71,286-296'),
                                                                    sectors = cms.string('10')
                                                                ),
                                                                cms.PSet(
                                                                    path = cms.string('S11/grid.[v].bin'),
                                                                    master = cms.int32(11),
                                                                    volumes = cms.string('14,15,20,21,24-27,32,33,40,41,48,49,56,57,62,63,70,71,286-296'),
                                                                    sectors = cms.string('11')
                                                                )),
                                                            cacheLastVolume = cms.untracked.bool(True)
                                                            )

# ################## STEP 5 mix pdt_cfi
from SimGeneral.MixingModule.mixObjects_cfi import *

mix = cms.EDProducer("MixingModule",
                             moduleLabel = cms.untracked.string("mix"),
                             digitizers = cms.PSet(),
                             LabelPlayback = cms.string(''),
                             maxBunch = cms.int32(3),
                             minBunch = cms.int32(-5), ## in terms of 25 ns

                             bunchspace = cms.int32(25),
                             mixProdStep1 = cms.bool(False),
                             mixProdStep2 = cms.bool(False),

                             playback = cms.untracked.bool(False),
                             useCurrentProcessOnly = cms.bool(False),
                             mixObjects = cms.PSet(
                                 mixCH = cms.PSet(
                                     mixCaloHits
                                 ),
                                 mixTracks = cms.PSet(
                                     mixSimTracks
                                 )
                                 ,
                                 mixVertices = cms.PSet(
                                     mixSimVertices
                                 ),
                                 mixSH = cms.PSet(
                                     mixSimHits
                                 ),
                                 mixHepMC = cms.PSet(
                                     mixHepMCProducts
                                 )
                             )
                             )