#coding = gbk
import re
import operator
def cleanInput(input):
  output = re.sub('[\n\r]+'," ",input)
  output = re.sub(ur'[\uff0c\u3002\uff1a\u25cb]+'," ",output)
  output = re.sub(' +',"",output)
  return output
def ngrams(input,n):
  input = list(input)
  output = {}
  for i in range(len(input)-n+1):
    ngramTemp = " ".join(input[i:i+n])
    if ngramTemp not in output:
      output[ngramTemp] = 0
    output[ngramTemp] += 1
  return output
  
with open("001.txt","rb") as file:
  text = file.read().decode('gbk')


ngrams = ngrams(cleanInput(text),2)
#print ngrams
sortedNgrams = sorted(ngrams.items(),key=operator.itemgetter(1),reverse=True)
#print sortedNgrams
print "2-grams count is: "+str(len(ngrams))
with open('outputdata.txt','w') as file:
  for items in sortedNgrams:
    name,frequency = items
    file.writelines(name.encode('utf-8')+"  "+str(frequency))
    file.writelines('\n')