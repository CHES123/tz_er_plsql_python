def f_sort_avg(ls):
    try:
        res = [x for x in ls if type(x) == int]
        res.sort()
        res.append(sum(res)/len(res))
        return res
    except Exception as e:
        return f"error: {e}"