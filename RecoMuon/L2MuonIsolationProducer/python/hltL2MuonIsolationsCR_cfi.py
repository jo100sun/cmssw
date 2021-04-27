import FWCore.ParameterSet.Config as cms
import RecoMuon.L2MuonIsolationProducer.hltL2MuonIsolations_cfi as _mod

hltL2MuonIsolationsCR = _mod.hltL2MuonIsolations.clone(
    StandAloneCollectionLabel = cms.InputTag("L2Muons","UpdatedAtVtx"),
    IsolatorPSet = cms.PSet( 
      ComponentName = cms.string( "CutsIsolatorWithCorrection" ),
      ConeSizes = cms.vdouble(0.24, 0.24, 0.24, 0.24, 0.24, 
        0.24, 0.24, 0.24, 0.24, 0.24, 
        0.24, 0.24, 0.24, 0.24, 0.24, 
        0.24, 0.24, 0.24, 0.24, 0.24, 
        0.24, 0.24, 0.24, 0.24, 0.24, 
        0.24),
      Thresholds = cms.vdouble(5.5, 5.5, 5.9, 5.7, 5.1, 
        4.9, 5.0, 5.0, 5.1, 5.0, 
        4.8, 4.8, 4.7, 4.7, 3.5, 
        3.1, 3.5, 3.9, 3.7, 3.7, 
        3.5, 3.5, 3.2, 3.3, 3.4, 
        3.4),
      EtaBounds = cms.vdouble(0.0435, 0.1305, 0.2175, 0.3045, 0.3915, 
        0.4785, 0.5655, 0.6525, 0.7395, 0.8265, 
        0.9135, 1.0005, 1.0875, 1.1745, 1.2615, 
        1.3485, 1.4355, 1.5225, 1.6095, 1.6965, 
        1.785, 1.88, 1.9865, 2.1075, 2.247, 
        2.411),
      ConeSizesRel = cms.vdouble(0.24, 0.24, 0.24, 0.24, 0.24, 
        0.24, 0.24, 0.24, 0.24, 0.24, 
        0.24, 0.24, 0.24, 0.24, 0.24, 
        0.24, 0.24, 0.24, 0.24, 0.24, 
        0.24, 0.24, 0.24, 0.24, 0.24, 
        0.24),
#some mild nonsense numbers
      ThresholdsRel = cms.vdouble(0.155, 0.155, 0.159, 0.157, 0.151, 
        0.149, 0.150, 0.150, 0.151, 0.150, 
        0.148, 0.148, 0.147, 0.147, 0.135, 
        0.131, 0.135, 0.139, 0.137, 0.137, 
        0.135, 0.135, 0.132, 0.133, 0.134, 
        0.134),
      EtaBoundsRel = cms.vdouble(0.0435, 0.1305, 0.2175, 0.3045, 0.3915, 
        0.4785, 0.5655, 0.6525, 0.7395, 0.8265, 
        0.9135, 1.0005, 1.0875, 1.1745, 1.2615, 
        1.3485, 1.4355, 1.5225, 1.6095, 1.6965, 
        1.785, 1.88, 1.9865, 2.1075, 2.247, 
        2.411),
      CutAbsoluteIso = cms.bool(True),
      CutRelativeIso = cms.bool(False),
      UseRhoCorrection = cms.bool(False),
      RhoSrc = cms.InputTag('hltKT6CaloJets','rho'),
      RhoMax = cms.double(9.9999999E7),
      RhoScaleBarrel = cms.double(1.0),
      RhoScaleEndcap = cms.double(1.0),
      EffAreaSFBarrel = cms.double(1.0),
      EffAreaSFEndcap = cms.double(1.0),
#only one should be on 
      ReturnAbsoluteSum = cms.bool(True),
      ReturnRelativeSum = cms.bool(False),
      AndOrCuts = cms.bool(True)
    ),
    WriteIsolatorFloat = cms.bool(False),
#    OutputMuIsoDeposits = cms.bool(True),
    ExtractorPSet = cms.PSet(
        DR_Veto_H = cms.double(0.1),
        Vertex_Constraint_Z = cms.bool(False),
        Threshold_H = cms.double(0.5),
        ComponentName = cms.string('CaloExtractor'),
        Threshold_E = cms.double(0.2),
        DR_Max = cms.double(1.0),
        DR_Veto_E = cms.double(0.07),
        Weight_E = cms.double(1.5),
        Vertex_Constraint_XY = cms.bool(False),
        DepositLabel = cms.untracked.string('EcalPlusHcal'),
        CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
        Weight_H = cms.double(1.0)
    )
)



