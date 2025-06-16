class term:
    ctag = ""
    def __str__(self):
        return ("term(" + self.ctag + ")")
# end-of-class(term)

# | TMtup of (term, term)
class term_tup(term):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1  # first term
        self.arg2 = arg2  # second term
        self.ctag = "TMtup"
    def __str__(self):
        return "TMtup(" + str(self.arg1) + ";" + str(self.arg2) + ")"
# end-of-class(term_tup)

# | TMfst of term
class term_fst(term):
    def __init__(self, arg1):
        self.arg1 = arg1  # tuple term
        self.ctag = "TMfst"
    def __str__(self):
        return "TMfst(" + str(self.arg1) + ")"
# end-of-class(term_fst)

# | TMsnd of term
class term_snd(term):
    def __init__(self, arg1):
        self.arg1 = arg1  # tuple term
        self.ctag = "TMsnd"
    def __str__(self):
        return "TMsnd(" + str(self.arg1) + ")"
# end-of-class(term_snd)

# | TMlet of (strn, term, term)
class term_let(term):
    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1  # variable name (string)
        self.arg2 = arg2  # term to bind
        self.arg3 = arg3  # body using bound variable
        self.ctag = "TMlet"
    def __str__(self):
        return "TMlet(" + self.arg1 + ";" + str(self.arg2) + ";" + str(self.arg3) + ")"
# end-of-class(term_let)

class tval:
    ctag = ""
    def __str__(self):
        return ("tval(" + self.ctag + ")")
# end-of-class(tval)

class tval_tup(tval):
    def __init__(self, val1, val2):
        self.arg1 = val1
        self.arg2 = val2
        self.ctag = "TVtup"
    def __str__(self):
        return f"TVtup({self.arg1}, {self.arg2})"

class styp:
    ctag = ""
    def __str__(self):
        return ("styp(" + self.ctag + ")")
# end-of-class(styp)

# | STbas of strn # int, bool, ...
class styp_bas:
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = "STbas"
    def __str__(self):
        return ("STbas(" + self.arg1 + ")")
# end-of-class(styp_bas(styp))

styp_int = styp_bas("int")
styp_bool = styp_bas("bool")
styp_list_int = styp_bas("list(int)")
styp_list_list_int = styp_bas("list(list(int))")

# | STtup of (styp, styp) # for pairs
class styp_tup:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = "STtup"
    def __str__(self):
        return ("STtup(" + str(self.arg1) + ";" + str(self.arg2) + ")")
# end-of-class(styp_tup(styp))

# | STtup of (styp, styp) # for pairs
class styp_tup:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = "STtup"
    def __str__(self):
        return ("STtup(" + str(self.arg1) + ";" + str(self.arg2) + ")")
# end-of-class(styp_tup(styp))

styp_int2 = styp_tup(styp_int, styp_int)

# | STfun of (styp, styp) # for functions
class styp_fun:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = "STfun"
    def __str__(self):
        return ("STfun(" + str(self.arg1) + ";" + str(self.arg2) + ")")
# end-of-class(styp_fun(styp))

styp_fun_int_int = styp_fun(styp_int, styp_int)

# | TMint of int
class term_int(term):
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = "TMint"
    def __str__(self):
        return ("TMint(" + str(self.arg1) + ")")
# end-of-class(term_int(term))

# | TMbtf of bool
class term_btf(term):
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = "TMbtf"
    def __str__(self):
        return ("TMbtf(" + str(self.arg1) + ")")
# end-of-class(term_btf(term))

# | TMvar of strn
class term_var(term):
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = "TMvar"
    def __str__(self):
        return ("TMvar(" + self.arg1 + ")")
# end-of-class(term_var(term))

# | TMlam of (strn(*var*), styp, term)
class term_lam(term):
    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.ctag = "TMlam"
    def __str__(self):
        return ("TMlam(" + self.arg1 + ";" + str(self.arg2) + ";" + str(self.arg3) + ")")
# end-of-class(term_lam(term))

# | TMapp of (term, term)
class term_app(term):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = "TMapp"
    def __str__(self):
        return ("TMapp(" + str(self.arg1) + ";" + str(self.arg2) + ")")
# end-of-class(term_app(term))

# | TMopr of (strn(*opr*), list(term))
class term_opr(term):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = "TMopr"
    def __str__(self):
        return ("TMopr(" + self.arg1 + ";" + str(self.arg2) + ")")
# end-of-class(term_opr(term))

# | TMif0 of (term, term, term)
class term_if0(term):
    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.ctag = "TMif0"
    def __str__(self):
        return ("TMif0(" + str(self.arg1) + ";" + str(self.arg2) + ";" + str(self.arg3) + ")")
# end-of-class(term_if0(term))

