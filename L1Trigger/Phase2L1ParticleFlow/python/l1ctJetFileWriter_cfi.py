import FWCore.ParameterSet.Config as cms

l1ctSeededConeJetFileWriter = cms.EDAnalyzer('L1CTJetFileWriter',
  collections = cms.untracked.VPSet([cms.PSet(jets = cms.InputTag("sc4PFL1PuppiCorrectedEmulator"),
                                              mht  = cms.InputTag("sc4PFL1PuppiCorrectedEmulatorMHT"))]),
  nJets = cms.uint32(12),
  nFramesPerBX = cms.uint32(9), # 360 MHz clock or 25 Gb/s link
  TMUX = cms.uint32(6),
  maxLinesPerFile = cms.uint32(1024),
  outputFilename = cms.string("L1CTSCJetsPatterns"),
  format = cms.string("EMP")
)
