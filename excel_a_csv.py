import pandas as pd

df = pd.read_excel("Documento.xlsx")

df.to_csv ("Documento.csv", index = None,  header=True) 
