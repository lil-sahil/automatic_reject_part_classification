import tkinter as tk
from tkinter import ttk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import datetime as dt
import os
from PIL import ImageTk,Image
import ctypes
import numpy.polynomial.polynomial as poly
import time

#Matplotlib style sheet
plt.style.use('ggplot')

directory = r'W:\BS_CFG2_En\Data'
# directory = r'C:\Users\sahil.nagpal\Desktop\Bushing Automatic Reject Handling\Data'

def resource_path(relative_path):
  try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS,
    # and places our data files in a folder relative to that temp
    # folder named as specified in the datas tuple in the spec file
    base_path = os.path.join(sys._MEIPASS, 'data')
  except Exception:
    # sys._MEIPASS is not defined, so use the original path
    base_path = r'C:\Users\sahil.nagpal\Desktop\Bushing Automatic Reject Handling\Reject_Handling\img'

  return os.path.join(base_path, relative_path)



def get_serial_number(string):
  full_serial_no = int(string.split('-')[-1])
  serial_no = int(string.split('-')[-1][2:])
  model = string.split('-')[0]+'-' + string.split('-')[1] +'-' + string.split('-')[2]
  return full_serial_no, serial_no, model.upper()



# Model Information - Zones and Servos__________________________________________________________________________________________________________________________________________________

s_1_p_1 = {'upper':[[119.68,7],[125.83,6.5],[131.97,6.25],[141.80,5],[149.17,8],[147.95,15],[151.62,22],[152.84,27],[156.54,36],[160.22,43],[162.67,47],[165.14,55],[168.82,63],[170.04,68],[171.29,75],[174.96,81],[177.41,86],[181.11,91]], 
            'lower':[[119.68,-3],[124.61,-1.4],[129.51,-1],[136.87,-2],[151.62,-2],[158.99,-1],[166.36,2.5],[171.29,3],[177.41,4],[182.34,4.5],[187.24,5],[190.93,6.5],[193.38,9]]}
s_1_p_2 = {'upper':[[120,11],[123.30,13],[124,19],[125.77,26.5],[129.45,34],[133.14,39],[136.81,46],[140.51,53],[144.19,57],[149.11,63],[154.01,67],[158.93,71],[162.61,75],[167.53,78],[169.98,82],[172.46,86],[174.90,90.5],[177.35,94.5],[179.80,97],[182.28,101]], 
            'lower':[[119.62,0],[123.30,-0.1],[127,3.5],[134.36,3.5],[140,3.5],[146.64,3.3],[154,3],[160.16,3.1],[167.53,3.8],[174.90,4],[181.05,4.3],[185.95,4.8],[191.08,5]]}

s_2_p_1 = {'upper':[[124.84,17],[131.44,19],[136.61,25],[141.51,31],[145.68,37],[149.85,45],[153.54,49.9],[157.72,56],[162.14,62],[166.32,66],[170.49,71.5],[173.44,77],[177.14,81.5],[179.59,85.1],[184.74,90]], 
            'lower':[[125.56,1],[131.19,0.1],[137.09,1],[144.71,2],[152.57,4],[159.44,4.9],[164.34,6],[175.41,6.5],[182.79,8],[188.69,9],[194.84,10.9]]}

s_3_p_1 = {'upper':[[240.21,44],[243.88,44],[246.36,44],[250.03,44.5],[254.93,44.9],[259.83,44.9],[263.53,45],[267.20,45.1],[272,50],[275.80,55],[279.50,59],[284.2,65],[288,70],[291.77,74],[295.47,77],[299.15,82],[302.84,85.5],[306.52,90],[310.22,94.5],[313.89,100]], 
            'lower':[[240.21,-6],[245.13,-6],[248.81,-5.5],[252.48,-4],[256.16,0.5],[259.83,1],[263.53,1],[268.43,0.2],[270.90,0.2],[274.58,0.2],[278.28,1],[283.17,4],[286.87,4.2],[290.55,4.5],[295.47,5],[299.15,7],[302.84,7.5],[307.74,10],[311.44,14],[313.89,17.5]]}
s_3_p_2 = {'upper':[[250.06,24],[253.73,28],[256.18,31],[259.88,36],[262.33,41.5],[266.03,46],[269.70,50],[273.40,54.5],[275.85,56.5],[279.52,61],[282,65],[285.67,70],[288.12,74],[291.82,78],[295.50,85],[299.20,90],[301.64,94],[304.09,97],[307.79,101],[311.47,103]], 
            'lower':[[250.06,-2],[253.73,-0.1],[256.18,-0.2],[258.65,-0.2],[262.33,0],[266.03,-0.01],[269.70,1],[273.40,0],[278.30,4.5],[282,5],[284.45,6.5],[288.12,9.5],[289.35,10.1],[293.05,12],[296.72,14],[301.64,16],[304.09,17],[307.79,18],[309.02,20],[312.69,21]]}
s_3_p_3 = {'upper':[[240.21,44],[243.88,44],[246.36,44],[250.03,44.5],[254.93,44.9],[259.83,44.9],[263.53,45],[267.20,45.1],[272,50],[275.80,55],[279.50,59],[284.2,65],[288,70],[291.77,74],[295.47,77],[299.15,82],[302.84,85.5],[306.52,90],[310.22,94.5],[313.89,100]], 
            'lower':[[240.21,-6],[245.13,-6],[248.81,-5.5],[252.48,-4],[256.16,0.5],[259.83,1],[263.53,1],[268.43,0.2],[270.90,0.2],[274.58,0.2],[278.28,1],[283.17,4],[286.87,4.2],[290.55,4.5],[295.47,5],[299.15,7],[302.84,7.5],[307.74,10],[311.44,14],[313.89,17.5]]}

