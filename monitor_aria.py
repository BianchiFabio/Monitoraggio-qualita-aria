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
                
    #                                                      CENTRALINE                                                                           #      

    #::::::::::::::::::::::::::::::::::::::::::::::::::::#           #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#    
    #                STAZIONE ANALIZZATA                 #           #                      STAZIONE ANALIZZATA                       #
    # Nome stazione  Brescia - via Turati                #           # Nome stazione         Brescia - Broletto                       #
    # Idstazione           652                           #           # Idstazione                   649                               #
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

    
#:::::::::::::::::::::::::::::::::::::::::::::::: IMPORT
import pandas as pd
import calendar

#:::::::::::::::::::::::::::::::::::::::::::::::: VARIABILI
yy = 2020
mm = 1
scelgo_sensore = 0
scelgo_val_min = 0
csv_stat       = pd.DataFrame()
csv            = pd.DataFrame()

#:::::::::::::::::::::::::::::::::::::::::::::::: PGESTIONE .csv CON PANDAS
csv = pd.read_csv   ('Dati_sensori_aria.csv', sep=',', header=0)         # csv e' indispenesabile il sep=';' dove ';' e' il delimitatore nel CSV che importi. In questo caso e' virgola
                                                                         # In header=N.riga in cui ci sono intestazioni di colonna
                                                                         # Di default, pd.read_csv usi header=0 (quando il names anche il parametro non è specificato),
                                                                         # il che significa che la prima riga (cioè indicizzata con 0th) viene interpretata come nome
                                                                         # di colonna.
                                                                         # Se i tuoi dati non hanno intestazione, allora usa pd.read_csv(..., header=None)
csv['DataCorr'] = pd.to_datetime(csv['Data'], format='%d/%m/%Y %I:%M:%S %p') # Trasformno la colonna Data (contenente dati NON datetime) in DataCorr (Contenente dati datetime)
csv = csv.drop(columns="Data")                                               # Elimino la colonna Data

def espongo_dati():
    global scelgo_val_min
    global scelgo_sensore
    global csv
    
    csv_stat = csv.drop(columns=["idOperatore","Stato","IdSensore"])

    print('\nDESCRIZIONE STATISTICA DI SINTESI')
    print('---------------------------------')
    print(csv_stat.describe())
    if scelgo_sensore == 6951:
        print ('Il valore di PM10 sono stabiliti in:')
        print (limiti.__doc__)
    if scelgo_sensore == 30158:
        print ('Il valore di PM2.5 sono stabiliti in:')
        print (limiti.__doc__)
    print ('\n','Valore raggiunto ordinato dal più grande al più piccolo\n -------------------------------------------------------\n',
       csv_stat.sort_values('Valore',ascending=False))
    selezione()

def selezione ():
    global scelgo_val_min
    global scelgo_sensore
    global csv
    print ('\n'*3)
    print (centraline.__doc__)
    scelgo_sensore = int(input('Inserisci IdSensore per il quale vuoi estrarre i dati > '))
    csv = csv[csv.IdSensore == scelgo_sensore] # Filtro la colonna IdSensore con l'input utente
    scelgo_val_min = int (input('Scegli valore minimo da esporre nei dati > '))
    csv = csv [csv.Valore > scelgo_val_min]    # Filtro la colonna Valore con l'input utente
    print ('\n'*3)
    espongo_dati()

selezione()
