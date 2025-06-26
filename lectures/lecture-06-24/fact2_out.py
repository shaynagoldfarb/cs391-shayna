##################################################################

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
def TINSige(x, y):
    return x >= y

##################################################################

def fun103(arg3):
  def fun104(arg4):
    def fun105(arg5):
      tmp115 = TINSige(arg4, arg3)
      tmp123 = None
      if (tmp115):
        tmp123 = arg5
      else:
        tmp116 = TVALint(1)
        tmp117 = TINSadd(arg4, tmp116)
        tmp118 = fun104(tmp117)
        tmp119 = TVALint(1)
        tmp120 = TINSadd(arg4, tmp119)
        tmp121 = TINSmul(tmp120, arg5)
        tmp122 = tmp118(tmp121)
        tmp123 = tmp122
      return tmp123
    return fun105
  tmp124 = TVALint(1)
  tmp125 = fun104(tmp124)
  tmp126 = TVALint(1)
  tmp127 = tmp125(tmp126)
  return tmp127

########################################################################

print("fact2(10) = " + str(fun103(10)))

########################################################################
