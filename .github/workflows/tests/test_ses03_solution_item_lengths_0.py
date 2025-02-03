test = {
  'name': 'test_ses03_solution_item_lengths_0',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> item_lengths(['hello', 'how', 'are', 'you', 'doing'])
          [5, 3, 3, 3, 5]
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