# TMfix of
# (strn(*f*), strn(*x*), styp(*arg*), styp(*res*), term)
class term_fix(term):
    def __init__(self, arg1, arg2, arg3, arg4, arg5):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.arg4 = arg4
        self.arg5 = arg5
        self.ctag = "TMfix"
    def __str__(self):
        return ("TMfix(" + self.arg1 + ";" + self.arg2 + ";" + str(self.arg3) + str(self.arg4) + ";" + str(self.arg5) + ")")
# end-of-class(term_fix(term))

# datatype tval =
# | TVint of int
# | TVbtf of bool
# | TVclo of (term, xenv)

class tval_int(tval):
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = "TVint"
    def __str__(self):
        return ("TVint(" + str(self.arg1) + ")")
# end-of-class(tval_int(tval))

class tval_btf(tval):
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = "TVbtf"
    def __str__(self):
        return ("TVbtf(" + str(self.arg1) + ")")
# end-of-class(tval_btf(tval))

class tval_clo(tval):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = "TVclo"
    def __str__(self):
        return ("TVclo(" + str(self.arg1) + ";" + str(self.arg2) + ")")
# end-of-class(tval_clo(tval))

##################################################################

# datatype xenv =
# | EVnil of ()
# | EVcons of (strn, tval, xenv)

class xenv:
    ctag = ""
    def __str__(self):
        return ("xenv(" + self.ctag + ")")
# end-of-class(xenv)

class xenv_nil(xenv):
    def __init__(self):
        self.ctag = "EVnil"
    def __str__(self):
        return ("EVnil(" + ")")
# end-of-class(xenv_nil(xenv))

class xenv_cons(xenv):
    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.ctag = "EVcons"
    def __str__(self):
        return ("EVcons(" + self.arg1 + ";" + str(self.arg2) + ";" + str(self.arg3) + ")")
# end-of-class(xenv_cons(xenv))

##################################################################

term_add = lambda a1, a2: term_opr("+", [a1, a2])
term_sub = lambda a1, a2: term_opr("-", [a1, a2])
term_mul = lambda a1, a2: term_opr("*", [a1, a2])
term_div = lambda a1, a2: term_opr("/", [a1, a2])
term_mod = lambda a1, a2: term_opr("%", [a1, a2])

term_lt0 = lambda a1, a2: term_opr("<", [a1, a2])
term_gt0 = lambda a1, a2: term_opr(">", [a1, a2])
term_eq0 = lambda a1, a2: term_opr("=", [a1, a2])
term_lte = lambda a1, a2: term_opr("<=", [a1, a2])
term_gte = lambda a1, a2: term_opr(">=", [a1, a2])
term_neq = lambda a1, a2: term_opr("!=", [a1, a2])
term_cmp = lambda a1, a2: term_opr("cmp", [a1, a2])

##################################################################

# #extern
# fun
# term_eval00(tm0: term): tval
# #extern
# fun
# term_eval01(tm0: term, env: xenv): tval

def term_eval00(tm0):
    return term_eval01(tm0, xenv_nil())

##################################################################

def xenv_search(env, x00):
    if env.ctag == "EVnil":
        return None
    if env.ctag == "EVcons":
        if env.arg1 == x00:
            return env.arg2
        else:
            return xenv_search(env.arg3, x00)
    raise TypeError(env) # HX-2025-06-03: deadcode!

##################################################################
        
