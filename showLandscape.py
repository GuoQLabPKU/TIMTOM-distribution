import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import seaborn as sns




data_dir = 'D:/TIMTOM/'
rotted_vec = pd.read_csv(data_dir + 'rot001vector_coord.txt', sep = ",")
rotted_vec_filter = rotted_vec[ rotted_vec.z > -0.7   ]



def moveDensity(data, step = 3):
    sort_rotted = data.sort_values('x')
    topstep_add = data['density'].values[0:data.shape[0]-step]
    new_density = [ ]  
    new_density.extend(data['density'].values[data.shape[0]-step:])
    new_density.extend(topstep_add)
    data['density'] = new_density
    return data 
    
    
    
    

###function parts
def transform_range(val, prev_min, prev_max, new_min, new_max):
    # Transform a value from one range to another.
    return (((val - prev_min) * (new_max - new_min)) / (prev_max - prev_min)) + new_min


rotted_vec_filter_new = rotted_vec_filter


#make color 
import matplotlib.colors as mcolors
colors = ["grey", "lightgrey", "red"]
cmap = mcolors.LinearSegmentedColormap.from_list("custom_palette", colors)

color = [cmap(i/rotted_vec_filter_new.shape[0]) for i in range(rotted_vec_filter_new.shape[0])]
colorStore = [ ]
#color = sns.color_palette("vlag",n_colors=count)
for i in range(rotted_vec_filter_new.shape[0]):
    index = int(transform_range(rotted_vec_filter_new['density'].values[i], np.min(rotted_vec_filter_new['density'].values), 
                                np.max(rotted_vec_filter_new['density'].values), 0, rotted_vec_filter_new.shape[0])-1)
 
    colorStore.append([color[index][0],color[index][1],color[index][2]])
    
    
#remove noisy density color 
newcolorStore = [ ]
for i in range(rotted_vec_filter_new.shape[0]):
    singlecolor = colorStore[i]
    distance = np.sqrt( (rotted_vec_filter_new['x'].values[i] + 0.5)**2 + (rotted_vec_filter_new['y'].values[i] - 0)**2)
    if (distance > 1) & (singlecolor[0] > 0.9):
        newcolorStore.append([0.7,0.7,0.7])      
    else:
        newcolorStore.append(singlecolor)
        
    
    
    
    
#keep only a small fraction of data 
import random 
keep_idx =  random.sample(list(np.arange(0,rotted_vec_filter_new.shape[0],1 )), 10000)
x = rotted_vec_filter_new['x'].values[keep_idx]
y = rotted_vec_filter_new['y'].values[keep_idx]
colorss = [newcolorStore[i] for i in keep_idx]
fig,ax = plt.subplots(figsize = (5,5), dpi = 300) 
ax = plt.subplot(111)
ax.scatter(x, y,  c=colorss,s=0.5)
fig.savefig(data_dir + 'scatter.png',transparent = True)