s_4_p_1 = {'upper':[[250.07,5],[251.55,8.1],[256.45,12.3],[262.34,9.6],[265.30,6.2],[267.75,6.8],[268.97,7.1],[272.67,7.5],[277.57,8.1],[280.02,8.5],[283.72,8.9],[287.39,9.1],[289.87,9.15],[292.32,10.15],[294.77,11.5],[297.24,12.9],[300,13.9],[305.84,11.1],[310.74,14.8],[315.66,14]], 
            'lower':[[250.07,-1.5],[252.04,-0.5],[254.048,0.4],[257.43,-0.8],[262.34,-2],[266.52,-1.8],[268.97,-1.1],[272.67,-0.9],[276.35,-0.8],[281.27,-0.9],[284.94,-0.85],[288.64,-0.8],[292.32,-0.8],[295.99,-0.75],[300,-0.95],[304.61,-0.25],[307.06,1],[310.74,1.8],[313.21,2],[315.66,2.6]]}
s_4_p_2 = {'upper':[[249.91,5.8],[253.84,8.1],[260,6.9],[263.69,6],[268.59,5.95],[272.29,5.9],[275.97,5.95],[279.67,6],[283.34,6],[285.79,6.5],[289.49,7.05],[291.94,8.5],[295,9.1],[299.31,8],[301.76,7.8],[304.24,8],[306.68,8.7],[310.36,8.8],[311.61,9],[312.83,10.5]], 
            'lower':[[249.91,-1.8],[253.35,0.9],[257.55,-3.9],[261.22,-3],[267.37,-2.8],[272.29,-2.1],[274.74,-1.5],[280.89,-0.9],[284.56,-0.5],[287.04,-0.5],[290.71,-0.9],[294.39,-0.8],[296.86,-0.5],[300.54,-0.1],[304.24,0.4],[305.46,1.8],[309.13,2.15],[311.61,2.7],[314.06,2.8],[315.27,3.1]]}

s_5_p_1 = {'upper':[[240.28,45],[245.17,44.9],[248.87,45],[252.54,45],[254.99,45.1],[258.69,45],[262.36,45.1],[266.06,44.8],[270.96,45.2],[274.66,49],[278.33,52],[282.03,56],[285.70,57],[289.40,64.5],[293.08,70],[296.78,74],[299.23,77],[302.90,86],[306.60,95.1],[309.05,101]], 
            'lower':[[240.28,-5],[251.31,-5],[254.99,0],[259.91,1],[263.58,1.5],[268.51,2],[272.21,4],[277.11,4.1],[279.56,4.7],[283.25,4.95],[286.93,4.94],[290.63,5],[294.30,6],[298,6.2],[300.45,7],[304.12,8],[309.05,9.5],[312.68,10.5]]}
s_5_p_2 = {'upper':[[250.07,24],[252.55,26],[256.22,30.8],[258.67,35],[262.37,39],[264.82,44],[267.29,46.2],[270.97,51],[273.42,55.5],[277.11,62],[279.56,65],[282.01,67],[285.71,74],[288.16,76],[290.61,80.5],[294.31,85.2],[297.98,91],[300.46,95],[304.13,101],[307.83,103]], 
            'lower':[[250.07,-4],[252.55,-4.8],[256.22,-3],[258.67,-2],[261.14,0],[263.59,0],[267.29,0],[269.74,1],[273.42,3],[277.11,4],[279.56,5.4],[283.24,7.2],[286.94,9.8],[290.61,12],[293.09,14],[295.53,15.2],[297.98,17.5],[301.68,19],[305.36,20],[310.28,20]]}
s_5_p_3 = {'upper':[[240.28,45],[245.17,44.9],[248.87,45],[252.54,45],[254.99,45.1],[258.69,45],[262.36,45.1],[266.06,44.8],[270.96,45.2],[274.66,49],[278.33,52],[282.03,56],[285.70,57],[289.40,64.5],[293.08,70],[296.78,74],[299.23,77],[302.90,86],[306.60,95.1],[309.05,101]], 
            'lower':[[240.28,-5],[251.31,-5],[254.99,0],[259.91,1],[263.58,1.5],[268.51,2],[272.21,4],[277.11,4.1],[279.56,4.7],[283.25,4.95],[286.93,4.94],[290.63,5],[294.30,6],[298,6.2],[300.45,7],[304.12,8],[309.05,9.5],[312.68,10.5]]}

s_6_p_1 = {'upper':[[250.07,4.8],[251.54,8],[256.45,12.2],[262.34,9.8],[265.28,6.3],[267.75,6.8],[268.97,7.1],[272.64,7.5],[277.57,8.1],[281.27,8.9],[283.72,9],[287.39,9],[291.09,9.25],[293.54,10.5],[294.76,11.8],[297.21,13],[299.69,13.9],[305.81,11.1],[310.74,14.4],[315.66,14]], 
            'lower':[[250.07,-1.8],[252.04,-0.8],[254.48,0.2],[257.43,-0.85],[262.83,-2],[266.52,-1.8],[270.19,-1],[272.64,-0.9],[277.57,-0.85],[284.94,-0.8],[288.61,-0.75],[292.31,-0.7],[295.99,-0.5],[300.91,-1],[304.59,-0.2],[307.06,1],[310.74,1.9],[313.18,2],[315.66,2.8]]}
