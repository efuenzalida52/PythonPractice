#Mini Project: Email Slicer Project

#practicing slicing first

#word = 'supercalifragilisticexpialidocious'
#print(word[0:5:1]) #starting at 0 index go up to 5 index by 1
#print(word[0:5:2]) #starting at 0 index go up to 5 index by 2
#print(word[5:9:1]) #print cali
#print(word[5:]) # index 5 till end
#print(word[5::2]) #start,(blank)end, step
#print(word[:7]) #start at beginning end at 7 (assumes stepping by 1)
#print(word[::-1]) #end to beginning by (-)1
#print(word[-2]) #by decrementing (-) you can move backwards through index

#practicing using index function

#print(word.index('cali'))#shows you what index number this part of index starts
#print(word[word.index('cali'):word.index('listic')]) #goes from start to start of 2nd word
#print(word[word.index('docious'):])
#print(word[word.index('fragilistic'):word.index('e')])#NOTE: index only returns first instance of phrase.
                                                      #Since 'super' has an 'e' this will return nothing.

###############################
###      EMAIL SLICER       ###
###############################

#Get user email address
email = input('Please enter your email address: ').strip()#removes any extra characters
print(email)

#slice out username
user = email[:email.index('@')] #beginning of email until @ sign


#slice out domain name
domain = email[email.index('@')+1 :] #start right after @ sign go till end

#format message
message = 'Your username is {} and your domain is {}'.format(user,domain)

#display output message
print(message)
