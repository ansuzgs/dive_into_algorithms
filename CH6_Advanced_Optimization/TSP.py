import numpy as np
import math
import matplotlib.collections as mc
import matplotlib.pylab as pl

def gen_lines(cities, itinerary):
    lines = []
    for j in range(0, len(itinerary)-1):
        lines.append([cities[itinerary[j]], cities[itinerary[j+1]]])
    return lines

def howfar(lines):
    distance = 0
    for j in range(0, len(lines)):
        distance += math.sqrt( abs( lines[j][1][0] - lines[j][0][0] )**2 + abs( lines[j][1][1] - lines[j][0][1] )**2 )
    return distance

def plot_itinerary(cities, itinerary, plot_title, the_name):
    lc = mc.LineCollection(gen_lines(cities, itinerary), linewidth = 2)
    fig, ax = pl.subplots()
    ax.add_collection(lc) # type: ignore
    ax.autoscale()
    ax.margins(0.1)
    pl.scatter(x, y)
    pl.title(plot_title)
    pl.xlabel('X coordinate')
    pl.ylabel('Y cooddinate')
    pl.savefig(str(the_name)+'.png')
    pl.close()

def find_nearest(cities, idx, nnitinerary):
    point = cities[idx]
    min_distance = float('inf')
    min_idx = -1
    for j in range(0, len(cities)):
        distance = math.sqrt( (point[0] - cities[j][0])**2 + (point[1] - cities[j][1])**2 )
        if distance < min_distance and distance > 0 and j not in nnitinerary:
            min_distance = distance
            min_idx = j
    return min_idx

def donn(cities, N):
    nnitinerary = [0]
    for j in range(0, N-1):
        next = find_nearest(cities, nnitinerary[len(nnitinerary)-1], nnitinerary)
        nnitinerary.append(next)
    return nnitinerary

def perturb(cities, itinerary):
    neighborids1 = math.floor(np.random.rand() * (len(itinerary)))
    neighborids2 = math.floor(np.random.rand() * (len(itinerary)))

    itinerary2 = itinerary.copy()

    itinerary2[neighborids1] = itinerary[neighborids2]
    itinerary2[neighborids2] = itinerary[neighborids1]

    distance1 = howfar(gen_lines(cities, itinerary))
    distance2 = howfar(gen_lines(cities, itinerary2))

    if distance1 > distance2:
        return itinerary2.copy()
    else:
        return itinerary.copy()
    
def perturb_sa1(cities, itinerary, time):
    neighborids1 = math.floor(np.random.rand() * (len(itinerary)))
    neighborids2 = math.floor(np.random.rand() * (len(itinerary)))

    itinerary2 = itinerary.copy()

    itinerary2[neighborids1] = itinerary[neighborids2]
    itinerary2[neighborids2] = itinerary[neighborids1]

    distance1 = howfar(gen_lines(cities, itinerary))
    distance2 = howfar(gen_lines(cities, itinerary2))

    random_draw = np.random.rand()
    temperature = 1/((time/1000)+1)

    #if distance1 > distance2 or (distance2 > distance1 and random_draw < temperature):
    #    return itinerary2.copy()
    #else:
    #    return itinerary.copy()
    itinerary_to_return = itinerary.copy()
    if((distance2>distance1 and random_draw<temperature) or distance1>distance2):
        itinerary_to_return = itinerary2.copy()
    return itinerary_to_return.copy()

def perturb_sa2(cities, itinerary, time):
    neighborids1 = math.floor(np.random.rand() * (len(itinerary)))
    neighborids2 = math.floor(np.random.rand() * (len(itinerary)))

    itinerary2 = itinerary.copy()

    random_draw2 = np.random.rand()
    small = min(neighborids1, neighborids2)
    big = max(neighborids1, neighborids2)

    if(random_draw2 >= 0.55):
        itinerary2[small:big] = itinerary2[small:big][::-1]
    elif(random_draw2 < 0.45):
        tempitin = itinerary[small:big]
        del(itinerary2[small:big])
        neighborids3 = math.floor(np.random.rand()*len(itinerary))
        for j in range(0, len(tempitin)):
            itinerary2.insert(neighborids3 + j, tempitin[j])
    else:
        itinerary2[neighborids1] = itinerary[neighborids2]
        itinerary2[neighborids2] = itinerary[neighborids1]

    distance1 = howfar(gen_lines(cities, itinerary))
    distance2 = howfar(gen_lines(cities, itinerary2))

    random_draw = np.random.rand()
    temperature = 1/((time/1000)+1)

    itinerary_to_return = itinerary.copy()

    scale = 3.5
    if((distance2>distance1 and random_draw<math.exp(scale*abs(distance1-distance2))*temperature) or distance1>distance2):
        itinerary_to_return = itinerary2.copy()
    return itinerary_to_return.copy()