s_6_p_2 = {'upper':[[249.98,6.8],[252.92,9.8],[256.86,6.2],[261.26,6.7],[263.70,6.8],[266.15,7],[269.85,7.3],[273.53,7.2],[276,7.4],[279.67,7.8],[283.37,7.9],[287.05,8],[290.75,8.5],[293.20,9.9],[296.87,9.8],[300.57,9.5],[303.02,10],[306.69,11],[309.17,12],[312.84,10]], 
            'lower':[[249.98,-1.8],[251.95,1.5],[255.38,-1.6],[258.32,-1],[262.48,-1],[266.15,-0.8],[269.85,-1.8],[273.53,-0.7],[276,-0.7],[279.67,-1],[285.82,-0.5],[288.27,-0.4],[293.20,-0.2],[295.64,-0.1],[299.34,-0.2],[301.79,0.2],[304.24,1],[306.69,1.2],[309.17,2.1],[311.62,2.1]]}


#Spindle Threshold
  #threshold = {spindle:[Lower_limit,Upper_limit,zero_check_stroke, Zero_check_load]}
threshold = {1:[120,190,120,10],
              2:[125,190,125,15],
              3:[255,314,255,25],
              4:[250,314,250,6],
              5:[255,310,255,25],
              6:[250,315,250,6]}

part_information = {'B5C-5K067-A':[1,3,4,5,6],
                    'B5C-5K067-B':[1,2,3,4,5,6],
                    'B5C-5K067-C':[1,3,4,5,6],
                    'B5C-5K067-D':[1,3,4,5,6],
                    'C5C-5K067-A':[1,2,3,4,5,6],
                    'C5C-5K067-B':[1,2,3,4,5,6],
                    'C5C-5K067-C':[1,2,3,4,5,6]}

part_information_zones = {
                          'B5C-5K067-A': {'s_1_p_1':s_1_p_1, 's_3_p_1': s_3_p_1, 's_4_p_1': s_4_p_1, 's_5_p_1': s_5_p_1, 's_6_p_1':s_6_p_1},
                          'B5C-5K067-B': {'s_1_p_2':s_1_p_2, 's_2_p_1':s_2_p_1, 's_3_p_1':s_3_p_1, 's_4_p_1':s_4_p_1, 's_5_p_1':s_5_p_1, 's_6_p_1':s_6_p_1},
                          'B5C-5K067-C': {'s_1_p_1':s_1_p_1, 's_3_p_2': s_3_p_2, 's_4_p_1': s_4_p_1, 's_5_p_2': s_5_p_2, 's_6_p_1':s_6_p_1},
                          'B5C-5K067-D': {'s_1_p_1':s_1_p_1, 's_3_p_1': s_3_p_1, 's_4_p_1': s_4_p_1, 's_5_p_1': s_5_p_1, 's_6_p_1':s_6_p_1},
                          'C5C-5K067-A': {'s_1_p_2':s_1_p_2, 's_2_p_1':s_2_p_1, 's_3_p_1':s_3_p_1, 's_4_p_2':s_4_p_2, 's_5_p_1':s_5_p_1, 's_6_p_2':s_6_p_2},
                          'C5C-5K067-B': {'s_1_p_2':s_1_p_2, 's_2_p_1':s_2_p_1, 's_3_p_3':s_3_p_3, 's_4_p_1':s_4_p_1, 's_5_p_3':s_5_p_3, 's_6_p_1':s_6_p_1},
                          'C5C-5K067-C': {'s_1_p_2':s_1_p_2, 's_2_p_1':s_2_p_1, 's_3_p_3':s_3_p_3, 's_4_p_2':s_4_p_2, 's_5_p_3':s_5_p_3, 's_6_p_2':s_6_p_2}
}

#Verify that all required Servos are present and Judge is Good for the very last bushing pressed. Also need to verify that they have not been pushed in more than 2 times.

