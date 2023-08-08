#skip the fourth character 

word = input()
first_part = word[0: 3]
second_part = word[4: ]

result = first_part + second_part
print(result)

#skipping letters 

word = input()
i = int(input())
index = i + 1
first_part = word[0 : i]
last_part = word[index : ]
print(first_part + last_part )