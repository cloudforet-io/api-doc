---
title: "Userfile"
linkTitle: "Userfile"
weight: 3
bookFlatSection: true
---
# [Userfile](#Userfile)



>  **Package : spaceone.api.file_manager.v1**

<br>
<br>

## Userfile





**UserFile Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**update**](./UserFile#update) | [UpdateUserFileRequest](UserFile#updateuserfilerequest) | [UserFileInfo](UserFile#userfileinfo) |
| [**delete**](./UserFile#delete) | [UserFileRequest](UserFile#userfilerequest) | [Empty](UserFile#empty) |
| [**get**](./UserFile#get) | [UserFileRequest](UserFile#userfilerequest) | [UserFileInfo](UserFile#userfileinfo) |
| [**list**](./UserFile#list) | [UserFileSearchQuery](UserFile#userfilesearchquery) | [UserFilesInfo](UserFile#userfilesinfo) |
| [**stat**](./UserFile#stat) | [UserFileStatQuery](UserFile#userfilestatquery) | [Struct](UserFile#struct) |



    
<br>

### update





> **POST** /file-manager/v1/userfile/update
>






    
<br>

### delete





> **POST** /file-manager/v1/userfile/delete
>






    
<br>

### get





> **POST** /file-manager/v1/userfile/get
>






    
<br>

### list





> **POST** /file-manager/v1/userfile/list
>






    
<br>

### stat





> **POST** /file-manager/v1/userfile/stat
>






    


<br>
<br>

## Message



### CreateUserFileRequest
* **name** (string)   `Required` 

    
* **tags** (Struct)  

    
* **reference** (UserFileReference)  

    
* **domain_id** (string)  

    
* **user_id** (string)  

    <br>

### UpdateUserFileRequest
* **file_id** (string)   `Required` 

    
* **tags** (Struct)  

    
* **reference** (UserFileReference)  

    <br>

### UserFileInfo
* **file_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **download_url** (string)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **reference** (UserFileReference)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **user_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    <br>

### UserFileReference
* **resource_type** (string)   `Required` 

    
* **resource_id** (string)   `Required` 

    <br>

### UserFileRequest
* **file_id** (string)   `Required` 

    <br>

### UserFileSearchQuery
* **query** (Query)  

    
* **file_id** (string)  

    
* **name** (string)  

    
* **resource_type** (string)  

    
* **resource_id** (string)  

    
* **domain_id** (string)  

    
* **user_id** (string)  

    <br>

### UserFileStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### UserFilesInfo
* **results** (UserFileInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>