def check_all_spindles(serial, df_merge):
  rework_spindles = []
  bad_spindles = []
  good_spindles = []
  combine = []

  try:
    model = df_merge.loc[df_merge['Full_Serial_Number'] == serial, 'Model_Type_'].values[0]
  
  except IndexError:
    verdict_label.config(text='Part not found in SEARCH PERIOD specified.\n\nIncrease SEARCH PERIOD and try scanning again.\n\nOr place part on HOLD', background = '#ff8080', font=('Helvetica 14 bold'))
  
  for spindle in part_information[model]:

    #Check if the data exists for each spindle
    if spindle in list(df_merge.loc[df_merge['Full_Serial_Number']== serial, 'Spindle'].values):
      date = df_merge.loc[(df_merge['Full_Serial_Number']== serial) & (df_merge['Spindle']== spindle), "Date_Time"].sort_values(ascending = False).iloc[0]
      index = df_merge.loc[(df_merge['Full_Serial_Number']== serial) & (df_merge['Spindle']== spindle), :].sort_values(by = 'Date_Time', ascending = False)['Index'].iloc[0]

        
      # Servo present, servo does not occur more than twice, and the servo is 'OK'
      if df_merge.loc[(df_merge['Full_Serial_Number']== serial) & (df_merge['Spindle']== spindle), "Judge"].count() <= 2 and df_merge.loc[(df_merge['Full_Serial_Number']== serial) & (df_merge['Spindle']== spindle), ["Judge","Date_Time"]].sort_values(by='Date_Time', ascending = False ).iloc[0]['Judge'] =='OK':
          
          good_spindles.append({'Spindle': spindle, 'Date': date, 'Index':index})
      
      elif df_merge.loc[(df_merge['Full_Serial_Number']== serial) & (df_merge['Spindle']== spindle), "Judge"].count() == 1:
        
        if df_merge.loc[(df_merge['Full_Serial_Number']== serial) & (df_merge['Spindle']== spindle) & (df_merge['Judge']== 'Alarm'), 'Judge'].count()==1:
          good_counter = 0
          for i in list(df_merge.loc[(df_merge['Full_Serial_Number']== serial) & (df_merge['Spindle']== spindle), ['Date_Time','Index']].values):
            combine.append({'Spindle': spindle, 'Date': i[0], 'Index':i[1]})
          
          if combine_data(combine,model) == True:
            good_counter += 1
          else:
            good_counter = 0
          
          if good_counter >= 1:
            good_spindles += combine
            combine = []
          else:
            rework_spindles += combine
            combine = []
        
        else:
          rework_spindles.append({'Spindle': spindle, 'Date': date, 'Index':index})
     
      # Servo occurs more than once
      elif df_merge.loc[(df_merge['Full_Serial_Number']== serial) & (df_merge['Spindle']== spindle), "Judge"].count() > 1:

        date_list = list(df_merge.loc[(df_merge['Full_Serial_Number']== serial) & (df_merge['Spindle']== spindle), ['Index', 'Date_Time']].sort_values(by = 'Date_Time', ascending =True )['Index'].values)
        bad_counter = 0

        try:
          for i in range(len(date_list)):
            if abs(date_list[i] - date_list[i+1]) >  1:
              bad_counter += 1
              index_value = date_list[i+1]
        
        except IndexError:
          pass
        
        good = 0
        if bad_counter == 1:
          if df_merge.loc[(df_merge['Full_Serial_Number']== serial) & (df_merge['Spindle']== spindle), ["Judge","Date_Time"]].sort_values(by='Date_Time', ascending = False ).iloc[0]['Judge'] =='OK':
            good_spindles.append({'Spindle': spindle, 'Date': date, 'Index':index})

          
          elif 'OK' in list(df_merge.loc[(df_merge['Full_Serial_Number']== serial) & (df_merge['Spindle']== spindle), 'Judge'].values):
            try:
              for x in df_merge.loc[(df_merge['Full_Serial_Number']== serial) & (df_merge['Spindle']== spindle) & (df_merge['Index'] == index_value),'Judge'].values:
                if x == 'OK':
                  good += 1
                  break
                else:
                  index_value += 1
            except IndexError:
              pass

            if good == 0:
              for i in list(df_merge.loc[(df_merge['Full_Serial_Number']== serial) & (df_merge['Spindle']== spindle), ['Date_Time','Index']].values):
                bad_spindles.append({'Spindle': spindle, 'Date': i[0], 'Index':i[1]})
            elif good == 1:
              for i in list(df_merge.loc[(df_merge['Full_Serial_Number']== serial) & (df_merge['Spindle']== spindle), ['Date_Time','Index']].values):
                good_spindles.append({'Spindle': spindle, 'Date': i[0], 'Index':i[1]})
          
          else:
            good_counter = 0
            for i in list(df_merge.loc[(df_merge['Full_Serial_Number']== serial) & (df_merge['Spindle']== spindle), ['Date_Time','Index']].values):
              combine.append({'Spindle': spindle, 'Date': i[0], 'Index':i[1]})
            
            if combine_data(combine,model) == True:
              good_counter += 1
            else:
              good_counter = 0
            
            if good_counter >= 1:
              good_spindles += combine
              combine = []
            else:
              bad_spindles += combine
              combine = []

        elif bad_counter > 1:
          for i in list(df_merge.loc[(df_merge['Full_Serial_Number']== serial) & (df_merge['Spindle']== spindle), ['Date_Time','Index']].values):
            bad_spindles.append({'Spindle': spindle, 'Date': i[0], 'Index':i[1]})
          # bad_spindles.append({'Spindle': spindle, 'Date': date, 'Index':index})
        
        elif bad_counter == 0 and "OK" in list(df_merge.loc[(df_merge['Full_Serial_Number']== serial) & (df_merge['Spindle']== spindle), "Judge"]):
          for i in list(df_merge.loc[(df_merge['Full_Serial_Number']== serial) & (df_merge['Spindle']== spindle), ['Date_Time','Index']].values):
            good_spindles.append({'Spindle': spindle, 'Date': i[0], 'Index':i[1]})

        else:
          #Get all NG Spindles
          good_counter = 0
          for i in list(df_merge.loc[(df_merge['Full_Serial_Number']== serial) & (df_merge['Spindle']== spindle), ['Date_Time','Index']].values):
            combine.append({'Spindle': spindle, 'Date': i[0], 'Index':i[1]})
          
          if combine_data(combine,model) == True:
            good_counter += 1
          else:
            good_counter = 0
          
          if good_counter >= 1:
            good_spindles += combine
            combine = []
          else:
            rework_spindles += combine
            combine = []
      else:
        rework_spindles.append({'Spindle': spindle, 'Date': date, 'Index':index})
    
    else:
        rework_spindles.append({'Spindle': spindle})
        
  return rework_spindles, good_spindles, bad_spindles

#Combine data_________________________________________________________________________________________________________________________________________

