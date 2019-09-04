# -*- encoding: utf-8
# yapf: disable


checkname = 'docker_container_diskstat'


info = [
    ['node-1', '[time]'],
    ['node-1', '1527265297'],
    ['node-1', '[io_service_bytes]'],
    ['node-1', '8:0', 'Read', '193536'],
    ['node-1', '8:0', 'Write', '0'],
    ['node-1', '8:0', 'Sync', '0'],
    ['node-1', '8:0', 'Async', '193536'],
    ['node-1', '8:0', 'Total', '193536'],
    ['node-1', '253:11', 'Read', '193536'],
    ['node-1', '253:11', 'Write', '0'],
    ['node-1', '253:11', 'Sync', '0'],
    ['node-1', '253:11', 'Async', '193536'],
    ['node-1', '253:11', 'Total', '193536'],
    ['node-1', '253:12', 'Read', '193536'],
    ['node-1', '253:12', 'Write', '0'],
    ['node-1', '253:12', 'Sync', '0'],
    ['node-1', '253:12', 'Async', '193536'],
    ['node-1', '253:12', 'Total', '193536'],
    ['node-1', '253:14', 'Read', '31657984'],
    ['node-1', '253:14', 'Write', '0'],
    ['node-1', '253:14', 'Sync', '0'],
    ['node-1', '253:14', 'Async', '31657984'],
    ['node-1', '253:14', 'Total', '31657984'],
    ['node-1', 'Total', '32238592'],
    ['node-1', '[io_serviced]'],
    ['node-1', '8:0', 'Read', '19'],
    ['node-1', '8:0', 'Write', '0'],
    ['node-1', '8:0', 'Sync', '0'],
    ['node-1', '8:0', 'Async', '19'],
    ['node-1', '8:0', 'Total', '19'],
    ['node-1', '253:11', 'Read', '19'],
    ['node-1', '253:11', 'Write', '0'],
    ['node-1', '253:11', 'Sync', '0'],
    ['node-1', '253:11', 'Async', '19'],
    ['node-1', '253:11', 'Total', '19'],
    ['node-1', '253:12', 'Read', '19'],
    ['node-1', '253:12', 'Write', '0'],
    ['node-1', '253:12', 'Sync', '0'],
    ['node-1', '253:12', 'Async', '19'],
    ['node-1', '253:12', 'Total', '19'],
    ['node-1', '253:14', 'Read', '998'],
    ['node-1', '253:14', 'Write', '0'],
    ['node-1', '253:14', 'Sync', '0'],
    ['node-1', '253:14', 'Async', '998'],
    ['node-1', '253:14', 'Total', '998'],
    ['node-1', 'Total', '1055'],
    ['node-1', '[names]'],
    ['node-1', 'dm-0', '253:0'],
    ['node-1', 'dm-1', '253:1'],
    ['node-1', 'dm-10', '253:10'],
    ['node-1', 'dm-11', '253:11'],
    ['node-1', 'dm-12', '253:12'],
    ['node-1', 'dm-13', '253:13'],
    ['node-1', 'dm-14', '253:14'],
    ['node-1', 'dm-15', '253:15'],
    ['node-1', 'dm-16', '253:16'],
    ['node-1', 'dm-17', '253:17'],
    ['node-1', 'dm-18', '253:18'],
    ['node-1', 'dm-19', '253:19'],
    ['node-1', 'dm-2', '253:2'],
    ['node-1', 'dm-20', '253:20'],
    ['node-1', 'dm-21', '253:21'],
    ['node-1', 'dm-22', '253:22'],
    ['node-1', 'dm-23', '253:23'],
    ['node-1', 'dm-24', '253:24'],
    ['node-1', 'dm-3', '253:3'],
    ['node-1', 'dm-4', '253:4'],
    ['node-1', 'dm-5', '253:5'],
    ['node-1', 'dm-6', '253:6'],
    ['node-1', 'dm-7', '253:7'],
    ['node-1', 'dm-8', '253:8'],
    ['node-1', 'dm-9', '253:9'],
    ['node-1', 'sda', '8:0'],
    ['node-2', '[time]'],
    ['node-2', '1527265297'],
    ['node-2', '[io_service_bytes]'],
    ['node-2', '8:0', 'Read', '229888'],
    ['node-2', '8:0', 'Write', '0'],
    ['node-2', '8:0', 'Sync', '0'],
    ['node-2', '8:0', 'Async', '229888'],
    ['node-2', '8:0', 'Total', '229888'],
    ['node-2', '253:11', 'Read', '229888'],
    ['node-2', '253:11', 'Write', '0'],
    ['node-2', '253:11', 'Sync', '0'],
    ['node-2', '253:11', 'Async', '229888'],
    ['node-2', '253:11', 'Total', '229888'],
    ['node-2', '253:12', 'Read', '229888'],
    ['node-2', '253:12', 'Write', '0'],
    ['node-2', '253:12', 'Sync', '0'],
    ['node-2', '253:12', 'Async', '229888'],
    ['node-2', '253:12', 'Total', '229888'],
    ['node-2', '253:13', 'Read', '47256064'],
    ['node-2', '253:13', 'Write', '0'],
    ['node-2', '253:13', 'Sync', '0'],
    ['node-2', '253:13', 'Async', '47256064'],
    ['node-2', '253:13', 'Total', '47256064'],
    ['node-2', 'Total', '47945728'],
    ['node-2', '[io_serviced]'],
    ['node-2', '8:0', 'Read', '18'],
    ['node-2', '8:0', 'Write', '0'],
    ['node-2', '8:0', 'Sync', '0'],
    ['node-2', '8:0', 'Async', '18'],
    ['node-2', '8:0', 'Total', '18'],
    ['node-2', '253:11', 'Read', '18'],
    ['node-2', '253:11', 'Write', '0'],
    ['node-2', '253:11', 'Sync', '0'],
    ['node-2', '253:11', 'Async', '18'],
    ['node-2', '253:11', 'Total', '18'],
    ['node-2', '253:12', 'Read', '18'],
    ['node-2', '253:12', 'Write', '0'],
    ['node-2', '253:12', 'Sync', '0'],
    ['node-2', '253:12', 'Async', '18'],
    ['node-2', '253:12', 'Total', '18'],
    ['node-2', '253:13', 'Read', '1584'],
    ['node-2', '253:13', 'Write', '0'],
    ['node-2', '253:13', 'Sync', '0'],
    ['node-2', '253:13', 'Async', '1584'],
    ['node-2', '253:13', 'Total', '1584'],
    ['node-2', 'Total', '1638'],
    ['node-2', '[names]'],
    ['node-2', 'dm-0', '253:0'],
    ['node-2', 'dm-1', '253:1'],
    ['node-2', 'dm-10', '253:10'],
    ['node-2', 'dm-11', '253:11'],
    ['node-2', 'dm-12', '253:12'],
    ['node-2', 'dm-13', '253:13'],
    ['node-2', 'dm-14', '253:14'],
    ['node-2', 'dm-15', '253:15'],
    ['node-2', 'dm-16', '253:16'],
    ['node-2', 'dm-17', '253:17'],
    ['node-2', 'dm-18', '253:18'],
    ['node-2', 'dm-19', '253:19'],
    ['node-2', 'dm-2', '253:2'],
    ['node-2', 'dm-20', '253:20'],
    ['node-2', 'dm-21', '253:21'],
    ['node-2', 'dm-22', '253:22'],
    ['node-2', 'dm-23', '253:23'],
    ['node-2', 'dm-24', '253:24'],
    ['node-2', 'dm-3', '253:3'],
    ['node-2', 'dm-4', '253:4'],
    ['node-2', 'dm-5', '253:5'],
    ['node-2', 'dm-6', '253:6'],
    ['node-2', 'dm-7', '253:7'],
    ['node-2', 'dm-8', '253:8'],
    ['node-2', 'dm-9', '253:9'],
    ['node-2', 'sda', '8:0']
]


