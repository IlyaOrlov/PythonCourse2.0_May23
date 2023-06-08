def Dec_mydec(fun):
    def mydec():
        print("===========")
        fun()
        print("===========")
    return mydec

@Dec_mydec
def Hello():
    print("Hello World")



