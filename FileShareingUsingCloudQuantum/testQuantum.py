import os
from dotenv import load_dotenv
load_dotenv()
# import qiskit
#pip install qiskit-ibm-runtime
# from qiskit import generate_preset_pass_manager
from qiskit_ibm_runtime import QiskitRuntimeService

ibm_token = os.getenv("IBM_QUANTUM_TOKEN")

service = QiskitRuntimeService(
    channel='ibm_quantum',
    instance='ibm-q/open/main',
    token=ibm_token
)

backends = service.backends()
print("Available Backends:")
for backend in backends:
    print(backend)
