---
title: "PublicDataTable"
linkTitle: "PublicDataTable"
weight: 3
bookFlatSection: true
---
# [PublicDataTable](#PublicDataTable)
description of data table


>  **Package : spaceone.api.dashboard.v1**

<br>
<br>

## PublicDataTable





**PublicDataTable Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**add**](./PublicDataTable#add) | [AddPublicDataTableRequest](PublicDataTable#addpublicdatatablerequest) | [PublicDataTableInfo](PublicDataTable#publicdatatableinfo) |
| [**transform**](./PublicDataTable#transform) | [TransformPublicDataTableRequest](PublicDataTable#transformpublicdatatablerequest) | [PublicDataTableInfo](PublicDataTable#publicdatatableinfo) |
| [**update**](./PublicDataTable#update) | [UpdatePublicDataTableRequest](PublicDataTable#updatepublicdatatablerequest) | [PublicDataTableInfo](PublicDataTable#publicdatatableinfo) |
| [**delete**](./PublicDataTable#delete) | [PublicDataTableRequest](PublicDataTable#publicdatatablerequest) | [Empty](PublicDataTable#empty) |
| [**load**](./PublicDataTable#load) | [LoadPublicDataTableRequest](PublicDataTable#loadpublicdatatablerequest) | [PublicDataTableInfo](PublicDataTable#publicdatatableinfo) |
| [**get**](./PublicDataTable#get) | [PublicDataTableRequest](PublicDataTable#publicdatatablerequest) | [PublicDataTableInfo](PublicDataTable#publicdatatableinfo) |
| [**list**](./PublicDataTable#list) | [PublicDataTableQuery](PublicDataTable#publicdatatablequery) | [PublicDataTablesInfo](PublicDataTable#publicdatatablesinfo) |



    
<br>

### add





> **POST** /data_table/v1/public-data-table/add
>






    
<br>

### transform





> **POST** /data_table/v1/public-data-table/transform
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



### AddOptions
* **ASSET** (AssetSource)   `Required` 

    
* **COST** (CostSource)   `Required` 

    
* **group_by** (string)  `Repeated`   

    
* **data_name** (string)  

    
* **date_format** (DateFormat)  

    
* **additional_labels** (Struct)  

    
* **time_diff** (TimeDiff)  

    <br>

### AddPublicDataTableRequest
* **widget_id** (string)   `Required` 

    
* **source_type** (SourceType)   `Required` 

    
* **options** (AddOptions)   `Required` 

    
* **name** (string)  

    
* **tags** (Struct)  

    <br>

### AggregateOperator
* **data_table_id** (string)   `Required` 

    
* **operator** (AggregateType)   `Required` 

    
* **group_by** (string)  

    <br>

### AssetSource
* **metric_id** (string)   `Required` 

    <br>

### ConcatOperator
* **data_tables** (string)  `Repeated`    `Required` 

    <br>

### CostSource
* **data_source_id** (string)   `Required` 

    
* **data_key** (string)   `Required` 

    <br>

### EvaluateOperator
* **data_table_id** (string)   `Required` 

    
* **expressions** (string)  `Repeated`    `Required` 

    <br>

### JoinOperator
* **data_tables** (string)  `Repeated`    `Required` 

    
* **on** (JoinType)  

    <br>

### LoadPublicDataTableRequest
* **data_table_id** (string)   `Required` 

    
* **granularity** (Granularity)   `Required` 

    
* **start** (string)  

    
* **end** (string)  

    
* **sort** (Sort)  `Repeated`   

    
* **page** (Page)  

    <br>

### PublicDataTableInfo
* **data_table_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **data_type** (DataType)   `Required` 

    
* **source_type** (SourceType)   `Required` 

    
* **operator** (Operator)   `Required` 

    
* **options** (Struct)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **labels_info** (Struct)   `Required` 

    
* **data_info** (Struct)   `Required` 

    
* **resource_group** (ResourceGroup)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **project_id** (string)   `Required` 

    
* **dashboard_id** (string)   `Required` 

    
* **widget_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    <br>

### PublicDataTableQuery
* **widget_id** (string)   `Required` 

    
* **query** (Query)  

    
* **data_table_id** (string)  

    
* **name** (string)  

    
* **data_type** (DataType)  

    
* **source_type** (SourceType)  

    
* **operator** (Operator)  

    <br>

### PublicDataTableRequest
* **data_table_id** (string)   `Required` 

    <br>

### PublicDataTablesInfo
* **results** (PublicDataTableInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### TimeDiff
* **years** (int32)   `Required` 

    
* **months** (int32)   `Required` 

    
* **days** (int32)   `Required` 

    <br>

### TransformOptions
* **JOIN** (JoinOperator)   `Required` 

    
* **CONCAT** (ConcatOperator)   `Required` 

    
* **AGGREGATE** (AggregateOperator)   `Required` 

    
* **WHERE** (WhereOperator)   `Required` 

    
* **EVALUATE** (EvaluateOperator)   `Required` 

    <br>

### TransformPublicDataTableRequest
* **widget_id** (string)   `Required` 

    
* **operator** (Operator)   `Required` 

    
* **options** (TransformOptions)   `Required` 

    
* **name** (string)  

    
* **tags** (Struct)  

    <br>

### UpdatePublicDataTableRequest
* **data_table_id** (string)   `Required` 

    
* **name** (string)  

    
* **options** (Struct)  

    
* **tags** (Struct)  

    <br>

### WhereOperator
* **data_table_id** (string)   `Required` 

    
* **conditions** (string)  `Repeated`    `Required` 

    <br>
