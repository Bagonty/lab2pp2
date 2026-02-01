#Python Sets
myset = {"abag", "baga", "gaba"}
print(myset)
yourset = {1, 2, 3, 4, 5}
print(yourset)
himset = {True, False, True}
print(himset)
herset = {3.14, 2.71, 1.61}
print(herset)
itset = {"baga", 42, True, 3.14}
print(itset)
#Access Items
for x in myset:
    print(x)
for x in yourset:
    print(x)
for x in himset:
    print(x)
for x in herset:
    print(x)
for x in itset:
    print(x)
print("baga" in myset)
print(3 in yourset)
#Python - Add Set Items
myset.add("new_item")
yourset.add(6)
himset.add(False)
herset.add(0.577)
itset.add("end")
print(myset)
print(yourset)
print(himset)
print(herset)
print(itset)
#Python - Add Set Items
myset.remove("abag")
yourset.remove(2)
himset.discard(True)
del herset
itset.clear()
print(myset)
print(yourset)
print(himset)
print(itset)
#Python - Loop Sets
for item in myset:
    print(item)
for item in yourset:
    print(item)
for item in himset:
    print(item)
for item in itset:
    print(item)
#Python - Join Sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
set4 = {"x", "y", "z"}
set5 = {4, 5, 6}
set6 = set4.union(set5)
set7 = set1 | set4
print(set6)
print(set7)
set1.update(set2)
print(set1)
#Python frozenset
fset = frozenset({"eee", "nanana", "ryry"})
print(fset)
print(type(fset))
rset = frozenset({10, 20, 30, 40})
print(rset)
print(type(rset))
pset = frozenset({True, False, True})
print(pset)
print(type(pset))
tset = frozenset({3.14, 2.71, 1.61})
print(tset)
print(type(tset))
uset = frozenset({"baga", 42, True, 3.14})
print(uset)
print(type(uset))
#Python - Set Methods
print(dir(myset))
print(dir(fset))
print(len(yourset))
print(len(rset))
print(type(himset))
print(type(pset))
print(type(tset))
print(type(itset))
print(type(uset))
print(max(yourset))
print(max(rset))
print(min(yourset))
print(min(rset))
print(sum(yourset))
print(sum(rset))
print(sorted(myset))
print(sorted(fset))
print(sorted(yourset))
print(sorted(rset))
print(myset.intersection(yourset))