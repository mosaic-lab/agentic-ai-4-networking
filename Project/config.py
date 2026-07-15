num_steps = 120

algorithms = [
    "heuristic_no_delay",
    "heuristic_low_delay",
    "heuristic_high_delay",
]
# , "agentic"]

colors = {
    "heuristic_no_delay": "blue",
    "heuristic_low_delay": "orange",
    "heuristic_high_delay": "red",
    "agentic": "green",
}

algo_delays = {
    "heuristic_no_delay": 0.0,
    "heuristic_low_delay": 0.5,
    "heuristic_high_delay": 10.0,
}

metric_names = ["total", "acceptance_rate"]

random_seed = 50

OPENROUTER_CHAT_COMPLETIONS_URL = "https://openrouter.ai/api/v1/chat/completions"
OPENROUTER_API_KEY = "sk-or-v1-..."

verbosity_level = 1  # 0: no print, 1: few prints (important messages), 2: more prints (detailed)

network_args = {
    "num_nodes": 15,
    "link_prob": 0.5,
    "capacity_min": 20,
    "capacity_max": 80,
    "latency_min": 1,
    "latency_max": 10,
    "loss_min": 0.0,
    "loss_max": 0.02,
    "fail_p_min": 0.001,
    "fail_p_max": 0.01,
}

base_demand = 8.0

traffic_pattern_args = {
    "latency_requirement_min_ms": 4.0,
    "latency_requirement_max_ms": 8.0,
}

traffic_args = {
    "seasonal_amplitude": 0.0,
    "seasonal_frequency": 24.0,
    "noise_power": 0.0,
}
