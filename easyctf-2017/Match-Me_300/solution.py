import hashlib

guy_prefs = []
girl_prefs = []

def load_preferences(_file):
    f = open(_file, "r").readlines()
    prefs = []
    for line in f:
        line = line.strip()

        index = line.find(" ")
        name = line[:index]
        preferences = line[index+1:].split(", ")
        data = {}
        data["name"] = name
        data["preferences"] = map(int, preferences)
        prefs.append(data)
    return prefs

guy_data = load_preferences("male_prefs.txt")
girl_data = load_preferences("female_prefs.txt")

guy_filtered = []
for guy in guy_data:
    new = []
    for girl in guy["preferences"]:
        new.append(girl_data[girl-1]["name"])
    data = {}
    data["name"] = guy["name"]
    data["preferences"] = new
    guy_filtered.append(data)

girl_filtered = []
for girl in girl_data:
    new = []
    for guy in girl["preferences"]:
        new.append(guy_data[guy-1]["name"])
    data = {}
    data["name"] = girl["name"]
    data["preferences"] = new
    girl_filtered.append(data)

girl_prefs = {d["name"]: d["preferences"] for d in girl_filtered}
guy_prefs = {d["name"]: d["preferences"] for d in guy_filtered}

guys = guy_prefs.keys()
girls = girl_prefs.keys()

free_guys = guys[:]
matches = {}
while free_guys:
    guy = free_guys.pop(0)
    preferences = guy_prefs[guy]
    for girl in preferences:
        other_guy = matches.get(girl)
        if other_guy:
            # Girl is taken
            girl_preferences = girl_prefs[girl]
            if girl_preferences.index(guy) < girl_preferences.index(other_guy):
                # Girl prefers guy over other_guy, so break them up
                print "[*] %s dumped %s for %s" % (girl, other_guy, guy)
                matches[girl] = guy

                # Ex needs to look for another partner
                free_guys.append(other_guy)
                break
        else:
            print "[*] Matched %s with %s" % (guy, girl)
            # Pair them up
            matches[girl] = guy
            break

guy_to_girl = dict([(v, k) for k, v in matches.iteritems()])

# Run the analysis with guys and girls swapped
free_girls = girls[:]
matches = {}
while free_girls:
    girl = free_girls.pop(0)
    preferences = girl_prefs[girl]
    for guy in preferences:
        other_girl = matches.get(guy)
        if other_girl:
            # Guy is taken
            guy_preferences = guy_prefs[guy]
            if guy_preferences.index(girl) < guy_preferences.index(other_girl):
                # Guy prefers girl over other_girl, so break them up
                print "[*] %s dumped %s for %s" % (guy, other_girl, girl)
                matches[guy] = girl

                # Ex needs to look for another partner
                free_girls.append(other_girl)
                break
        else:
            print "[*] Matched %s with %s" % (girl, guy)
            # Pair them up
            matches[guy] = girl
            break

guy_to_girl2 = matches
stable = {}
for x in matches:
    if guy_to_girl[x] == guy_to_girl2[x]:
        # Only keep matches that are the same between the two groupings
        stable[x] = guy_to_girl[x]

print "[*] Done matching"

string = "".join(["(%s,%s)" % (m,stable[m]) for m in sorted(stable)])
print hashlib.md5(string).hexdigest()

# 51cacb0258b7862d646964c0da7c6125
