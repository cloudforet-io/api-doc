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
| [**update**](./File#update) | [UpdateFileRequest](File#updatefilerequest) | [FileInfo](File#fileinfo) |
| [**delete**](./File#delete) | [FileRequest](File#filerequest) | [Empty](File#empty) |
| [**get**](./File#get) | [FileRequest](File#filerequest) | [FileInfo](File#fileinfo) |
| [**list**](./File#list) | [FileSearchQuery](File#filesearchquery) | [FilesInfo](File#filesinfo) |
| [**stat**](./File#stat) | [FileStatQuery](File#filestatquery) | [Struct](File#struct) |



    
<br>

### update





> **POST** /file-manager/v1/file/update
>






    
<br>

### delete





> **POST** /file-manager/v1/file/delete
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
* **name** (string)   `Required` 

    
* **resource_group** (ResourceGroup)   `Required` 

    
* **tags** (Struct)  

    
* **reference** (FileReference)  

    
* **domain_id** (string)  

    
* **workspace_id** (string)  

    
* **project_id** (string)  

    <br>

### FileInfo
* **file_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **download_url** (string)   `Required` 

    
* **reference** (FileReference)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **resource_group** (ResourceGroup)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **project_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    <br>

### FileReference
* **resource_type** (string)   `Required` 

    
* **resource_id** (string)   `Required` 

    <br>

### FileRequest
* **file_id** (string)   `Required` 

    <br>

### FileSearchQuery
* **query** (Query)  

    
* **file_id** (string)  

    
* **name** (string)  

    
* **resource_type** (string)  

    
* **resource_id** (string)  

    
* **domain_id** (string)  

    
* **workspace_id** (string)  

    
* **project_id** (string)  

    <br>

### FileStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### FilesInfo
* **results** (FileInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### UpdateFileRequest
* **file_id** (string)   `Required` 

    
* **tags** (Struct)  

    
* **reference** (FileReference)  

    <br>