def combine_data(data_dict,model):
  merge = []
  
  for i in data_dict:
    try:
      # path = r'W:\BS_CFG2_En\Data\{}-{}-{}'.format(i['Date'].month,i['Date'].day,i['Date'].year)
      path = r'{}\{}-{}-{}'.format(directory, i['Date'].month,i['Date'].day,i['Date'].year)
      os.chdir(path)
        
      for csv in os.listdir():
        try:
          if int(csv.split('_')[2])==i['Spindle'] and int(csv.split('_')[3]) == i['Index']:
            df = pd.read_csv('{}'.format(csv),header = 2)
            merge.append(df)
            break
        except FileNotFoundError:
          print('File Does Not Exit')
          return False
    except:
      print('File Does Not Exit')
      return False

  threshold_value = threshold[data_dict[0]['Spindle']]

  graph = pd.concat(merge).sort_values(by = 'Stroke')

  if (len(graph.loc[(graph['Stroke']<threshold_value[2]) & (graph['Load']>threshold_value[3]),:]) == 0) and (graph['Stroke'].max() >= threshold_value[1]):
    pass
  else:
    return False

  graph = graph[graph['Load']>0.5]
  
  x_values = graph['Stroke']
  y_values = graph['Load']

  #Creating a polynomial
  graph_best_fit = poly.polyfit(x_values,y_values,len(graph))

  for _ in part_information_zones[model].items():
    if int(_[0].split('_')[1]) == data_dict[0]['Spindle']:
      upper_zone = _[1]['upper']
      lower_zone = _[1]['lower']
      break
  
  for i in upper_zone:
    if i[0] >= threshold_value[0]: #and i[0] <= threshold_value[1]:
      #compare the polynomial to the zone
      graph_value = poly.polyval(i[0],graph_best_fit)
      if graph_value < i[1]:
        continue
      else:
        return False
  
  for i in lower_zone:
    if i[0] >= threshold_value[0]: #and i[0] <= threshold_value[1]:
      #compare the polynomial to the zone
      graph_value = poly.polyval(i[0],graph_best_fit)
      if graph_value > i[1]:
        continue
      else:
        print(graph_value, i[1], data_dict)
        return False

  return True

# Get Graph___________________________________________________________________________________________________________________________________________

def get_graphs(info_list):

  data_list = []

  for i in info_list:
    try:
      # path = r'W:\BS_CFG2_En\Data\{}-{}-{}'.format(i['Date'].month,i['Date'].day,i['Date'].year)
      path = r'{}\{}-{}-{}'.format(directory, i['Date'].month,i['Date'].day,i['Date'].year)
      os.chdir(path)
        
      for csv in os.listdir():
        try:
            if int(csv.split('_')[2])==i['Spindle'] and int(csv.split('_')[3]) == i['Index']:
                spindle_check = i['Spindle']
                data_list.append([path,spindle_check,csv])
                break
        except FileNotFoundError:
            ctypes.windll.user32.MessageBoxW(0, "Graph File Not Found!", "Graph File Location Error", 1)

    except:
        ctypes.windll.user32.MessageBoxW(0, "Graph File Not Found!", "Graph File Location Error", 1)
  
  plot_graph(data_list)


#Plotting the Graphs
def plot_graph(csv):
  check = False
  model = get_serial_number(search_bar.get())[2][1:12]

  spindle_list = [1,2,3,4,5,6]

  for i in spindle_list:
    fig = plt.figure()
    axes = fig.add_axes([0.1,0.1,0.8,0.8])
    

    #Displaying the upper and lower limits
    for _ in part_information_zones[model]:
      if int(_[2]) == i:
        zone_upper = part_information_zones[model][_]['upper']
        zone_lower = part_information_zones[model][_]['lower']
        break
    
    axes.plot([_[0] for _ in zone_upper], [_[1] for _ in zone_upper], 'r--', marker = 'o', markersize = 4)
    axes.plot([_[0] for _ in zone_lower], [_[1] for _ in zone_lower], 'r--', marker = 'o', markersize = 4)
  
    for y in csv:
      os.chdir(y[0])

      if i == y[1]:
        plot = pd.read_csv('{}'.format(y[2]), header = 2)
        check = True
        
        
        axes.plot(plot['Stroke'], plot['Load'], 'b')
        axes.set_xlabel('Stroke')
        axes.set_ylabel('Load')
        axes.set_title('Servo {}'.format(y[1]))
        fig.canvas.set_window_title('Servo {} - Force v.s Distance Graph'.format(y[1]))

    if check == True:
      plt.show()  
      check = False
    else:
      plt.close()
    
#Check Graph
# def check_graph(data_dict, model):

#   try:
#     # path = r'W:\BS_CFG2_En\Data\{}-{}-{}'.format(i['Date'].month,i['Date'].day,i['Date'].year)
#     path = r'{}\{}-{}-{}'.format(directory, data_dict['Date'].month,data_dict['Date'].day,data_dict['Date'].year)
#     os.chdir(path)

#     for csv in os.listdir():
#       try:
#         if int(csv.split('_')[2]) == data_dict['Spindle'] and int(csv.split('_')[3]) == data_dict['Index']:
#           graph = pd.read_csv('{}'.format(csv), header = 2)
#           threshold_value = threshold[data_dict['Spindle']]
          
#           x_values = graph[(graph['Stroke'] > threshold_value[0]) & (graph['Stroke'] < threshold_value[1])]['Stroke']
#           y_values = graph[(graph['Stroke'] > threshold_value[0]) & (graph['Stroke'] < threshold_value[1])]['Load']
          
#           #Creating a polynomial of degree 3
#           graph_best_fit = np.polyfit(x_values,y_values,3)

#           for _ in part_information_zones[model].items():
#             if int(_[0].split('_')[1]) == data_dict['Spindle']:
#               upper_zone = _[1]['upper']
#               lower_zone = _[1]['lower']
#               break
          
