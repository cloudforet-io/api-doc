---
title: "PublicFolder"
linkTitle: "PublicFolder"
weight: 3
bookFlatSection: true
---
# [PublicFolder](#PublicFolder)
description of dashboard


>  **Package : spaceone.api.dashboard.v1**

<br>
<br>

## PublicFolder





**PublicFolder Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./PublicFolder#create) | [CreatePublicFolderRequest](PublicFolder#createpublicfolderrequest) | [PublicFolderInfo](PublicFolder#publicfolderinfo) |
| [**update**](./PublicFolder#update) | [UpdatePublicFolderRequest](PublicFolder#updatepublicfolderrequest) | [PublicFolderInfo](PublicFolder#publicfolderinfo) |
| [**share**](./PublicFolder#share) | [SharePublicFolderRequest](PublicFolder#sharepublicfolderrequest) | [PublicFolderInfo](PublicFolder#publicfolderinfo) |
| [**unshare**](./PublicFolder#unshare) | [PublicFolderRequest](PublicFolder#publicfolderrequest) | [PublicFolderInfo](PublicFolder#publicfolderinfo) |
| [**delete**](./PublicFolder#delete) | [PublicFolderRequest](PublicFolder#publicfolderrequest) | [Empty](PublicFolder#empty) |
| [**get**](./PublicFolder#get) | [PublicFolderRequest](PublicFolder#publicfolderrequest) | [PublicFolderInfo](PublicFolder#publicfolderinfo) |
| [**list**](./PublicFolder#list) | [PublicFolderQuery](PublicFolder#publicfolderquery) | [PublicFoldersInfo](PublicFolder#publicfoldersinfo) |
| [**stat**](./PublicFolder#stat) | [PublicFolderStatQuery](PublicFolder#publicfolderstatquery) | [Struct](PublicFolder#struct) |



    
<br>

### create





> **POST** /dashboard/v1/public-folder/create
>






    
<br>

### update





> **POST** /dashboard/v1/public-folder/update
>






    
<br>

### share





> **POST** /dashboard/v1/public-folder/share
>






    
<br>

### unshare





> **POST** /dashboard/v1/public-folder/unshare
>






    
<br>

### delete





> **POST** /dashboard/v1/public-folder/delete
>






    
<br>

### get





> **POST** /dashboard/v1/public-folder/get
>






    
<br>

### list





> **POST** /dashboard/v1/public-folder/list
>






    
<br>

### stat





> **POST** /dashboard/v1/public-folder/stat
>






    


<br>
<br>

## Message



### CreatePublicFolderRequest
* **name** (string)   `Required` 

    
* **tags** (Struct)  

    
* **dashboards** (Struct)  `Repeated`   

    
* **resource_group** (ResourceGroup)  

    
* **workspace_id** (string)  

    
* **project_id** (string)  

    <br>

### PublicFolderInfo
* **folder_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **shared** (bool)   `Required` 

    
* **scope** (FolderScope)   `Required` 

    
* **resource_group** (ResourceGroup)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **project_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    <br>

### PublicFolderQuery
* **query** (Query)  

    
* **folder_id** (string)  

    
* **name** (string)  

    
* **shared** (bool)  

    
* **scope** (FolderScope)  

    
* **workspace_id** (string)  

    
* **project_id** (string)  

    <br>

### PublicFolderRequest
* **folder_id** (string)   `Required` 

    <br>

### PublicFolderStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### PublicFoldersInfo
* **results** (PublicFolderInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### SharePublicFolderRequest
* **dashboard_id** (string)   `Required` 

    
* **scope** (FolderScope)  

    <br>

### UpdatePublicFolderRequest
* **folder_id** (string)   `Required` 

    
* **name** (string)  

    
* **tags** (Struct)  

    <br>
