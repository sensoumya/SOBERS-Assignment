import os
import sys
import csv
from schema import field_names, field_map


def extract_data(file):
    try:
        client = os.path.basename(os.path.splitext(file)[0])
        with open(file, 'r') as rf:
            csv_file = csv.DictReader(rf)
            return [{field: target['method'](
                [line[fld] for fld in target['target_field']]) if target[
                'method'] else line[target['target_field'][0]] for field, target
                     in field_map[client].items()} for line in csv_file]
    except Exception as e:
        print(f'Failed to extract data from {file}, due to reason:{e}')


def write_csv(out_file, data, write_header=False):
    try:
        with open(out_file, 'a', newline='') as wf:
            wcsv = csv.DictWriter(wf, fieldnames=field_names)
            wcsv.writeheader() if write_header else ''
            wcsv.writerows(data)
        return True
    except Exception as e:
        print(f'Failed to write data to {out_file}, due to reason:{e}')


if __name__ == '__main__':
    output_file = 'merged_data.csv'
    data_folder = 'data'
    if output_file in os.listdir():
        os.remove(output_file)
    input_files = [os.path.join(data_folder, f) for f in os.listdir(data_folder)
                   if f.endswith('.csv')]
    if not input_files:
        print('No files input files to read from')
        sys.exit(0)
    print(f"Merging following files:{','.join(input_files)}")
    write_csv(output_file, [], True)
    for file in input_files:
        if data := extract_data(file):
            print(f'Merging done for file: {file}') if write_csv(output_file,
                                                                 data) else ''
