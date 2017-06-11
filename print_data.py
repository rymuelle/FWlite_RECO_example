import ROOT
from DataFormats.FWLite import Events, Handle

events = Events ('8660679E-9E78-E611-BA80-02163E0142C5.root')
#events = Events ('singleMuon_13TeV.root')


#handle  = Handle ('std::vector<reco::Muon>')
handle  = Handle ('std::vector<reco::Track>')

# like and edm::InputTag
#label = ("globalMuons::HLT")
label = ("ALCARECOMuAlCalIsolatedMu:GlobalMuon")


ROOT.gROOT.SetBatch()
#fileOut =  "13TeV_realistic"
fileOut =  "run2016G_globalMuons"

outFile = ROOT.TFile("{}.root".format(fileOut), "recreate")

ROOT.gROOT.SetStyle('Plain') # white background
zmassHist = ROOT.TH1F ("zmass", "Z Candidate Mass", 50, 50, 100)
muon_pt = ROOT.TH1F ("muon_pt", "muon pt", 50, 0, 250)
muon_eta = ROOT.TH1F ("muon_eta", "muon eta", 50, -4, 4)
muon_phi = ROOT.TH1F ("muon_phi", "muon phi", 50, -3.3, 3.3)





# loop over events
for event in events:
    # use getByLabel, just like in cmsRun
    event.getByLabel (label, handle)
    # get the product
    muons = handle.product()
    # use muons to make Z peak
    numMuons = len (muons)
    for count in range(numMuons):
        muon = muons[count]
        if muon.pt() < 30: continue
        muon_pt.Fill(muon.pt())
        muon_eta.Fill(muon.eta())
        muon_phi.Fill(muon.phi())

#    if muons < 2: continue
#    for outer in xrange (numMuons - 1):
#        outerMuon = muons[outer]
#        for inner in xrange (outer + 1, numMuons):
#            innerMuon = muons[inner]
#            if outerMuon.charge() * innerMuon.charge() >= 0:
#                continue
#            inner4v = ROOT.TLorentzVector (innerMuon.px(), innerMuon.py(),
#                                           innerMuon.pz(), innerMuon.energy())
#            outer4v = ROOT.TLorentzVector (outerMuon.px(), outerMuon.py(),
#                                           outerMuon.pz(), outerMuon.energy())
#            if (inner4v + outer4v).M() > 1000:zmassHist.Fill( (inner4v + outer4v).M() )
# make a canvas, draw, and save it
c1 = ROOT.TCanvas()
zmassHist.Draw()
c1.Print ("zmass_py.png")

muon_pt.Draw()
c1.SaveAs("muon_pt.png")
muon_eta.Draw()
c1.SaveAs("muon_eta.png")
muon_phi.Draw()
c1.SaveAs("muon_phi.png")

outFile.Write()
outFile.Close()

'''
vector<reco::Muon>                    "muons"                     ""                "RECO"

vector<reco::Muon>                    "ALCARECOMuAlCalIsolatedMu"   "SelectedMuons"   "RECO"


/afs/cern.ch/work/r/rymuelle/public/8_0_X_Align/CMSSW_8_0_17/src/8660679E-9E78-E611-BA80-02163E0142C5.root
import ROOT
from DataFormats.FWLite import Events, Handle


events = Events (8660679E-9E78-E611-BA80-02163E0142C5.root)

handle  = Handle (std::vector<reco::Track>

label = ("GlobalMuon")

ROOT.gROOT.SetBatch() 

for event in events:
	event.getByLabel (label, handle)
 	muons = handle.product()

	numMuons = len (muons)
    if muons < 2: continue
    for outer in xrange (numMuons - 1):
        outerMuon = muons[outer]
    	for inner in xrange (outer + 1, numMuons):
    	      innerMuon = muons[inner]
    	      if outerMuon.charge() * innerMuon.charge() >= 0:
    	          continue
    	 	  print innerMuon.energy()


    	 	  /afs/cern.ch/work/r/rymuelle/public/8_0_X_Align/CMSSW_8_0_17/src
    	 	  '''