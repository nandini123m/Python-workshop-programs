a=input("Enter the word:")
vow=" "
non_vow=" "
for x in a:
    if(x=="a" or x=="e" or x=="i" or x=="o" or x=="u"):
        vow=vow+x
    else:
        non_vow=non_vow+x
print("Vowels:",vow,len(vow))
print("Non vowels:",non_vow,len(non_vow))
