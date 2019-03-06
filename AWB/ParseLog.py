import re
import sys
	
def get_reg_PublishFrameControl():
    #Working
    reg_PublishFrameControl = r"""
    \d+-\d+\s+\d+:\d+:\d+\.\d+\s+\d+\s+\d+\s+\w+\s+\w+\s+:\s+
    \[\s+\w+\]
    \[\w+\]\s+camxcawbioutil\.cpp:\d+\s+
    (?P<Function>PublishFrameControlToMainMetadata)
    \(\)\s+\w+\s+\w+\s+\w+\s+\w+:\s+
    (?P<ReqId>\d+)
    \s+\w+:
    (?P<camID>\d+)
    \s+\w+\(\w+:
    (?P<Gain_R>(\d+\.\d+)|([-]\d+\.\d+))
    ,\s+\w+:
    (?P<Gain_G>(\d+\.\d+)|([-]\d+\.\d+))
    ,\s+\w+:
    (?P<Gain_B>(\d+\.\d+)|([-]\d+\.\d+))    
    \)\s+\w+\(
    (?P<CCT>\d+)
    \),\s+\w+:\(\w+/\w+:
    (?P<R_G_Ratio>(\d+\.\d+)|([-]\d+\.\d+))    
    \s+\w+\/\w+:
    (?P<B_G_Ratio>(\d+\.\d+)|([-]\d+\.\d+))    
    \)\s+\w+:\s+
    (?P<FlashState>\d+)
    """
    #pattern = re.compile(reg_PublishFrameControl, re.VERBOSE)
    #line = "02-21 09:16:36.973   720  2503 I CamX    : [ INFO][STATS_AWB] camxcawbioutil.cpp:2311 PublishFrameControlToMainMetadata() Published PropertyIDAWBFrameControl for reqID: 1 camId:0 Gain(R:1.953914, G:1.000000, B:1.708272) CCT(4593), Decision_AfterTC:(R/G:0.511793 B/G:0.585387) FlashState: 0"
    #print(pattern.search(line))
    
    return reg_PublishFrameControl
	
def print_menu():
    print("="*60)
    print(" "*20+"AWB LOG PARSING")
    print("="*60)
    
def main():
    if len(sys.argv) != 2 :
        print("Please provide file name as an arguement")
        exit(-1)
    file_name = sys.argv[1]
    publishcontrol = parse_file(file_name)
    if len(publishcontrol) == 0:
        print("Required logs are missing from file")
        exit(-1)
    print_menu()
    choice = 0
    #choice = input("Select any one option: ")

    if choice == 0:
        plot_graph_default(publishcontrol)
    else :
        print("Invalid choice")

def parse_file(file_name):
    PublishFrameControl = []
    pattern_PublishFrameControl = re.compile(get_reg_PublishFrameControl(), re.VERBOSE)
    with open(file_name) as infile:
        for line in infile:
            match1 = pattern_PublishFrameControl.search(line)
            if match1 is not None:
                #print(line)
                dict = match1.groupdict()
                PublishFrameControl.append(dict)

    #print(PublishFrameControl)
    return PublishFrameControl

def show_graph_multi(plt, r,g,b,yaxis_name):
    import numpy as np
    plt.plot(np.arange(len(r)),r, label="Red",color="red")
    plt.plot(np.arange(len(g)),g, label="Green",color="green")
    plt.plot(np.arange(len(b)),b, label="Blue",color="blue")
    plt.xlabel("Request ID")
    plt.xticks(np.arange(0,len(b),20))
    plt.ylabel(yaxis_name)
    plt.legend()

def show_graph_single(plt, values ,yaxis_name, label_name):
    import numpy as np
    plt.plot(np.arange(len(values)),values, label=label_name)
    plt.xlabel("Request ID")
    plt.xticks(np.arange(0,len(values),20))
    plt.ylabel(yaxis_name)
    plt.legend()

def plot_graph_default(publichcontrol):
    import matplotlib.pyplot as plt
    
    r = []
    g = []
    b = []
    c = []
    
    for l in publichcontrol:
            r.append(float(l["Gain_R"]))
            g.append(float(l["Gain_G"]))
            b.append(float(l["Gain_B"]))
            c.append(int(l["CCT"]))
    
    plt.figure("Default Graph")	
    
    plt.subplot(211)
    show_graph_multi(plt,r,g,b, "RGB Gains")
    
    plt.subplot(212)
    show_graph_single(plt,c,"CCT","CCT")
    plt.legend()
   
    plt.show()

if __name__ == "__main__":
    main()
    #pyinstaller --onefile ParseLog_Generic.py

