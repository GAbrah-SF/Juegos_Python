import time


def hora():
    time_out = time.strftime(f"%I:%M %p.").lower()

    if int(time_out[:2]) == 1:
        return f"Es la: {time_out}"
    else:
        return f"Son las: {time_out}"


if __name__ == '__main__':
    print(f"\n{hora()}")