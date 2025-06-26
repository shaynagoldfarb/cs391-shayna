Tests performed:

term_int(1)
term_btf(True)

term_add = lambda a1, a2: term_opr("+", [a1, a2])
term_add(term_int(1), term_int(2))

term_lte(term_int(3), term_int(3))
term_dbl = term_lam("x", styp_int, term_add(term_var("x"), term_var("x")))

term_app(term_dbl, term_int(5))

term_fact = term_fix("f", "n", styp_int, styp_int,
    term_if0(term_lte(term_var("n"), term_int(0)),
        term_int(1),
        term_mul(term_var("n"), term_app(term_var("f"), term_sub(term_var("n"), term_int(1))))
    )
)

term = term_add(term_int(3), term_int(4))
cmp = term_comp00(term)
print(tcmp_pyemit(cmp))

term = term_app(term_dbl, term_int(10))
print(tcmp_pyemit(term_comp00(term)))