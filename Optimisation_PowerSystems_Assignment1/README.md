# Optimisation Power Systems Assignment 1

## Overview
This project focuses on optimization in modern power systems, specifically addressing the integration of distributed energy resources (DER) and flexible load management. The goal is to minimize costs while ensuring efficient energy usage and maintaining the state of charge (SOC) of battery storage systems.

## Project Structure
The project is organized as follows:

- **data/question_1c/**: Contains all data files used in the optimization model.
  - `Task1c_model copy.ipynb`: Jupyter Notebook with Python code for optimization, including data loading, parameter extraction, and model formulation.
  - `appliance_params.json`: JSON file with appliance parameters such as maximum power and ramp rates.
  - `bus_params.json`: JSON file with bus system parameters, including tariffs and import/export limits.
  - `DER_production.json`: JSON file with DER production profiles, specifically solar power generation data.
  - `usage_preferences.json`: JSON file containing user preferences for energy usage, including load profiles and SOC preferences.

- **src/**: Contains the source code for the application.
  - `main.py`: Main entry point for the application, handling the overall workflow and running the optimization model.
  - `utils.py`: Utility functions for data processing and parameter retrieval.

- **requirements.txt**: Lists the Python dependencies required for the project, including libraries such as Gurobi, pandas, numpy, and matplotlib.

## Setup Instructions
1. Clone the repository or download the project files.
2. Navigate to the project directory.
3. Install the required dependencies using pip:
   ```
   pip install -r requirements.txt
   ```

## Usage
To run the optimization model, execute the `main.py` script:
```
python src/main.py
```

## License
This project is licensed under the MIT License. See the LICENSE file for more details.