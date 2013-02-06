# Gets the NYC escalator outage data from a webservice. Then calculates the fraction that are out for repairs.
import untangle, requests, sys
def fraction_repairs():
    try:
        r = requests.get("http://www.grandcentral.org/developers/data/nyct/nyct_ene.xml")

    except requests.ConnectionError:
        print("Got connection error. Check network.")
        sys.exit()
    if not r.status_code == 200:
        print("Webserver error, status code: "+str(r.status_code)+". Try again later.")
        sys.exit()
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
