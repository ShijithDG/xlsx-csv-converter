import pandas as pd

try :
    data = pd.read_excel(r"C:\Users\datag\Downloads\sample_data.xlsx")
    #print(data, 'this  data from xlsx file')
    
    csv_file = data.to_csv('xlsx-converted(1).csv', index=True)

except Exception as e :
    
    print(f"error : {e}")
    
finally :
    
    print('all task are done')