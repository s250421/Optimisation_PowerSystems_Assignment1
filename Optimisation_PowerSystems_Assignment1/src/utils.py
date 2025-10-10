def load_json(file_path):
    import json
    with open(file_path, 'r') as f:
        return json.load(f)

def save_json(data, file_path):
    import json
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

def extract_parameters(data, keys):
    return {key: data.get(key) for key in keys}

def calculate_efficiency(input_value, efficiency_ratio):
    return input_value * efficiency_ratio

def normalize_data(data, max_value):
    return [x / max_value for x in data] if max_value > 0 else data

def get_time_series(data, time_key):
    return data.get(time_key, [])

def calculate_penalty(value, penalty_rate):
    return value * penalty_rate