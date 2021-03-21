from datetime import datetime

field_names = ['timestamp', 'transaction', 'amount', 'to', 'from']

field_map = {'bank1': {'timestamp': {'target_field': ['timestamp'],
                                     'method': lambda arg: datetime.strptime(
                                         arg[0], "%b %d %Y").strftime(
                                         "%d-%m-%Y")},
                       'transaction': {'target_field': ['type'],
                                       'method': ''},
                       'amount': {'target_field': ['amount'],
                                  'method': ''},
                       'from': {'target_field': ['from'],
                                'method': ''},
                       'to': {'target_field': ['to'],
                              'method': ''}
                       },
             'bank2': {'timestamp': {'target_field': ['date'],
                                     'method': lambda arg: datetime.strptime(
                                         arg[0], "%d-%m-%Y").strftime(
                                         "%d-%m-%Y")},
                       'transaction': {'target_field': ['transaction'],
                                       'method': ''},
                       'amount': {'target_field': ['amounts'],
                                  'method': ''},
                       'from': {'target_field': ['from'],
                                'method': ''},
                       'to': {'target_field': ['to'],
                              'method': ''}
                       },
             'bank3': {'timestamp': {'target_field': ['date_readable'],
                                     'method': lambda arg: datetime.strptime(
                                         arg[0], "%d %b %Y").strftime(
                                         "%d-%m-%Y")},
                       'transaction': {'target_field': ['type'],
                                       'method': ''},
                       'amount': {'target_field': ['euro', 'cents'],
                                  'method': lambda args: (int(
                                      args[0]) * 100 + int(args[1])) / 100},
                       'from': {'target_field': ['from'],
                                'method': ''},
                       'to': {'target_field': ['to'],
                              'method': ''}
                       }
             }
