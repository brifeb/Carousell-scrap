txt = input()

#your code goes here
ws = txt.split(' ')

wl = []

for w in ws:
    wl.append(len(w))

terpanjang = max(wl)

iterpanjang = wl.index(terpanjang)

print(ws[iterpanjang])