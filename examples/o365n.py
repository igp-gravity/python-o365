# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 07:07:48 2020

@author: chens
"""


from O365 import Account

credentials = ('701c36fa-d363-4258-ba82-0e8a3d836ffa', '******')

account = Account(credentials, auth_flow_type ='credentials', tenant_id='bbcb9797-d502-4c33-801d-9c3272867d74')
if account.authenticate():
   print('Authenticated!')

#print(account.con.token_backend.token)

storage = account.storage()
drives = storage.get_drives()
my_drive = storage.get_default_drive()
root_folder = my_drive.get_root_folder()
attachments_folder = my_drive.get_special_folder('attachments')

for item in root_folder.get_items(limit=25):
    
    if item.is_folder:
        print(list(item.get_items(2)))  # print the first to element on this folder.
    elif item.is_file:
        if item.is_photo:
            print(item.camera_model)  # print some metadata of this photo
        elif item.is_image:
            print(item.dimensions)  # print the image dimensions
        else:
            # regular file:
            print(item.mime_type)  # print the mime type
            print(item.web_url)
            
