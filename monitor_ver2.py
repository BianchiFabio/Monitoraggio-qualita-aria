import pandas as pd
import matplotlib.pyplot as plt

dati = pd.read_csv ('200505_Dati_sensori_aria.csv', sep=";",header = 0)
# Carico i dati dal .csv nel pd dati ATTENZIONE AL SEPARATORE DEI DATI DEL CSV: A VOLTE E' , A VOLTE E' ;
print (dati.head(2))

datiPM10 = dati [dati.IdSensore == 6951] # filtro le righe che contengono i dati IdSensore selezionato
datiPM2_5 = dati [dati.IdSensore == 30158] # filtro le righe che contengono i dati IdSensore selezionato

# PM 10
fig, ax = plt.subplots()
# aggiungo una colonna che contiene le date contenute in Data e le trasforma in type datetime
#datiPM10 ['DataCORR'] = pd.to_datetime(datiPM10['Data'], format='%d/%m/%Y %I:%M:%S %p') # versione fino al 24/04/20
datiPM10 ['DataCORR'] = pd.to_datetime(datiPM10['Data'], format='%d/%m/%Y %M:%S')        # versione dal 05/05/20 compreso 

dati1_chart = datiPM10 [['DataCORR', 'Valore']].sort_values(by='DataCORR')#, ascending =True
#dati1_chart.plot (kind = 'bar', x = 'DataCORR', title = 'PM 10', figsize=(20,8), fontsize=6, ax=ax)
dati1_chart.plot (x = 'DataCORR', title = 'PM 10', figsize=(18,8), fontsize=15, ax=ax)
ax.grid(which='major', linestyle='-', linewidth='1.5', color='green')
ax.grid(which='minor', linestyle=':', linewidth='0.5', color='red')

# -------------------------------------------------------------------------
# PM 2.5
fig2, ax = plt.subplots()
# aggiungo una colonna che contiene le date contenute in Data e le trasforma in type datetime
#datiPM2_5 ['DataCORR'] = pd.to_datetime(datiPM2_5['Data'], format='%d/%m/%Y %I:%M:%S %p') # versione fino al 24/04/20
datiPM2_5 ['DataCORR'] = pd.to_datetime(datiPM2_5['Data'], format='%d/%m/%Y %M:%S')        # versione dal 05/05/20 compreso 

dati2_chart = datiPM2_5 [['DataCORR', 'Valore']].sort_values(by='DataCORR')#, ascending =True
#dati1_chart.plot (kind = 'bar', x = 'DataCORR', title = 'PM 10', figsize=(20,8), fontsize=6, ax=ax)
dati2_chart.plot (x = 'DataCORR', title = 'PM 2.5', figsize=(18,8), fontsize=15, ax=ax)
ax.grid(which='major', linestyle='-', linewidth='1.5', color='green')
ax.grid(which='minor', linestyle=':', linewidth='0.5', color='red')

plt.show()

# ---------------------------

#::::::::::::::::::::::::::::::::::::::::::::::::
# Fabio Bianchi
# 12/01/2020
# Monitoraggio qualita' aria
#
# Disclaimer: tutti i dati riportati devono essere riscontrati dall'utilizzatore finale e NON hanno carattere di ufficialità
#             Il creatore del codice declina ogni responsabilità dalla diffusione illecita o non confutata di tali dati.

#:::::::::::::::::::::::::::::::::::::::::::::::: CENTRALINE
# Mappa delle stazioni
# https://www.dati.lombardia.it/Ambiente/Mappa-stazioni-qualit-dell-aria/npva-smv6
# Elenco delle stazioni e del tipo di sensori installati
# https://www.dati.lombardia.it/Ambiente/Stazioni-qualit-dell-aria/ib47-atvt
# Elenco stazioni e utilizzo filtri
# https://www.dati.lombardia.it/Ambiente/Stazioni-qualit-dell-aria/ib47-atvt/data

