---
title: "File"
linkTitle: "File"
weight: 3
bookFlatSection: true
---
# [File](#File)



>  **Package : spaceone.api.file_manager.v1**

<br>
<br>

## File





**File Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**add**](./File#add) | [CreateFileRequest](File#createfilerequest) | [FileInfo](./File#fileinfo) |
| [**update**](./File#update) | [UpdateFileRequest](File#updatefilerequest) | [FileInfo](./File#fileinfo) |
| [**delete**](./File#delete) | [FileRequest](File#filerequest) | [Empty](./File#empty) |
| [**get_download_url**](./File#get_download_url) | [FileRequest](File#filerequest) | [FileInfo](./File#fileinfo) |
| [**get**](./File#get) | [GetFileRequest](File#getfilerequest) | [FileInfo](./File#fileinfo) |
| [**list**](./File#list) | [FileQuery](File#filequery) | [FilesInfo](./File#filesinfo) |
| [**stat**](./File#stat) | [FileStatQuery](File#filestatquery) | [Struct](./File#struct) |



    
<br>

### add





> **POST** /file-manager/v1/file/add
>






    
<br>

### update





> **POST** /file-manager/v1/file/update
>






    
<br>

### delete





> **POST** /file-manager/v1/file/delete
>






    
<br>

### get_download_url





> **POST** /file-manager/v1/file/get-download-url
>






    
<br>

### get





> **POST** /file-manager/v1/file/get
>






    
<br>

### list





> **POST** /file-manager/v1/file/list
>






    
<br>

### stat





> **POST** /file-manager/v1/file/stat
>






    


<br>
<br>

## Message



### CreateFileRequest
* **name** (string)  `Required` 

    
* **tags** (Struct) 

    
* **reference** (FileReference) 

    
* **domain_id** (string) 

    <br>

### FileInfo
* **file_id** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **state** (FileState)  `Required` 

    
* **scope** (FileScope)  `Required` 

    
* **file_type** (string)  `Required` 

    
* **upload_url** (string)  `Required` 

    
* **upload_options** (Struct)  `Required` 

    
* **download_url** (string)  `Required` 

    
* **tags** (Struct)  `Required` 

    
* **reference** (FileReference)  `Required` 

    
* **user_id** (string)  `Required` 

    
* **user_domain_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    <br>

### FileQuery
* **query** (Query) 

    
* **file_id** (string) 

    
* **name** (string) 

    
* **state** (FileState) 

    
* **scope** (FileScope) 

    
* **file_type** (string) 

    
* **resource_type** (string) 

    
* **resource_id** (string) 

    
* **user_domain_id** (string) 

    
* **domain_id** (string) 

    <br>

### FileReference
* **resource_type** (string)  `Required` 

    
* **resource_id** (string)  `Required` 

    <br>

### FileRequest
* **file_id** (string)  `Required` 

    
* **domain_id** (string) 

    <br>

### FileStatQuery
* **query** (StatisticsQuery)  `Required` 

    
* **domain_id** (string)  `Required` 

    <br>

### FilesInfo
* **results** (FileInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### GetFileRequest
* **file_id** (string)  `Required` 

    
* **domain_id** (string) 

    
* **only** (string) 

    <br>

### UpdateFileRequest
* **file_id** (string)  `Required` 

    
* **tags** (Struct) 

    
* **reference** (FileReference) 

    
* **domain_id** (string) 

    <br>
