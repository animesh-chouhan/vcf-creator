import argparse
from .vcf import  vcard_generator

usage = "usage: vcf_creator [options]"
parser = argparse.ArgumentParser(usage)

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

args= parser.parse_args()

if args.out == None:
  out_file = args.filename.split(".")[0] + ".vcf"
else:
  out_file = args.out + ".vcf"

res = vcard_generator(args.filename)
if res != 0:
  with open(out_file , "w+") as file:
    file.write(res)
    print("Done processing.")
