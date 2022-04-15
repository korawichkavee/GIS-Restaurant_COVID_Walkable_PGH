import pandas as pd
import os
import winsound

# Get the list of all files and directories
path = "RawData/"
dir_list = os.listdir(path)
print("Files and directories in '", path, "' :")
print("There are "+str(len(dir_list))+" files in "+path)

# Importing raw datasets & append all files
for file in range(len(dir_list)):
    df_tempo = pd.read_csv(path + dir_list[file])
    print(dir_list[file])
    #Remove fileds not needed
    df_tempo = df_tempo[["Version Year","IUSA Number", "Company Name", "Address", "City", "State", "ZIP Code","Primary SIC Description"]]
    if file == 0:
        df = df_tempo
    df = df.append(df_tempo)
del df_tempo

# for each year
df2019 = df[df["Version Year"]==2019]
df2020 = df[df["Version Year"]==2020]
df2021 = df[df["Version Year"]==2021]

#export
df.to_csv("PghRestaurantAllYear" + ".csv",index=False)
df2019.to_csv("PghRestaurant2019" + ".csv",index=False)
df2020.to_csv("PghRestaurant2020" + ".csv",index=False)
df2021.to_csv("PghRestaurant2021" + ".csv",index=False)

#FINISH
duration = 1000  # milliseconds
freq = 440  # Hz
winsound.Beep(freq, duration)
