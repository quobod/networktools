def non_none_value(*args):
    errors = []

    for a in args:
        if a == None:
            errors.append({"{}".format(a): "Nonne"})
        else:
            continue

    if len(errors) > 0:
        return {"status": False, "errors": errors}
    else:
        return {"status": True}