#           for i in upper_zone:
#             if i[0] >= threshold_value[0]:
#               #compare the polynomial to the zone
#               graph_value = graph_best_fit[0]*(i[0]**3) + graph_best_fit[1]*(i[0]**2) + graph_best_fit[2]*(i[0]) + graph_best_fit[3]
              
#               if graph_value < i[1]:
#                 continue
#               else:
#                 return False
          
#           for i in lower_zone:
#             if i[0] >= threshold_value[0]:
#               #compare the polynomial to the zone
#               graph_value = graph_best_fit[0]*(i[0]**3) + graph_best_fit[1]*(i[0]**2) + graph_best_fit[2]*(i[0]) + graph_best_fit[3]
#               if graph_value > i[1]:
#                 continue
#               else:
#                 return False
          
#           return True
#       except:
#         print('File not Found')
#         #Need to add pop-up
#         return False

#   except:
#     # Put a pop up here
#     print('File Does not exist')
#     return False

  


#CSV Log Data______________________________________________________________________________
def log_reject():
  log_file = pd.read_csv(resource_path('log.csv'))
  full_serial_no, serial_no, model = get_serial_number(search_bar.get())
  log_file.loc[len(log_file)] = [datetime.now().strftime('%Y-%h-%d_%H:%M:%S'),
                                  model.upper(),
                                  full_serial_no,
                                  'Rejected',
                                  comment_bar.get()]

  log_file.to_csv(resource_path('log.csv'),index = False)
  search_bar.delete(0,'end')
  comment_bar.delete(0,'end')
  verdict_label.config(text='', background = '#ffffff')
  search_bar.focus()



def log_rework():
  log_file = pd.read_csv(resource_path('log.csv'))
  full_serial_no, serial_no, model = get_serial_number(search_bar.get())
  log_file.loc[len(log_file)] = [datetime.now().strftime('%Y-%h-%d_%H:%M:%S'),
                                  model.upper(),
                                  full_serial_no,
                                  'Reworked',
                                  comment_bar.get()]
                                  
  log_file.to_csv(resource_path('log.csv'),index = False)
  search_bar.delete(0,'end')
  comment_bar.delete(0,'end')
  verdict_label.config(text='', background = '#ffffff')
  search_bar.focus()

def log_release():
  log_file = pd.read_csv(resource_path('log.csv'))
  full_serial_no, serial_no, model = get_serial_number(search_bar.get())
  log_file.loc[len(log_file)] = [datetime.now().strftime('%Y-%h-%d_%H:%M:%S'),
                                  model.upper(),
                                  full_serial_no,
                                  'Release',
                                  comment_bar.get()]
  
  log_file.to_csv(resource_path('log.csv'),index = False)
  search_bar.delete(0,'end')
  comment_bar.delete(0,'end')
  verdict_label.config(text='', background = '#ffffff')
  search_bar.focus()

#__________________________________________________________________________________________________________________________________________________________
def main(user_input):

  #Setting the directory for the Data.
  try:
    os.chdir(directory)
  except:
    ctypes.windll.user32.MessageBoxW(0, "Main Directory not Found!", "Main-Directory Error", 1)
  
  #If the correct number of characters are not found

  if len(user_input) != 23:
    return (verdict_label.config(text='Part contains incorrect number of characters.\nPlace part on HOLD or try scanning again.', background = '#ff8080', font=('Helvetica 14 bold')))


  try:
    #Create function to extract serial number
    full_serial_number, serial_number, model = get_serial_number(user_input)
  except ValueError:
    return (verdict_label.config(text='Part not found.\nPlace part on HOLD or try scanning again.', background = '#ff8080', font=('Helvetica 14 bold')))



  # Find the CSV files where the serial number is found

  df_merge = pd.DataFrame()
  list_of_relevant_dataframes = []
  list_of_relevant_csv_dates = []


  time_frame = int(time_frame_bar.get())

  if time_frame < 14:
    time_frame = 14

  # time_frame = int(5)

  list_of_days = []
  for i in range(time_frame+1):
    tdelta = dt.timedelta(days =i)
    day = "NUM_"+ (dt.datetime.today()-tdelta).strftime("%#m-%#d-%Y")+'.csv'
    list_of_days.append(day)
    list_of_days.append('NUM_red_rabbit.csv')

  for csv in os.listdir():
    if csv in list_of_days:
      csv_df = pd.read_csv(csv, encoding = 'ISO-8859-1')
      
      #If in the future the code breaks, delete the comparison after the | operator in the two statements below. "FutureWarning: elementwise comparison failed; returning scalar instead, but in the future will perform elementwise comparison result = method(y)"
      if csv_df[(csv_df['Serial_No'] == serial_number) | (csv_df['Serial_No'] == str(serial_number))].shape[0] >=1:
          list_of_relevant_csv_dates.append((csv.split('_')[1]).split('.')[0])
          csv_df = csv_df.loc[((csv_df['Serial_No'] == serial_number) | (csv_df['Serial_No'] == str(serial_number)))]
          list_of_relevant_dataframes.append(csv_df)

  if len(list_of_relevant_dataframes) == 0:
    return (verdict_label.config(text='Part not found in SEARCH PERIOD specified.\n\nIncrease SEARCH PERIOD and try scanning again.\n\nOr place part on HOLD', background = '#ff8080', font=('Helvetica 14 bold')))

  try:
    df_merge = pd.concat(list_of_relevant_dataframes)
  except ValueError:
    return (verdict_label.config(text='Part not found in SEARCH PERIOD specified.\n\nIncrease SEARCH PERIOD and try scanning again.\n\nOr place part on HOLD', background = '#ff8080', font=('Helvetica 14 bold')))

  # Dataframe cleaning

  df_merge['Full_Serial_Number'] = df_merge[['Model_Type', 'Serial_No']].apply(lambda x: int(str(x[0][-2:])+ str(x[1])), axis = 1)

  df_merge['Model_Type_'] = df_merge['Model_Type'].apply(lambda x: x[1:-4])

  df_merge['Date_Time'] = df_merge['Date'].apply(lambda x: datetime.strptime(x, '%m/%d/%Y %H:%M'))

  global rework_spindles
  global good_spindles
  global bad_spindles
  

  rework_spindles, good_spindles, bad_spindles = check_all_spindles(full_serial_number, df_merge)

  spindle_list_good = []
  spindle_list_rework = []
  spindle_list_scrap = []
  if len(rework_spindles) == 0 and len(bad_spindles) == 0:
    for i in good_spindles:
      spindle_list_good.append(i['Spindle'])

    verdict_label.config(text='JSN: {}\n\nPart is Good to release IF:\nNO DAMAGE on sleeves and\nbushings are sitting FLUSH\n\nGraph data is good for all Spindles: {}'.format(full_serial_number, set(spindle_list_good)), background = '#ccffdd', font=('Helvetica 14 bold'))
    # verdict_label.config(text=df_merge.loc[df_merge['Full_Serial_Number']== full_serial_number,['Full_Serial_Number','Spindle','Judge','Program']], background = '#ccffdd', font=('Helvetica 14 bold'))
      

  elif len(rework_spindles) != 0 and len(bad_spindles) == 0:
    for i in rework_spindles:
      spindle_list_rework.append(i['Spindle'])
    verdict_label.config(text='JSN: {}\nPart is able to be reworked\nRework the following Spindles: {}'.format(full_serial_number, set(spindle_list_rework)), background = '#cccc00', font=('Helvetica 14 bold'))

  
  else:
    for i in bad_spindles:
      spindle_list_scrap.append(i['Spindle'])
    verdict_label.config(text='JSN: {}\nHold Part for Engineer\nLook at the following spindles: {}'.format(full_serial_number, set(spindle_list_scrap)), background = '#ff8080', font=('Helvetica 14 bold'))


