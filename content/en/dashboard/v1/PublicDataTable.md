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
| [**load**](./PublicDataTable#load) | [LoadPublicDataTableRequest](PublicDataTable#loadpublicdatatablerequest) | [Struct](PublicDataTable#struct) |
| [**get**](./PublicDataTable#get) | [PublicDataTableRequest](PublicDataTable#publicdatatablerequest) | [PublicDataTableInfo](PublicDataTable#publicdatatableinfo) |
| [**list**](./PublicDataTable#list) | [PublicDataTableQuery](PublicDataTable#publicdatatablequery) | [PublicDataTablesInfo](PublicDataTable#publicdatatablesinfo) |



    
<br>

### add





> **POST** /dashboard/v1/public-data-table/add
>






    
<br>

### transform





> **POST** /dashboard/v1/public-data-table/transform
>






    
<br>

### update





> **POST** /dashboard/v1/public-data-table/update
>






    
<br>

### delete





> **POST** /dashboard/v1/public-data-table/delete
>






    
<br>

### load





> **POST** /dashboard/v1/public-data-table/load
>






    
<br>

### get





> **POST** /dashboard/v1/public-data-table/get
>






    
<br>

### list





> **POST** /dashboard/v1/public-data-table/list
>






    


<br>
<br>

## Message



### AddLabelsOperator
* **data_table_id** (string)   `Required` 

    
* **labels** (Struct)   `Required` 

    <br>

### AddOptions
* **ASSET** (AssetSource)   `Required` 

    
* **COST** (CostSource)   `Required` 

    
* **data_name** (string)   `Required` 

    
* **data_unit** (string)  

    
* **group_by** (ListValue)  

    
* **filter** (Filter)  `Repeated`   

    
* **filter_or** (Filter)  `Repeated`   

    
* **timediff** (TimeDiff)  

    <br>

### AddPublicDataTableRequest
* **widget_id** (string)   `Required` 

    
* **source_type** (SourceType)   `Required` 

    
* **options** (AddOptions)   `Required` 

    
* **name** (string)  

    
* **vars** (Struct)  

    
* **tags** (Struct)  

    <br>

### AggregateOperator
* **data_table_id** (string)   `Required` 

    
* **function** (Struct)   `Required` 

    
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

    
* **plugin_id** (string)   `Required` 

    
* **data_key** (string)   `Required` 

    <br>

### EvaluateOperator
* **data_table_id** (string)   `Required` 

    
* **expressions** (ListValue)   `Required` 

    <br>

### JoinOperator
* **data_tables** (string)  `Repeated`    `Required` 

    
* **right_keys** (string)  `Repeated`    `Required` 

    
* **left_keys** (string)  `Repeated`    `Required` 

    
* **how** (JoinType)  

    <br>

### LoadPublicDataTableRequest
* **data_table_id** (string)   `Required` 

    
* **granularity** (Granularity)   `Required` 

    
* **start** (string)  

    
* **end** (string)  

    
* **sort** (Sort)  `Repeated`   

    
* **page** (Page)  

    
* **vars** (Struct)  

    <br>

### PivotFieldOptions
* **labels** (string)  `Repeated`    `Required` 

    
* **column** (string)   `Required` 

    
* **data** (string)   `Required` 

    <br>

### PivotOperator
* **data_table_id** (string)   `Required` 

    
* **fields** (PivotFieldOptions)   `Required` 

    
* **function** (string)  

    
* **select** (string)  `Repeated`   

    
* **order_by** (PivotOrderBy)  

    
* **limit** (int32)  

    <br>

### PivotOrderBy
* **type** (string)   `Required` 

    
* **desc** (bool)   `Required` 

    <br>

### PublicDataTableInfo
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

    
* **cache_key** (string)   `Required` 

    
* **error_message** (string)   `Required` 

    
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

### QueryOperator
* **data_table_id** (string)   `Required` 

    
* **conditions** (string)  `Repeated`    `Required` 

    <br>

### TimeDiff
* **years** (int32)   `Required` 

    
* **months** (int32)   `Required` 

    
* **data_name** (string)   `Required` 

    <br>

### TransformOptions
* **JOIN** (JoinOperator)   `Required` 

    
* **CONCAT** (ConcatOperator)   `Required` 

    
* **AGGREGATE** (AggregateOperator)   `Required` 

    
* **QUERY** (QueryOperator)   `Required` 

    
* **EVAL** (EvaluateOperator)   `Required` 

    
* **PIVOT** (PivotOperator)   `Required` 

    
* **ADD_LABELS** (AddLabelsOperator)   `Required` 

    
* **VALUE_MAPPING** (ValueMappingOperator)   `Required` 

    <br>

### TransformPublicDataTableRequest
* **widget_id** (string)   `Required` 

    
* **operator** (Operator)   `Required` 

    
* **options** (TransformOptions)   `Required` 

    
* **name** (string)  

    
* **vars** (Struct)  

    
* **tags** (Struct)  

    <br>

### UpdatePublicDataTableRequest
* **data_table_id** (string)   `Required` 

    
* **name** (string)  

    
* **options** (Struct)  

    
* **vars** (Struct)  

    
* **tags** (Struct)  

    <br>

### ValueMappingCases
* **key** (string)   `Required` 

    
* **operator** (ValueMappingOperator)   `Required` 

    
* **match** (string)   `Required` 

    
* **value** (string)   `Required` 

    <br>

### ValueMappingOperator
* **data_table_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **field_type** (FieldType)   `Required` 

    
* **cases** (ValueMappingCases)  `Repeated`    `Required` 

    
* **else** (string)   `Required` 

    
* **condition** (string)   `Required` 

    <br>
