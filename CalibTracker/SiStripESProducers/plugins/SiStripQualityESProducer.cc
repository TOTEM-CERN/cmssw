// -*- C++ -*-
//
// Package:    SiStripQualityESProducer
// Class:      SiStripQualityESProducer
// 
/**\class SiStripQualityESProducer SiStripQualityESProducer.h CalibTracker/SiStripESProducers/plugins/SiStripQualityESProducer.cc

 Description: <one line class summary>

 Implementation:
     <Notes on implementation>
*/
//
// Original Author:  Domenico GIORDANO
//         Created:  Wed Oct  3 12:11:10 CEST 2007
// $Id$
//
//



#include "CalibTracker/SiStripESProducers/plugins/SiStripQualityESProducer.h"



SiStripQualityESProducer::SiStripQualityESProducer(const edm::ParameterSet& iConfig):
  pset_(iConfig),
  toGet(iConfig.getParameter<Parameters>("ListOfRecordToMerge"))
{
  
  setWhatProduced(this);
  
  edm::LogInfo("SiStripQualityESProducer") << "ctor" << std::endl;
}


boost::shared_ptr<SiStripQuality> SiStripQualityESProducer::produce(const SiStripQualityRcd& iRecord)
{
  
  edm::LogInfo("SiStripQualityESProducer") << "produce called" << std::endl;

  SiStripQuality* quality = new SiStripQuality();
  edm::ESHandle<SiStripBadStrip> obj;
  std::string tagName;  
  std::string recordName;
  for(Parameters::iterator itToGet = toGet.begin(); itToGet != toGet.end(); ++itToGet ) {
    tagName = itToGet->getParameter<std::string>("tag");
    recordName = itToGet->getParameter<std::string>("record");

    edm::LogInfo("SiStripQualityESProducer") << "[SiStripQualityESProducer::produce] Getting data from record " << recordName << " with tag " << tagName << std::endl;

    if (recordName=="SiStripBadModuleRcd"){
      iRecord.getRecord<SiStripBadModuleRcd>().get(tagName,obj); 
    } else if (recordName=="SiStripBadFiberRcd"){
      iRecord.getRecord<SiStripBadFiberRcd>().get(tagName,obj); 
    } else if (recordName=="SiStripBadChannelRcd"){
      iRecord.getRecord<SiStripBadChannelRcd>().get(tagName,obj); 
    } else {
      edm::LogError("SiStripQualityESProducer") << "[SiStripQualityESProducer::produce] Skipping the requested data for unexisting record " << recordName << " with tag " << tagName << std::endl;
      continue;
    }

    quality->add( obj.product() );    
    edm::LogInfo("SiStripQualityESProducer") << "[SiStripQualityESProducer::produce] Got data from record " << recordName << " with tag " << tagName << std::endl;
  }
  quality->cleanUp();

  boost::shared_ptr<SiStripQuality> pQuality(quality);

  return pQuality ;
}

