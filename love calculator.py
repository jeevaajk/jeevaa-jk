def calculate_love_score(name1,name2):
    full_name=(name1+name2).lower()
    l = full_name.count("l")
    o = full_name.count("o")
    v = full_name.count("v")
    e = full_name.count("e")
    totl=l+o+v+e
    t = full_name.count("t")
    r = full_name.count("r")
    u = full_name.count("u")
    e1 = full_name.count("e")
    total=t+r+u+e1
    print(int(str(total)+str(totl)))
calculate_love_score("Jeevaa", "Annie Joshy")

    

   