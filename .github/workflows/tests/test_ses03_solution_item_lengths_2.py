test = {
  'name': 'test_ses03_solution_item_lengths_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> x = item_lengths('All happy families are alike'.split())
          >>> x[0]
          3
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
