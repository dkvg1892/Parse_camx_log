#Author: Deepakkumar Gupta

import re
import sys
	
def get_reg_readhalaec():
    #Working
    reg_readhalaec = r"""
    \d+-\d+\s+\d+:\d+:\d+\.\d+\s+\d+\s+\d+\s+V\s+CamX\s+:\s+
    \[\s+\w+\]
    \[\w+\]\s+camxcaecstatsprocessor\.cpp:\d+\s+
    (?P<Function>ReadHALAECParam)
    \(\)\s+\w+:
    (?P<ReqId>\d+)
    ,\s+\w+:
    (?P<camID>\d+)
    ,\s+\w+:
    (?P<AECompensation>(\-\d+)|(\d+))
    ,\s+\w+:
    (?P<AELock>(\-\d+)|(\d+))
    ,\s+\w+:
    (?P<AEMode>\d+)
    ,\s+\w+:
    (?P<AEMeteringMode>\d+)
    ,\s+\w+:
    (?P<AETrigger>\d+)
    ,\s+\w+:
    (?P<AFTrigger>\d+)
    ,\s+\w+:
    (?P<captureIntent>\d+)
    ,\s+\w+:
    (?P<controlMode>\d+)
    ,\s+\w+:
    (?P<controlSceneMode>\d+)
    ,\s+\w+:
    (?P<flashMode>\d+)
    ,\s+\w+:
    (?P<exposureTime>\d+)
    ,\s+\w+:
    (?P<sensitivity>\d+)
    ,\s+\w+:
    (?P<AEAntibandingModeValue>\d+)
    ,\s+\w+:
    (?P<ISOExpTimePrioritySet>\d+)
    ,\s+\w+:
    (?P<ISOorExposureTimePriorityValue>\d+)
    ,\s+\w+:
    (?P<Gain>(\d+.\d+))
    \s+\w+:
    (?P<ISOValue>\d+)
    ,\s+\w+\s+\w+:\(\w+:
    (?P<FPS_Range_min>\d+)
    \s+\w+:
    (?P<FPS_Range_max>\d+)
    \),\s+\w+:
    (?P<AEBracketMode>\d+)
    ,\s+\w+:
    (?P<videoHDRType>\d+)
    ,\s+\w+\s+
    (?P<ZSLEnable>\d+)
    ,\s+\w+:
    (?P<FrameDuration>\d+)
    \s+\w+\s+\(\w+:
    (?P<face_count>\d+)
    \s+\w+:
    (?P<face_x>\d+)
    \s+\w+:
    (?P<face_y>\d+)
    \s+\w+:
    (?P<face_dx>\d+)
    \s+\w+:
    (?P<face_dy>\d+)
    \),\s+\w+\s+\(\w+:
    (?P<Touch_x>\d+\.\d+)
    \s+\w+:
    (?P<Touch_y>\d+\.\d+)
    \s+\w+:
    (?P<Touch_dx>\d+\.\d+)
    \s+\w+:
    (?P<Touch_dy>\d+\.\d+)
    #\),\s+\w+:\s+
    #(?P<controlPostRawSensitivityBoost>\d+)
    #\s+\w+:\s+
    #(?P<disableADRC>\d+)
    #,\s+\w+:\s+
    #(?P<DynamicConvergenceSpeed>\d+\.\d+)
    """
    #pattern = re.compile(reg_readhalaec, re.VERBOSE)
    #line = "02-21 09:17:16.114   729  2754 V CamX    : [ VERB][STATS_AEC] camxcaecstatsprocessor.cpp:2826 ReadHALAECParam() ReqId:1, camID:0, AECompensation:0, AELock:0, AEMode:2, AEMeteringMode:1, AETrigger:0, AFTrigger:0, captureIntent:1, controlMode:1, controlSceneMode:1, flashMode:1, exposureTime:39496, sensitivity:47, AEAntibandingModeValue:3, ISOExpTimePrioritySet:0, ISOorExposureTimePriorityValue:0, Gain:0.000000 ISOValue:0, FPS Range:(min:8 max:30), AEBracketMode:0, videoHDRType:0, ZSLEnable 0, FrameDuration:0 Face (Cnt:0 x:0 y:0 dx:0 dy:0), Touch (x:0.000000 y:0.000000 dx:0.000000 dy:0.000000), controlPostRawSensitivityBoost: 100 disableADRC: 0, DynamicConvergenceSpeed: 0.000000"
    #print(pattern.search(line).groupdict(), end=" ")
    
    return reg_readhalaec
	
