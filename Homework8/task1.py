import os
import json
import csv
import pickle


def get_size(path):
    if os.path.isfile(path):
        return os.path.getsize(path)

    size = 0
    for root, dirs, files in os.walk(path):
        for name in dirs + files:
            full_path = os.path.join(root, name)
            if os.path.isfile(full_path):
                size += os.path.getsize(full_path)
            else:
                size += get_size(full_path)

    return size


def traverse_directory(dir_path):
    results = []
    for root, dirs, files in os.walk(dir_path):
        for name in files + dirs:
            full_path = os.path.join(root, name)
            results.append({"Path": full_path,
                            "Type": ("File" if os.path.isfile(full_path) else "Directory"),
                            "Size": get_size(full_path)})

    return results


def save_results_to_json(results, file_path):
    with open(file_path, "w") as file:
        json.dump(results, file)


def save_results_to_csv(results, file_path):
    with open(file_path, "w") as file:
        writer = csv.DictWriter(file, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)


def save_results_to_pickle(results, file_path):
    with open(file_path, "wb") as file:
        pickle.dump(results, file)