# TODO: can be removed after refactoring + plugin section feature
parsed = {('node-1', 'dm-11'): (1527265297,
                       {'bytes': {'Async': 193536,
                                  'Read': 193536,
                                  'Sync': 0,
                                  'Total': 193536,
                                  'Write': 0},
                        'ios': {'Async': 19,
                                'Read': 19,
                                'Sync': 0,
                                'Total': 19,
                                'Write': 0},
                        'name': 'dm-11'}),
 ('node-1', 'dm-12'): (1527265297,
                       {'bytes': {'Async': 193536,
                                  'Read': 193536,
                                  'Sync': 0,
                                  'Total': 193536,
                                  'Write': 0},
                        'ios': {'Async': 19,
                                'Read': 19,
                                'Sync': 0,
                                'Total': 19,
                                'Write': 0},
                        'name': 'dm-12'}),
 ('node-1', 'dm-14'): (1527265297,
                       {'bytes': {'Async': 31657984,
                                  'Read': 31657984,
                                  'Sync': 0,
                                  'Total': 31657984,
                                  'Write': 0},
                        'ios': {'Async': 998,
                                'Read': 998,
                                'Sync': 0,
                                'Total': 998,
                                'Write': 0},
                        'name': 'dm-14'}),
 ('node-1', 'sda'): (1527265297,
                     {'bytes': {'Async': 193536,
                                'Read': 193536,
                                'Sync': 0,
                                'Total': 193536,
                                'Write': 0},
                      'ios': {'Async': 19,
                              'Read': 19,
                              'Sync': 0,
                              'Total': 19,
                              'Write': 0},
                      'name': 'sda'}),
 ('node-2', 'dm-11'): (1527265297,
                       {'bytes': {'Async': 229888,
                                  'Read': 229888,
                                  'Sync': 0,
                                  'Total': 229888,
                                  'Write': 0},
                        'ios': {'Async': 18,
                                'Read': 18,
                                'Sync': 0,
                                'Total': 18,
                                'Write': 0},
                        'name': 'dm-11'}),
 ('node-2', 'dm-12'): (1527265297,
                       {'bytes': {'Async': 229888,
                                  'Read': 229888,
                                  'Sync': 0,
                                  'Total': 229888,
                                  'Write': 0},
                        'ios': {'Async': 18,
                                'Read': 18,
                                'Sync': 0,
                                'Total': 18,
                                'Write': 0},
                        'name': 'dm-12'}),
 ('node-2', 'dm-13'): (1527265297,
                       {'bytes': {'Async': 47256064,
                                  'Read': 47256064,
                                  'Sync': 0,
                                  'Total': 47256064,
                                  'Write': 0},
                        'ios': {'Async': 1584,
                                'Read': 1584,
                                'Sync': 0,
                                'Total': 1584,
                                'Write': 0},
                        'name': 'dm-13'}),
 ('node-2', 'sda'): (1527265297,
                     {'bytes': {'Async': 229888,
                                'Read': 229888,
                                'Sync': 0,
                                'Total': 229888,
                                'Write': 0},
                      'ios': {'Async': 18,
                              'Read': 18,
                              'Sync': 0,
                              'Total': 18,
                              'Write': 0},
                      'name': 'sda'})}


discovery = {'': [('SUMMARY', 'diskstat_default_levels')]}


checks = {'': [('SUMMARY',
                {},
                [(0,
                  'Read: 0.00 B/s',
                  [('disk_read_throughput', 0.0, None, None, None, None)]),
                 (0,
                  'Write: 0.00 B/s',
                  [('disk_write_throughput', 0.0, None, None, None, None)]),
                 (0,
                  'Read operations: 0.00 1/s',
                  [('disk_read_ios', 0.0, None, None, None, None)]),
                 (0,
                  'Write operations: 0.00 1/s',
                  [('disk_write_ios', 0.0, None, None, None, None)])])]}