def get_reg_print_frame():
	
    #02-23 07:18:00.429   729  2754 V CamX    : [ VERB][STATS_AEC] caeccore.cpp:1468: printFrameControl CID:0 FID:2 Mode:PerFrame State:Off Lux:240 exifISO:50 (Short, Safe, Long)  G(1.190 1.190 1.190) ET(10000000 10000000 10000000) SI (11902659 11902659 11902659) delta (0.00 0.00 0.00) SensCorrF:1.00 Influence:1.00 LED(1:0 2:0) Ratios(rg:-1.000 bg:-1.000) Entry(First:1.00 Last:0.00) predictive gain 1.00
    #Working
    reg_print_frame= r"""
    \d+-\d+\s+\d+:\d+:\d+\.\d+\s+\d+\s+\d+\s+V\s+CamX\s+:\s+
    \[\s+\w+\]
    \[\w+\]\s+caeccore\.cpp:\d+:\s+
    (?P<Function>printFrameControl)
    \s+\w+:
    (?P<CID>\d+)
    \s+\w+:
    (?P<FID>\d+)
    \s+\w+:PerFrame
    #(?P<Mode>\w+)
    \s+\w+:
    (?P<State>\w+)
    \s+\w+:
    (?P<Lux>\w+)
    \s+\w+:
    (?P<exifISO>\w+)
    \s+\(Short\,\s+Safe\,\s+Long\)\s+G\(
    (?P<G_Short>\d+\.\d+)
    \s+
    (?P<G_Safe>\d+\.\d+)
    \s+
    (?P<G_Long>\d+\.\d+)
    \)\s+ET\(
    (?P<ET_Short>\d+)
    \s+
    (?P<ET_Safe>\d+)
    \s+
    (?P<ET_Long>\d+)
    \)\s+SI\s+\(
    (?P<SI_Short>\d+)
    \s+
    (?P<SI_Safe>\d+)
    \s+
    (?P<SI_Long>\d+)
    \)\s+delta\s+\(
    (?P<delta_Short>(\d+\.\d+)|([-]\d+\.\d+))
    \s+
    (?P<delta_Safe>(\d+\.\d+)|([-]\d+\.\d+))
    \s+
    (?P<delta_Long>(\d+\.\d+)|([-]\d+\.\d+))
    \)\s+SensCorrF:
    (?P<SensCorrF>\d+\.\d+)
    \s+Influence:
    (?P<Influence>\d+\.\d+)
    \s+LED\(\d+:
    (?P<LED1>\d+)
    \s+\d+:
    (?P<LED2>\d+)
    \)\s+Ratios\(rg:
    (?P<rg>(-\d+\.\d+)|(\d+\.\d+))
    \s+bg:
    (?P<bg>(-\d+\.\d+)|(\d+\.\d+))
    \)\s+Entry\(First:
    (?P<First>(\d+\.\d+)|([-]\d+\.\d+))
    \s+Last:
    (?P<Last>(\d+\.\d+)|([-]\d+\.\d+))
    \)\s+predictive\s+gain\s+
    (?P<Predictive_gain>(\d+\.\d+)|([-]\d+\.\d+))
    """
    #pattern = re.compile(reg_print_frame, re.VERBOSE)
    #line = "02-18 13:50:57.659   651  1935 V CamX    : [ VERB][STATS_AEC] caeccore.cpp:1432: printFrameControl CID:0 FID:16 Mode:PerFrame State:Off Lux:321 exifISO:250 (Short, Safe, Long)  G(2.387 2.387 2.387) ET(10000000 10000000 10000000) SI (23873946 23873946 23873946) delta (-2.02 -2.02 -2.02) SensCorrF:1.00 Influence:1.00 LED(1:0 2:0) Ratios(rg:-1.000 bg:-1.000) Entry(First:1.00 Last:0.00) predictive gain 1.00"
	#line = "12-10 22:13:48.048   734  2063 V CamX    : [ VERB][STATS_AEC] caeccore.cpp:1412: printFrameControl CID:0 FID:1 Mode:PerFrame State:Off Lux:240 exifISO:64 (Short, Safe, Long)  G(1.428 1.428 1.428) ET(8333333 8333333 8333333) SI (11902660 11902660 11902660) delta (0.00 0.00 0.00) SensCorrF:1.00 Influence:1.00 LED(1:0 2:0) Ratios(rg:-1.000 bg:-1.000) Entry(First:1.00 Last:0.00) predictive gain 1.00
    #print(pattern.search(line).groupdict())
    
    return reg_print_frame
	
def print_menu():
    print("="*60)
    print(" "*20+"AEC LOG PARSING")
    print("="*60)
    print("0 --> Default Gain and Exposure time")
    print("1 --> AE compensation vs Gain and Exposure time")
    print("2 --> AE Metering mode vs Gain and Exposure time")
    print("3 --> AE AntiBanding vs Gain and Exposure time")
    
def main():
    if len(sys.argv) != 2 :
        print("Please provide file name as an arguement")
        exit(-1)
    file_name = sys.argv[1]
    readhalaec, printframecontrol = parse_file(file_name)
    if len(readhalaec) == 0 or len(printframecontrol) == 0:
        print("Required logs are missing from file")
        exit(-1)
    print_menu()
    choice = input("Select any one option: ")

    if choice == 0:
        plot_graph_default(readhalaec,printframecontrol)
    elif choice == 1:
        plot_graph_Option2(["AECompensation","SI_Short","SI_Safe","SI_Long"], readhalaec,printframecontrol)
    elif choice == 2:
        plot_graph_Option("AEMeteringMode",readhalaec,printframecontrol)
    elif choice == 3:
        plot_graph_Option("AEAntibandingModeValue",readhalaec,printframecontrol)
    else :
        print("Invalid option selected")

