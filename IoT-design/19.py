from decimal import Decimal as D # rename for brevity
D(3.14) # pi, from float, so approximation issues
D('3.14') # pi, from a string, so no approximation issues
D(0.1) * D(3) - D(0.3) # from float, we still have the issue
D('0.1') * D(3) - D('0.3') # from string, all perfect
D('1.4').as_integer_ratio() # 7/5 = 1.4 (isn't this cool?!)
