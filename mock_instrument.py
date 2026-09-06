# Simulates a real oscilloscope for practicing PyVISA-style code safely

import random

class MockScope:
    def __init__(self):
        self.connected = True
        self.id_string = "MOCKTEK,DS-2024,SN00219384,FW3.1.2"

    def query(self, command):
        command = command.strip().upper()

        if command == "*IDN?":
            return self.id_string

        elif command == "*RST":
            return "RESET OK"

        elif command == "MEASURE:VOLTAGE:DC?":
            return f"{round(random.uniform(3.15, 3.45), 3)}"

        elif command == "MEASURE:VOLTAGE:AC?":
            return f"{round(random.uniform(0.01, 0.05), 3)}"

        elif command == "MEASURE:CURRENT:DC?":
            return f"{round(random.uniform(0.48, 0.56), 3)}"

        elif command == "MEASURE:FREQUENCY?":
            return f"{round(random.uniform(59.8, 60.2), 2)}"

        elif command == "SYSTEM:ERROR?":
            return "0,\"No error\""

        else:
            return "ERROR: UNKNOWN COMMAND"

    def close(self):
        self.connected = False
        return "CONNECTION CLOSED"