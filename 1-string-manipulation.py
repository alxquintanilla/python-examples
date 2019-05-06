print("\n")
print("***************")
print("* Hello World *")
print("***************")
# String manipulation section

strVar = "some val"
print("\n "+strVar)
print("val was found in position:" + str(strVar.find("val")))

strVar = "Superman, Batman, etc"
splitResult = strVar.split(",");

print("\n"+strVar)
print("Your heroes are: {"+ (splitResult[0]) +","+ (splitResult[1])+"}")

print("\nsubstring : "+ (strVar[0:8]))

print("\nreplace : "+ strVar.replace("Superman","Wonder Woman"))
