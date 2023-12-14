---
title: "PublicFile"
linkTitle: "PublicFile"
weight: 3
bookFlatSection: true
---
# [PublicFile](#PublicFile)



>  **Package : spaceone.api.file_manager.v1**

<br>
<br>

## PublicFile





**PublicFile Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**add**](./PublicFile#add) | [CreatePublicFileRequest](PublicFile#createpublicfilerequest) | [PublicFileInfo](PublicFile#publicfileinfo) |
| [**update**](./PublicFile#update) | [UpdatePublicFileRequest](PublicFile#updatepublicfilerequest) | [PublicFileInfo](PublicFile#publicfileinfo) |
| [**delete**](./PublicFile#delete) | [PublicFileRequest](PublicFile#publicfilerequest) | [Empty](PublicFile#empty) |
| [**get_download_url**](./PublicFile#get_download_url) | [PublicFileRequest](PublicFile#publicfilerequest) | [PublicFileInfo](PublicFile#publicfileinfo) |
| [**get**](./PublicFile#get) | [PublicFileRequest](PublicFile#publicfilerequest) | [PublicFileInfo](PublicFile#publicfileinfo) |
| [**list**](./PublicFile#list) | [PublicFileSearchQuery](PublicFile#publicfilesearchquery) | [PublicFilesInfo](PublicFile#publicfilesinfo) |
| [**stat**](./PublicFile#stat) | [PublicFileStatQuery](PublicFile#publicfilestatquery) | [Struct](PublicFile#struct) |



    
<br>

### add





> **POST** /file-manager/v1/public-file/add
>






    
<br>

### update





> **POST** /file-manager/v1/public-file/update
>






    
<br>

### delete





> **POST** /file-manager/v1/public-file/delete
>






    
<br>

### get_download_url





> **POST** /file-manager/v1/public-file/get-download-url
>






    
<br>

### get





> **POST** /file-manager/v1/public-file/get
>






    
<br>

### list





> **POST** /file-manager/v1/public-file/list
>






    
<br>

### stat





> **POST** /file-manager/v1/public-file/stat
>






    


<br>
<br>

## Message



### CreatePublicFileRequest
* **name** (string)   `Required` 

    
* **tags** (Struct)  

    
* **reference** (PublicFileReference)  

    <br>

### PublicFileInfo
* **public_file_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **state** (PublicFileState)   `Required` 

    
* **file_type** (string)   `Required` 

    
* **upload_url** (string)   `Required` 

    
* **upload_options** (Struct)   `Required` 

    
* **download_url** (string)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **reference** (PublicFileReference)   `Required` 

    
* **created_at** (string)   `Required` 

    <br>

### PublicFileReference
* **resource_type** (string)   `Required` 

    
* **resource_id** (string)   `Required` 

    <br>

### PublicFileRequest
* **public_file_id** (string)   `Required` 

    <br>

### PublicFileSearchQuery
* **query** (Query)  

    
* **public_file_id** (string)  

    
* **name** (string)  

    
* **state** (PublicFileState)  

    
* **file_type** (string)  

    
* **resource_type** (string)  

    
* **resource_id** (string)  

    <br>

### PublicFileStatQuery
* **query** (StatisticsQuery)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### PublicFilesInfo
* **results** (PublicFileInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### UpdatePublicFileRequest
* **public_file_id** (string)   `Required` 

    
* **tags** (Struct)  

    
* **reference** (PublicFileReference)  

    <br>
