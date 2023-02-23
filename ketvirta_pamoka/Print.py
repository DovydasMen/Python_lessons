# object(s)	Any object, and as many as you like. Will be converted to string before printed
# sep='separator'	Optional. Specify how to separate the objects, if there is more than one. Default is ' '
# end='end'	Optional. Specify what to print at the end. Default is '\n' (line feed)
# file	Optional. An object with a write method. Default is sys.stdout
# flush	Optional. A Boolean, specifying if the output is flushed (True) or buffered (False). Default is False

# print statment negali likti galutiniame product versijoje
print("hello world")
print("hello", "World")
print(*["hello", "world"])
#* unpacking zenklas, greituoju budu iteruoti.
print("hello world", sep=",")
print("hello", "world", sep=" amazing ")

print('Hello world', 'Antanas', sep= '')