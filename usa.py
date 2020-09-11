from random import choice

# states graph from https://www-cs-faculty.stanford.edu/~knuth/contiguous-usa.dat
states = """AL FL
AL GA
AL MS
AL TN
AR LA
AR MO
AR MS
AR OK
AR TN
AR TX
AZ CA
AZ NM
AZ NV
AZ UT
CA NV
CA OR
CO KS
CO NE
CO NM
CO OK
CO UT
CO WY
CT MA
CT NY
CT RI
DC MD
DC VA
DE MD
DE NJ
DE PA
FL GA
GA NC
GA SC
GA TN
IA IL
IA MN
IA MO
IA NE
IA SD
IA WI
ID MT
ID NV
ID OR
ID UT
ID WA
ID WY
IL IN
IL KY
IL MO
IL WI
IN KY
IN MI
IN OH
KS MO
KS NE
KS OK
KY MO
KY OH
KY TN
KY VA
KY WV
LA MS
LA TX
MA NH
MA NY
MA RI
MA VT
MD PA
MD VA
MD WV
ME NH
MI OH
MI WI
MN ND
MN SD
MN WI
MO NE
MO OK
MO TN
MS TN
MT ND
MT SD
MT WY
NC SC
NC TN
NC VA
ND SD
NE SD
NE WY
NH VT
NJ NY
NJ PA
NM OK
NM TX
NV OR
NV UT
NY PA
NY VT
OH PA
OH WV
OK TX
OR WA
PA WV
SD WY
TN VA
UT WY
VA WV"""
states = states.split("\n")

# all of the edges need to go both ways. Also, who cares about DC?!
temp1 = [ (i,j) for i, j in [s.split(" ") for s in states ] if i != 'DC' and j != 'DC']
temp2 = [ (j,i) for i, j in [s.split(" ") for s in states ] if i != 'DC' and j != 'DC']
states = temp1 + temp2

mean = lambda a: sum(a) / len(a)

def newStateDict(states, val=0):
	out = {}
	for (i,j) in states:
		out[i] = val
	return out
	
def randomNextState(states, current):
	poss = [s for s in states if s[0] == current]
	return choice(poss)[1]

def transit(states):
	visits = newStateDict(states)
	current = "ME"
	while min(visits.values()) == 0:
		visits[current] += 1
		current = randomNextState(states, current)
	return visits

s = newStateDict(states)
for i in s:
	s[i] = []

N = 10000
tot = 0
for i in range(N):
	v = transit(states)
	tot += sum(v.values())
	for i in v:
		s[i] += [v[i]]

print ("Number of steps: " + str(tot/N))
for i in s:
	print (i, mean(s[i]))
