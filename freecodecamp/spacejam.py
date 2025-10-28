def space_jam(s:str)->str:

    return s.replace(" ","").replace("","  ").strip().upper()

print(space_jam("freeCodeCamp"))
print(space_jam("   free   Code   Camp   "))