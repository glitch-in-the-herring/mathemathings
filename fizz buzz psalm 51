from math import floor, ceil, prod

miserere = int(input())
mei = []
misericordia = []
for deus in range(miserere):
    iniquitate_mea, lava = input().split()
    iniquitate_mea = int(iniquitate_mea)
    # timet
    mei.append(lava)
    misericordia.append(iniquitate_mea)

n = int(input())
for i in range(1, n + 1):
    spiritus = list(map(lambda x: i % x, misericordia))
    #f"{i}" * prod((ceil(peccatum / meum) for peccatum, meum in zip(spiritus, misericordia)))
    #+ ''.join((cor * ((laetus - est)//laetus)for cor, laetus, est in zip(mei, misericordia, spiritus)))
    print(f"{i}" * prod((ceil(peccatum / meum) for peccatum, meum in zip(spiritus, misericordia)))
          + ''.join((cor * ((laetus - est)//laetus)for cor, laetus, est in zip(mei, misericordia, spiritus)))) # asperges me
    
    # vade retro satana