#:::::::::::::::::::::::::::::::::::::::::::::::: SENSORI
# Link dati sensori GENERALE.
# All'interno troverai i dati di tutti i sensori di tutte le stazioni:
# https://www.dati.lombardia.it/Ambiente/Dati-sensori-aria/nicp-bhqi
# Spostati nel seguente link per scaricare il relativo CSV:
# https://www.dati.lombardia.it/Ambiente/Dati-sensori-aria/nicp-bhqi/data
# I dati sono raccolti e eggregati dal 1 gennaio al 31 dicembre di ogni anno

def centraline ():
    '''
    Disclaimer: tutti i dati riportati devono essere riscontrati dall'utilizzatore finale e NON hanno carattere di ufficialità
                Il creatore del codice declina ogni responsabilità dalla diffusione illecita o non confutata di tali dati.                
                
    #                                                                CENTRALINE                                                                           #      

    #::::::::::::::::::::::::::::::::::::::::::::::::::::#           #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#    
    #                STAZIONE ANALIZZATA                 #           #                          STAZIONE ANALIZZATA                       #
    # Nome stazione              Brescia - via Turati    #           # Nome stazione                 Brescia - Broletto                  #
    # Idstazione                 652                     #           # Idstazione                            649                                 #
    # ---------------------------------------------------#           # ---------------------------------------------------------------#
    # IdSensore | NomeTipoSensore          | UnitaMisura #           # IdSensore | NomeTipoSensore          | DataStop  | UnitaMisura #
    # ----------|--------------------------|-------------#           # ----------|--------------------------|-----------+-------------#   
    # 6781      | Biossido di Azoto        | µg/m³       #           # 6767      | Ozono                    | 27/02/2004| µg/m³       #
    # 30166     | Benzene                  | µg/m³       #           # 6766      | Ossidi di Azoto          |           | µg/m³       #
    # 6782      | Monossido di Carbonio    | mg/m³       #           # 6761      | Biossido di Azoto        |           | µg/m³       #
    # 6784      | Ossidi di Azoto          | µg/m³       #           # 30158     | Particelle sospese PM2.5 |           | µg/m³       #
    #           |                          |             #           # 6764      | Monossido di Carbonio    |           | mg/m³       #
    #           |                          |             #           # 6951      | PM10 (SM2005)            |           | µg/m³       #
    #           |                          |             #           # 6762      | Biossido di Zolfo        | 06/06/2000| µg/m³       #
    # ---------------------------------------------------#           # -------------------------------------------------+-------------#     
    #          lat 45.5395294 lng 10.2317859             #           #           lat 45.540057846971386 lng 10.222818449274216        #
    #::::::::::::::::::::::::::::::::::::::::::::::::::::#           #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#    
    '''

def limiti():
    '''
    #                                           Limiti di legge della concentrazione di PM10 e PM2.5                                         #
    #                                                     https://www.pm10.it/limiti.html                                                    #
    
    #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#     #::::::::::::::::::::::::::::::::::::::::::::::::::::#
    #    Valore massimo per la media annuale | Valore massimo giornaliero (24 ore) #     # Numero massimo di superamenti consentiti in un anno#
    #                 PM10    PM2.5          |         PM10    PM2.5               #     #                 PM10     | PM2.5                   #
    #                (μg/m3) (μg/m3)         |        (μg/m3) (μg/m3)              #     #                (μg/m3)  |(μg/m3)                   #
    # ---------------------------------------|-------------------------------------#     # -----------------------|---------------------------#
    # Italia e Europa     40      25         |          50      --                 #     #     # Italia e Europa  35    |  --                 #
    # Australia           --       8         |          50      25                 #     #     # Australia        --    |  --                 #
    # Cina                70      35         |         150      75                 #     #     # Cina             --    |  --                 #
    # Hong Kong           50      35         |         100      75                 #     #     # Hong Kong         9    |   9                 #
    # Giappone            --      15         |       100-200    35                 #     #     # Giappone         --    |  --                 #
    # Russia              40      25         |          60      35                 #     #     # Russia           --    |  --                 #
    # USA                 --      12         |         150      35                 #     #     # USA               1    | media su 3 anni     #
    # OMS (2005)          20      10         |          50      25                 #     #     # OMS (2005)       --    |  --                 #
    # -----------------------------------------------------------------------------#     #----------------------------------------------------#
    '''

