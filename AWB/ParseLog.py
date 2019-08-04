#Author: Deepakkumar Gupta


import sys
import awb_common as awb	

def print_main_menu():
    print("="*60)
    print(" "*20+"AWB LOG PARSING")
    print("="*60)

def dump_into_file(dict_data,csv_file,csv_columns):
    import csv
    #csv_columns = ['No','Name','Country']

    #csv_file = "Names.csv"
    try:
        with open(csv_file, 'wb') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            #writer.writrows(dict_data)
            for data in dict_data:
                writer.writerow(data)
    except IOError:
        print("I/O error")
def ask_for_cameraID(cid_avail):
    cid_to_display = input("Enter camera ID (Enter -1 to display graph for all available camera): ")
    cid_to_use = []
    if cid_to_display != -1 and (cid_to_display < 0 or cid_to_display > 5  or cid_avail[cid_to_display] == 0):
        print("Please select valid camera ID or logs not available for selected camera ID")
        exit(-1)

    if cid_to_display != -1:
        for i in range(len(cid_avail)):
            cid_to_use.append(0)
        cid_to_use[cid_to_display] = 1
    else:
        cid_to_use = cid_avail
    return cid_to_use

def main():
    if len(sys.argv) != 2 :
        print("Please provide file name as an arguement")
        exit(-1)
    file_name = sys.argv[1]
    cid_avail, publishcontrol = awb.parse_file(file_name)
    if len(publishcontrol) == 0:
        print("Required logs are missing from file")
        exit(-1)
    dump_into_file(publishcontrol,"publishcontrol.csv", awb.get_empty_PublishFrameControl_dict())

    while True:

        print_main_menu()
        cid_to_use= ask_for_cameraID(cid_avail)
        plot_graph_default(cid_to_use,["Gain_R","Gain_G","Gain_B","CCT"],publishcontrol)
        run_again = input("Do you want to plot more graphs (YES: 1 or NO: 0): ")
        if run_again == 0:
            break


def show_graph_multi(cid_avail,plt, short,safe,longs,yaxis_name):
    import numpy as np
    i = 0
    length = 0
    color = ["green", "blue", "red", "black", "yellow"]
    linestyles = ['-','--', '-.', ':']
    for z in zip(short,safe,longs):

        if cid_avail[i] == 1:
    
            plt.plot(np.arange(len(z[0])),z[0], label="CID:"+str(i)+" Red", color=color[i], linestyle=linestyles[0])
            plt.plot(np.arange(len(z[1])),z[1], label="CID:"+str(i)+" Green", color=color[i], linestyle=linestyles[1])
            plt.plot(np.arange(len(z[2])),z[2], label="CID:"+str(i)+" Blue", color=color[i], linestyle=linestyles[2])
            length = max(length,len(z[2]))
        i = i+1
        
    plt.xlabel("Request ID")
    #plt.xticks(np.arange(0,length,20))
    plt.ylabel(yaxis_name)
    plt.legend()

def show_graph_single(cid_avail,plt, values ,yaxis_name, label_name):
    import numpy as np
    i=0
    length = 0
    color = ["green", "blue", "red", "black", "yellow"]
    linestyles = ['-','--', '-.', ':']
    for l in values:
        if cid_avail[i] == 1:
            plt.plot(np.arange(len(l)),l, label="CID:"+str(i)+" "+label_name, color=color[i], linestyle=linestyles[0])
            length = max(length,len(l))
        i=i+1
    plt.xlabel("Request ID")
    #plt.xticks(np.arange(0,length,20))
    plt.ylabel(yaxis_name)
    plt.legend()
    
def onclick(event):
    #https://matplotlib.org/3.1.1/users/event_handling.html
    print '%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' % ('double' if event.dblclick else 'single', event.button, event.x, event.y, event.xdata, event.ydata)

def plot_graph_default(cid_avail,var,publishcontrol):
    import matplotlib.pyplot as plt
    g_et = []
    for v in var:
        g_et.append(awb.get_data(publishcontrol,v,1))
    print("Please wait, generating graph ... ")
    fig = plt.figure("Default Graph")
    
    ax1 = plt.subplot(211)
    #cid1 = fig.canvas.mpl_connect('button_press_event', onclick)
    show_graph_multi(cid_avail,plt,g_et[0],g_et[1],g_et[2], "RGB Gains")
    
    ax2 = plt.subplot(212)
    show_graph_single(cid_avail,plt,g_et[3], "CCT","CCT")
    plt.legend()
    ax1.get_shared_x_axes().join(ax1, ax2)
    plt.show()


if __name__ == "__main__":
    main()
    #pyinstaller --onefile ParseLog_Generic.py

