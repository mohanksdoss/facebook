print("Hello")

str = "I am Awesome"

print (str)

fn = " Umadevi "
ln = " Rajedran "



print (fn,ln )

# Data Type LIST

# List id data type that allows multiple values
values =[1, 2, 3, "uma", 5, 6]
print("The output is", values[3])   # Uma
print(values[-1])     # 6  last values in the list
print(values[1:4])  # 2 3 uma

# inserting into list
values.insert(4, "devi")
print(values)           # [1, 2, 3, 'uma', 'devi', 5, 6]
print("The new values added to list is", values[4])     # The new values added to list is devi

# Appending values to the list
values.append(7)
print("The new appended values to the list is", values[-1])  # The new appended values to the list is 7

# Updating the existing values
values[3] ="UMA"
values[4] ="DEVI"
print("The updated values are",values)    # The updated values are [1, 2, 3, 'UMA', 'DEVI', 5, 6, 7]

# Deleting exisitng values
del values[-1]
print("Delected the last value now the list has only these values ",values) # Delected the last value now the list has only these values  [1, 2, 3, 'UMA', 'DEVI', 5, 6]

