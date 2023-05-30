---
title: "Schema"
linkTitle: "Schema"
weight: 3
bookFlatSection: true
---
# [Schema](#Schema)



>  **Package : spaceone.api.repository.v2**

<br>
<br>

## Schema





**Schema Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Schema#create) | [CreateSchemaRequest](Schema#createschemarequest) | [SchemaInfo](Schema#schemainfo) |
| [**update**](./Schema#update) | [UpdateSchemaRequest](Schema#updateschemarequest) | [SchemaInfo](Schema#schemainfo) |
| [**sync**](./Schema#sync) | [SchemaRequest](Schema#schemarequest) | [SchemaInfo](Schema#schemainfo) |
| [**delete**](./Schema#delete) | [SchemaRequest](Schema#schemarequest) | [Empty](Schema#empty) |
| [**get**](./Schema#get) | [GetSchemaRequest](Schema#getschemarequest) | [SchemaInfo](Schema#schemainfo) |
| [**list**](./Schema#list) | [SchemaQuery](Schema#schemaquery) | [SchemasInfo](Schema#schemasinfo) |
| [**stat**](./Schema#stat) | [SchemaStatQuery](Schema#schemastatquery) | [Struct](Schema#struct) |



    
<br>

### create





> **POST** /repository/v2/schema/create
>






    
<br>

### update





> **POST** /repository/v2/schema/update
>






    
<br>

### sync





> **POST** /repository/v2/schema/sync
>






    
<br>

### delete





> **POST** /repository/v2/schema/delete
>






    
<br>

### get





> **POST** /repository/v2/schema/get
>






    
<br>

### list





> **POST** /repository/v2/schema/list
>






    
<br>

### stat





> **POST** /repository/v2/schema/stat
>






    


<br>
<br>

## Message



### CreateSchemaRequest
* **schema_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **schema** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **sync_mode** (SyncMode)  

    
* **sync_options** (SyncOptions)  

    
* **labels** (ListValue)  

    
* **tags** (Struct)  

    <br>

### GetSchemaRequest
* **schema_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **only** (string)  `Repeated`   

    <br>

### SchemaInfo
* **schema_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **sync_mode** (SyncMode)   `Required` 

    
* **sync_options** (SyncOptions)   `Required` 

    
* **schema** (Struct)   `Required` 

    
* **labels** (ListValue)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **remote_repository** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    <br>

### SchemaQuery
* **domain_id** (string)   `Required` 

    
* **query** (Query)  

    
* **schema_id** (string)  

    
* **name** (string)  

    
* **sync_mode** (SyncMode)  

    
* **remote_repository_name** (string)  

    <br>

### SchemaRequest
* **schema_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### SchemaStatQuery
* **query** (StatisticsQuery)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### SchemasInfo
* **results** (SchemaInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### UpdateSchemaRequest
* **schema_id** (string)   `Required` 

    
* **schema** (Struct)   `Required` 

  *is_required: flase*

    
* **domain_id** (string)   `Required` 

    
* **name** (string)  

    
* **sync_mode** (SyncMode)  

    
* **sync_options** (SyncOptions)  

    
* **labels** (ListValue)  

    
* **tags** (Struct)  

    <br>
