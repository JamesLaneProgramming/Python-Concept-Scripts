import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-v', '--verbose', action='store_true', help='Displays verbose output to stdout.')
args = parser.parse_args()

def main():
    if(args.verbose):
        print("Hello")

if __name__ == '__main__':
    main()
