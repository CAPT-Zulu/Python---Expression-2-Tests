import re
# Made by: TheBox
# Version: 4.3
# I made it just to convert ugly pac3 and holopad to an easier format to manage.
# I may add more formats in the future but I wont add any from e2holo to anything cause theres to many issues that could cause problems.

# Variables Conversion
conversion = 3
    # Conversion from holopad to pac3 = 0,
    # Conversion from pac3 to holopad = 1,
    # Conversion from holopad to e2holo = 2,
    # Conversion from pac3 to e2holo = 3
    # Conversion from holopad to TheBox's Custom Format = 4
    # Conversion from pac3 to TheBox's Custom Format = 5

# Variables Input
indentation_input = 1
    # The levels of indentation the string imported is
    # Important for most conversions because of indentation in the spaces between the lines

# Variables Output
indentation_output = "    "
    # Output indentation / what is put in front of all the lines of code that outputs
separation_output = 1
    # Separation of the output lines

# Variables Customization
starting_number = 1
    # Only applies to pac3 to holopad, holopad to e2holo and pac3 to e2holo but the starting_number which the holo list starts at
material = '"debugwhite"'
    # Material set for holos which dont initaly have a material
    # If not using leave as "debugwhite"
parent = "HoloParent"
    # Entity parent for all holos
    # For a holo parent use "x" or "holoEntity(x)" depending on the conversion (replace x with the holo parents number)
additional_text = ""
    # Really only useful for conversion to e2holo so you can add optional text to the end of each line in the output
    # Must manually add a space to sperate the line I kept this in cause sometimes I need this
    # If not using leave it blank

# String Import
str_import = \
"""#(DO NOT PUT TEXT IN THIS LINE)#
    I++, HN++, HT[HN,table] = table(I, Base, Base, 0, vec(0, 0, 0), ang(0, 0, 0), vec(0.16, 0.25, 0.1), "models/props_wasteland/prison_bedframe001b.mdl", "", vec4(255, 255, 255, 255), 0)
	
    I++, HN++, HT[HN,table] = table(I, Base, Base, 0, vec(-8.0187, 2.92, 0.5547), ang(0, 0, 0), vec(0.1, 0.15, 0.1), "models/holograms/rcube_thick.mdl", "", vec4(255, 255, 255, 255), 0)
	
    I++, HN++, HT[HN,table] = table(I, Base, Base, 0, vec(-5.1047, 0.0093, 3.7002), ang(0, 0, 0), vec(0.1, 0.6, 0.699), "models/holograms/cube.mdl", "", vec4(255, 255, 255, 255), 0)
	
    I++, HN++, HT[HN,table] = table(I, Base, Base, 0, vec(-0.004, 3.909, 4.9), ang(0, 0, 0), vec(1, 0.2, 0.5), "models/holograms/cube.mdl", "", vec4(255, 255, 255, 255), 0)
	
    I++, HN++, HT[HN,table] = table(I, Base, Base, 0, vec(0, 0, 0), ang(0, -90, 0), vec(0.07, 0.2, 0.1), "models/props_wasteland/kitchen_shelf002a.mdl", "", vec4(255, 255, 255, 255), 0)
	
    I++, HN++, HT[HN,table] = table(I, Base, Base, 0, vec(-0.0072, 3.909, 3.8115), ang(0, 0, 0), vec(1, 0.2, 0.68), "models/holograms/cube.mdl", "", vec4(255, 255, 255, 255), 0)
	
    I++, HN++, HT[HN,table] = table(I, Base, Base, 0, vec(-6.543, 0.005, 2.9795), ang(0, 0, 0), vec(0.2, 0.854, 0.55), "models/holograms/hq_rcube_thin.mdl", "", vec4(255, 255, 255, 255), 0)
	
    I++, HN++, HT[HN,table] = table(I, Base, Base, 0, vec(5.947, 0, 6.125), ang(0, 0, 90), vec(0.3, 0.3, 0.853), "models/holograms/hq_rcylinder_thin.mdl", "", vec4(255, 255, 255, 255), 0)
	
    I++, HN++, HT[HN,table] = table(I, Base, Base, 0, vec(8.3087, 0.0105, 2.1699), ang(0, 0, 0), vec(0.1, 0.15, 0.05), "models/holograms/rcube_thick.mdl", "", vec4(255, 255, 255, 255), 0)
	
    I++, HN++, HT[HN,table] = table(I, Base, Base, 0, vec(0, 0, 4.9), ang(0, 0, 0), vec(1, 0.15, 0.5), "models/holograms/cube.mdl", "", vec4(255, 255, 255, 255), 0)
	
    I++, HN++, HT[HN,table] = table(I, Base, Base, 0, vec(-5.947, 0, 6.125), ang(0, 0, 90), vec(0.3, 0.3, 0.853), "models/holograms/hq_rcylinder_thin.mdl", "", vec4(255, 255, 255, 255), 0)
	
    I++, HN++, HT[HN,table] = table(I, Base, Base, 0, vec(5.105, 0.0093, 3.7002), ang(0, 0, 0), vec(0.1, 0.6, 0.699), "models/holograms/cube.mdl", "", vec4(255, 255, 255, 255), 0)
	
    I++, HN++, HT[HN,table] = table(I, Base, Base, 0, vec(0, 0, 0), ang(0, -90, 0), vec(0.19, 0.2, 0.1), "models/props_wasteland/kitchen_shelf002a.mdl", "", vec4(255, 255, 255, 255), 0)
	
    I++, HN++, HT[HN,table] = table(I, Base, Base, 0, vec(7.3061, 0.0028, 3.1084), ang(0, 0, 0), vec(0.1, 0.1, 0.4), "models/holograms/rcube.mdl", "", vec4(255, 255, 255, 255), 0)
	
    I++, HN++, HT[HN,table] = table(I, Base, Base, 0, vec(6.5431, 0.005, 2.9795), ang(0, 0, 0), vec(0.2, 0.854, 0.55), "models/holograms/hq_rcube_thin.mdl", "", vec4(255, 255, 255, 255), 0)
	
    I++, HN++, HT[HN,table] = table(I, Base, Base, 0, vec(0, 0, 1.4063), ang(0, 0, 0), vec(1, 0.6, 0.1), "models/holograms/cube.mdl", "", vec4(255, 255, 255, 255), 0)
	
    I++, HN++, HT[HN,table] = table(I, Base, Base, 0, vec(-0.0072, -3.909, 3.8115), ang(0, 0, 0), vec(1, 0.2, 0.68), "models/holograms/cube.mdl", "", vec4(255, 255, 255, 255), 0)
	
    I++, HN++, HT[HN,table] = table(I, Base, Base, 0, vec(-0.0007, -4.9335, 3.6289), ang(0, -90, 0), vec(0.02, 0.02, 0.02), "models/maxofs2d/construct_sign.mdl", "", vec4(255, 255, 255, 255), 0)
"""#(DO NOT PUT TEXT IN THIS LINE)#

