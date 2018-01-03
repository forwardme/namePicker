
def ngrams(input,n):
  input = input.split(' ')
  output = []
  for i in range(len(input)-n+1):
    output.append(input[i:i+n])
  return output
  
with open("/(001)国风·周南.txt","rb") as file:
  text = file.read()

ngrams = ngrams(text,2)
print ngrams
print "2-grams count is: "+str(len(ngrams))