import os
import csv
import unittest
from script import extract_data, write_csv

output_file = 'test.csv'
file = os.path.join('data', 'bank3.csv')
data = extract_data(file)

class testCsv(unittest.TestCase):
    def test_field_map(self):
        for row in data:
            if row['timestamp'] == '06-10-2019':
                self.assertEqual(row['amount'], 1060.08)
                self.assertEqual(row['transaction'], 'add')
                self.assertEqual(row['from'], '188')
                self.assertEqual(row['to'], '198')
        # print('All testcases for test_field_map passed')

    def test_write_file(self):
        if output_file in os.listdir():
            os.remove(output_file)
        write_csv(output_file, [], True)
        write_csv(output_file, data)
        with open(output_file, 'r') as rf:
            rcsv = csv.DictReader(rf)
            row_count = sum(1 for _ in rcsv)
            self.assertEqual(row_count, 2)
            headers = rcsv.fieldnames
            self.assertEqual(headers,
                             ['timestamp', 'transaction', 'amount', 'to',
                              'from'])
        # print('All testcases for test_write_file passed')

if __name__ == '__main__':
    unittest.main()