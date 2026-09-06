from mock_instrument import MockScope

scope = MockScope()

idn = scope.query("*IDN?")
voltage = scope.query("MEASURE:VOLTAGE:DC?")
current = scope.query("MEASURE:CURRENT:DC?")
frequency = scope.query("MEASURE:FREQUENCY?")
error_status = scope.query("SYSTEM:ERROR?")

if error_status != '0,"No error"':
    print(f"WARNING: Instrument reported an error: {error_status}")

print("Error status check completed.")

print(f"Scope is {idn}")
print(f"Measured DC Voltage: {voltage} V")
print(f"Measured DC Current: {current} A")
print(f"Measured Frequency: {frequency} Hz")
print(f"System Error Status: {error_status}")