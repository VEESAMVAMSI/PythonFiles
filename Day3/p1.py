#write a funtion which  takes two arguments a,b type cast their value of second argument into integer then
# mjltiply both the arguments and print the   last digit of digit
#positional arguments-by dafault values,perfect assing to the valuesa,b-1,2
#keyword arguments-name(b=11,a=23)
#default arguments
#unknown arguments
def name(a,b):
    b=int(b)
    res=b*a
    print(res%10)
name(5,6.5)