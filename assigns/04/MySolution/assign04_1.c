#include "runtime.h"

extern lamval1 f91(lamval1 x)
{
  lamval1 ret0;
  lamval1 tmp1, tmp2;

  tmp1 = LAMOPR_igt(x, LAMVAL_int(100));

  if (((lamval1_int)tmp1)->data)
  {
    // if x > 100 then x - 10
    ret0 = LAMOPR_sub(x, LAMVAL_int(10));
  }
  else
  {
    // else f91(f91(x + 11))
    tmp1 = LAMOPR_add(x, LAMVAL_int(11));
    tmp2 = f91(tmp1);
    ret0 = f91(tmp2);
  }

  return ret0;
}
