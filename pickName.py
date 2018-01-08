#coding = gbk
import re

def cleanInput(input):
  output = re.sub('[\n\r]+'," ",input)
  output = re.sub(ur'[\uff0c\u3002\uff1a\u25cb]+'," ",output)
  output = re.sub(' +',"",output)
  return output
def ngrams(input,n):
  input = list(input)
  output = []
  for i in range(len(input)-n+1):
    output.append(tuple(input[i:i+n]))
  return output
  
with open("001.txt","rb") as file:
  text = file.read().decode('gbk')


ngrams = ngrams(cleanInput(text),2)

print ngrams
print "2-grams count is: "+str(len(ngrams))
with open('outputdata.txt','w') as file:
  for items in ngrams:
    for item in items:
      file.writelines(item.encode('utf-8'))
    file.writelines('\n')