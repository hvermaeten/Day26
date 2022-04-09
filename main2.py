sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆
word_list = sentence.split()
# Write your code below:
result = {word:len(word) for word in word_list}


print(result)