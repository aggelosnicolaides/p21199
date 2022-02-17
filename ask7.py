
with open("lexiko.txt", 'r+') as f:
   f = f.read()
print(f)


proto = {
                "x":3,"y":4,"name":"bob"
            }
deftero = {
                  "x":13,"y":-4,"name":"malory"
              }
trito = {
                "x":-3,"y":104,"name":"trudy"
            }
tetarto = {
        "x":1,"y":14,"name":"alice"
    }
lexiko = {
    "proto" : proto ,
    "deftero" : deftero ,
    "trito" : trito ,
    "tetarto" : tetarto
}


print("")
print("Οι λέξεις κλειδιά είναι οι εξής :")
print(proto.keys())
print("")
print("Διαλέξτε ένα κλειδί :")
a = input()

if a in proto.keys() :
    timi1 = proto[a]

if a in deftero.keys() :
    timi2 = deftero[a]

if a in trito.keys() :
    timi3 = trito[a]

if a in tetarto.keys() :
    timi4 = tetarto[a]



if timi1 > timi2 and timi1 > timi3 and timi1 > timi4 :
    maxtimi = timi1
if timi2 > timi1 and timi2 > timi3 and timi2 > timi4 :
    maxtimi = timi2
if timi3 > timi1 and timi3 > timi2 and timi3 > timi4 :
    maxtimi = timi3
if timi4 > timi1 and timi4 > timi2 and timi4 > timi3:
    maxtimi = timi4

if timi1 < timi2 and timi1 < timi3 and timi1 < timi4:
    mintimi = timi1
if timi2 < timi1 and timi2 < timi3 and timi2 < timi4:
    mintimi = timi2
if timi3 < timi1 and timi3 < timi2 and timi3 < timi4:
    mintimi = timi3
if timi4 < timi1 and timi4 < timi2 and timi4 < timi3:
    mintimi = timi4

if a == "name" :
   if len(timi1) > len(timi2) and len(timi1) > len(timi3) and len(timi1) > len(timi4) :
       maxname = timi1
   if len(timi2) > len(timi1) and len(timi2) > len(timi3) and len(timi2) > len(timi4) :
       maxname = timi2
   if len(timi3) > len(timi1) and len(timi3) > len(timi2) and len(timi3) > len(timi4) :
       maxname = timi3
   if len(timi4) > len(timi1) and len(timi4) > len(timi2) and len(timi4) > len(timi3):
       maxname = timi4

   if len(timi1) < len(timi2) and len(timi1) < len(timi3) and len(timi1) < len(timi4):
       minname = timi1
   if len(timi2) < len(timi1) and len(timi2) < len(timi3) and len(timi2) < len(timi4):
       minname = timi2
   if len(timi3) < len(timi1) and len(timi3) < len(timi2) and len(timi3) < len(timi4):
       minname = timi3
   if len(timi4) < len(timi1) and len(timi4) < len(timi2) and len(timi4) < len(timi3):
       minname = timi4
   print("Το μεγαλήτερο σε έκταση όνομα είναι :")
   print(maxname)
   print("Το μικρότερο σε έκταση όνομα είναι :")
   print(minname)

if a != "name" :
   print("Η μικρότερη τιμή είναι :")
   print(mintimi)
   print("Η μεγαλήτερη τιμή είναι : ")
   print(maxtimi)









