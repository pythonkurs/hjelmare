# Gets the NYC escalator outage data from a webservice. Then calculates the fraction that are out for repairs.
import untangle, requests
def fraction_repairs():
    r = requests.get("http://www.grandcentral.org/developers/data/nyct/nyct_ene.xml")
    xml_file = r.content
    doc = untangle.parse(xml_file)
    outages = doc.NYCOutages.outage
    numberOutages=len(outages)
    numberRepairs=0
    for outage in outages:
        if outage.reason.cdata == "REPAIR":
            numberRepairs += 1
    fractionRepairs = float(numberRepairs) / numberOutages
    return fractionRepairs
