def default_report_fn(kind, val, idx):
  print('{} value at {}: {}'.format(kind, idx, val))

def bisect_range(values, left, right, is_good_value, report_fn = default_report_fn):
  mid = 0
  val = 0
  original_right = right
  while left < right:
    mid = int((left + right) / 2)
    val = values[mid]
    if is_good_value(val):
      report_fn('pass', val, mid)
      left = mid + 1
    else:
      report_fn('fail', val, mid)
      right = mid
    # print('l={} r={}'.format(left, right))
  mid = int((left + right) / 2)
  val = values[mid]
  if original_right == mid:
    # there may be no fail case at all
    if is_good_value(val):
      report_fn('no fails', -1, None)
      return (None, -1)
  report_fn('first fail', mid, val)
  return (val, mid)

def bisect(values, is_fail_value, report_fn = default_report_fn):
  '''Find the first fail value by bisecting the inputs.'''
  return bisect_range(values, 0, len(values) - 1, is_fail_value, report_fn)

def run_subprocess_evaluation(command):
  import subprocess
  completion = subprocess.call(args, shell=True)
  return completion == 0

def create_subprocess_evaluation(command_format):
  return lambda v: run_subprocess_evaluation(command_format.format(v))

def main_with_parsed_args(args):
  lines = []
  with open(args.infile) as f:
    for l in f:
      if len(l) > 0 and not l.startswith("#"):
        lines.append(l)
  bisect(lines, create_subprocess_evaluation(args.fmt))

def main_with_text_args(text_args):
  import argparse
  parser = argparse.ArgumentParser(description="bisects a given file to find the first one with nonzero result")
  parser.add_argument('-c', '--command', dest='fmt', default='{}', help='python string format to turn line into shell command (default: {})')
  parser.add_argument('file', help='text file to bisect, empty and # lines ignored')
  args = parser.parse_args(text_args)
  main_with_args(args)
 
def main():
  main_with_text_args(None)

if __name__ == '__main__':
  main()
