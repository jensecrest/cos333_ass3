#!/usr/bin/env python

#-----------------------------------------------------------------------
# runserver.py
# Author: Jennifer Secrest and AnneMarie Caballero
# (Taken from PennyFlaskJinja)
#-----------------------------------------------------------------------

import argparse
import sys
from sys import argv, stderr
from reg import app

def main():

    try:
        parser = argparse.ArgumentParser(allow_abbrev=False,
            description="The registrar application")
        parser.add_argument("port", type=int,
            help = "the port at which the server should listen")

        args = parser.parse_args()
        port = args.port

        app.run(host='0.0.0.0', port=port, debug=True)

    except argparse.ArgumentError as ex:
        print(argv[0] + ": " + str(ex), file=stderr)
        sys.exit(2)
    except Exception as ex:
        print(argv[0] + ": " + str(ex), file=stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
