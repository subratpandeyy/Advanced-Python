register={"Ram","Shyam","Mohan","Sohan","Rohan"}
present={"Ram","Shyam","Mohan","subrat"}
register.add("Sasikumar")
register.update({"Sagar","Brundaban","Ayush"})


notpresent = register-present
presentbutnoreg = present-register
presentinboth=register&present





print("Register student:", register)
print("Present student:", present)
print("Present in both:", presentinboth)
print("absent:", notpresent)
print("Present but no register:", presentbutnoreg)