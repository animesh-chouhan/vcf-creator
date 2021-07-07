import argparse
import logging
from .vcf import vcard_generator

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)


def main():
    parser = argparse.ArgumentParser(prog="vcf_creator")

    print("""
     _    ______________   ______                __            
    | |  / / ____/ ____/  / ____/_______  ____ _/ /_____  _____
    | | / / /   / /_     / /   / ___/ _ \/ __ `/ __/ __ \/ ___/
    | |/ / /___/ __/    / /___/ /  /  __/ /_/ / /_/ /_/ / /    
    |___/\____/_/       \____/_/   \___/\__,_/\__/\____/_/                                                             
    """)

    parser.add_argument("filename", type=str, help="input csv file")

    parser.add_argument("-o", "--out",
                        metavar="FILE",
                        help="write output to FILE.vcf "
                        "[default:<input filename>.vcf]")

    args = parser.parse_args()

    if args.out == None:
        out_file = args.filename.split(".")[0] + ".vcf"
    else:
        out_file = args.out + ".vcf"

    res = vcard_generator(args.filename)
    if res != -1:
        with open(out_file, "w+") as file:
            file.write(res)
            # print("vCard file written.")
            logging.info("vCard file written.")
    else:
        logging.error("Exiting.")