# main('mb5c-5k067-ad-102623270')


#Tkinter______________________________________________________________________________________________________________________________________________________________

HEIGHT = 900
WIDTH = 1100

root = tk.Tk()
root.title('CD6 Bushing - Part Examine')
root.iconbitmap(resource_path('icon.ico'))
# root.resizable(0,0)


canvas = tk.Canvas(
  root, 
  height=HEIGHT, 
  width= WIDTH)

canvas.pack()


frame = tk.Frame(
  root,
  bg = '#ffffff')

frame.place(
  relwidth = 1, 
  relheight = 1)

#Title Block and Title

title_block = tk.Frame(
  frame,
  height = 100,
  width = WIDTH)

title_block.pack()

# title_block.place(
#   relx=0.1, 
#   rely=0.05, 
#   relwidth = 0.8, 
#   relheight = 0.2)


title = tk.Label(
  title_block,
  text = 'CD6 BUSHING - Part Examine',
  bg = '#1a1a1a',
  fg = '#ffffff')

title.place(
  relwidth = 1, 
  relheight = 1)

title.config(font=('Helvetica 34 bold'))

#Search bar and Search button
scanner_img = ImageTk.PhotoImage(Image.open(resource_path('scanner.png')))
scanner_label = tk.Label(frame, 
  image=scanner_img,
  borderwidth = 0)

scanner_label.place(
  relx = 0.16,
  rely = 0.20
)


search_bar = ttk.Entry(
  frame
)


search_bar.place(
  relx = 0.2,
  rely = 0.2,
  relwidth=0.32,
  relheight = 0.05
)

search_button = ttk.Button(
  frame, 
  text='Search Part',
  command = lambda: main(search_bar.get())
  )


time_frame_label = tk.Label(
  frame,
  text = 'Search Period\n(Days)',
  bg = '#ffffff',
)

time_frame_label.place(
  relx = 0.54,
  rely = 0.201,
)

time_frame_label.config(font=('Helvetica 10 bold'))

time_frame_bar = ttk.Entry(
  frame
)

time_frame_bar.place(
  relx = 0.63,
  rely = 0.2,
  relwidth=0.05,
  relheight = 0.05
)
time_frame_bar.insert(tk.END,14)

search_button.place(
  relx = 0.7,
  rely = 0.2,
  relwidth=0.2,
  relheight = 0.05
)


#Servo Information

graph_title_img = ImageTk.PhotoImage(Image.open(resource_path('graph_title.png')))

servo_label = tk.Label(
  frame,
  text = 'Click to View\nForce vs Stroke Curves',
  bg = '#ffffff',
  image = graph_title_img,
  compound = tk.LEFT
)

servo_label.place(
  relx = 0.02,
  rely = 0.3,
  relheight = 0.1,
  relwidth = 0.3
)

servo_label.config(font=('Helvetica 10 bold'))

servo_info_block = tk.Frame(
  frame,
  bg = '#ffffff'
)

servo_info_block.place(
  relx=0.03, 
  rely=0.4, 
  relwidth = 0.3, 
  relheight = 0.25
)

good_spindles_Button = ttk.Button(
  servo_info_block,
  text = 'Good Spindles',
  # bg='#ccffdd',
  command = lambda: get_graphs(good_spindles)
)

good_spindles_Button.place(
  relx = 0.1,
  relwidth = 0.75, 
  relheight = 1/3
)

