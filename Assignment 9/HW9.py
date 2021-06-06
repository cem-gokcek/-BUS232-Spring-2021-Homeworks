import pandas

#taking the data from the excel
#hocam please be careful on the adres 
excel_data_hami = pandas.read_excel('C:/Users/Arrow/Desktop/Assignment 9/HW9.xlsx', sheet_name='Sayfa1')

#finding the columns names
columnsName = excel_data_hami.columns.ravel()

#finding the datas from each columns
columns0List = excel_data_hami[columnsName[0]].tolist()
columns1List = excel_data_hami[columnsName[1]].tolist()
columns2List = excel_data_hami[columnsName[2]].tolist()
columns3List = excel_data_hami[columnsName[3]].tolist()
columns4List = excel_data_hami[columnsName[4]].tolist()

#creating a data frame
df = pandas.DataFrame({columnsName[1]: columns1List,
                       columnsName[2]: columns2List,
                       columnsName[3]: columns3List,
                       columnsName[4]: columns4List},
                  index=columns0List)

#calculation
df["HAMI"] = df[columnsName[1]] + df[columnsName[2]] + df[columnsName[3]] - df[columnsName[4]]

#removing the columns which are not necessary for the final output
df = df.drop(columns = [columnsName[1], columnsName[2], columnsName[3], columnsName[4]])

#the final excel output
df.to_excel("HW9+.xlsx")
