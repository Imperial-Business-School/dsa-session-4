test = {
  'name': 'test_ses03_solution_longest_item_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> x = longest_item('All happy families are alike'.split())
          >>> isinstance(x, int) # check that result is an integer
          True
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
