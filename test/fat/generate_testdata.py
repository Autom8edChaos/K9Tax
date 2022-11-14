import yaml, os, pprint, csv
from string import Template
from prettytable import from_csv

def process_testcases():
    # loading templates
    with open('test/fat/templates.yaml') as file:
        templates = yaml.full_load(file)

    tc_dir = 'test/fat/testcases'
    data = {}
    for filename in sorted(os.listdir(tc_dir)):
        if filename.endswith(".yaml"):
            tc_id = filename.split('_')[0]
            substitutions = { 'tc_id': tc_id }
            
            with open('/'.join([tc_dir, filename]), 'r') as f:
                content = yaml.full_load(f)

            for name, section_content in content.items():
                seq_id = 1
                if name.startswith('_'):
                    continue
                for item in section_content:
                    substitutions['seq_id'] = str(seq_id)
                    seq_id += 1
                    if not name in data:
                        data[name] = []
                    full_item = templates[name].copy()
                    if item:
                        full_item.update(item)
                    full_item = parse_variables(full_item, substitutions)
                    data[name].append(full_item)
    return data

def make_csv(path, data):
    for name, d in data.items():
        filename = f'{path}{name}.csv'
        with open(filename, 'w', encoding='utf8', newline='') as file:
            fc = csv.DictWriter(file, fieldnames=d[0].keys())
            fc.writeheader()
            fc.writerows(d)
        with open(filename) as file:
            table = from_csv(file)
            print(table.get_string(title=filename), '\n')


def parse_variables(data, repl):
    if isinstance(data, dict):
        return {key: parse_variables(value, repl) for key, value in data.items()}
    if isinstance(data, list):
        return [parse_variables(list_item, repl) for list_item in data]
    if isinstance(data, str):  # only string replace on strings
        return Template(data).safe_substitute(repl)
    return data

if __name__ == '__main__':
    os.system('clear')
    data = process_testcases()
    make_csv('test/fat/testdata/', data)

# python test/fat/generate_testdata.py