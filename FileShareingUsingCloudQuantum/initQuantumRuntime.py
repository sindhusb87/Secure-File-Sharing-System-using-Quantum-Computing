import os
from dotenv import load_dotenv
load_dotenv()
from qiskit_ibm_runtime import QiskitRuntimeService

service = QiskitRuntimeService(
    channel='ibm_quantum',
    instance='ibm-q/open/main',
    token=os.getenv("IBM_QUANTUM_TOKEN")
)

# Or save your credentials on disk.
QiskitRuntimeService.save_account(channel='ibm_quantum', instance='ibm-q/open/main', token=os.getenv("IBM_QUANTUM_TOKEN"), overwrite=True)