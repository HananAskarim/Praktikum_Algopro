def konversiSuhu(C = 0, F = 0):
    "Fungsi mengkonversikan Celcius ke Fahrenheit atau sebaliknya"
    if C != 0:
        y = ((9*C/5) + 32)
        print("Suhu", C, "Celcius setara dengan", y, "Fahrenheit")
    elif F != 0:
        b = ((F-32) * 5/9)
        print("Suhu", F, "Celcius setara dengan", b, "Celcius")
    else:
        print("Suhu 0 Celcius setara dengan 32 Fahrenheit")
    return;
