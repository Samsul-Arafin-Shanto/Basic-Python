var = "3/4"
print (var)
var = "\u00BE"
print (var)

var = "\u0031\u0030"
print (var)

string = "Hello"
tobytes = string.encode('utf-8')
print (tobytes)
string = tobytes.decode('utf-8')
print (string)

stringa = "\u20B9"
print (stringa)
tobytesa = stringa.encode('utf-8')
print (tobytesa)
stringa = tobytesa.decode('utf-8')
print (stringa)