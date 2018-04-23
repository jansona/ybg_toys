def my_first_interpreter(code):
    # Make your esolang interpreter here
    counter = 0
    sr = ''
    for o in code:
        if o=='+':
            counter+=1
            counter%=256
        elif o=='.':
            sr+=chr(counter)
    print(sr)            
    return sr

print(my_first_interpreter("++++++\
++++++++++++++++++++++++++++++++++\
+++++++++++++++++++++++++.+.+.+.+.\
+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+."))