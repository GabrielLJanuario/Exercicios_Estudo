import json
import datetime
from datetime import datetime

from Tools.scripts.generate_global_objects import Printer

#NewestReportDate: Data mais recente entre "NewestPefinDate", "NewestProtestsDate", "NewestLawsuitsDate"
#data1
#data2
#data3
data_atual="2024-09-28T10:24:00"
prova='{"Pefin": {"NewestPefinDate": "2019-07-18T00:00:00", "OldestPefinDate": "2019-07-18T00:00:00", "TotalPefinValue": 82.02, "TotalPefinNumber": 1}, "Refin": {"NewestRefinDate": null, "OldestRefinDate": null, "TotalRefinValue": 0, "TotalRefinNumber": 0}, "Score": {"Score": 400, "NonPaymentProbability": 45}, "Lawsuits": {"NewestLawsuitsDate": null, "OldestLawsuitsDate": null, "TotalLawsuitsValue": 0, "TotalLawsuitsNumber": 0}, "Protests": {"NewestProtestsDate": "2019-07-19T00:00:00", "OldestProtestsDate": null, "TotalProtestsValue": 0, "TotalProtestsNumber": 0}, "GeneralData": {"CPF": "69795975153", "Name": "VILMA MARIA ROCHA OLIVEIRA", "BirthDate": "1977-08-30T00:00:00", "MothersName": "MARIA OLIVEIRA COSTA", "SituationCode": "2", "SituationDate": "2021-09-29T00:00:00"}, "BankruptcyParticipation": {"BankruptcyParticipationDetails": []}}'
leitura=json.loads(prova)
teste= json.dumps(leitura)
lista_dif=[]
first_date=leitura['Pefin']['NewestPefinDate']
second_date=leitura['Protests']['NewestProtestsDate']
tird_date=leitura['Lawsuits']['NewestLawsuitsDate']

if first_date is not None and first_date < data_atual:
    data1_dif=abs(datetime.strptime(first_date, "%Y-%m-%dT%H:%M:%S")-datetime.strptime(data_atual,"%Y-%m-%dT%H:%M:%S"))
else:
    data1_dif = None

if second_date is not None and second_date < data_atual:
    data2_dif=abs(datetime.strptime(second_date, "%Y-%m-%dT%H:%M:%S")-datetime.strptime(data_atual,"%Y-%m-%dT%H:%M:%S"))
else:
    data2_dif = None
if tird_date is not None and tird_date < data_atual:
    data3_dif = abs(
        datetime.strptime(tird_date, "%Y-%m-%dT%H:%M:%S") - datetime.strptime(data_atual, "%Y-%m-%dT%H:%M:%S"))
else:
    data3_dif = None


if data1_dif is not None:
    data_dif=data1_dif
    if data2_dif is not None:
        data_dif = min(data1_dif, data2_dif)
        if data3_dif is not None:
            data_dif=min(data1_dif,data2_dif,data3_dif)


if data_dif == data1_dif and data1_dif is not None:
    print("A data mais perto da data atual é NewestPefinDate com " + data_dif + " de diferença")
    if data_dif == data2_dif and data2_dif is not None:
        print("A data mais perto da data atual é NewestProtestsDate com " + data_dif + " de diferença")
        if data_dif == data3_dif and data3_dif is not None:
            print("A data mais perto da data atual é NewestLawsuitsDate com " + data_dif + " de diferença")








