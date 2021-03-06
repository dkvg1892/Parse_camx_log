#Author: Deepakkumar Gupta

import re
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
    (?P<CID>\d+)
    ,\s+\w+:
    (?P<AE_Compensation>(\-\d+)|(\d+))
    ,\s+\w+:
    (?P<AELock>(\-\d+)|(\d+))
    ,\s+\w+:
    (?P<AEMode>\d+)
    ,\s+\w+:
    (?P<AE_Metering_Mode>\d+)
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
    (?P<AE_Antibanding_Mode>\d+)
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
def get_reg_mtr_out():

    #05-14 12:35:57.848   856  1933 V CamX    : [ VERB][STATS_AEC] caeccore.cpp:1054: runMetering MtrOut:CID:2,Frame:10, Lux:366.856, Luma(Final:18.016, Avg:20.143, Mtr:18.016), (Short, Safe, Long)Targets(58, 58, 58) ExpIndex(385.9,385.9,385.9)
    #Working
    reg_mtr_out= r"""
    \d+-\d+\s+\d+:\d+:\d+\.\d+\s+\d+\s+\d+\s+V\s+CamX\s+:\s+
    \[\s+\w+\]
    \[\w+\]\s+caeccore\.cpp:\d+:\s+
    (?P<Function>runMetering)
    \s+\w+:\w+:
    (?P<CID>\d+)
    \,\w+:
    (?P<FID>\d+)
    \,\s+\w+:
    (?P<Lux_Index>\d+\.\d+)
    \,\s+\w+\(\w+:
    (?P<Final_Luma>\d+\.\d+)
    \,\s+\w+:
    (?P<Avg_Luma>\d+\.\d+)
    \,\s+\w+:
    (?P<Mtr_Luma>\d+\.\d+)
    \)\,\s+\(\w+\,\s+\w+\,\s+\w+\)\w+\(
    (?P<Short_target>\d+)
    \,\s+
    (?P<Safe_target>\d+)
    \,\s+
    (?P<Long_target>\d+)
    \)\s+\w+\(
    (?P<EI_Short>\d+\.\d+)
    \,
    (?P<EI_Safe>\d+\.\d+)
    \,
    (?P<EI_Long>\d+\.\d+)
    \)
    """
    # pattern = re.compile(reg_mtr_out, re.VERBOSE)
    # line = "05-14 12:35:57.848   856  1933 V CamX    : [ VERB][STATS_AEC] caeccore.cpp:1054: runMetering MtrOut:CID:2,Frame:10, Lux:366.856, Luma(Final:18.016, Avg:20.143, Mtr:18.016), (Short, Safe, Long) Targets(58, 58, 58) ExpIndex(385.9,385.9,385.9)"
    # print(pattern.search(line).groupdict())
    return reg_mtr_out

def get_reg_conv_out():

    #05-12 15:23:09.461   647  1815 V CamX    : [ VERB][STATS_AEC] caeccore.cpp:1095: runConvergence ConvOut:CID 1 Frame 45 Settle 1 BrightSettle 1, prevEV 0.0 (Short, Safe, Long) ExpIndex 320.0 320.0 320.0  Adjust 0.0 0.0 0.0 mode 1 lock 0
    #Working
    reg_conv_out= r"""
    \d+-\d+\s+\d+:\d+:\d+\.\d+\s+\d+\s+\d+\s+V\s+CamX\s+:\s+
    \[\s+\w+\]
    \[\w+\]\s+caeccore\.cpp:\d+:\s+
    (?P<Function>runConvergence)
    \s+\w+:\w+\s+
    (?P<CID>\d+)
    \s+\w+\s+
    (?P<FID>\d+)
    \s+\w+\s+
    (?P<Settle>\d+)
    """
    #pattern = re.compile(reg_conv_out, re.VERBOSE)
    #line = "05-12 15:23:09.461   647  1815 V CamX    : [ VERB][STATS_AEC] caeccore.cpp:1095: runConvergence ConvOut:CID 1 Frame 45 Settle 1 BrightSettle 1, prevEV 0.0 (Short, Safe, Long) ExpIndex 320.0 320.0 320.0  Adjust 0.0 0.0 0.0 mode 1 lock 0"
    #print(pattern.search(line).groupdict())
    return reg_conv_out

def get_empty_readhalaec_dict():
    dicts = {'AE_Compensation': '0', 'FPS_Range_min': '0', 'face_dy': '0', 'face_dx': '0', 'sensitivity': '0', 'FPS_Range_max': '0', 'captureIntent': '0', 'AFTrigger': '0', 'AELock': '0', 'AE_Antibanding_Mode': '0', 'Function': 'ReadHALAECParam', 'ISOExpTimePrioritySet': '0', 'ISOValue': '0', 'ZSLEnable': '0', 'AETrigger': '0', 'face_count': '0', 'controlSceneMode': '0', 'Gain': '0.000000', 'ISOorExposureTimePriorityValue': '0', 'exposureTime': '0', 'CID': '0', 'Touch_y': '0.000000', 'Touch_x': '0.000000', 'AE_Metering_Mode': '0', 'face_x': '0', 'ReqId': '0', 'videoHDRType': '0', 'controlMode': '0', 'face_y': '0', 'Touch_dx': '0.000000', 'Touch_dy': '0.000000', 'FrameDuration': '0', 'flashMode': '0', 'AEMode': '0', 'AEBracketMode': '0'}
    return dicts

