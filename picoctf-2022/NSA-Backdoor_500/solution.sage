import binascii

p = 165904771154636133744258537155010957898841320976199637310247946276091086685264203988382040434355973963755682908150999129715814054881305005279715109357952947956732031939179558028421896612221813299929875548130332311862653487519381871784418328675201518221252865046296276946334529508065441554563296058286139050519
p_factors = [2, 36479, 35291, 48847, 60509, 41411, 34337, 63059, 51307, 35069, 36353, 44449, 38677, 48073, 47869, 39313, 43987, 41953, 60859, 36653, 53527, 39443, 36467, 58511, 61403, 50821, 62233, 46153, 43313, 32969, 33871, 61211, 60127, 50153, 55339, 39581, 56501, 65537, 35023, 33199, 37277, 57037, 59651, 38501, 34057, 61949, 53773, 53479, 44771, 43261, 60757, 59149, 44729, 36571, 42533, 59509, 48337, 43591, 47933, 53419, 34747, 58787, 39397, 48109, 55987, 36833, 46439]
q = 163014145749020966527362866473385169718851721616099580892964038460874458300229566597051127131837727765676578472743831728487190199884657664763105462749319055787715119759660870245251139666933894434217213010123667901776317139730147215838019956603683024166830240694839515087101545941555671169130305164821949513799
q_factors = [2, 101429, 70709, 101573, 130639, 86239, 70793, 79181, 110069, 95911, 91957, 70271, 128747, 129527, 37463, 80737, 88721, 79687, 74017, 99923, 125863, 76481, 96097, 75079, 94723, 86453, 100279, 94201, 40841, 69761, 86923, 98963, 72577, 66301, 71837, 89917, 71011, 92143, 86627, 125921, 90499, 101267, 129169, 122827, 127703, 71999, 106031, 72613, 77471, 127763, 122599, 93479, 119869, 131009, 71119, 113749, 124739, 86257, 96731, 120193, 122819, 119027, 124277]

y = 10230032503199327401627250197724560775036794598711422665723109931676519461895914673194564237493916409402558127512886358873803179536380707057619495689636200687781954441142174029241144881327227202661664191310764629981802657920761688261004112252169112426965031045536336715452675037702961365337153084172783532803944620209595563642571571582446196525253936276114792293498364692848661775627038690031115596892209486013286807489946833754362053483783351963874845312871919843366223439690687364781525787508405007854160604940091661277136966835886272138480439484770420207321578040718683150104120608394567288448245169695693978008067
n = p * q

g = 3
#
# # Pohlig-Hellman in (p-1)/2
# yp = y % p
# xp = 0
# xp_mod = 1
#
# for order in p_factors[1:]: # to remove the 2
#     # reduce the problem
#     new_problem = power_mod(yp, (p-1)//order, p)
#     # find a generator of that group
#     new_generator = power_mod(g, (p-1)//order, p)
#     # Pollard Rho
#     new_problem = GF(p)(new_problem)
#     new_generator = GF(p)(new_generator)
#     new_xp = discrete_log_rho(new_problem, new_generator, order)
#     #
#     xp = CRT(xp, new_xp, xp_mod, order)
#     xp_mod *= order
#
# # Pohlig-Hellman in (q-1)
# yq = y % q
# xq = 0
# xq_mod = 1
#
# for order in q_factors: # we need the 2
#     # reduce the problem
#     new_problem = power_mod(yq, (q-1)//order, q)
#     # find a generator of that grouq
#     new_generator = power_mod(g, (q-1)//order, q)
#     # Qollard Rho
#     new_problem = GF(q)(new_problem)
#     new_generator = GF(q)(new_generator)
#     new_xq = discrete_log_rho(new_problem, new_generator, order)
#     #
#     xq = CRT(xq, new_xq, xq_mod, order)
#     xq_mod *= order
#
# # CRT
# sol = CRT(xp, xq, xp_mod, xq_mod)
# print(sol)
# assert power_mod(3, sol, n) == y

FLAG = 6761206136364956042543115511656117287459997182370725750216519365964645492075597809265459735465904421593434798989163735237601079093143075290768252231659823854613212550367058280764704659736260884494123474393197674396671222781050516498237888800855673625678996522915484034617335407132225828890304685522445069598071661190832280329336245887071550221185686663967281711429527620799501680188766322697854887670032916650514365631738478632013325671631118969640902867453845697430120429970284509265267396263861041846682825227522174532072701528643702538640622049297405723899758929478966589868728439511498980556467237071877156366590
assert pow(3, FLAG, n) == y
print(binascii.unhexlify(hex(FLAG)[2:]))
print(FLAG)
# print(hex(FLAG))
