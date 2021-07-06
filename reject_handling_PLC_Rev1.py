import pandas as pd
import numpy as np
from datetime import datetime
import datetime as dt
import os
import numpy.polynomial.polynomial as poly
from pycomm3 import LogixDriver



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


# PLC _ Bit Information

  #read_tag = 'PART_TRACKING[9]'
  #write_tag = 'test_tag'

def read_tag(tag_name = 'PART_TRACKING[9]'):
  with LogixDriver('192.100.3.206/0') as plc:
    return plc.read('{}'.format(tag_name))
  
def write_tag(value, tag_name ='test_tag'):
  with LogixDriver('192.100.3.206/0') as plc:
    return plc.write(('{}'.format(tag_name),'{}'.format(value)))

GOOD = 1
BAD = 0


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
              3:[255.47,314,255,25],
              4:[250,316,250,6],
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

  model = df_merge.loc[df_merge['Full_Serial_Number'] == serial, 'Model_Type_'].values[0]
  
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
     
      # Servo occurs more than twice
      elif df_merge.loc[(df_merge['Full_Serial_Number']== serial) & (df_merge['Spindle']== spindle), "Judge"].count() > 1:

        date_list = list(df_merge.loc[(df_merge['Full_Serial_Number']== serial) & (df_merge['Spindle']== spindle), ['Index', 'Date_Time']].sort_values(by = 'Date_Time', ascending =True )['Index'].values)
        bad_counter = 0

        try:
          for i in range(len(date_list)):
            if abs(date_list[i] - date_list[i+1]) >  1:
              bad_counter += 1
        
        except IndexError:
          pass

        if bad_counter == 1:
          if df_merge.loc[(df_merge['Full_Serial_Number']== serial) & (df_merge['Spindle']== spindle), ["Judge","Date_Time"]].sort_values(by='Date_Time', ascending = False ).iloc[0]['Judge'] =='OK':
            good_spindles.append({'Spindle': spindle, 'Date': date, 'Index':index})
          
          else:
            for i in list(df_merge.loc[(df_merge['Full_Serial_Number']== serial) & (df_merge['Spindle']== spindle), ['Date_Time','Index']].values):
              bad_spindles.append({'Spindle': spindle, 'Date': i[0], 'Index':i[1]})

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

  graph = graph[graph['Load']>0.3]
  
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
    if i[0] >= threshold_value[0]:
      #compare the polynomial to the zone
      graph_value = poly.polyval(i[0],graph_best_fit)
      if graph_value < i[1]:
        continue
      else:
        return False
  
  for i in lower_zone:
    if i[0] >= threshold_value[0]:
      #compare the polynomial to the zone
      graph_value = poly.polyval(i[0],graph_best_fit)
      if graph_value > i[1]:
        continue
      else:
        print(graph_value, i[1], data_dict)
        return False
  
  return True

#__________________________________________________________________________________________________________________________________________________________
def main(user_input):

  while True:
    #Setting the directory for the Data.
    try:
      os.chdir(directory)
    except:
      return write_tag(BAD)

    try:
      #Create function to extract serial number
      full_serial_number, serial_number, model = get_serial_number(read_tag()[1]['JSN'])

      # Find the CSV files where the serial number is found

      df_merge = pd.DataFrame()
      list_of_relevant_dataframes = []
      list_of_relevant_csv_dates = []


      time_frame = int(0)

      list_of_days = []
      for i in range(time_frame+1):
        tdelta = dt.timedelta(days =i)
        day = "NUM_"+ (dt.datetime.today()-tdelta).strftime("%#m-%#d-%Y")+'.csv'
        list_of_days.append(day)
        list_of_days.append('NUM_red_rabbit.csv')

      for csv in os.listdir():
        if csv in list_of_days:
          csv_df = pd.read_csv(csv, encoding = 'ISO-8859-1')
          
          if csv_df[(csv_df['Serial_No'] == serial_number) | (csv_df['Serial_No'] == str(serial_number))].shape[0] >=1:
            list_of_relevant_csv_dates.append((csv.split('_')[1]).split('.')[0])
            csv_df = csv_df.loc[((csv_df['Serial_No'] == serial_number) | (csv_df['Serial_No'] == str(serial_number)))]
            list_of_relevant_dataframes.append(csv_df)

      

      if len(list_of_relevant_dataframes) == 0:
        write_tag(BAD)

      try:
        df_merge = pd.concat(list_of_relevant_dataframes)
      except ValueError:
        write_tag(BAD)

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

        write_tag(GOOD)
        # verdict_label.config(text=df_merge.loc[df_merge['Full_Serial_Number']== full_serial_number,['Full_Serial_Number','Spindle','Judge','Program']], background = '#ccffdd', font=('Helvetica 14 bold'))
          

      elif len(rework_spindles) != 0 and len(bad_spindles) == 0:
        for i in rework_spindles:
          spindle_list_rework.append(i['Spindle'])
        write_tag(BAD)

      
      else:
        for i in bad_spindles:
          spindle_list_scrap.append(i['Spindle'])
        write_tag(BAD)

    except ValueError:
      write_tag(BAD)


# main('mb5c-5k067-ad-202453018')