def get_empty_printframecontrol_dict():
    dicts = {'CID': '0', 'Lux': '0', 'ET_Long': '0', 'exifISO': '0', 'LED2': '0', 'Function': 'printFrameControl', 'delta_Safe': '0.00', 'SI_Safe': '0', 'G_Short': '0.0', 'rg': '0.000', 'SensCorrF': '0.00', 'ET_Short': '0', 'G_Safe': '0.0', 'LED1': '0', 'bg': '0.000', 'Last': '0.00', 'ET_Safe': '0', 'G_Long': '0.0', 'FID': '0', 'SI_Short': '0', 'First': '0.00', 'Predictive_gain': '0.00', 'Influence': '0.00', 'State': 'Off', 'delta_Short': '0.00', 'delta_Long': '0.00', 'SI_Long': '0'}
    return dicts

def get_empty_mtrout_dict():
    dicts = {'Function': 'runMetering', 'Short_target': '0', 'Safe_target': '0', 'CID': '0', 'Lux_Index': '0.00', 'Long_target': '0', 'EI_Safe': '0.00', 'EI_Long': '0.00', 'Final_Luma': '0.00', 'Mtr_Luma': '0.00', 'FID': '0', 'Avg_Luma': '0.00', 'EI_Short': '0.00'}
    return dicts

def get_empty_convout_dict():
    dicts = {'Function': 'runConvergence', 'Settle': '0', 'FID': '0', 'CID': '0'}
    return dicts
def parse_file(file_name):
    #get_reg_mtr_out()
    #get_reg_conv_out()
    readhalaec = [get_empty_readhalaec_dict()]
    printframecontrol = [get_empty_printframecontrol_dict()]
    mtrout = [get_empty_mtrout_dict()]
    convout = [get_empty_convout_dict()]
    cid_avail = [0,0,0,0,0,0]  #assuming max six camera id available in log
    settled = [{0,0}]
    pattern_readhalaec = re.compile(get_reg_readhalaec(), re.VERBOSE)
    pattern_printframecontrol = re.compile(get_reg_print_frame(), re.VERBOSE)
    pattern_mtrout = re.compile(get_reg_mtr_out(), re.VERBOSE)
    pattern_convout = re.compile(get_reg_conv_out(), re.VERBOSE)
    next_line = 0
    with open(file_name) as infile:
        for line in infile:
            match1 = pattern_readhalaec.search(line)
            match2 = pattern_mtrout.search(line)
            match3 = pattern_printframecontrol.search(line)
            match4 = pattern_convout.search(line)
            if match1 is not None:
                dict = match1.groupdict()
                readhalaec.append(dict)
                cid_avail[int(dict["CID"])] = 1
                if next_line == 1:
                    printframecontrol.append(printframecontrol[-1])
                    mtrout.append(mtrout[-1])
                if next_line == 2:
                    printframecontrol.append(printframecontrol[-1])
                next_line = 1
            if match2 is not None:
                dict = match2.groupdict()
                mtrout.append(dict)
                if next_line == 0:
                    readhalaec.append(readhalaec[-1])
                if next_line == 2:
                    readhalaec.append(readhalaec[-1])
                    printframecontrol.append(printframecontrol[-1])
                next_line = 2
            if match3 is not None:
                dict = match3.groupdict()
                printframecontrol.append(dict)
                if next_line == 1:
                    mtrout.append(mtrout[-1])
                if next_line == 0:
                    readhalaec.append(readhalaec[-1])
                    mtrout.append(mtrout[-1])
                next_line = 0
            if match4 is not None:
                dict = match4.groupdict()
                convout.append(dict)
    #print(len(readhalaec),len(printframecontrol), len(mtrout))
    #print(mtrout)
    return cid_avail, readhalaec[1:], printframecontrol[1:], mtrout[1:]

def fill_empty_data(*argv):
    for arg in argv:
        for a in arg:
            if len(a) == 0:
                a.append(-1)
            else:
                a.append(a[-1])

def get_data(dictionary, var_name):
    var = [[],[],[],[],[],[]]
    for l in dictionary:
        #print(l)
        cid = int(l["CID"])
        fill_empty_data(var)
        val = l[var_name]
        if val.find('.') == -1:
            var[cid][-1] = int(l[var_name])
        else:
            var[cid][-1] = float(l[var_name])
    return var
    
