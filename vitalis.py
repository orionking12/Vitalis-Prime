#!/usr/bin/env python3
import os
import sys
import subprocess
import argparse
import time
import signal
from dotenv import load_dotenv

# =====================================================================
# VITALIS-PRIME: UNIFIED ORCHESTRATOR (v2.0)
# ARCHITECT: JORGE HUMBERTO DAVALOS GONZALEZ
# =====================================================================

load_dotenv()

def run_service(name, command):
    print(f"[*] Starting {name}...")
    try:
        process = subprocess.Popen(command, shell=True)
        return process
    except Exception as e:
        print(f"[!] Error starting {name}: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description="Vitalis-Prime Unified Orchestrator")
    parser.add_argument("mode", choices=["all", "kernel", "holoscope", "swarm"],
                        help="Select component to launch")
    args = parser.parse_args()

    processes = []

    try:
        if args.mode in ["all", "kernel"]:
            p = run_service("Bridge & Kernel", "npm start")
            if p: processes.append(p)
            time.sleep(5) # Wait for kernel to spin up

        if args.mode in ["all", "holoscope"]:
            p = run_service("Holoscope 3D", "python src/visualization/holoscopio_visual.py")
            if p: processes.append(p)

        if args.mode in ["all", "swarm"]:
            p = run_service("Adversarial Swarm", "python src/stress_test/enjambre_adversario.py")
            if p: processes.append(p)

        print("[+] All selected services are running. Press Ctrl+C to terminate.")
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("\n[!] Termination requested. Cleaning up...")
        for p in processes:
            p.terminate()
        sys.exit(0)

if __name__ == "__main__":
    main()
