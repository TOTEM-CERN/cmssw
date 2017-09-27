from SimG4Core.Application.hectorParameter_cfi import *
import FWCore.ParameterSet.Config as cms

# Configure the output module (save the result in a file)
o1 = cms.OutputModule("PoolOutputModule",
                              outputCommands = cms.untracked.vstring('keep *'),
                              fileName = cms.untracked.string('file:test.root')
                              )
outpath = cms.EndPath(o1)

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

# g4sh

totemGeomXMLFiles = cms.vstring(
    'Geometry/CMSCommonData/data/materials.xml',
    'Geometry/CMSCommonData/data/rotations.xml',
    'Geometry/CMSCommonData/data/extend/cmsextent.xml',
    'Geometry/CMSCommonData/data/cms.xml',
    'Geometry/CMSCommonData/data/beampipe/2015/v1/beampipe.xml',
    'Geometry/CMSCommonData/data/cmsBeam.xml',
    'Geometry/CMSCommonData/data/cmsMother.xml',
    'Geometry/CMSCommonData/data/mgnt.xml',
    'Geometry/ForwardCommonData/data/forward.xml',
    'Geometry/ForwardCommonData/data/totemRotations.xml',
    'Geometry/ForwardCommonData/data/totemMaterials.xml',
    'Geometry/ForwardCommonData/data/totemt1.xml',
    'Geometry/ForwardCommonData/data/totemt2.xml',
    'Geometry/ForwardCommonData/data/ionpump.xml',
    'Geometry/VeryForwardData/data/RP_Box.xml',
    'Geometry/VeryForwardData/data/RP_Box/RP_Box_000.xml',
    'Geometry/VeryForwardData/data/RP_Box/RP_Box_001.xml',
    'Geometry/VeryForwardData/data/RP_Box/RP_Box_002.xml',
    'Geometry/VeryForwardData/data/RP_Box/RP_Box_003.xml',
    'Geometry/VeryForwardData/data/RP_Box/RP_Box_004.xml',
    'Geometry/VeryForwardData/data/RP_Box/RP_Box_005.xml',
    'Geometry/VeryForwardData/data/RP_Box/RP_Box_020.xml',
    'Geometry/VeryForwardData/data/RP_Box/RP_Box_021.xml',
    'Geometry/VeryForwardData/data/RP_Box/RP_Box_022.xml',
    'Geometry/VeryForwardData/data/RP_Box/RP_Box_023.xml',
    'Geometry/VeryForwardData/data/RP_Box/RP_Box_024.xml',
    'Geometry/VeryForwardData/data/RP_Box/RP_Box_025.xml',
    'Geometry/VeryForwardData/data/RP_Box/RP_Box_100.xml',
    'Geometry/VeryForwardData/data/RP_Box/RP_Box_101.xml',
    'Geometry/VeryForwardData/data/RP_Box/RP_Box_102.xml',
    'Geometry/VeryForwardData/data/RP_Box/RP_Box_103.xml',
    'Geometry/VeryForwardData/data/RP_Box/RP_Box_104.xml',
    'Geometry/VeryForwardData/data/RP_Box/RP_Box_105.xml',
    'Geometry/VeryForwardData/data/RP_Box/RP_Box_120.xml',
    'Geometry/VeryForwardData/data/RP_Box/RP_Box_121.xml',
    'Geometry/VeryForwardData/data/RP_Box/RP_Box_122.xml',
    'Geometry/VeryForwardData/data/RP_Box/RP_Box_123.xml',
    'Geometry/VeryForwardData/data/RP_Box/RP_Box_124.xml',
    'Geometry/VeryForwardData/data/RP_Box/RP_Box_125.xml',
    'Geometry/VeryForwardData/data/RP_Hybrid.xml',
    'Geometry/VeryForwardData/data/RP_Materials.xml',
    'Geometry/VeryForwardData/data/RP_Transformations.xml',
    'Geometry/VeryForwardData/data/RP_Detectors_Assembly.xml',
    'Geometry/VeryForwardData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_000.xml',
    'Geometry/VeryForwardData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_001.xml',
    'Geometry/VeryForwardData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_002.xml',
    'Geometry/VeryForwardData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_003.xml',
    'Geometry/VeryForwardData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_004.xml',
    'Geometry/VeryForwardData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_005.xml',
    'Geometry/VeryForwardData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_020.xml',
    'Geometry/VeryForwardData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_021.xml',
    'Geometry/VeryForwardData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_022.xml',
    # 'Geometry/VeryForwardData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_023.xml',  # this RP is now equipped with pixels
    'Geometry/VeryForwardData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_024.xml',
    'Geometry/VeryForwardData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_025.xml',
    'Geometry/VeryForwardData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_100.xml',
    'Geometry/VeryForwardData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_101.xml',
    'Geometry/VeryForwardData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_102.xml',
    'Geometry/VeryForwardData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_103.xml',
    'Geometry/VeryForwardData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_104.xml',
    'Geometry/VeryForwardData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_105.xml',
    'Geometry/VeryForwardData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_120.xml',
    'Geometry/VeryForwardData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_121.xml',
    'Geometry/VeryForwardData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_122.xml',
    # 'Geometry/VeryForwardData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_123.xml',  # this RP is now equipped with pixels
    'Geometry/VeryForwardData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_124.xml',
    'Geometry/VeryForwardData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_125.xml',
    'Geometry/VeryForwardData/data/RP_Device.xml',
    'Geometry/VeryForwardData/data/RP_Vertical_Device.xml',
    'Geometry/VeryForwardData/data/RP_Horizontal_Device.xml',
    'Geometry/VeryForwardData/data/RP_220_Right_Station.xml',
    'Geometry/VeryForwardData/data/RP_220_Left_Station.xml',
    'Geometry/VeryForwardData/data/RP_147_Right_Station.xml',
    'Geometry/VeryForwardData/data/RP_147_Left_Station.xml',
    'Geometry/VeryForwardData/data/RP_Stations_Assembly.xml',
    'Geometry/VeryForwardData/data/RP_Sensitive_Dets.xml',
    'Geometry/VeryForwardData/data/RP_Cuts_Per_Region.xml',
    'Geometry/VeryForwardData/data/RP_Param_Beam_Region.xml')

