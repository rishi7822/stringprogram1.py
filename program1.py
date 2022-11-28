#program to split a substring in substring manner
input = "believe_in_yourself"

#split intializee
split_string = input.split('_')

output = []

#iteration
for i in range(len(split_string)):
    temp = split_string[:i+1]
    temp = "_".join(temp)
    output.append(temp)


print(output)