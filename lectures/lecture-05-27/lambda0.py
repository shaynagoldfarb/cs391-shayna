# datatype term =
# | TMvar of strn
# | TMlam of (strn, term)
# | TMapp of (term, term)

class term:
    ctag = ""
    def __str__(self):
        return ("term(" + self.ctag + ")")
# end-of-class(term)

class term_var(term):
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = "TMvar"
    def __str__(self):
        return ("TMvar(" + self.arg1 + ")")
# end-of-class(term_var(term))

class term_lam(term):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = "TMlam"
    def __str__(self):
        return ("TMlam(" + self.arg1 + "," + str(self.arg2) + ")")
# end-of-class(term_lam(term))

class term_app(term):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = "TMapp"
    def __str__(self):
        return ("TMapp(" + str(self.arg1) + "," + str(self.arg2) + ")")
# end-of-class(term_app(term))

var_x = term_var("x")
var_y = term_var("y")
term_I = term_lam("x", var_x) # lam x. x
print("term_I = " + str(term_I))
term_K = term_lam("x", term_lam("y", var_x)) # lam x. lam y. x
term_K1 = term_lam("x", term_lam("y", var_y)) # lam x. lam y. y
print("term_K = " + str(term_K))
print("term_K1 = " + str(term_K1))

def term_subst(tm0, x00, sub):
    def subst(tm0):
        return term_subst(tm0, x00, sub)
    # |TMvar(x1) =>
    #  if x0 = x1 then u0 else t0
    if (tm0.ctag == "TMvar"):
        x01 = tm0.arg1
        # print("term_subst: TMvar")
        # print("x00 = " + x00)
        # print("x01 = " + x01)
        return sub if (x00==x01) else tm0
    # |TMlam(x1, t1) =>
    #  if x0 = x1
    #  then t0 else TMlam(x1, term_subst(t1, x0, u0))
    if (tm0.ctag == "TMlam"):
        x01 = tm0.arg1
        tm1 = tm0.arg2
        return tm0 if (x00==x01) else term_lam(x01, subst(tm1))
    # |TMapp(t1, t2) =>
    #  TMapp(term_subst(t1, x0, u0), term_subst(t2, x0, u0))
    if (tm0.ctag == "TMapp"):
        tm1 = tm0.arg1
        tm2 = tm0.arg2
        return term_app(subst(tm1), subst(tm2))
    raise TypeError(tm0) # HX-2025-05-27: should be deadcode!

test_tm1 = term_subst(var_x, "x", term_I)
print("test_tm1 = " + str(test_tm1))
test_tm2 = term_subst(var_x, "y", term_I)
print("test_tm2 = " + str(test_tm2))
test_tm3 = term_subst(term_app(var_x, var_y), "y", term_I)
print("test_tm3 = " + str(test_tm3))
