---
title: "PrivateDataTable"
linkTitle: "PrivateDataTable"
weight: 3
bookFlatSection: true
---
# [PrivateDataTable](#PrivateDataTable)
description of data table


>  **Package : spaceone.api.dashboard.v1**

<br>
<br>

## PrivateDataTable





**PrivateDataTable Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**add**](./PrivateDataTable#add) | [AddPrivateDataTableRequest](PrivateDataTable#addprivatedatatablerequest) | [PrivateDataTableInfo](PrivateDataTable#privatedatatableinfo) |
| [**transform**](./PrivateDataTable#transform) | [TransformPrivateDataTableRequest](PrivateDataTable#transformprivatedatatablerequest) | [PrivateDataTableInfo](PrivateDataTable#privatedatatableinfo) |
| [**update**](./PrivateDataTable#update) | [UpdatePrivateDataTableRequest](PrivateDataTable#updateprivatedatatablerequest) | [PrivateDataTableInfo](PrivateDataTable#privatedatatableinfo) |
| [**delete**](./PrivateDataTable#delete) | [PrivateDataTableRequest](PrivateDataTable#privatedatatablerequest) | [Empty](PrivateDataTable#empty) |
| [**load**](./PrivateDataTable#load) | [LoadPrivateDataTableRequest](PrivateDataTable#loadprivatedatatablerequest) | [Struct](PrivateDataTable#struct) |
| [**get**](./PrivateDataTable#get) | [PrivateDataTableRequest](PrivateDataTable#privatedatatablerequest) | [PrivateDataTableInfo](PrivateDataTable#privatedatatableinfo) |
| [**list**](./PrivateDataTable#list) | [PrivateDataTableQuery](PrivateDataTable#privatedatatablequery) | [PrivateDataTablesInfo](PrivateDataTable#privatedatatablesinfo) |



    
<br>

### add





> **POST** /dashboard/v1/private-data-table/add
>






    
<br>

### transform





> **POST** /dashboard/v1/private-data-table/transform
>






    
<br>

### update





> **POST** /dashboard/v1/private-data-table/update
>






    
<br>

### delete





> **POST** /dashboard/v1/private-data-table/delete
>






    
<br>

### load





> **POST** /dashboard/v1/private-data-table/load
>






    
<br>

### get





> **POST** /dashboard/v1/private-data-table/get
>






    
<br>

### list





> **POST** /dashboard/v1/private-data-table/list
>






    


<br>
<br>

## Message



### AddPrivateDataTableRequest
* **widget_id** (string)   `Required` 

    
* **source_type** (SourceType)   `Required` 

    
* **options** (AddOptions)   `Required` 

    
* **name** (string)  

    
* **vars** (Struct)  

    
* **tags** (Struct)  

    <br>

### LoadPrivateDataTableRequest
* **data_table_id** (string)   `Required` 

    
* **granularity** (Granularity)   `Required` 

    
* **start** (string)  

    
* **end** (string)  

    
* **sort** (Sort)  `Repeated`   

    
* **page** (Page)  

    
* **vars** (Struct)  

    <br>

### PrivateDataTableInfo
* **data_table_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **state** (State)   `Required` 

    
* **data_type** (DataType)   `Required` 

    
* **source_type** (SourceType)   `Required` 

    
* **operator** (Operator)   `Required` 

    
* **options** (Struct)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **labels_info** (Struct)   `Required` 

    
* **data_info** (Struct)   `Required` 

    
* **sort_keys** (string)  `Repeated`    `Required` 

    
* **error_message** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **user_id** (string)   `Required` 

    
* **dashboard_id** (string)   `Required` 

    
* **widget_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    <br>

### PrivateDataTableQuery
* **widget_id** (string)   `Required` 

    
* **query** (Query)  

    
* **data_table_id** (string)  

    
* **name** (string)  

    
* **data_type** (DataType)  

    
* **source_type** (SourceType)  

    
* **operator** (Operator)  

    <br>

### PrivateDataTableRequest
* **data_table_id** (string)   `Required` 

    <br>

### PrivateDataTablesInfo
* **results** (PrivateDataTableInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### TransformPrivateDataTableRequest
* **widget_id** (string)   `Required` 

    
* **operator** (Operator)   `Required` 

    
* **options** (TransformOptions)   `Required` 

    
* **name** (string)  

    
* **vars** (Struct)  

    
* **tags** (Struct)  

    <br>

### UpdatePrivateDataTableRequest
* **data_table_id** (string)   `Required` 

    
* **name** (string)  

    
* **options** (Struct)  

    
* **vars** (Struct)  

    
* **tags** (Struct)  

    <br>
