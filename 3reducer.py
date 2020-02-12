s = open("02.txt","r")
r = open("03.txt", "w")

thisKey = ""
thisValue = 0.0


counter = 0
old_value = None


for line in s:
  data = line.strip().split('\t')
  paymentType, amount = data

  if paymentType != thisKey:
    thisKey = paymentType 
    thisValue = 0.0
  
 
  if old_value is None:
    old_value = paymentType

  if old_value == paymentType:
    counter = counter + 1
  else:
    r.write(old_value + '\t' + str(counter)+'\n' )
    counter = 1
    old_value = paymentType

r.write(old_value + '\t' + str(counter)+'\n' )

s.close()
r.close()
