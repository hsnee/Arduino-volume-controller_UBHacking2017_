import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--force', dest='force', action='store_const', const=True)
args = parser.parse_args()
force =  args.force
if force==True:
    print 'something'
