num=int(input("\nEnter the number:"))
def factorial(num):
  if num==0 or num==1:
    return 1
  else:
    return num*factorial(num)
    result=factorial(num)
    print("the factorial of given number",num,"is",result)
    