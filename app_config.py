import os

CLIENT_ID = "5d69341c-d7d7-4a3f-8c10-aead276f5ff6"
CLIENT_SECRET = "24t0AOlEdr[eH2:axXZo]fm:Q1f:-Xu_"
AUTHORITY = "https://login.microsoftonline.com/common"

REDIRECT_PATH = "/getAToken"  

ENDPOINT = 'https://graph.microsoft.com/v1.0/users' 
GET_NOTEBOOKS_ENDPOINT = 'https://graph.microsoft.com/v1.0/me/onenote/notebooks' 
GET_SECTIONS_ENDPOINT = 'https://graph.microsoft.com/v1.0/me/onenote/sections' 
GET_PAGES_ENDPOINT = 'https://graph.microsoft.com/v1.0/me/onenote/pages?$select=title,contentUrl'  

SCOPE = ["Notes.Read"]

SESSION_TYPE = "filesystem"  

