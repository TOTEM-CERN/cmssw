{
gROOT->Reset();

#include <string>
#include <iostream>
#include <math.h>
using namespace std;

// draw 2D reco histograms showing the events on six different RPs
//
// usage: the ROOT file to open should be in TFile file(...)
// you can choose to plot only horizontal RPs (showVertical parameter)
// then run it as a ROOT script
//
// > root
// > .x [path to the script]


// the reco plots in absolute coordinates can be transformed to the coordinates of the detector plane
// translation (xt, yt) + rotation by 'a' degrees
//
// [ cos a	sin a	0	] [ 1	0	xt	] [ x ] [ x2 ]
// [ sin a	-cos a	0	]*[ 0	1	yt	]*[ y ]=[ y2 ]
// [ 0		0	1	] [ 0	0	1	] [ 1 ] [ 1  ]
//

// PARAMS
const bool to_transform = false; 
const bool plotAll = false;
const int chArId = 1;
const int chStId = 0;
TFile file("eliza_300k.root");
// END PARAMS

// CONST
const double xt[24] = { 
0.0, 0.0, 53.423, 19.312, 0.0, 0.0, 
0.0, 0.0, 18.969, 17.577, 0.0, 0.0,
0.0, 0.0, 53.412, 18.792, 0.0, 0.0, 
0.0, 0.0, 18.745, 17.847, 0.0, 0.0 };

const double yt[24] = { 
52.287, -52.636, 0.0, 0.0, 16.563, -16.159, 
16.545, -16.675, 0.0, 0.0, 16.971, -16.974,
52.295, -52.342, 0.0, 0.0, -16.533, 16.191, 
16.550, -16.631, 0.0, 0.0, 16.804, -17.545 };

// rotations - with the tilted right far pots in 210 station
double degree[24] = { 
135.0, -45.0, 45.0, 45.0, 135.0, -45.0, 
135.0, -45.0, 45.0, 45.0, 135.0, -45.0,
135.0, -45.0, 45.0, 53.0, 143.0, -37.0, 
135.0, -45.0, 45.0, 45.0, 135.0, -45.0 };

string rpNames[6] = {"near top", "near bottom", "near horizontal", "far horizontal", "far top", "far bottom"};
string rpGroupNames[2] = {"near", "far"};
const int divX = plotAll ? 3 : 2;
const int divY = plotAll ? 2 : 1;
const int RPCount = divX*divY;
const int plotRange = 70;
const int x_bin_number = 100;
const int y_bin_number = 100;
// END CONST

TTreeReader reader("Events", &file);
TTreeReaderArray<edm::DetSet<TotemRPLocalTrack>> ps(reader, "TotemRPLocalTrackedmDetSetVector_totemRPLocalTrackFitter__TestFlatGun.obj._sets");

TH2D** h = new TH2D*[RPCount]; 

for(int i=0; i<RPCount; ++i) {
	if(!to_transform && !plotAll) h[i] = new TH2D(rpGroupNames[i].c_str(), rpGroupNames[i].c_str(), x_bin_number, -plotRange, plotRange, y_bin_number, -plotRange, plotRange);
	else if(to_transform && !plotAll) h[i] = new TH2D(rpNames[i+2].c_str(), rpNames[i+2].c_str(), x_bin_number, -plotRange, plotRange, y_bin_number, -plotRange, plotRange);
	else h[i] = new TH2D(rpNames[i].c_str(), rpNames[i].c_str(), x_bin_number, -plotRange, plotRange, y_bin_number, -plotRange, plotRange);

	h[i]->GetXaxis()->SetTitle("x [mm]");
	h[i]->GetYaxis()->SetTitle("y [mm]");
}




while (reader.Next()) {
	for (int i=0; i<ps.GetSize(); i++) {
		
		int arId = (ps[i].detId()>> 24) & 0x1;
		int stId = (ps[i].detId()>> 22) & 0x3;
		int rpId = (ps[i].detId()>> 19) & 0x7;
		int plId = (ps[i].detId()>> 15) & 0xF;		//always 0 in reco
		
		if(arId!=chArId || stId!=chStId) continue;
		if(to_transform && !plotAll && rpId!=2 && rpId!=3) continue;

		for (auto &psEl : ps[i]) {  
			double xVal = psEl.getX0();
			double yVal = psEl.getY0();

			int rpPosId = 12*arId + 6*(stId==0 ? 0 : 1) + rpId;	

			//cout << rpPosId << endl;

			double d = degree[rpPosId] * 3.14159 / 180;
			double xVal2 = to_transform ? ((xVal+xt[rpPosId])*cos(d) + (yVal+yt[rpPosId])*sin(d)) : xVal;
			double yVal2 = to_transform ? ((xVal+xt[rpPosId])*sin(d) - (yVal+yt[rpPosId])*cos(d)) : yVal;

			int hId = plotAll ? rpId : (to_transform ? rpId-2 : rpId/3);
			h[hId]->Fill(xVal2, yVal2);
		}

  	}
}

TCanvas *cc = new TCanvas("RPs", "RPs", 1800, 1800*divY/divX); 
cc->Divide(divX, divY);

int j=1;
for(int i=0; i<RPCount; ++i) {
	cc->cd(i+1);
	h[i]->SetStats(false);
	h[i]->Draw("COLZ");
}



}

