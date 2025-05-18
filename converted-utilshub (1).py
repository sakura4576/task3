import sys
import json
def fill_values(obj, values_map):
    if isinstance(obj, dict):
        if "id" in obj:
            obj["value"] = values_map.get(obj["id"], None)
        # Рекурсивно обрабатываем все вложенные объекты
        for key, val in obj.items():
            if isinstance(val, (dict, list)):
                fill_values(val, values_map)
    elif isinstance(obj, list):
        for item in obj:
            fill_values(item, values_map)
def main():
    if len(sys.argv) != 4:
        print("Использование: python script.py values.json tests.json report.json")
        return
    values_path = sys.argv[1]
    tests_path = sys.argv[2]
    report_path = sys.argv[3]
    with open(values_path, 'r', encoding='utf-8') as f:
        values_data = json.load(f)
    with open(tests_path, 'r', encoding='utf-8') as f:
        tests_data = json.load(f)
    fill_values(tests_data, values_data)
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(tests_data, f, ensure_ascii=False, indent=4)
if __name__ == "__main__":
    main()

