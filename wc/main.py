import argparse
from ccwc.funcs import count_bytes, count_lines, count_words, count_characters
parser = argparse.ArgumentParser()
parser.add_argument("file", help="Path to the file to evaluate.")
parser.add_argument("-c", action="store_true", help="Return the number of bytes in file.")
parser.add_argument("-l", action="store_true", help="Return the number of lines in a file.")
parser.add_argument("-w", action="store_true", help="Return the number of words in a file.")
parser.add_argument("-m", action="store_true", help="Return the number of characters in a file.")
args = parser.parse_args()
if args.c:
    print(f"{count_bytes(args.file)} {args.file}")
elif args.l:
    with open(args.file, 'r') as f:
        print(f"{count_lines(f)} {args.file}")
elif args.w:
    with open(args.file, 'r') as f:
         print(f"{count_words(f)} {args.file}")
elif args.m:
    with open(args.file, 'r') as f:
        print(f"{count_characters(f)} {args.file}")
else:
    with open(args.file, 'r') as f:
        print(f"{count_lines(f)}      {count_words(f)}     {count_bytes(args.file)}    {args.file}")

