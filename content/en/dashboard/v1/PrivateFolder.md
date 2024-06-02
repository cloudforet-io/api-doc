---
title: "PrivateFolder"
linkTitle: "PrivateFolder"
weight: 3
bookFlatSection: true
---
# [PrivateFolder](#PrivateFolder)
description of dashboard


>  **Package : spaceone.api.dashboard.v1**

<br>
<br>

## PrivateFolder





**PrivateFolder Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./PrivateFolder#create) | [CreatePrivateFolderRequest](PrivateFolder#createprivatefolderrequest) | [PrivateFolderInfo](PrivateFolder#privatefolderinfo) |
| [**update**](./PrivateFolder#update) | [UpdatePrivateFolderRequest](PrivateFolder#updateprivatefolderrequest) | [PrivateFolderInfo](PrivateFolder#privatefolderinfo) |
| [**delete**](./PrivateFolder#delete) | [PrivateFolderRequest](PrivateFolder#privatefolderrequest) | [Empty](PrivateFolder#empty) |
| [**get**](./PrivateFolder#get) | [PrivateFolderRequest](PrivateFolder#privatefolderrequest) | [PrivateFolderInfo](PrivateFolder#privatefolderinfo) |
| [**list**](./PrivateFolder#list) | [PrivateFolderQuery](PrivateFolder#privatefolderquery) | [PrivateFoldersInfo](PrivateFolder#privatefoldersinfo) |
| [**stat**](./PrivateFolder#stat) | [PrivateFolderStatQuery](PrivateFolder#privatefolderstatquery) | [Struct](PrivateFolder#struct) |



    
<br>

### create





> **POST** /dashboard/v1/private-folder/create
>






    
<br>

### update





> **POST** /dashboard/v1/private-folder/update
>






    
<br>

### delete





> **POST** /dashboard/v1/private-folder/delete
>






    
<br>

### get





> **POST** /dashboard/v1/private-folder/get
>






    
<br>

### list





> **POST** /dashboard/v1/private-folder/list
>






    
<br>

### stat





> **POST** /dashboard/v1/private-folder/stat
>






    


<br>
<br>

## Message



### CreatePrivateFolderRequest
* **name** (string)   `Required` 

    
* **tags** (Struct)  

    
* **dashboards** (Struct)  `Repeated`   

    <br>

### PrivateFolderInfo
* **folder_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **user_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    <br>

### PrivateFolderQuery
* **query** (Query)  

    
* **folder_id** (string)  

    
* **name** (string)  

    <br>

### PrivateFolderRequest
* **folder_id** (string)   `Required` 

    <br>

### PrivateFolderStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### PrivateFoldersInfo
* **results** (PrivateFolderInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### UpdatePrivateFolderRequest
* **folder_id** (string)   `Required` 

    
* **name** (string)  

    
* **tags** (Struct)  

    <br>
