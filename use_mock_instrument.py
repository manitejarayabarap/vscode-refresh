# Main stable version — verified working baseline

from mock_instrument import MockScope

scope = MockScope()

idn = scope.query("*IDN?")
voltage = scope.query("MEASURE:VOLTAGE:DC?")
current = scope.query("MEASURE:CURRENT:DC?")
frequency = scope.query("MEASURE:FREQUENCY?")
error_status = scope.query("SYSTEM:ERROR?")

# Verifies instrument is not reporting a fault before logging readings

if error_status != '0,"No error"':
    print(f"WARNING: Instrument reported an error: {error_status}")

print("Error status check completed.")

print(f"Scope is {idn}")
print(f"Measured DC Voltage: {voltage} V (nominal range: 3.15–3.45V)")
print(f"Measured DC Current: {current} A (typical range: 0.48-0.56A)")
print(f"Measured Frequency: {frequency} Hz")
print(f"System Error Status: {error_status}")