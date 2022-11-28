import mybisect
import unittest

def bisect_logged(values, is_good_value):
  logs = []
  report_logs = lambda k, v, x: logs.append((k, v, x))
  return mybisect.bisect(values, is_good_value, report_logs)

class MyBisectTest(unittest.TestCase):

  def test_simple_even(self):
    values = ['a', 'b', 'c', 'd']
    is_good_value = lambda v : v < 'c'
    val, idx = bisect_logged(values, is_good_value)
    self.assertEqual(val, 'c')
    self.assertEqual(idx, 2)

  def test_simple_odd(self):
    values = ['a', 'b', 'c', 'd', 'e']
    is_good_value = lambda v : v < 'c'
    val, idx = bisect_logged(values, is_good_value)
    self.assertEqual(val, 'c')
    self.assertEqual(idx, 2)

  def test_simple_dupe(self):
    values = ['a', 'c', 'c', 'c', 'e']
    is_good_value = lambda v : v < 'c'
    val, idx = bisect_logged(values, is_good_value)
    self.assertEqual(val, 'c')
    self.assertEqual(idx, 1)

  def test_all_good(self):
    values = ['a', 'c', 'c', 'c', 'e']
    is_good_value = lambda v : v < 'f'
    val, idx = bisect_logged(values, is_good_value)
    self.assertEqual(val, None)
    self.assertEqual(idx, -1)

  def test_all_bad(self):
    values = ['a', 'c', 'c', 'c', 'e']
    is_good_value = lambda v : v > 'f'
    val, idx = bisect_logged(values, is_good_value)
    self.assertEqual(val, 'a')
    self.assertEqual(idx, 0)

  def test_single_good(self):
    values = ['a']
    is_good_value = lambda v : v < 'f'
    val, idx = bisect_logged(values, is_good_value)
    self.assertEqual(val, None)
    self.assertEqual(idx, -1)

  def test_single_bad(self):
    values = ['a']
    is_good_value = lambda v : v > 'f'
    val, idx = bisect_logged(values, is_good_value)
    self.assertEqual(val, 'a')
    self.assertEqual(idx, 0)

if __name__ == '__main__':
  unittest.main()
