
import matplotlib as mpl
mpl.use('Agg')
import pylab
import pandas as pd
import pymongo


def plot(x, y, z, filename):
    vmin = z.min()
    vmax = z.max()
    scale = 10
    cm = mpl.pyplot.cm.get_cmap('jet')
    fig, ax = mpl.pyplot.subplots()
    
    sc = ax.scatter(x, y, s=z*10, c=z, linewidth=0, alpha=0.5, vmin=vmin, vmax=vmax)
    ax.grid()
    ax.set_xlabel('field_x')
    ax.set_ylabel('field_y')
    fig.colorbar(sc)
    mpl.pyplot.savefig("%s" % filename)


if __name__ == '__main__':
    import sys
    
    p = sys.argv
    
    if len(p) < 6:
        print "usage: python %s <db_host> <db_port> <db_name> <coll_name> <time>" % p[0]
    
    coll = pymongo.Connection(p[1], int(p[2]))[p[3]][p[4]]
    df = pd.DataFrame(list(coll.find({"time": int(p[5])}))[0]['dist'])
    df.columns = ['x', 'y', 'z']
    plot(df['x'], df['y'], df['z'], "%s_%s.png" % (p[4], p[5]))

    

