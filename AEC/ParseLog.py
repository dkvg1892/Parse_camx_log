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
    print("4 --> Luma vs Gain and Exposure time")
    print("5 --> Lux index vs Gain and Exposure time")


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

def ask_for_type_of_sensitivity():
    print "Which type of sensitivity do you want to display:\n 1. Short \n 2. Safe \n 3. Long \n 4. All of the above"

    sensitivity_type = input("Please select any one option : ")
    if sensitivity_type < 1 or sensitivity_type > 4:
        print "Invalid option selected"
        exit(-1)
    return sensitivity_type

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
def main():
    if len(sys.argv) != 2 :
        print("Please provide file name as an arguement")
        exit(-1)
    file_name = sys.argv[1]
    cid_avail, readhalaec, printframecontrol, mtrout = aec.parse_file(file_name)
    if len(readhalaec) == 0 or len(printframecontrol) == 0:
        print("Required logs are missing from file")
        exit(-1)
    dump_into_file(readhalaec,"readhalaec.csv", aec.get_empty_readhalaec_dict())
    dump_into_file(printframecontrol,"printframecontrol.csv",aec.get_empty_printframecontrol_dict())
    dump_into_file(mtrout,"mtrout.csv",aec.get_empty_mtrout_dict())
    while True:
        print_main_menu()
        choice = input("Select any one option: ")

        if choice > 5 or choice < 0 :
            print("Invalid option selected")
            exit(-1)
        cid_to_use= ask_for_cameraID(cid_avail)
        sensitivity_type_display = ask_for_type_of_sensitivity()
        if choice == 0:
            plot_graph_default(cid_to_use, sensitivity_type_display ,["G_Short","G_Safe","G_Long","ET_Safe","ET_Short","ET_Long"],printframecontrol)
        elif choice == 1:
            plot_graph_Option2(cid_to_use, sensitivity_type_display ,["AE_Compensation"],["G_Short","G_Safe","G_Long","ET_Safe","ET_Short","ET_Long","SI_Short","SI_Safe","SI_Long"], readhalaec,printframecontrol)
        elif choice == 2:
            plot_graph_Option(cid_to_use, sensitivity_type_display ,["AE_Metering_Mode"],["G_Short","G_Safe","G_Long","ET_Safe","ET_Short","ET_Long"],readhalaec,printframecontrol)
        elif choice == 3:
            plot_graph_Option(cid_to_use, sensitivity_type_display , ["AE_Antibanding_Mode"],["G_Short","G_Safe","G_Long","ET_Safe","ET_Short","ET_Long"],readhalaec,printframecontrol)
        elif choice == 4:
            plot_graph_Option(cid_to_use, sensitivity_type_display , ["Final_Luma","Short_target","Safe_target","Long_target"],["G_Short","G_Safe","G_Long","ET_Safe","ET_Short","ET_Long"],mtrout,printframecontrol)
        elif choice == 5:
            plot_graph_Option(cid_to_use, sensitivity_type_display , ["Lux_Index"],["G_Short","G_Safe","G_Long","ET_Safe","ET_Short","ET_Long"],mtrout,printframecontrol)
        else :
            print("Invalid option selected")
        run_again = input("Do you want to plot more graphs (YES: 1 or NO: 0): ")
        if run_again == 0:
            break


def show_graph_multi(cid_avail, s_type, plt, short,safe,longs,yaxis_name):
    import numpy as np
    i = 0
    length = 0
    color = ["green", "blue", "red", "black", "yellow"]
    linestyles = ['-','--', '-.', ':']
    j = 0
    for z in zip(short,safe,longs):
        j = 0
        if cid_avail[i] == 1:
            if s_type == 1 or s_type == 4:
                plt.plot(np.arange(len(z[0])),z[0], label="CID:"+str(i)+" Short",color=color[i],linestyle=linestyles[j])
                j = j+1
            if s_type == 2 or s_type == 4:
                plt.plot(np.arange(len(z[1])),z[1], label="CID:"+str(i)+" Safe",color=color[i],linestyle=linestyles[j])
                j = j+1
            if s_type == 3 or s_type == 4:
                plt.plot(np.arange(len(z[2])),z[2], label="CID:"+str(i)+" Long",color=color[i],linestyle=linestyles[j])
                j = j+1
            length = max(length,len(z[2]))
        i = i+1
        
    plt.xlabel("Request ID")
    #plt.xticks(np.arange(0,length,20))
    plt.ylabel(yaxis_name)
    plt.legend()
    #plt.plot(np.arange(len(z[0])),z[0], label="CID:"+str(i)+" Short",color=color[i],linestyle=linestyles[0], marker='o', markerfacecolor='blue', markersize=2)