def term_eval01(tm0, env):
    # print("term_eval01: tm0 = " + str(tm0))
    if (tm0.ctag == "TMint"):
        return tval_int(tm0.arg1)
    if (tm0.ctag == "TMbtf"):
        return tval_btf(tm0.arg1)
    if (tm0.ctag == "TMlam"):
        return tval_clo(tm0, env)
    if (tm0.ctag == "TMfix"):
        return tval_clo(tm0, env)
    if (tm0.ctag == "TMvar"):
        tv0 = xenv_search(env, tm0.arg1)
        assert tv0 is not None
        return tv0
    if (tm0.ctag == "TMopr"):
        pnm = tm0.arg1
        ags = tm0.arg2 # list of arguments
        if (pnm == "+"):
            assert len(ags) == 2
            tv1 = term_eval01(ags[0], env)
            tv2 = term_eval01(ags[1], env)
            # print("TMopr: tv1 = " + str(tv1))
            # print("TMopr: tv2 = " + str(tv2))
            assert tv1.ctag == "TVint"
            assert tv2.ctag == "TVint"
            return tval_int(tv1.arg1 + tv2.arg1)
        if (pnm == "-"):
            assert len(ags) == 2
            tv1 = term_eval01(ags[0], env)
            tv2 = term_eval01(ags[1], env)
            assert tv1.ctag == "TVint"
            assert tv2.ctag == "TVint"
            return tval_int(tv1.arg1 - tv2.arg1)
        if (pnm == "*"):
            assert len(ags) == 2
            tv1 = term_eval01(ags[0], env)
            tv2 = term_eval01(ags[1], env)
            assert tv1.ctag == "TVint"
            assert tv2.ctag == "TVint"
            return tval_int(tv1.arg1 * tv2.arg1)
        if (pnm == "%"):
            assert len(ags) == 2
            tv1 = term_eval01(ags[0], env)
            tv2 = term_eval01(ags[1], env)
            assert tv1.ctag == "TVint"
            assert tv2.ctag == "TVint"
            return tval_int(tv1.arg1 % tv2.arg1)
        if (pnm == "/"):
            assert len(ags) == 2
            tv1 = term_eval01(ags[0], env)
            tv2 = term_eval01(ags[1], env)
            assert tv1.ctag == "TVint"
            assert tv2.ctag == "TVint"
            return tval_int(tv1.arg1 // tv2.arg1)
        if (pnm == "<"):
            assert len(ags) == 2
            tv1 = term_eval01(ags[0], env)
            tv2 = term_eval01(ags[1], env)
            assert tv1.ctag == "TVint"
            assert tv2.ctag == "TVint"
            return tval_btf(tv1.arg1 < tv2.arg1)
        if (pnm == ">"):
            assert len(ags) == 2
            tv1 = term_eval01(ags[0], env)
            tv2 = term_eval01(ags[1], env)
            assert tv1.ctag == "TVint"
            assert tv2.ctag == "TVint"
            return tval_btf(tv1.arg1 > tv2.arg1)
        if (pnm == "="):
            assert len(ags) == 2
            tv1 = term_eval01(ags[0], env)
            tv2 = term_eval01(ags[1], env)
            assert tv1.ctag == "TVint"
            assert tv2.ctag == "TVint"
            return tval_btf(tv1.arg1 == tv2.arg1)
        if (pnm == "<="):
            assert len(ags) == 2
            tv1 = term_eval01(ags[0], env)
            tv2 = term_eval01(ags[1], env)
            assert tv1.ctag == "TVint"
            assert tv2.ctag == "TVint"
            return tval_btf(tv1.arg1 <= tv2.arg1)
        if (pnm == ">="):
            assert len(ags) == 2
            tv1 = term_eval01(ags[0], env)
            tv2 = term_eval01(ags[1], env)
            assert tv1.ctag == "TVint"
            assert tv2.ctag == "TVint"
            return tval_btf(tv1.arg1 >= tv2.arg1)
        if (pnm == "!="):
            assert len(ags) == 2
            tv1 = term_eval01(ags[0], env)
            tv2 = term_eval01(ags[1], env)
            assert tv1.ctag == "TVint"
            assert tv2.ctag == "TVint"
            return tval_btf(tv1.arg1 != tv2.arg1)
        raise TypeError(pnm) # HX-2025-06-03: unsupported!
    if (tm0.ctag == "TMapp"):
        tm1 = tm0.arg1
        tv1 = term_eval01(tm1, env)
        assert tv1.ctag == "TVclo"
        tm2 = tm0.arg2
        tv2 = term_eval01(tm2, env)
        tmf = tv1.arg1
        env = tv1.arg2
        if tmf.ctag == "TMlam":
            x01 = tmf.arg1
            env = xenv_cons(x01, tv2, env)
            return term_eval01(tmf.arg2, env)
        if tmf.ctag == "TMfix":
            f00 = tmf.arg1
            env = xenv_cons(f00, tv1, env)
            x01 = tmf.arg2
            env = xenv_cons(x01, tv2, env)
            return term_eval01(tmf.arg3, env)
        raise TypeError(tmf) # HX-2025-06-03: type error!
    if (tm0.ctag == "TMif0"):
        tm1 = tm0.arg1
        tv1 = term_eval01(tm1, env)
        assert tv1.ctag == "TVbtf"
        if tv1.arg1:
            return term_eval01(tm0.arg2, env) # then
        else:
            return term_eval01(tm0.arg3, env) # else
    if (tm0.ctag == "TMtup"):
        tv1 = term_eval01(tm0.arg1, env)
        tv2 = term_eval01(tm0.arg2, env)
        return tval_tup(tv1, tv2)

    if (tm0.ctag == "TMfst"):
        tvtup = term_eval01(tm0.arg1, env)
        assert tvtup.ctag == "TVtup"
        return tvtup.arg1

    if (tm0.ctag == "TMsnd"):
        tvtup = term_eval01(tm0.arg1, env)
        assert tvtup.ctag == "TVtup"
        return tvtup.arg2
    if (tm0.ctag == "TMlet"):
        val = term_eval01(tm0.arg2, env)
        new_env = xenv_cons(tm0.arg1, val, env)
        return term_eval01(tm0.arg3, new_env)
    raise TypeError(tm0)

# int8 = (int, int, int, int, int, int, int, int)
def board8():
    zero = term_int(0)
    return term_tup(zero, term_tup(zero, term_tup(zero, term_tup(zero,
           term_tup(zero, term_tup(zero, term_tup(zero, zero)))))))

# board_get: if i=0 then bd.0 else if i=1 then bd.1 … 
def board_get():
    return term_fix("board_get", "bd", None, None,
        term_lam("i", None,
            term_if0(term_opr("=", [term_var("i"), term_int(0)]),
                  term_fst(term_var("bd")),
            term_if0(term_opr("=", [term_var("i"), term_int(1)]),
                  term_snd(term_var("bd")),
            term_if0(term_opr("=", [term_var("i"), term_int(2)]),
                  term_snd(term_var("bd")),
            term_if0(term_opr("=", [term_var("i"), term_int(3)]),
                  term_snd(term_var("bd")),
            term_if0(term_opr("=", [term_var("i"), term_int(4)]),
                  term_snd(term_var("bd")),
            term_if0(term_opr("=", [term_var("i"), term_int(5)]),
                  term_snd(term_var("bd")),
            term_if0(term_opr("=", [term_var("i"), term_int(6)]),
                  term_snd(term_var("bd")),
            term_if0(term_opr("=", [term_var("i"), term_int(7)]),
                  term_snd(term_var("bd")),
            term_int(-1)  # default case
            ))))))))))

# fun safety_test1: can a piece on row i0 and col j0 capture one on row i and col j
def safety_test1():
    return term_lam("i0", None, term_lam("j0", None, term_lam("i", None,
           term_lam("j", None,
               term_opr("and", [
                   term_opr("!=", [term_var("j0"), term_var("j")]),
                   term_opr("!=", [
                       term_opr("abs", [term_opr("-", [term_var("i0"), term_var("i")])]),
                       term_opr("abs", [term_opr("-", [term_var("j0"), term_var("j")])])
                   ])
               ])
           ))))

# fun safety_test2: can a piece on row i0 and col j0 capture any r<=i
def safety_test2():
    return term_fix("safety_test2", "u", None, None,
        term_lam("i", None,
            term_if0(term_opr(">=", [term_var("i"), term_int(0)]),
                term_let("j", term_app(term_app(term_var("board_get"), term_var("u.bd")), term_var("i")),
                    term_if0(
                        term_app(term_app(term_app(term_app(term_var("safety_test1"),
                             term_var("u.i0")), term_var("u.j0")),
                             term_var("i")), term_var("j")),
                        term_app(term_app(term_var("safety_test2"), term_var("u")), term_opr("-", [term_var("i"), term_int(1)])),
                        term_btf(False)
                    )
                ),
                term_btf(True)
            )
        )
    )

# search: finds num of distinct solutions to the puzzle
def search():
    return term_fix("search", "bd", None, None,
        term_lam("i", None,
        term_lam("j", None,
        term_lam("nsol", None,
            term_if0(term_opr("<", [term_var("j"), term_int(8)]),
                term_let("safe", term_app(term_app(term_app(term_app(term_var("safety_test2"),
                                                     term_var("i")), term_var("j")),
                                                     term_var("bd")), term_opr("-", [term_var("i"), term_int(1)])),
                    term_if0(term_var("safe"),
                        term_let("bd1", term_app(term_app(term_app(term_var("board_set"),
                                                       term_var("bd")), term_var("i")), term_var("j")),
                            term_if0(term_opr("=", [term_opr("+", [term_var("i"), term_int(1)]), term_int(8)]),
                                term_app(term_app(term_app(term_var("search"), term_var("bd")), term_var("i")), term_opr("+", [term_var("j"), term_int(1)])),
                                term_app(term_app(term_app(term_var("search"), term_var("bd1")), term_opr("+", [term_var("i"), term_int(1)])), term_int(0))
                            )
                        ),
                        term_app(term_app(term_app(term_var("search"), term_var("bd")), term_var("i")), term_opr("+", [term_var("j"), term_int(1)]))
                    )
                ),
                term_if0(term_opr(">", [term_var("i"), term_int(0)]),
                    term_app(term_app(term_app(term_var("search"), term_var("bd")), term_opr("-", [term_var("i"), term_int(1)])),
                        term_opr("+", [
                            term_app(term_app(term_var("board_get"), term_var("bd")), term_opr("-", [term_var("i"), term_int(1)])),
                            term_int(1)
                        ])
                    ),
                    term_var("nsol")
                )
            )
        ))))
