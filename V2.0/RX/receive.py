#!/usr/bin/env python3

import subprocess
import os

RX_SCRIPT = "./ax25_rx.py"
WAV_FILE = "received.wav"

while True:

    # Remove old recording
    if os.path.exists(WAV_FILE):
        os.remove(WAV_FILE)

    print("\n====================================")
    print("Starting AX.25 Receiver")
    print("====================================\n")

    rx = subprocess.Popen(
        ["python3", RX_SCRIPT],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    while True:

        cmd = input(
            "Type 'stop' to stop reception\n"
            "Type 'exit' to quit completely\n> "
        ).strip().lower()

        if cmd == "stop":

            print("\nStopping Receiver...\n")

            rx.terminate()

            try:
                rx.wait(timeout=5)
            except:
                rx.kill()

            break

        elif cmd == "exit":

            print("\nStopping Receiver...\n")

            rx.terminate()

            try:
                rx.wait(timeout=5)
            except:
                rx.kill()

            print("\nExiting...\n")
            exit()

    if not os.path.exists(WAV_FILE):

        print("\nreceived.wav not found!\n")
        continue

    print("\nreceived.wav saved successfully")

    decode = input(
        "\nDecode received.wav ? (yes/no)\n> "
    ).strip().lower()

    if decode == "yes":

        print("\n====================================")
        print("Running Direwolf")
        print("====================================\n")

        try:

            with open(WAV_FILE, "rb") as wav:

                subprocess.run(
                    ["direwolf", "-r", "48000", "-"],
                    stdin=wav
                )

        except Exception as e:

            print("\nDirewolf Error:")
            print(e)

    again = input(
        "\nStart receiving again? (yes/no)\n> "
    ).strip().lower()

    if again != "yes":

        print("\nGoodbye!\n")
        break
