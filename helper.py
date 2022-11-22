import time

def show_time(sttime,entime,op=""):
    print(f"sttime: {entime}")
    print(f"entime: {sttime}")
    print(f"Delta: {entime - sttime} secs for op: {op}")

    return entime - sttime