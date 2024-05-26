---
title: "PublicDataTable"
linkTitle: "PublicDataTable"
weight: 3
bookFlatSection: true
---
# [PublicDataTable](#PublicDataTable)
description of data table


>  **Package : spaceone.api.data_table.v1**

<br>
<br>

## PublicDataTable





**PublicDataTable Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./PublicDataTable#create) | [CreatePublicDataTableRequest](PublicDataTable#createpublicdatatablerequest) | [PublicDataTableInfo](PublicDataTable#publicdatatableinfo) |
| [**update**](./PublicDataTable#update) | [UpdatePublicDataTableRequest](PublicDataTable#updatepublicdatatablerequest) | [PublicDataTableInfo](PublicDataTable#publicdatatableinfo) |
| [**delete**](./PublicDataTable#delete) | [PublicDataTableRequest](PublicDataTable#publicdatatablerequest) | [Empty](PublicDataTable#empty) |
| [**load**](./PublicDataTable#load) | [LoadPublicDataTableRequest](PublicDataTable#loadpublicdatatablerequest) | [PublicDataTableInfo](PublicDataTable#publicdatatableinfo) |
| [**get**](./PublicDataTable#get) | [PublicDataTableRequest](PublicDataTable#publicdatatablerequest) | [PublicDataTableInfo](PublicDataTable#publicdatatableinfo) |
| [**list**](./PublicDataTable#list) | [PublicDataTableQuery](PublicDataTable#publicdatatablequery) | [PublicDataTablesInfo](PublicDataTable#publicdatatablesinfo) |



    
<br>

### create





> **POST** /data_table/v1/public-data-table/create
>






    
<br>

### update





> **POST** /data_table/v1/public-data-table/update
>






    
<br>

### delete





> **POST** /data_table/v1/public-data-table/delete
>






    
<br>

### load





> **POST** /data_table/v1/public-data-table/load
>






    
<br>

### get





> **POST** /data_table/v1/public-data-table/get
>






    
<br>

### list





> **POST** /data_table/v1/public-data-table/list
>






    


<br>
<br>

## Message



### CreatePublicDataTableRequest
* **widget_id** (string)   `Required` 

    
* **name** (string)  

    
* **source_type** (SourceType)  

    
* **options** (Struct)  

    
* **tags** (Struct)  

    <br>

### LoadPublicDataTableRequest
* **data_table_id** (string)   `Required` 

    
* **sort** (Sort)  `Repeated`   

    
* **page** (Page)  

    <br>

### PublicDataTableInfo
* **data_table_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **source_type** (SourceType)   `Required` 

    
* **options** (Struct)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **labels_info** (Struct)   `Required` 

    
* **resource_group** (ResourceGroup)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **project_id** (string)   `Required` 

    
* **public_dashboard_id** (string)   `Required` 

    
* **widget_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    <br>

### PublicDataTableQuery
* **widget_id** (string)   `Required` 

    
* **query** (Query)  

    
* **data_table_id** (string)  

    
* **name** (string)  

    
* **source_type** (SourceType)  

    <br>

### PublicDataTableRequest
* **data_table_id** (string)   `Required` 

    <br>

### PublicDataTablesInfo
* **results** (PublicDataTableInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### UpdatePublicDataTableRequest
* **data_table_id** (string)   `Required` 

    
* **name** (string)  

    
* **options** (Struct)  

    
* **tags** (Struct)  

    <br>
