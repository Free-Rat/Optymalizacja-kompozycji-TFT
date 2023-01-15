import newfuncje

nc, nt, tr, tg, tb, vr, vg, vb = newfuncje.get_data(newfuncje.F_NAME)

# print(nc, nt, tr, tg, tb, vr, vg, vb)

newfuncje.draw_plot(nc, "czas", tr, tg, tb)

lbg = 0
lbr = 0
lgr = 0

print(len(vb), len(vg), len(vr))

for i in range(len(vb)):
    lbg += vb[i]/vg[i]
    lbr += vb[i]/vr[i]
    lgr += vg[i]/vr[i]

bg = lbg/len(vg)
br = lbr/len(vg)
gr = lgr/len(vg)

print("wynik bruteforca wzgledem greedy", bg)
print("wynik bruteforca wzgledem randomowego doboru", br)
print("wynik greedy wzgledem randomowego doboru", gr)
