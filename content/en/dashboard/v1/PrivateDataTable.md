---
title: "PrivateDataTable"
linkTitle: "PrivateDataTable"
weight: 3
bookFlatSection: true
---
# [PrivateDataTable](#PrivateDataTable)
description of data table


>  **Package : spaceone.api.data_table.v1**

<br>
<br>

## PrivateDataTable





**PrivateDataTable Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./PrivateDataTable#create) | [CreatePrivateDataTableRequest](PrivateDataTable#createprivatedatatablerequest) | [PrivateDataTableInfo](PrivateDataTable#privatedatatableinfo) |
| [**update**](./PrivateDataTable#update) | [UpdatePrivateDataTableRequest](PrivateDataTable#updateprivatedatatablerequest) | [PrivateDataTableInfo](PrivateDataTable#privatedatatableinfo) |
| [**delete**](./PrivateDataTable#delete) | [PrivateDataTableRequest](PrivateDataTable#privatedatatablerequest) | [Empty](PrivateDataTable#empty) |
| [**load**](./PrivateDataTable#load) | [LoadPrivateDataTableRequest](PrivateDataTable#loadprivatedatatablerequest) | [PrivateDataTableInfo](PrivateDataTable#privatedatatableinfo) |
| [**get**](./PrivateDataTable#get) | [PrivateDataTableRequest](PrivateDataTable#privatedatatablerequest) | [PrivateDataTableInfo](PrivateDataTable#privatedatatableinfo) |
| [**list**](./PrivateDataTable#list) | [PrivateDataTableQuery](PrivateDataTable#privatedatatablequery) | [PrivateDataTablesInfo](PrivateDataTable#privatedatatablesinfo) |



    
<br>

### create





> **POST** /data_table/v1/private-data-table/create
>






    
<br>

### update





> **POST** /data_table/v1/private-data-table/update
>






    
<br>

### delete





> **POST** /data_table/v1/private-data-table/delete
>






    
<br>

### load





> **POST** /data_table/v1/private-data-table/load
>






    
<br>

### get





> **POST** /data_table/v1/private-data-table/get
>






    
<br>

### list





> **POST** /data_table/v1/private-data-table/list
>






    


<br>
<br>

## Message



### CreatePrivateDataTableRequest
* **widget_id** (string)   `Required` 

    
* **name** (string)  

    
* **source_type** (SourceType)  

    
* **options** (Struct)  

    
* **tags** (Struct)  

    <br>

### LoadPrivateDataTableRequest
* **data_table_id** (string)   `Required` 

    
* **sort** (Sort)  `Repeated`   

    
* **page** (Page)  

    <br>

### PrivateDataTableInfo
* **data_table_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **source_type** (SourceType)   `Required` 

    
* **options** (Struct)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **labels_info** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **user_id** (string)   `Required` 

    
* **private_dashboard_id** (string)   `Required` 

    
* **widget_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    <br>

### PrivateDataTableQuery
* **widget_id** (string)   `Required` 

    
* **query** (Query)  

    
* **data_table_id** (string)  

    
* **name** (string)  

    
* **source_type** (SourceType)  

    <br>

### PrivateDataTableRequest
* **data_table_id** (string)   `Required` 

    <br>

### PrivateDataTablesInfo
* **results** (PrivateDataTableInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### UpdatePrivateDataTableRequest
* **data_table_id** (string)   `Required` 

    
* **name** (string)  

    
* **options** (Struct)  

    
* **tags** (Struct)  

    <br>
