import csv
import os.path
import logging

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

ATTRIBUTES = {
    "name": ["FN", "N"],
    "organisation": "ORG",
    "phone": "TEL;WORK;VOICE",
    "email": "EMAIL",
    "address": "ADR;HOME",
    "birthday": "BDAY"
}

# ATTRIBUTES = {
#     "FN": "name",
#     "N": "name",
#     "ORG": "organisation",
#     "TEL;WORK;VOICE": "phone",
#     "EMAIL": "email",
#     "ADR;HOME": "address",
#     "BDAY": "birthday"
# }

attributes_present = {}


def vcard_formatter(row):
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

    for vcf_attr in ATTRIBUTES.keys():
        if vcf_attr in attributes_present.keys():
            # Taking FN and N in account
            if type(ATTRIBUTES[vcf_attr]) == list:
                for multiple in ATTRIBUTES[vcf_attr]:
                    ret.append(multiple + ":" +
                               row[attributes_present[vcf_attr]])
            else:
                ret.append(ATTRIBUTES[vcf_attr] + ":" +
                           row[attributes_present[vcf_attr]])

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
        # print("File doesn't exist.")
        logging.error("File doesn't exist.")
        return -1
    else:
        # print("File found. Processing...")
        logging.info("File found. Processing...")
        with open(filename, newline='') as csvfile:
            # Perform various checks on the csv dialect
            try:
                head = csvfile.readline()
                logging.info("Header is " + head.strip())
                dialect = csv.Sniffer().sniff(head)
                # Reset the read position back to the start
                csvfile.seek(0)
            except csv.Error:
                # print("File appears not to be in csv format.")
                logging.error("File appears not to be in csv format.")
                return -1

            # Read the csv file
            reader = csv.reader(csvfile, dialect)
            # Get header
            header = [h.strip().lower() for h in reader.__next__()]
            # Name is required
            if "name" not in header:
                # print("Header not supported.")
                logging.error("Header not supported.")
                return -1

            # Set attributes_present
            for i, attr in enumerate(header):
                attributes_present[attr] = i

            ret = []
            # Iterate over the rows
            for row in reader:
                ret.append(vcard_formatter(row))

            # print("Done processing.")
            logging.info("Done processing.")
            return "\n".join(ret)
