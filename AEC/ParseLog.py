#Author: Deepakkumar Gupta


import sys
import aec_common as aec	

def print_main_menu():
    print("="*60)
    print(" "*20+"AEC LOG PARSING")
    print("="*60)
    print("0 --> Default Gain and Exposure time")
    print("1 --> AE compensation vs Gain and Exposure time")
    print("2 --> AE Metering mode vs Gain and Exposure time")
    print("3 --> AE AntiBanding vs Gain and Exposure time")

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
    cid_avail, readhalaec, printframecontrol = aec.parse_file(file_name)
    if len(readhalaec) == 0 or len(printframecontrol) == 0:
        print("Required logs are missing from file")
        exit(-1)
    while True:
        print_main_menu()
        choice = input("Select any one option: ")

        if choice == 0:
            cid_to_use= ask_for_cameraID(cid_avail)
            plot_graph_default(cid_to_use,["G_Short","G_Safe","G_Long","ET_Safe","ET_Short","ET_Long"],printframecontrol)
        elif choice == 1:
            cid_to_use = ask_for_cameraID(cid_avail)
            plot_graph_Option2(cid_to_use,["AECompensation"],["G_Short","G_Safe","G_Long","ET_Safe","ET_Short","ET_Long","SI_Short","SI_Safe","SI_Long"], readhalaec,printframecontrol)
        elif choice == 2:
            cid_to_use = ask_for_cameraID(cid_avail)
            plot_graph_Option(cid_to_use,["AEMeteringMode"],["G_Short","G_Safe","G_Long","ET_Safe","ET_Short","ET_Long"],readhalaec,printframecontrol)
        elif choice == 3:
            cid_to_use = ask_for_cameraID(cid_avail)
            plot_graph_Option(cid_to_use, ["AEAntibandingModeValue"],["G_Short","G_Safe","G_Long","ET_Safe","ET_Short","ET_Long"],readhalaec,printframecontrol)
        else :
            print("Invalid option selected")
        run_again = input("Do you want to plot more graphs (YES: 1 or NO: 0): ")
        if run_again == 0:
            break


def show_graph_multi(cid_avail,plt, short,safe,longs,yaxis_name):
    import numpy as np
    i = 0
    length = 0
    for z in zip(short,safe,longs):

        if cid_avail[i] == 1:
            plt.plot(np.arange(len(z[0])),z[0], label="CID:"+str(i)+" Short")
            plt.plot(np.arange(len(z[1])),z[1], label="CID:"+str(i)+" Safe")
            plt.plot(np.arange(len(z[2])),z[2], label="CID:"+str(i)+" Long")
            length = max(length,len(z[2]))
        i = i+1
        
    plt.xlabel("Request ID")
    plt.xticks(np.arange(0,length,20))
    plt.ylabel(yaxis_name)
    plt.legend()

def show_graph_single(cid_avail,plt, values ,yaxis_name, label_name):
    import numpy as np
    i=0
    length = 0
    for l in values:
        if cid_avail[i] == 1:
            plt.plot(np.arange(len(l)),l, label="CID:"+str(i)+" "+label_name)
            length = max(length,len(l))
        i=i+1
    plt.xlabel("Request ID")
    plt.xticks(np.arange(0,length,20))
    plt.ylabel(yaxis_name)
    plt.legend()
    

def plot_graph_default(cid_avail,var,printframecontrol):
    import matplotlib.pyplot as plt
    g_et = []
    for v in var:
        g_et.append(aec.get_data(printframecontrol,v,1))
    print("Please wait, generating graph ... ")
    plt.figure("Default Graph")	
    
    plt.subplot(211)
    show_graph_multi(cid_avail,plt,g_et[0],g_et[1],g_et[2], "Gain")
    
    plt.subplot(212)
    show_graph_multi(cid_avail,plt,g_et[3],g_et[4],g_et[5], "Exposure time")
    plt.legend()
   
    plt.show()

   
def plot_graph_Option(cid_avail,var1,var2, readhalaec,printframecontrol):
    import matplotlib.pyplot as plt
    r = []
    for v in var1:
        r.append(aec.get_data(readhalaec,v,0))
    g_et = []
    for v in var2:
        g_et.append(aec.get_data(printframecontrol,v,1))

    print("Please wait, generating graph ... ")
            
    plt.figure(var1[0] + " Graph")	
    
    plt.subplot(311)
    show_graph_single(cid_avail,plt,r[0],var1[0],var1[0])
	
    plt.subplot(312)
    show_graph_multi(cid_avail,plt,g_et[0],g_et[1],g_et[2], "Gain")
    
    plt.subplot(313)
    show_graph_multi(cid_avail,plt,g_et[3],g_et[4],g_et[5], "Exposure time")
    plt.legend()
   
    plt.show()

def plot_graph_Option2(cid_avail,var1,var2,readhalaec,printframecontrol):
    import matplotlib.pyplot as plt
    r = []
    for v in var1:
        r.append(aec.get_data(readhalaec,v,0))
    g_et = []
    for v in var2:
        g_et.append(aec.get_data(printframecontrol,v,1))

    print("Please wait, generating graph ... ")
    
    plt.figure(var1[0] + " Graph")	
    
    plt.subplot(411)
    show_graph_single(cid_avail,plt,r[0],var1[0],var1[0])
	
	
    plt.subplot(412)
    show_graph_multi(cid_avail,plt,g_et[0],g_et[1],g_et[2], "Gain")
    
    plt.subplot(413)
    show_graph_multi(cid_avail,plt,g_et[3],g_et[4],g_et[5], "Exposure time")
    plt.legend()
	
    plt.subplot(414)
    show_graph_multi(cid_avail,plt,g_et[6],g_et[7],g_et[8], "Sensitivity")
    plt.legend()
   
    plt.show()

if __name__ == "__main__":
    main()
    #pyinstaller --onefile ParseLog_Generic.py

