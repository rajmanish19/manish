input_file =open("sample_input.txt","r")
output_file = open("output.txt","w+")
goodies={}
output_list=[]
for f in input_file:
    a=f.index(":")
    print(f[a+1:].strip())
    print(f[:a])
    goodies[f[:a]]=f[a+1:].strip()
print(goodies) 
b=list(goodies.values())
b=[int(i)for i in b]

b.sort(reverse=True)
print(b)

num_of_employees=int(input("Enter number of employees: "))
c=(len(b)-num_of_employees)

print(c)


for i in range(c):
    max_price=b[i]
    min_price=b[num_of_employees+i]
    if i == 0:
        diff=max_price-min_price
        idx_choosen=i
    elif (max_price-min_price)<diff:
        diff=max_price-min_price
        idx_choosen=i

choosen_prices=b[idx_choosen:num_of_employees+idx_choosen]

diff=max(choosen_prices)-min(choosen_prices)
print("diff",diff)

cnt=0
for key,value in goodies.items():
    b[cnt]
    if int(value)in choosen_prices and cnt<num_of_employees:
        str1=key+": "+value
        
        output_list.append(str1)
        cnt+=1
        print(str1)

output_file.write("The goodies selected for distribution: ")

output_file.write("\n")

for i in output_list:
    output_file.write(i)
    output_file.write("\n")
output_file.write("And the difference between the chosen goodie with highest price and the lowest price is "+str(diff))

input_file.close()
output_file.close()