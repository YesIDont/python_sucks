user_name = 'Vader'
# use \n for new line
# and escape characters with \
print("My name is " + user_name + ",\njoin the dark side.")
print(user_name.lower())
print(user_name.isupper())
print(user_name.upper().isupper())
print(len(user_name))
print(user_name[0]) # get character by index
print(user_name.index('V')) # get index of letter, throws error if not found
print(user_name.replace('V', 'Tr'))
