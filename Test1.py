import re

convert = 3 # Conversion from holopad to pac3 = 0, conversion from pac3 to holopad = 1, conversion from holopad to e2holo = 2, conversion from pac3 to e2holo = 3

Spaces = "    "
num = 1 # Only applies to pac3 to holopad but the number which the list starts at
mat = "Mat1" # Material for all holos
parent = "Bullet" # holoparent for all holos

str_import = \
"""    I++, HN++, HT[HN,table] = table(I, Base, Base, 0, vec(5.3457, 0, 0), ang(90, 0, 0), vec(0.058, 0.058, 0.075), "models/sprops/misc/domes/size_1/dome_12x30.mdl", "sprops/textures/sprops_metal2", vec4(194, 116, 77, 255), 0)
	
    I++, HN++, HT[HN,table] = table(I, Base, Base, 0, vec(1.2969, 0.6465, 0), ang(0, 0, -90), vec(0.04, 0.02, 0.01), "models/props_c17/gravestone002a.mdl", "sprops/textures/sprops_chrome2", vec4(44, 40, 40, 255), 0)
	
    I++, HN++, HT[HN,table] = table(I, Base, Base, 0, vec(1.7725, 0, -0.6), ang(90, 0, 0), vec(0.06, 0.06, 0.015), "models/props_phx/misc/smallcannon.mdl", "sprops/textures/sprops_chrome2", vec4(44, 40, 40, 255), 0)
	
    I++, HN++, HT[HN,table] = table(I, Base, Base, 0, vec(2.5859, 0.6465, 0), ang(0, 0, -90), vec(0.04, 0.02, 0.01), "models/props_c17/gravestone002a.mdl", "sprops/textures/sprops_chrome2", vec4(44, 40, 40, 255), 0)
	
    I++, HN++, HT[HN,table] = table(I, Base, Base, 0, vec(0, 0, 0), ang(0, 0, 0), vec(2, 2, 2), "models/shells/shell_338mag.mdl", "", vec4(255, 218, 108, 255), 0)
	
    I++, HN++, HT[HN,table] = table(I, Base, Base, 0, vec(1.9453, -0.499, 0), ang(0, 0, 90), vec(0.165, 0.015, 0.015), "models/props_c17/gravestone002a.mdl", "sprops/textures/sprops_chrome2", vec4(44, 40, 40, 255), 0)"""

str_import = str_import.splitlines()

if convert == 0:
    for line in str_import:
        if line != "	":
            string2 = re.findall('\(.*?\)',line[42:])
            string3 = re.findall('\".*?\"',line[42:])
            model = string3.pop()
            angle = string2.pop()
            color = string2.pop()
            size = string2.pop()
            area = string2.pop()
            export = ("    I++, HN++, HT[HN,table] = table(I, Base, Base, 0, vec" + area + ", ang" + angle + ", vec" + size + ", " + model + ", " + mat + ", vec4" + color + ", " + str(parent) + ")")
            print(export)
            print()
elif convert == 1:
    for line in str_import:
        if line != "	":
            num += 1
            string2 = re.findall('\(.*?\)',line[36:])
            string3 = re.findall('\".*?\"',line[36:])
            color = string2.pop()
            size = string2.pop()
            angle = string2.pop()
            area = string2.pop()
            model = string3.pop()
            export = ("    #[   ]#    Holos[" + str(num) + ", array] = array(vec" + area + ", vec" + size + ", vec4" + color + ", ang" + angle + ", " + model + ", " + mat + ", " + str(parent) + ")")
            print(export)
            print()
elif convert == 2:
    for line in str_import:
        if line != "	":
            string2 = re.findall('\(.*?\)',line[42:])
            string3 = re.findall('\".*?\"',line[42:])
            model = string3.pop()
            angle = string2.pop()
            color = string2.pop()
            size = string2.pop()
            area = string2.pop()
            export = ("    holoCreate(" + str(num) + ", " + str(parent) + ":toWorld(vec" + area + "),vec" + size + ", " + str(parent) + ":toWorld(ang" + angle + "), vec4" + color + ", " + model + ") holoParent(" + str(num) + ", " + str(parent) + ") holoMaterial(" + str(num) + ", " + mat + ")")
            print(export)
            print()
elif convert == 3:
    for line in str_import:
        if line != "	":
            num += 1
            string2 = re.findall('\(.*?\)',line[36:])
            string3 = re.findall('\".*?\"',line[36:])
            color = string2.pop()
            size = string2.pop()
            angle = string2.pop()
            area = string2.pop()
            model = string3.pop()
            export = ("    holoCreate(" + str(num) + ", " + str(parent) + ":toWorld(vec" + area + "),vec" + size + ", " + str(parent) + ":toWorld(ang" + angle + "), vec4" + color + ", " + model + ") holoParent(" + str(num) + ", " + str(parent) + ") holoMaterial(" + str(num) + ", " + mat + ")")
            print(export)
            print()