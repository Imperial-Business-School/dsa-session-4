test = {
  'name': 'test_ses03_solution_item_lengths_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> item_lengths('All happy families are alike'.split())
          [3, 5, 8, 3, 5]
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from ses03 import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
