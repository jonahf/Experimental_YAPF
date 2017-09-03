from yapf.yapflib import style


# Number of columns (not counting indents) that a
# complex line is allowed to occupy.
COMPLEX_EFFECTIVE_COLUMN_LIMIT = 60

# Threshold after which the line is considered complex,
# and the column limit is changed by a certain amount.
COMPLEX_LINE_THRESHOLD = 120

# Complexity threshold after which penalties will be added
# for each additional token added to the line
PENALIZE_COMPLEXITY_THRESHOLD = 75


def ColumnLimit(uwline, indent_amt):
  if COMPLEX_EFFECTIVE_COLUMN_LIMIT == 0:
    return style.Get('COLUMN_LIMIT')
  if uwline.line_complexity <= COMPLEX_LINE_THRESHOLD:
    return style.Get('COLUMN_LIMIT')

  effective_limit = style.Get('COLUMN_LIMIT') - indent_amt

  # if effective_limit > COMPLEX_EFFECTIVE_COLUMN_LIMIT:
  #   print " # Complex line: ", uwline
  #   print " #     Complexity: ", uwline.line_complexity

  new_effective_limit = min(effective_limit, COMPLEX_EFFECTIVE_COLUMN_LIMIT)
  return new_effective_limit + indent_amt


def ComplexityPenalty(next_token, previous_token=None):
  """
  Creates a complexity penalty for the current token and next token. 
  
  Used for both formatting decision state, and for estimating total
  line complexity. Previous token is used during formatting decision,
  and affects whether a split happens before or after that token. 

  These apply to the threshold for column limit condensing
  as well as the threshold for penalizing additional complexity
  on a broken line.
  """
  n_token = next_token
  p_token = previous_token
  if not p_token:
    p_token = n_token

  p_token_value = n_token.previous_token.value
  n_token_value = n_token.value

  result = 0
  if n_token_value in {"if", "elif", "else"}:
    result += 25
    if p_token != n_token and n_token_value == "if":
      # print p_token.value, n_token.value
      if p_token.name not in {"NAME", "RPAR"}:
        result += 40

  if n_token_value in {"for", "while", "do", "in"}:
    result += 20

  if p_token_value in {"[", "{"}:
    result += 10
  if n_token_value in {"]", "}"}:
    result += 30

  if p_token_value in {".", "not", "and", "or"}:
    result += 2

  if p_token_value in {"(", ")", ",", "=", "+", "-", "*", "/"}:
    result += 2

  return result
