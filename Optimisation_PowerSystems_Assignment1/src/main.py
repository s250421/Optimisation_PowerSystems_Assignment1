import json
import gurobipy as gp
from gurobipy import GRB
from pathlib import Path

def load_data():
    data_dir = Path("../data/question_1c/")
    with open(data_dir / "appliance_params.json", "r") as f:
        appliance_params = json.load(f)
    with open(data_dir / "bus_params.json", "r") as f:
        bus_params = json.load(f)
    with open(data_dir / "DER_production.json", "r") as f:
        der_production = json.load(f)
    with open(data_dir / "usage_preferences.json", "r") as f:
        usage_preferences = json.load(f)
    
    return appliance_params, bus_params, der_production, usage_preferences

def main():
    appliance_params, bus_params, der_production, usage_preferences = load_data()
    
    # Here you would call the optimization function using the loaded parameters
    # For example:
    # model, results = run_optimization(appliance_params, bus_params, der_production, usage_preferences)
    
    # Print or process results as needed
    # print(results)

if __name__ == "__main__":
    main()