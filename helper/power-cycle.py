# Copyright (C) 2024 Dr. Matthias Kesenheimer - All Rights Reserved.
# You may use, distribute and modify this code under the terms of the GPL3 license.
#
# You should have received a copy of the GPL3 license with this file.
# If not, please write to: m.kesenheimer@gmx.net.

#!/usr/bin/env python3
import argparse
import sys

# import custom libraries
sys.path.insert(0, "../lib/")
from FaultInjectionLib import ProGlitcher, PicoGlitcher, Helper

class Main:
    def __init__(self, args):
        self.args = args

        if self.args.rpico == "":
            print("[+] Initializing ProGlitcher")
            self.glitcher = ProGlitcher()
            self.glitcher.init()
        else:
            print("[+] Initializing PicoGlitcher")
            self.glitcher = PicoGlitcher()
            self.glitcher.init(port=args.rpico)

        self.dump_filename = f"{Helper.timestamp()}_memory_dump.bin"

    def run(self):
        print("[+] Power cycling target")
        # power cycle target
        self.glitcher.power_cycle_target(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--rpico", required=False, help="rpico port", default="")
    args = parser.parse_args()

    main = Main(args)

    try:
        main.run()
    except KeyboardInterrupt:
        print("\nExitting...")
        sys.exit(1)