def show_graph_single(cid_avail,plt, values ,yaxis_name, label_name):
    import numpy as np
    i=0
    length = 0
    color = ["green", "blue", "red", "black", "yellow"]
    linestyles = ['-','--', '-.', ':']
    for l in values:
        if cid_avail[i] == 1:
            plt.plot(np.arange(len(l)),l, label="CID:"+str(i)+" "+label_name, color=color[i],linestyle=linestyles[0])
            length = max(length,len(l))
        i=i+1
    plt.xlabel("Request ID")
    #plt.xticks(np.arange(0,length,20))
    plt.ylabel(yaxis_name)
    plt.legend()
    

def plot_graph_default(cid_avail, s_type, var,printframecontrol):
    import matplotlib.pyplot as plt
    print("Please wait, generating graph ... ")
    g_et = []
    for v in var:
        g_et.append(aec.get_data(printframecontrol,v))

    plt.figure("Default Graph")	
    
    ax1 = plt.subplot(211)
    show_graph_multi(cid_avail, s_type, plt,g_et[0],g_et[1],g_et[2], "Gain")

    ax2 = plt.subplot(212,)
    show_graph_multi(cid_avail, s_type, plt,g_et[3],g_et[4],g_et[5], "Exposure time")
    
    ax1.get_shared_x_axes().join(ax1, ax2)

    plt.legend()
   
    plt.show()

   
def plot_graph_Option(cid_avail, s_type, var1,var2, dict1,dict2):
    import matplotlib.pyplot as plt
    print("Please wait, generating graph ... ")
    r = []
    #print(dict1)
    for v in var1:
        r.append(aec.get_data(dict1,v))
    g_et = []
    for x in var2:
        g_et.append(aec.get_data(dict2,x))


            
    plt.figure(var1[0] + " Graph")	
    
    ax1 = plt.subplot(311)
    #show_graph_single(cid_avail,plt,r[0],var1[0],var1[0])
    if len(r) > 1 :
        show_graph_multi(cid_avail, s_type, plt,r[1],r[2],r[3], var1[0])
    show_graph_single(cid_avail,plt,r[0],var1[0],var1[0])
	
    ax2 = plt.subplot(312)
    show_graph_multi(cid_avail, s_type, plt,g_et[0],g_et[1],g_et[2], "Gain")
    
    ax3 = plt.subplot(313)
    show_graph_multi(cid_avail, s_type, plt,g_et[3],g_et[4],g_et[5], "Exposure time")
    ax1.get_shared_x_axes().join(ax1, ax2, ax3)
    plt.legend()
   
    plt.show()

def plot_graph_Option2(cid_avail, s_type, var1,var2,readhalaec,printframecontrol):
    import matplotlib.pyplot as plt
    print("Please wait, generating graph ... ")
    r = []
    for v in var1:
        r.append(aec.get_data(readhalaec,v))
    g_et = []
    for v in var2:
        g_et.append(aec.get_data(printframecontrol,v))



    plt.figure(var1[0] + " Graph")
    
    ax1 = plt.subplot(411)
    show_graph_single(cid_avail,plt,r[0],var1[0],var1[0])
	
	
    ax2 = plt.subplot(412)
    show_graph_multi(cid_avail, s_type, plt,g_et[0],g_et[1],g_et[2], "Gain")
    
    ax3 = plt.subplot(413)
    show_graph_multi(cid_avail, s_type, plt,g_et[3],g_et[4],g_et[5], "Exposure time")
    plt.legend()
	
    ax4 = plt.subplot(414)
    show_graph_multi(cid_avail, s_type, plt,g_et[6],g_et[7],g_et[8], "Sensitivity")
    ax1.get_shared_x_axes().join(ax1,ax2, ax3,ax4)
    plt.legend()
   
    plt.show()

if __name__ == "__main__":
    main()
    #pyinstaller --onefile ParseLog_Generic.py
    #https://stackoverflow.com/questions/7908636/possible-to-make-labels-appear-when-hovering-over-a-point-in-matplotlib
