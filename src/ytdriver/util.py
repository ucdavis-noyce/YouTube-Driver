def time2seconds(s):
    """
    Converts a given time (video duration, ad time, etc.) to seconds
    """
    s = s.split(':')
    s.reverse()
    wait = 0
    factor = 1
    for t in s:
        wait += int(t) * factor
        factor *= 60
    return wait
