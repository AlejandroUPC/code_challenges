import argparse
from ccwc.funcs import count_bytes, count_lines, count_words
parser = argparse.ArgumentParser()
parser.add_argument("file", help="Path to the file to evaluate.")
parser.add_argument("-c", action="store_true", help="Return the number of bytes in file.")
parser.add_argument("-l", action="store_true", help="Return the number of lines in a file.")
parser.add_argument("-w", action="store_true", help="Return the number of words in a file.")
args = parser.parse_args()
print(args)
if args.c:
    print(f"{count_bytes(args.file)} {args.file}")
if args.l:
    with open(args.file, 'r') as f:
        print(f"{count_lines(f)} {args.file}")
if args.w:
    with open(args.file, 'r') as f:
         print(f"{count_words(f)} {args.file}")
