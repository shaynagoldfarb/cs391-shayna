def TVALint(x):
    return x
def TINSadd(x, y):
    return x + y
def TINSsub(x, y):
    return x - y
def TINSmul(x, y):
    return x * y
def TINSile(x, y):
    return x <= y

def fun102(arg2):
  tmp107 = TVALint(0)
  tmp108 = TINSile(arg2, tmp107)
  tmp114 = None
  if (tmp108):
    tmp109 = TVALint(1)
    tmp114 = tmp109
  else:
    tmp110 = TVALint(1)
    tmp111 = TINSsub(arg2, tmp110)
    tmp112 = fun102(tmp111)
    tmp113 = TINSmul(arg2, tmp112)
    tmp114 = tmp113
  return tmp114

print("fact(10) = " + str(fun102(10)))
