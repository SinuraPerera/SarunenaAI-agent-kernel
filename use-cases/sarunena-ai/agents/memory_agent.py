import json
import os

MEMORY_FILE = "farmer_memory.json"


def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return {}


def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f)


def save_farmer(name, crop):
    memory = load_memory()
    memory[name] = crop
    save_memory(memory)


def get_farmer_crop(name):
    memory = load_memory()
    return memory.get(name)