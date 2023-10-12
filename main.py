import requests
import time
import smtplib
from bs4 import BeautifulSoup

list = [1072, 1057, 1085, 1033, 1032, 1054]
list2 = []

file = open('./text.txt', 'r')
for line in file:
    list2.append(line.removesuffix('\n'))
file.close()

while True:
    __VIEWSTATE = '/wEPDwUKMTE0NjMzNTU5Ng9kFgICAw9kFgwCAQ8QDxYEHg5EYXRhVmFsdWVGaWVsZAUEY29kZR4NRGF0YVRleHRGaWVsZAUEbmFtZWQQFQ0EWWVhcgQyMDExBDIwMTIEMjAxMwQyMDE0BDIwMTUEMjAxNgQyMDE3BDIwMTgEMjAxOQQyMDIwBDIwMjEEMjAyMhUNAAQyMDExBDIwMTIEMjAxMwQyMDE0BDIwMTUEMjAxNgQyMDE3BDIwMTgEMjAxOQQyMDIwBDIwMjEEMjAyMhQrAw1nZ2dnZ2dnZ2dnZ2dnFgECDGQCAw8QDxYEHwEFCU1vbnRobmFtZR8ABQRDb2RlZBAVAwVNb250aAREZWMuBE1heS4VAwACMTIBNRQrAwNnZ2dkZAIFDxAPFgQfAQULQ291cnNlIFR5cGUfAAUIVHlwZUNvZGVkEBUDC0NvdXJzZSBUeXBlC1Bhc3MgQ291cnNlCkNCRVMgKE5ldykVAwABUAFDFCsDA2dnZxYBAgFkAgcPEA8WBh8ABQlDbGFzc2NvZGUfAQUFY25hbWUeC18hRGF0YUJvdW5kZ2QQFS0QLS1TZWxlY3QgQ2xhc3MtLSxBZHZhbmNlIERpcGxvbWEgQ291cnNlIGluIEZyZW5jaCAoUGFydCBUaW1lKSpBZHZhbmNlIERpcGxvbWEgQ291cnNlIGluIFVyZHUgKFBhcnQgVGltZSkeQi5TQy4gKEluZm9ybWF0aW9uIFRlY2hub2xvZ3kpEEJhY2hlbG9yIG9mIEFydHMjQmFjaGVsb3Igb2YgQnVzaW5lc3MgQWRtaW5pc3RyYXRpb24UQmFjaGVsb3Igb2YgQ29tbWVyY2UcQmFjaGVsb3Igb2YgQ29tbWVyY2UgKEhvbnMuKSFCYWNoZWxvciBvZiBDb21wdXRlciBBcHBsaWNhdGlvbnMTQmFjaGVsb3Igb2YgU2NpZW5jZSRCYWNoZWxvciBvZiBTY2llbmNlIChCaW8tVGVjaG5vbG9neSknQmFjaGVsb3Igb2YgU2NpZW5jZSAoRmFzaGlvbiBEZXNpZ25pbmcpIkJhY2hlbG9yIG9mIFNjaWVuY2UgKEhvbWUgU2NpZW5jZSkoQmFjaGVsb3Igb2YgVm9jYXRpb24gKEJlYXV0eSAmIFdlbGxuZXNzKSNCYWNoZWxvciBvZiBWb2NhdGlvbiAoRGF0YSBTY2llbmNlKS1CYWNoZWxvciBvZiBWb2NhdGlvbiAoSGVhbHRoIENhcmUgTWFuYWdlbWVudCkwQmFjaGVsb3Igb2YgVm9jYXRpb24gKE1lbnRhbCBIZWFsdGggQ291bnNlbGxpbmcpKkJhY2hlbG9yIG9mIFZvY2F0aW9uIChQcmludGluZyBUZWNobm9sb2d5KStCYWNoZWxvciBvZiBWb2NhdGlvbiAoU29mdHdhcmUgRGV2ZWxvcG1lbnQpMkJhY2hlbG9yIG9mIFZvY2F0aW9uIChXZWIgVGVjaG5vbG9neSAmIE11bHRpbWVkaWEpKENlcnRpZmljYXRlIENvdXJzZSBpbiBHZXJtYW4gKFBhcnQgVGltZSkpQ2VydGlmaWNhdGUgQ291cnNlIGluIFBlcnNpYW4gKFBhcnQgVGltZSkpQ2VydGlmaWNhdGUgQ291cnNlIGluIFJ1c3NpYW4gKFBhcnQgVGltZSkkRGlwbG9tYSBDb3Vyc2UgaW4gRnJlbmNoIChGdWxsIFRpbWUpJERpcGxvbWEgQ291cnNlIGluIEZyZW5jaCAoUGFydCBUaW1lKSREaXBsb21hIENvdXJzZSBpbiBHZXJtYW4gKFBhcnQgVGltZSkiRGlwbG9tYSBDb3Vyc2UgaW4gVXJkdSAoUGFydCBUaW1lKRpMTC5CLiAoVGhyZWUgWWVhcnMgQ291cnNlKQpNLkEuIERBTkNFDk0uQS4gRklORSBBUlRTC00uQS4gRlJFTkNIDk0uQS4gR0VPR1JBUEhZCk0uQS4gSElOREkMTS5BLiBISVNUT1JZF00uQS4gTVVTSUMgSU5TVFJVTUVOVEFMEE0uQS4gTVVTSUMgVk9DQUwWTS5BLiBQT0xJVElDQUwgU0NJRU5DRRZNLkEuIFJFTElHSU9VUyBTVFVESUVTDU0uQS4gU0FOU0tSSVQdTS5BLkJVU0lORVNTIEVDT05PTUlDUyAmIEkuVC4WTS5TYy4gSU5URVJORVQgU1RVRElFUyFNQVNURVIgSU4gRklORSBBUlRTIChBUFBMSUVEIEFSVCkrTWFzdGVyIG9mIFZvY2F0aW9uIChDb3NtZXRvbG9neSAmIFdlbGxuZXNzKSZQLiBHLiBEaXBsb21hIGluIENvbXB1dGVyIEFwcGxpY2F0aW9ucwxQcmFrIFNoYXN0cmkVLQAENDA0MAQ0MDQzBDEwNTcEMTAzMgQxMDU0BDEwODUEMTA5MQQxMDcyBDEwMzMEMTA3NAQxMDg2BDEwODIEMTEzOAQxMTQwBDExNDEEMTEzNgQxMTAyBDExMDMEMTEwMAQ1MDEyBDUwMTMENTAxNAQ0MDMyBDQwMzMENDAzNAQ0MDM4BDEwNjIEMjE1MwQyMTU5BDIxNjEEMjE1NgQyMTYzBDIwODkEMjE0OAQyMTQ5BDIxNjcEMjE1MAQyMTU1BDIxODIEMjE3MwQyMTgxBDIxOTIEMzAzNQQxMTMyFCsDLWdnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZxYBAghkAgkPEA8WBh8ABQljbGFzc2NvZGUfAQUFY25hbWUfAmdkEBUCEy0gIFNlbGVjdCBTZW1lc3Rlci0wQmFjaGVsb3Igb2YgQ29tcHV0ZXIgQXBwbGljYXRpb25zLCBTZW1lc3RlciAtIFZJFQIABjEwNzIwNhQrAwJnZxYBZmQCCw8PFgIeB0VuYWJsZWRnZGRkTncYR6loV5/miaD8cARSrTpgTS5sp5cD/IfsGExuCoU='
    __EVENTTARGET = 'DrpDwnCMaster'
    __EVENTARGUMENT = ''
    __LASTFOCUS = ''
    __VIEWSTATEGENERATOR = '72A7EE3D'
    endpoint = "https://collegeadmissions.gndu.ac.in/studentArea/GNDUEXAMRESULT.aspx"

    
    for x in list:
        form = {
            '__VIEWSTATE': __VIEWSTATE,
            '__VIEWSTATEGENERATOR': __VIEWSTATEGENERATOR,
            '__EVENTTARGET': __EVENTTARGET,
            '__LASTFOCUS: ': __LASTFOCUS,
            '__EVENTARGUMENT': __EVENTARGUMENT,
            'DrpDwnYear': '2022',
            'DrpDwnMonth': '5',
            'DropDownCourseType': 'P',
            'DrpDwnCMaster': x,
        }

        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(endpoint, data=form, headers=headers)
        soup = BeautifulSoup(response.content, 'html5lib')
        res = soup.find('select', attrs={'id': 'DrpDwnCdetail'})
        for option in res.find_all('option'):
            if option['value'] not in list2:
                fromaddr = '----'
                toaddrs = '----'
                subject = "New result! Alert"
                message = option.text + ' **Result Announced!** \n\nhttp://result.gndu.ac.in/download/' + option['value'] + '.pdf'
               
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login(fromaddr, "----")
                msg = ("From: %s\r\nTo: %s\r\nSubject: %s\n\n%s"
                    % (fromaddr, toaddrs, subject, message))
                s.sendmail(fromaddr, toaddrs, msg)
                s.quit()

                file = open('./text.txt', 'a')
                file.write(option['value'] + '\n')
                file.close()
                list2.append(option['value'])
            print(list2)
    time.sleep(900)