ctppsDiamondGeomXMLFiles = cms.vstring(
    # diamond detectors
    'Geometry/VeryForwardData/data/CTPPS_Diamond_Materials.xml',
    'Geometry/VeryForwardData/data/CTPPS_Diamond_Transformations.xml',
    'Geometry/VeryForwardData/data/CTPPS_Diamond_X_Distance.xml',
    'Geometry/VeryForwardData/data/CTPPS_Diamond_Parameters.xml',
    'Geometry/VeryForwardData/data/CTPPS_Timing_Station_Parameters.xml',
    'Geometry/VeryForwardData/data/CTPPS_Timing_Horizontal_Pot.xml',
    'Geometry/VeryForwardData/data/CTPPS_Timing_Positive_Station.xml',
    'Geometry/VeryForwardData/data/CTPPS_Timing_Negative_Station.xml',
    'Geometry/VeryForwardData/data/CTPPS_Timing_Stations_Assembly.xml',
    'Geometry/VeryForwardData/data/CTPPS_Diamond_Segments/CTPPS_Diamond_Pattern1_Segment1.xml',
    'Geometry/VeryForwardData/data/CTPPS_Diamond_Segments/CTPPS_Diamond_Pattern2_Segment1.xml',
    'Geometry/VeryForwardData/data/CTPPS_Diamond_Segments/CTPPS_Diamond_Pattern2_Segment2.xml',
    'Geometry/VeryForwardData/data/CTPPS_Diamond_Segments/CTPPS_Diamond_Pattern3_Segment1.xml',
    'Geometry/VeryForwardData/data/CTPPS_Diamond_Segments/CTPPS_Diamond_Pattern3_Segment2.xml',
    'Geometry/VeryForwardData/data/CTPPS_Diamond_Segments/CTPPS_Diamond_Pattern3_Segment3.xml',
    'Geometry/VeryForwardData/data/CTPPS_Diamond_Segments/CTPPS_Diamond_Pattern3_Segment4.xml',
    'Geometry/VeryForwardData/data/CTPPS_Diamond_Segments/CTPPS_Diamond_Pattern4_Segment1.xml',
    'Geometry/VeryForwardData/data/CTPPS_Diamond_Segments/CTPPS_Diamond_Pattern4_Segment2.xml',
    'Geometry/VeryForwardData/data/CTPPS_Diamond_Segments/CTPPS_Diamond_Pattern4_Segment3.xml',
    'Geometry/VeryForwardData/data/CTPPS_Diamond_Segments/CTPPS_Diamond_Pattern4_Segment4.xml',
    'Geometry/VeryForwardData/data/CTPPS_Diamond_Segments/CTPPS_Diamond_Pattern4_Segment5.xml',
    'Geometry/VeryForwardData/data/CTPPS_Diamond_Planes/CTPPS_Diamond_Plane1.xml',
    'Geometry/VeryForwardData/data/CTPPS_Diamond_Planes/CTPPS_Diamond_Plane2.xml',
    'Geometry/VeryForwardData/data/CTPPS_Diamond_Planes/CTPPS_Diamond_Plane3.xml',
    #'Geometry/VeryForwardData/data/CTPPS_Diamond_Planes/CTPPS_Diamond_Plane4.xml',     # being replaced by UFSD
    'Geometry/VeryForwardData/data/CTPPS_Diamond_Detector_Assembly.xml',
    'Geometry/VeryForwardData/data/CTPPS_Diamond_Sensitive_Dets.xml',
)

