
# Display the program's instructions.
print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch.Press Ctrl-C to quit.')
input() # press Enter to begin
print('Started')
sec = 1
minu = 0
hours = 0
try:
    input()
    while True:
        print(minu,":",sec, end="\r")
        if sec==60:
            sec=0
        else:
            sec +=1
        if minu==60:
            minu=0
        else:
            minu+=1
        if hours==24:
            hours+=1
            
        time.sleep(1)
except KeyboardInterrupt:
 # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone.')
