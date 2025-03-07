# Running Example

Quantum circuits found in the article "Running Example"

## Requirements

- python 3.12
- pip 24.0

## Setup

1. create and activate a Python virtual environment using the `venv` module
```shell
python3 -m venv env
source env/bin/activate
```

1. install dependencies
```shell
pip install -r requirements.txt
```

## Running the simulation script

```shell
python bell_state_on_simulator.py
```

This generates 3 artifacts: the circuit drawing `.circuit.png`, the results histogram `.histogram.png` and the results object `.results.txt`
