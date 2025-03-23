import netsquid as ns

qubits = ns.qubits.create_qubits(1)
qubit = qubits[0]
ns.qubits.reduced_dm(qubit)

ns.qubits.operate(qubits, ns.X)
ns.qubits.reduced_dm(qubit)

measuremet_result, prob = ns.qubits.measure(qubit)
if measuremet_result == 0:
    state = "|0>"
else:
    state = "|1>"
print(f"Measured {state} with probability {prob:.1f}")

measurement_result, prob = ns.qubits.measure(qubit, observable=ns.X)
if measurement_result == 0:
    state = "|+>"
else:
    state = "|->"
print(f"Measured {state} with probability {prob:.1f}")
ns.qubits.reduced_dm(qubit)

