#Convert English to Pig Latin
##TODO handle trailing punctuation better

def pig_latin(text):
    split_list = text.split()    
    for word in split_list:
        scratch_pad = ''
        for letter in word:
            if letter in 'aeiouy':
                if len(scratch_pad) == 0:
                    word = word + 'yay'
                else:
                    word = word[len(scratch_pad):]
                    word = word + scratch_pad + 'ay'
                break
            scratch_pad += letter
        print(word, end = ' ')

pig_latin(input("inputyay ethay ordway youyay antway igpay atinlayed :"))
