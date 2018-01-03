#coding = gbk
def ngrams(input,n):
  input = input.split('\r\n')
  output = []
  for i in range(len(input)-n+1):
    output.append(input[i:i+n])
  return output
  
with open("(001)国风·周南.txt","rb") as file:
  text = file.read().decode('gbk')

ngrams = ngrams(text,2)
print ngrams[1][0]
print "2-grams count is: "+str(len(ngrams))