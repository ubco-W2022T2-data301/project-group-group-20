def load_and_process(path_to_csv_file):

   df1 = (pd.read_csv('BankChurners.csv'))\
             .drop(columns = ['Avg_Utilization_Ratio','Avg_Open_To_Buy', 'Total_Trans_Ct', 'Total_Amt_Chng_Q4_Q1','Total_Ct_Chng_Q4_Q1','Total_Trans_Amt'])\
             .dropna(subset = ['Months_on_book','Total_Revolving_Bal'])\
             .reset_index(drop=True)\
             .rename(columns={"Customer_Age": "Age"}
                    )
   df2 = (
       df1
       .dropna()\
       .sort_values('Total_Revolving_Bal', ascending = False)\
       .rename(columns={"CLIENTNUM": "Client"})
   )
       
   return df2
