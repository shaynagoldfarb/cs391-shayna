(* ****** ****** *)
(* ****** ****** *)
//
// HX-2025-05-21:
// This is like declaring a class
// and also have some constructors
//
datatype term =
| TMvar of strn
| TMlam of (strn, term)
| TMapp of (term, term)
//
(* ****** ****** *)
(* ****** ****** *)
  
fun
term_print(t0: term): void =
(
case+ t0 of
//
|
TMvar(x0) =>
prints("TMvar(", x0, ")")
//
|
TMlam(x0, t1) =>
prints("TMlam(", x0, ";", t1, ")")
//
|
TMapp(t1, t2) =>
prints("TMapp(", t1, ";", t2, ")")
//
) where
{
  #impltmp
  g_print<term> = term_print
}(*where*)//end-of-[term_print(t0)]

(* ****** ****** *)
//
fun
term_size
(t0: term): sint =
(
case+ t0 of
|
TMvar(x0) => 1
|
TMlam(x0, t1) =>
1 + term_size(t1)
|
TMapp(t1, t2) =>
(1+term_size(t1)+term_size(t2))
)
//
(* ****** ****** *)
//
(*
HX-2025-05-21:
term_subst(t0, x0, u0) = t0[x0->u0]
*)
#extern
fun
term_subst
( t0: term
, x0: strn, u0: term): term
//
#implfun
term_subst
(t0, x0, u0) =
(
case+ t0 of
|TMvar(x1) =>
 if x0 = x1 then u0 else t0
|TMlam(x1, t1) =>
 if x0 = x1
 then t0 else TMlam(x1, term_subst(t1, x0, u0))
|TMapp(t1, t2) =>
 TMapp(term_subst(t1, x0, u0), term_subst(t2, x0, u0))
)(*case+*)//end-of-[term_subst(t0,x0,u0)]
//
(* ****** ****** *)
(* ****** ****** *)
//
(***********************************************************************)
(* end of [CS391-2025-Summer/lectures/lecture-05-21/lambda0.dats] *)
(***********************************************************************)
