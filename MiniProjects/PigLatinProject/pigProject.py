#Pig Latin Project

#Get sentence from user
original = input('Please enter a sentence you would like converted into pig latin: ').strip().lower()
 
#Split sentence into words
words = original.split()
#print(words) #check to see how sentence was split

#Loop through words & convert to pig latin
new_words=[]

for word in words:                   # if it starts with a vowel, add 'yay'
    if word[0]in 'aeiou':
        new_word= word+'yay' 
        new_words.append(new_word)
    else:                            #otherwise move first constant cluster to end and and 'ay'
        vowel_pos = 0
        for letter in word:
            if letter not in 'aeiou':
                vowel_pos=vowel_pos+1
            else:
                break
        cons = word[:vowel_pos]
        the_rest=word[vowel_pos:]
        new_word= the_rest + cons+'ay'
        new_words.append(new_word)

#print(new_words)#check if printing words correctly
       
    
#Stick words back together

output =' '.join(new_words) #join words together with a space      

#output the final string
print(output)
