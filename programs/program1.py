num=input("Enter the numbers")
keypad={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
result=[""]
for n in num:
    output=[]
    for r in result:
        for i in keypad[n]:
            output.append(r+i)
        result=output

print(result)
