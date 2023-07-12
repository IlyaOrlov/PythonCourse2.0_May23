def actionfun(arg1, arg2, /, *, additional_sign, sign):
    if sign == "+":
        return f"{additional_sign}{arg1 + arg2}"
    else:
        return f"{additional_sign}{arg1 - arg2}"


res = actionfun(10, 20, sign="-", additional_sign=">")
print(res)