def parse_file(file_name):
    readhalaec = []
    printframecontrol = []
    pattern_readhalaec = re.compile(get_reg_readhalaec(), re.VERBOSE)
    pattern_printframecontrol = re.compile(get_reg_print_frame(), re.VERBOSE)
    with open(file_name) as infile:
        for line in infile:
            #print(line)
            match1 = pattern_readhalaec.search(line)
            match2 = pattern_printframecontrol.search(line)
            if match1 is not None:
                dict = match1.groupdict()
                readhalaec.append(dict)
            if match2 is not None:
                dict = match2.groupdict()
                #print(dict)
                #print(line)
                printframecontrol.append(dict)

    #print(readhalaec)
    #print(printframecontrol)
	#print(len(readhalaec),len(printframecontrol))
    return readhalaec, printframecontrol

def show_graph_multi(plt, short,safe,long,yaxis_name):
    import numpy as np
    plt.plot(np.arange(len(short)),safe, label="Short")
    plt.plot(np.arange(len(safe)),safe, label="Safe")
    plt.plot(np.arange(len(long)),long, label="Long")
    plt.xlabel("Request ID")
    plt.xticks(np.arange(0,len(long),20))
    plt.ylabel(yaxis_name)
    plt.legend()

def show_graph_single(plt, values ,yaxis_name, label_name):
    import numpy as np
    plt.plot(np.arange(len(values)),values, label=label_name)
    plt.xlabel("Request ID")
    plt.xticks(np.arange(0,len(values),20))
    plt.ylabel(yaxis_name)
    plt.legend()

def plot_graph_default(readhalaec,printframecontrol):
    import matplotlib.pyplot as plt
    
    g_short = []
    g_safe = []
    g_long = []
    
    et_short = []
    et_safe = []
    et_long = []
    
    for l in printframecontrol:
            g_safe.append(float(l["G_Safe"]))
            g_short.append(float(l["G_Short"]))
            g_long.append(float(l["G_Long"]))
            et_safe.append(int(l["ET_Safe"]))
            et_short.append(int(l["ET_Short"]))
            et_long.append(int(l["ET_Long"]))
    
    plt.figure("Default Graph")	
    
    plt.subplot(211)
    show_graph_multi(plt,g_short,g_safe,g_long, "Gain")
    
    plt.subplot(212)
    show_graph_multi(plt,et_short,et_safe,et_long, "Exposure time")
    plt.legend()
   
    plt.show()

def plot_graph_Option(str, readhalaec,printframecontrol):
    import matplotlib.pyplot as plt
    
    values = []
    g_short = []
    g_safe = []
    g_long = []
    
    et_short = []
    et_safe = []
    et_long = []
    
    for l in readhalaec:
        values.append(float(l[str]))
	
    for l in printframecontrol:
        g_safe.append(float(l["G_Safe"]))
        g_short.append(float(l["G_Short"]))
        g_long.append(float(l["G_Long"]))
        et_safe.append(int(l["ET_Safe"]))
        et_short.append(int(l["ET_Short"]))
        et_long.append(int(l["ET_Long"]))
    
    plt.figure("AE Compensation Graph")	
    
    plt.subplot(311)
    show_graph_single(plt,values,str,str)
	
	
    plt.subplot(312)
    show_graph_multi(plt,g_short,g_safe,g_long, "Gain")
    
    plt.subplot(313)
    show_graph_multi(plt,et_short,et_safe,et_long, "Exposure time")
    plt.legend()
   
    plt.show()

def plot_graph_Option2(str, readhalaec,printframecontrol):
    import matplotlib.pyplot as plt
    
    values = []
    g_short = []
    g_safe = []
    g_long = []
    
    et_short = []
    et_safe = []
    et_long = []
	
    si_short = []
    si_safe = []
    si_long = []
    
    for l in readhalaec:
        values.append(float(l[str[0]]))
	
    for l in printframecontrol:
        g_safe.append(float(l["G_Safe"]))
        g_short.append(float(l["G_Short"]))
        g_long.append(float(l["G_Long"]))
        et_safe.append(int(l["ET_Safe"]))
        et_short.append(int(l["ET_Short"]))
        et_long.append(int(l["ET_Long"]))
        si_short.append(int(l[str[2]]))
        si_safe.append(int(l[str[1]]))
        si_long.append(int(l[str[3]]))
    
    plt.figure("AE Compensation Graph")	
    
    plt.subplot(411)
    show_graph_single(plt,values,str[0],str[0])
	
	
    plt.subplot(412)
    show_graph_multi(plt,g_short,g_safe,g_long, "Gain")
    
    plt.subplot(413)
    show_graph_multi(plt,et_short,et_safe,et_long, "Exposure time")
    plt.legend()
	
    plt.subplot(414)
    show_graph_multi(plt,si_short,si_safe,si_long, "Sensitivity")
    plt.legend()
   
    plt.show()

if __name__ == "__main__":
    main()
    #pyinstaller --onefile ParseLog_Generic.py