ctppsUFSDGeomXMLFiles = cms.vstring(
    # UFSDetectors
    'Geometry/VeryForwardData/data/CTPPS_UFSD_Segments/CTPPS_UFSD_Pattern1.xml',
    'Geometry/VeryForwardData/data/CTPPS_UFSD_Segments/CTPPS_UFSD_Pattern2_SegmentA.xml',
    'Geometry/VeryForwardData/data/CTPPS_UFSD_Segments/CTPPS_UFSD_Pattern2_SegmentB.xml',
    'Geometry/VeryForwardData/data/CTPPS_UFSD_Planes/CTPPS_UFSD_Plane4.xml',
    'Geometry/VeryForwardData/data/CTPPS_UFSD_Parameters.xml',
    'Geometry/VeryForwardData/data/CTPPS_UFSD_Sensitive_Dets.xml',
)


# pixel files
ctppsPixelGeomXMLFiles = cms.vstring(
    'Geometry/VeryForwardData/data/ppstrackerMaterials.xml',
    'Geometry/VeryForwardData/data/CTPPS_Pixel_Module.xml',
    'Geometry/VeryForwardData/data/CTPPS_Pixel_Module_2x2.xml',
    'Geometry/VeryForwardData/data/CTPPS_Pixel_Assembly_Box_Real_023.xml',
    'Geometry/VeryForwardData/data/CTPPS_Pixel_Assembly_Box_Real_123.xml',
    'Geometry/VeryForwardData/data/CTPPS_Pixel_Sens.xml'
)

XMLIdealGeometryESSource = cms.ESSource("XMLIdealGeometryESSource",
                                                geomXMLFiles = totemGeomXMLFiles+ctppsDiamondGeomXMLFiles+ctppsUFSDGeomXMLFiles+ctppsPixelGeomXMLFiles,
                                                rootNodeName = cms.string('cms:CMSE')
                                                )

# position of RPs
XMLIdealGeometryESSource.geomXMLFiles.append("Geometry/VeryForwardData/data/CTPPS_Diamond_X_Distance.xml")
XMLIdealGeometryESSource.geomXMLFiles.append("Geometry/VeryForwardData/data/2017_07_08_fill5912/RP_Dist_Beam_Cent.xml")

# extended geometries
ctppsGeometryESModule = cms.ESProducer("CTPPSGeometryESModule",
                                                 verbosity = cms.untracked.uint32(1),
                                               compactViewTag = cms.string('XMLIdealGeometryESSource_CTPPS')
                                                 )


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

# ################## STEP 4 mix pdt_cfi
#
from SimGeneral.MixingModule.mixObjects_cfi import *
from SimGeneral.MixingModule.pixelDigitizer_cfi import *
from SimGeneral.MixingModule.stripDigitizer_cfi import *
from SimGeneral.MixingModule.ecalDigitizer_cfi import *
from SimGeneral.MixingModule.hcalDigitizer_cfi import *
from SimGeneral.MixingModule.castorDigitizer_cfi import *
from SimGeneral.MixingModule.trackingTruthProducer_cfi import *

mix = cms.EDProducer("MixingModule",
                             moduleLabel = cms.untracked.string("mix"),
                             digitizers = cms.PSet(
                                 #     pixel = cms.PSet(
                                 #       pixelDigitizer
                                 #     )
                                 #                         ,
                                 #       strip = cms.PSet(
                                 #     stripDigitizer
                                 #       )
                                 #                           ,
                                 #     ecal = cms.PSet(
                                 #       ecalDigitizer
                                 #     ),
                                 # #     hcal = cms.PSet(
                                 # #       hcalDigitizer
                                 # #     ),
                                 #     castor  = cms.PSet(
                                 #       castorDigitizer
                                 #     ),
                                 #     mergedtruth = cms.PSet(
                                 #         trackingParticles
                                 #     )
                             ),
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


#from SimGeneral/MixingModule/python/mix_Objects_cfi.py
mix.mixObjects.mixSH.input =  cms.VInputTag(  # note that this list needs to be in the same order as the subdets
    cms.InputTag("g4SimHits","TotemHitsRP"),
    cms.InputTag("g4SimHits","CTPPSHitsDiamond"),
    cms.InputTag("g4SimHits","CTPPSHitsUFSD"),
    cms.InputTag("g4SimHits","CTPPSHitsPixel"))

mix.mixObjects.mixSH.subdets = cms.vstring(
    'TotemHitsRP',
    'CTPPSHitsDiamond',
    'CTPPSHitsUFSD',
    'CTPPSHitsPixel'
)

mix.mixObjects.mixSH.crossingFrames = cms.untracked.vstring('TotemHitsRP',
                                                                    'CTPPSHitsDiamond',
                                                                    'CTPPSHitsUFSD',
                                                                    'CTPPSHitsPixel'
                                                                    )