def perturb_sa3(cities, itinerary, time, maxitin):
    neighborids1 = math.floor(np.random.rand() * (len(itinerary)))
    neighborids2 = math.floor(np.random.rand() * (len(itinerary)))

    global mindistance
    global minitinerary
    global minidx

    itinerary2 = itinerary.copy()
    
    random_draw = np.random.rand()
    random_draw2 = np.random.rand()
    small = min(neighborids1, neighborids2)
    big = max(neighborids1, neighborids2)

    if(random_draw2 >= 0.55):
        itinerary2[small:big] = itinerary2[small:big][::-1]
    elif(random_draw2 < 0.45):
        tempitin = itinerary[small:big]
        del(itinerary2[small:big])
        neighborids3 = math.floor(np.random.rand()*len(itinerary))
        for j in range(0, len(tempitin)):
            itinerary2.insert(neighborids3 + j, tempitin[j])
    else:
        itinerary2[neighborids1] = itinerary[neighborids2]
        itinerary2[neighborids2] = itinerary[neighborids1]

    distance1 = howfar(gen_lines(cities, itinerary))
    distance2 = howfar(gen_lines(cities, itinerary2))

    temperature = 1/((time/1000)+1)

    itinerary_to_return = itinerary.copy()

    scale = 3.5
    if((distance2>distance1 and random_draw<math.exp(scale*abs(distance1-distance2))*temperature) or distance1>distance2):
        itinerary_to_return = itinerary2.copy()

    reset = True
    resetthresh = 0.04
    if(reset and (time-minidx) > (maxitin*resetthresh)):
        itinerary_to_return = minitinerary
        minidx = time
    
    if(howfar(gen_lines(cities, itinerary_to_return)) < mindistance):
        mindistance = howfar(gen_lines(cities, itinerary2))
        minitinerary = itinerary_to_return
        minidx = time

    if(abs(time-maxitin) <= 1):
        itinerary_to_return = minitinerary.copy()

    return itinerary_to_return.copy()


random_seed = 1729
np.random.seed(random_seed)

N = 40
x = np.random.rand(N)
y = np.random.rand(N)

points = zip(x,y)
cities = list(points)

itinerary = list(range(0,N))
nnitinerary = donn(cities, N)

itinerary_ps = itinerary.copy()
itinerary_sa1 = itinerary.copy()
itinerary_sa2 = itinerary.copy()
global mindistance
global minitinerary
global minidx
mindistance = howfar(gen_lines(cities, itinerary))
minitinerary = itinerary
minidx = 0
maxitin = len(itinerary)*50000
itinerary_sa3 = itinerary.copy()
for n in range(0, maxitin):
    itinerary_ps = perturb(cities, itinerary_ps)
    itinerary_sa1 = perturb_sa1(cities, itinerary_sa1, n)
    itinerary_sa2 = perturb_sa2(cities, itinerary_sa2, n)
    itinerary_sa3 = perturb_sa3(cities, itinerary_sa3, n, maxitin)


total_distance_random = howfar(gen_lines(cities, itinerary))
total_distance_NN = howfar(gen_lines(cities, nnitinerary))
total_distance_ps = howfar(gen_lines(cities, itinerary_ps))
total_distance_sa1 = howfar(gen_lines(cities, itinerary_sa1))
total_distance_sa2 = howfar(gen_lines(cities, itinerary_sa2))
total_distance_sa3 = howfar(gen_lines(cities, itinerary_sa3))
print(total_distance_random)
print(total_distance_NN)
print(total_distance_ps)
print(total_distance_sa1)
print(total_distance_sa2)
print(total_distance_sa3)

plot_itinerary(cities, itinerary, 'TSP - Random Itinerary', 'figure2')
plot_itinerary(cities, nnitinerary, 'TSP - Nearest Neighbor', 'figure3')
plot_itinerary(cities, itinerary_ps, 'TSP - Perturbe', 'figure4')
plot_itinerary(cities, itinerary_sa1, 'TSP - Perturbe Simulated Annealing 1', 'figure5')
plot_itinerary(cities, itinerary_sa2, 'TSP - Perturbe Simulated Annealing 2', 'figure6')
plot_itinerary(cities, itinerary_sa3, 'TSP - Perturbe Simulated Annealing 3', 'figure7')



