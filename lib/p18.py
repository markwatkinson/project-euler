def build_triangle(string):
  triangle = []
  for row in string.strip().splitlines():
    triangle += [[int(n) for n in row.split(' ')]]
  return triangle


def traverse_triangle(triangle):
  # we make a new triangle whose elements are the maximum sum up to that point

  triangle_ = []
  for i, row in enumerate(triangle):
    row_ = []
    for j, cell in enumerate(row):
      # valid movements are from cells diagonally above
      # special case: the top cell
      if i == 0: row_ += [cell]
      # special case: the left side
      elif j == 0: row_ += [cell + triangle_[i-1][j]]
      # special caes: the right side
      elif j == len(row)-1: row_ += [cell + triangle_[i-1][-1]]
      else:
        # look at the two cells above us, and add the maximum
        prev_row = triangle_[i-1]
        left = prev_row[j-1]
        right = prev_row[j]
        max_ = max(left, right)
        row_ += [cell + max_]
    triangle_ += [row_]
  return triangle_

def solve(triangle_str):
  t = build_triangle(triangle_str)
  t_ = traverse_triangle(t)
  return max(t_[-1])

if __name__ == '__main__':
  print solve(t)