rework_spindles_Button = ttk.Button(
  servo_info_block,
  text = 'Rework Spindles',
  # bg = '#cccc00',
  command = lambda: get_graphs(rework_spindles)
)

rework_spindles_Button.place(
  relx = 0.1,
  rely = 1/3,
  relwidth = 0.75, 
  relheight = 1/3
)


bad_spindles_Button = ttk.Button(
  servo_info_block,
  text = 'Bad Spindles',
  # bg = '#ff8080',
  command = lambda: get_graphs(bad_spindles)
)

bad_spindles_Button.place(
  relx = 0.1,
  rely = 2/3,
  relwidth = 0.75, 
  relheight = 2/6,
)

# servo_4_Button = tk.Button(
#   servo_info_block,
#   text = 'Servo 4'
# )

# servo_4_Button.place(
#   rely = 3/6,
#   relwidth = 1, 
#   relheight = 1/6
# )

# servo_5_Button = tk.Button(
#   servo_info_block,
#   text = 'Servo 5'
# )

# servo_5_Button.place(
#   rely = 4/6,
#   relwidth = 1, 
#   relheight = 1/6
# )

# servo_6_Button = tk.Button(
#   servo_info_block,
#   text = 'Servo 6'
# )

# servo_6_Button.place(
#   rely = 5/6,
#   relwidth = 1, 
#   relheight = 1/6
# )

# Verdict

verdict_frame = tk.Frame(
  frame,
  bg = 'black'
)

verdict_frame.place(
  relx = 0.45,
  rely = 0.4,
  relheight = 0.3,
  relwidth = 0.5
)

verdict_label = tk.Label(
  verdict_frame,
  borderwidth=2
)
verdict_label.place(
  relx = 0.01,
  rely = 0.01,
  relheight = 0.98,
  relwidth = 0.98
)

#Decision Buttons
decision_frame = tk.Frame(
  frame,
  bg = 'white'
)

decision_frame.place(
  relx = 0.45,
  rely = 0.8,
  relheight = 0.15,
  relwidth = 0.5
)


def reject_on_enter(e):
  reject_button['background'] = '#ee3611'
  reject_button.config(font=('Helvetica 14 bold'))

def reject_on_leave(e):
  reject_button['background'] = '#f04625'
  reject_button.config(font=('Helvetica 12 bold'))

reject_img = ImageTk.PhotoImage(Image.open(resource_path('trashcan.png')))

reject_button = tk.Button(
  decision_frame,
  text = 'REJECT',
  bg = '#f04625',
  image = reject_img,
  compound = tk.BOTTOM,
  command = lambda: log_reject()
)

reject_button.place(
  rely = 0.05,
  relx = 0,
  relwidth = 1/3, 
  relheight = 0.9
)

reject_button.config(font=('Helvetica 12 bold'))
reject_button.bind('<Enter>',reject_on_enter)
reject_button.bind('<Leave>',reject_on_leave)



def rework_on_enter(e):
  rework_button['background'] = '#e6e600'
  rework_button.config(font=('Helvetica 14 bold'))

def rework_on_leave(e):
  rework_button['background'] = '#ffff00'
  rework_button.config(font=('Helvetica 12 bold'))

rework_img = ImageTk.PhotoImage(Image.open(resource_path('rework.png')))

rework_button = tk.Button(
  decision_frame,
  bg = '#ffff00',
  text = 'REWORK',
  image = rework_img,
  compound = tk.BOTTOM,
  command = lambda: log_rework()
)

rework_button.place(
  rely = 0.05,
  relx = 1/3,
  relwidth = 1/3, 
  relheight = 0.9
)

rework_button.config(font=('Helvetica 12 bold'))
rework_button.bind('<Enter>',rework_on_enter)
rework_button.bind('<Leave>',rework_on_leave)


def release_on_enter(e):
  release_button['background'] = '#89ae37'
  release_button.config(font=('Helvetica 14 bold'))

def release_on_leave(e):
  release_button['background'] = '#97c23d'
  release_button.config(font=('Helvetica 12 bold'))

release_img = ImageTk.PhotoImage(Image.open(resource_path('release.png')))

release_button = tk.Button(
  decision_frame,
  text = 'RELEASE',
  bg = '#97c23d',
  image = release_img,
  compound = tk.BOTTOM,
  command = lambda: log_release()
)

release_button.place(
  rely = 0.05,
  relx = 2/3,
  relwidth = 1/3, 
  relheight = 0.9
)

release_button.config(font=('Helvetica 12 bold'))
release_button.bind('<Enter>',release_on_enter)
release_button.bind('<Leave>',release_on_leave)


#Comment Box
comment_label = tk.Label(
  frame,
  text = 'Enter Comment\nif Neccasary:',
  bg = '#ffffff'
  # image = graph_title_img,
  # compound = tk.LEFT
)

comment_label.place(
  relx = 0.45,
  rely = 0.73
)

comment_label.config(font=('Helvetica 10 bold'))



comment_frame = tk.Frame(
  frame,
  bg = 'black'
)

comment_frame.place(
  relx = 0.55,
  rely = 0.73,
  relheight = 0.05,
  relwidth = 0.4
)

comment_bar = ttk.Entry(
  comment_frame
)


comment_bar.place(
  relwidth=1,
  relheight = 1
)

#Figure

figure_img = ImageTk.PhotoImage(Image.open(resource_path('full_figure.png')))

figure_label = tk.Label(
  frame,
  bg = 'white',
  image = figure_img,
  border = 0
)

figure_label.place(
  rely = 0.7,
  relx = 0.05
)

root.mainloop()