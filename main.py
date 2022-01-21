import csv
import json
import Encryption
import requests
import time

token = Encryption.token
empty = ""

with open('test2.csv', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for i in csv_reader:
                print(i)
                if i['Prefix'] == empty:
                        del i['Prefix']
                if i['FirstName'] == "":
                        del i['FirstName']
                if i['LastName'] == empty:
                        del i['LastName']
                if i['Suffix'] == empty:
                        del i['Suffix']
                if i['DateOfBirth'] == empty:
                        del i['DateOfBirth']
                if i['Email'] == empty:
                        del i['Email']
                if i['Address1'] == empty:
                        del i['Address1']
                if i['Address2'] == empty:
                        del i['Address2']
                if i['City'] == empty:
                        del i['City']
                if i['State']== empty:
                        del i['State']
                if i['ZipCode']== empty:
                        del i['ZipCode']
                if i['PrimaryPhone']== empty:
                        del i['PrimaryPhone']
                if i['PrimaryPhoneType']== empty:
                        del i['PrimaryPhoneType']
                if i['PrimaryFax']== empty:
                        del i['PrimaryFax']
                if i['PhoneAdditional1']== empty:
                        del i['PhoneAdditional1']
                if i['PhoneAdditionalType1']== empty:
                        del i['PhoneAdditionalType1']
                if i['PhoneAdditional2']== empty:
                        del i['PhoneAdditional2']
                if i['PhoneAdditionalType2']== empty:
                        del i['PhoneAdditionalType2']
                if i['PhoneAdditional3']== empty:
                        del i['PhoneAdditional3']
                if i['PhoneAdditionalType3']== empty:
                        del i['PhoneAdditionalType3']
                if i['DEANumber']== empty:
                        del i['DEANumber']
                if i['DEANumbers']== empty:
                        del i['DEANumbers']
                if i['NADEANumbers'] == empty:
                        del i['NADEANumbers']
                if i['MedicalLicenseNumbers'] == empty:
                        del i['MedicalLicenseNumbers']
                if i['NPINumber'] == empty:
                        del i['NPINumber']
                if i['ClinicianRoleType'] == empty:
                        del i['ClinicianRoleType']
                if i['EPCSRequested'] == empty:
                        del i['EPCSRequested']
                if i['Active'] == empty:
                        del i['Active']
                url = 'https://my.staging.dosespot.com/webapi/api/clinicians'

                payload = i
                headers = {'Content-Type': 'application/x-www-form-urlencoded',
                           'Authorization': 'Bearer ' + token
                           }
                response = requests.post(url, headers=headers, data=payload)
                print(response.text)
                time.sleep(20)


