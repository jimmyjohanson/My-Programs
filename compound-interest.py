def compound_interest(principle, rate, time):
 
    Amnt = principle * (pow((1 + rate / 100), time))
    CI = Amnt - principle
    print("Compound interest is", CI)

compound_interest(10000, 10.25, 5)
