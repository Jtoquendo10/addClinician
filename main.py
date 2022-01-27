import csv
import json
import Encryption
import requests
import time

token = Encryption.token
empty = ""
        #Scroll to line 141

def addClinician():
        with open('addClinician.csv', encoding='utf-8-sig') as csv_file:
                csv_reader = csv.DictReader(csv_file, dialect='excel')
                try:
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
                                if i['NADEANumbers'] == empty:
                                        del i['NADEANumbers']
                                if i['MedicalLicenseNumbers'] == empty:
                                        del i['MedicalLicenseNumbers']
                                if i['NPINumber'] == empty:
                                        del i['NPINumber']
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

                except csv.Error as e:
                        sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))

def addClinic():
        with open('addClinic.csv', encoding='utf-8-sig') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                try:
                        for i in csv_reader:
                                print(i)
                                if i['ClinicName'] == empty:
                                        del i['ClinicName']
                                if i['ClinicNameLongForm'] == "":
                                        del i['ClinicNameLongForm']
                                if i['Address1'] == empty:
                                        del i['Address1']
                                if i['Address2'] == empty:
                                        del i['Address2']
                                if i['Active'] == empty:
                                        del i['Active']
                                if i['City'] == empty:
                                        del i['City']
                                if i['State'] == empty:
                                        del i['State']
                                if i['ZipCode'] == empty:
                                        del i['ZipCode']
                                if i['PrimaryPhone'] == empty:
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

                                url = 'https://my.staging.dosespot.com/webapi/api/clinics'

                                payload = i
                                headers = {'Content-Type': 'application/x-www-form-urlencoded',
                                           'Authorization': 'Bearer ' + token
                                           }
                                response = requests.post(url, headers=headers, data=payload)
                                print(response.text)
                                time.sleep(20)

                except csv.Error as e:
                        sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))

        #Enter 1 to add clinicians or enter 2 to add a clinic

selection = input('Please select an operation:\n 1. Add Clincician\n 2. Add Clinic\n')
try:
        if selection == "1":
                addClinician()
        elif selection == "2":
                addClinic()
        else:
                print('Could not read input')
except Exception as e:
        print('An error has occurred')
        print(e)

