from numpy.linalg import norm

sorts_by_name = {
    "asum"       : sum,
    "al2"        : (lambda v: norm(v, ord=2)),
    "amax"       : max,
    "amaxratio"  : (lambda v: float(max(v)) / min(v)), # could also do scaling?
    "amaxdiff"   : (lambda v: max(v) - min(v)),
    "none"       : None,
    "dsum"       : (lambda v: -sum(v)),
    "dl2"        : (lambda v: -norm(v, ord=2)),
    "dmax"       : (lambda v: -max(v)),
    "dmaxtratio" : (lambda v: float(min(v)) / max(v)), # see above
    "dmaxdiff"   : (lambda v: min(v) - max(v))
}