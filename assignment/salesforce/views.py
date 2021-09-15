from django.shortcuts import render, redirect
from .models import *
import requests

params = {'grant_type':'password', 
'client_id':'3MVG9fe4g9fhX0E7euFpL0PpD1TNY4boPYoeZ105b.C18mw32b4CgkhZjsDzE4uQCT3B6.Sng4XkhJZ5zQAgJ', 
'client_secret':'923D785504966E827D70DB2DFC754B773FB63AD7217069497CBCA37A38ECACB5', 
'username':'sanayshah2@test.com', 
'password':'Sanay$hah2xCNPhgKjcsWX6qXe3XVFnc6F8'}
r = requests.post('https://login.salesforce.com/services/oauth2/token', params = params).json()
access_token = r['access_token']
instance_url = r['instance_url']
headers = {
    'Content_type': 'applicaton/json',
    'Accept-Encoding':'gzip',
    'Authorization':'Bearer ' + access_token
}

def home(request):
        users = Users.objects.all()
        accounts = Account.objects.all()
        contacts = Contact.objects.all()
        return render(request, 'salesforce/home.html', {'users':users, 'accounts':accounts, 'contacts':contacts})



def get_users(request):
    query = 'SELECT FIELDS(ALL) from User LIMIT 200'
    userslist = requests.request('get', instance_url + '/services/data/v52.0/query/',params = {'q':query}, headers=headers).json()
    for x in userslist['records']:
        if Users.objects.filter(user_id = x['Id']).exists():
            continue
        else:      
            Users.objects.create(username = x['Username'], name = x['Name'], user_id = x['Id'], email = x['Email'], created_date = x['CreatedDate'])
    return redirect('home')

def get_accounts(request):
    query = 'SELECT FIELDS(ALL) from Account LIMIT 200'
    accountslist = requests.request('get', instance_url + '/services/data/v52.0/query/',params = {'q':query}, headers=headers).json()
    for x in accountslist['records']:
        if Account.objects.filter(account_id = x['Id']).exists():
            continue
        else:      
            Account.objects.create(account_id = x['Id'], name = x['Name'], user_id = x['OwnerId'], created_date = x['CreatedDate'])
    return redirect('home')

def get_contacts(request):
    query = 'SELECT FIELDS(ALL) from Contact LIMIT 200'
    contactslist = requests.request('get', instance_url + '/services/data/v52.0/query/',params = {'q':query}, headers=headers).json()
    for x in contactslist['records']:
        if Contact.objects.filter(contact_id = x['Id']).exists():
            continue
        else:      
            Contact.objects.create(contact_id = x['Id'], name = x['Name'], user_id = x['OwnerId'], account_id = x['AccountId'], created_date = x['CreatedDate'])
    return redirect('home')