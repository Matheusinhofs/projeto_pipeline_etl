# utiliza o pandas para carregar um arquivo CSV e gera um relatório de perfil usando ydata-profiling
import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv('data.csv')
profile = ProfileReport(df, title="Profiling Report")
profile.to_file("profiling_report.html")