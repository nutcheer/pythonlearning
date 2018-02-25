language = ['C','C++','C#','Java','Python','Ruby','R','PHP','JavaScript','Perl','Basic','Pascal','HTML']
print(language)
print("My favorite coding-language is "+language[4])
print(language.pop(-1)+" is not a common language so I decide to del it from my list.")
language.append("Go")

Best_language = "PHP"
language.remove(Best_language)
print("\n"+Best_language+" is the \"BEST\" language in the world so I decide to del it from my list!")
print("So my list has still "+str(len(language))+" languages.")
print(language)
