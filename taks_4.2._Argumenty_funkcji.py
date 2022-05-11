def check_palidrom(palidrom):
    if palidrom[-1::-1] == palidrom[0: len(palidrom)]:
        print(f"The word {palidrom} is palidrom")
    else:
        print(f"The word {palidrom} is not palidrom")
      
check_palidrom("potop")
check_palidrom("kajak")
check_palidrom("python")
check_palidrom("oko")
check_palidrom("komputer")
check_palidrom("biurko")
check_palidrom("owocowo")
check_palidrom("sos")