# # # # Dont recommend editing below here # # # #

# Split Function
def splitline(lineL, starting_numberL, areaL, sizeL, angleL, colorL, modelL, matL):
    string1 = re.findall('\(.*?\)', lineL[indentation_input*4+starting_numberL:])
    string2 = re.findall('\".*?\"', lineL[indentation_input*4+starting_numberL:])
    if string2[matL] != '""':
        return string1[areaL], string1[sizeL], string1[angleL], string1[colorL], string2[modelL], string2[matL]
    else:
        return string1[areaL], string1[sizeL], string1[angleL], string1[colorL], string2[modelL], material

# String to list
str_import = str_import.splitlines()
str_import.pop(0)
export = []

# Main Conversion Lines
for line in str_import:
    if len(line) > (indentation_input*4):
        if conversion == 0:
            area, size, angle, color, model, mat = splitline(line, 38, 3, 2, 0, 1, 0, 1)
            export.append("I++, HN++, HT[HN,table] = table(I, Base, Base, 0, vec" + area + ", ang" + angle + ", vec" + size + ", " + model + ", " + mat + ", vec4" + color + ", " + str(parent) + ")")
        elif conversion == 1:
            area, size, angle, color, model, mat = splitline(line, 32, 0, 2, 1, 3, 0, 1)
            export.append("#[   ]#    Holos[" + str(starting_number) + ", array] = array(vec" + area + ", vec" + size + ", vec4" + color + ", ang" + angle + ", " + model + ", " + mat + ", " + str(parent) + ")")
        elif conversion == 2:
            area, size, angle, color, model, mat = splitline(line, 38, 3, 2, 0, 1, 0, 1)
            export.append("holoCreate(" + str(starting_number) + ", " + str(parent) + ":toWorld(vec" + area + "),vec" + size + ", " + str(parent) + ":toWorld(ang" + angle + "), vec4" + color + ", " + model + ") holoParent(" + str(starting_number) + ", " + str(parent) + ") holoMaterial(" + str(starting_number) + ", " + mat + ")")
        elif conversion == 3:
            area, size, angle, color, model, mat = splitline(line, 32, 0, 2, 1, 3, 0, 1)
            export.append("holoCreate(" + str(starting_number) + ", " + str(parent) + ":toWorld(vec" + area + "),vec" + size + ", " + str(parent) + ":toWorld(ang" + angle + "), vec4" + color + ", " + model + ") holoParent(" + str(starting_number) + ", " + str(parent) + ") holoMaterial(" + str(starting_number) + ", " + mat + ")")
        elif conversion == 4:
            area, size, angle, color, model, mat = splitline(line, 38, 3, 2, 0, 1, 0, 1)
            export.append("Not added in this version")
        elif conversion == 5:
            area, size, angle, color, model, mat = splitline(line, 32, 0, 2, 1, 3, 0, 1)
            export.append("Not added in this version")
        else:
            print("Conversion number invalid")
        starting_number += 1
# Export Printing
for lines_in_export in export:
    print(str(indentation_output) + str(lines_in_export) + str(additional_text))
    for spaces in range(0,separation_output): print()