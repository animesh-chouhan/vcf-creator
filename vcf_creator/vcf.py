import csv
import os.path

ATTRIBUTES = {
    "name": "FN",
    "organisation": "ORG",
    "phone": "TEL;WORK;VOICE",
    "email": "EMAIL",
    "address": "ADR;HOME",
    "birthday": "BDAY",
    "anniversary": "ANNIVERSARY",
}

attributes_present = {}

def vcard_formatter(values):
    """
    Parameters
    ---------
    values: array of data present in a row

    Returns
    -------
    str
        a string of vcard formatted row
    """

    ret = ["BEGIN:VCARD", "VERSION:4.0"]

    for attr in ATTRIBUTES.keys():
        if attr in attributes_present.keys():
            ret.append(ATTRIBUTES[attr] + ":" + values[attributes_present[attr]])
    
    ret.append("END:VCARD")
    return "\n".join(ret)
    
def vcard_generator(filename):
    """
    Parameters
    ---------
    filename: csv file to process
       
    Returns
    -------
    str
        a string of vcard formatted data
    
    """

    # Check if the file exists
    if not os.path.isfile(filename):                        
        print("File doesn't exist.")
        return 0
    else:
        print("File found. Processing...")
        with open(filename, newline='') as csvfile:
            # Perform various checks on the csv dialect
            try:
                dialect = csv.Sniffer().sniff(csvfile.readline())
                # Reset the read position back to the start
                csvfile.seek(0)
            except csv.Error:
                print("File appears not to be in csv format.")
                return 0

            # Read the csv file
            reader = csv.reader(csvfile, dialect)
            # Get header
            header = reader.__next__()
            # Iterate over the rows
            for i, attr in enumerate(header):
                attributes_present[attr] = i
            
            ret = []
            for row in reader:
                ret.append(vcard_formatter(row))
            return "\n".join(ret)
