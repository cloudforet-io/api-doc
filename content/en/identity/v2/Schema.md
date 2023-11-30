---
title: "Schema"
linkTitle: "Schema"
weight: 3
bookFlatSection: true
---
# [Schema](#Schema)



>  **Package : spaceone.api.identity.v2**

<br>
<br>

## Schema





**Schema Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Schema#create) | [CreateSchemaRequest](Schema#createschemarequest) | [SchemaInfo](Schema#schemainfo) |
| [**update**](./Schema#update) | [UpdateSchemaRequest](Schema#updateschemarequest) | [SchemaInfo](Schema#schemainfo) |
| [**delete**](./Schema#delete) | [SchemaRequest](Schema#schemarequest) | [Empty](Schema#empty) |
| [**get**](./Schema#get) | [SchemaRequest](Schema#schemarequest) | [SchemaInfo](Schema#schemainfo) |
| [**list**](./Schema#list) | [SchemaSearchQuery](Schema#schemasearchquery) | [SchemasInfo](Schema#schemasinfo) |
| [**stat**](./Schema#stat) | [SchemaStatQuery](Schema#schemastatquery) | [Struct](Schema#struct) |



    
<br>

### create





> **POST** /identity/v2/schema/create
>






    
<br>

### update





> **POST** /identity/v2/schema/update
>






    
<br>

### delete





> **POST** /identity/v2/schema/delete
>






    
<br>

### get





> **POST** /identity/v2/schema/get
>






    
<br>

### list





> **POST** /identity/v2/schema/list
>






    
<br>

### stat





> **POST** /identity/v2/schema/stat
>






    


<br>
<br>

## Message



### CreateSchemaRequest
* **schema_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **schema_type** (SchemaType)   `Required` 

    
* **schema** (Struct)   `Required` 

    
* **provider** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **related_schema_id** (string)  

    
* **options** (Struct)  

    
* **tags** (Struct)  

    <br>

### SchemaInfo
* **schema_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **schema_type** (SchemaType)   `Required` 

    
* **schema** (Struct)   `Required` 

    
* **provider** (string)   `Required` 

    
* **related_schema_id** (string)   `Required` 

    
* **options** (Struct)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **is_managed** (bool)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    <br>

### SchemaRequest
* **schema_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### SchemaSearchQuery
* **domain_id** (string)   `Required` 

    
* **query** (Query)  

    
* **schema_id** (string)  

    
* **name** (string)  

    
* **schema_type** (SchemaType)  

    
* **provider** (string)  

    
* **related_schema_id** (string)  

    
* **is_managed** (bool)  

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

    
* **domain_id** (string)   `Required` 

    
* **name** (string)  

    
* **schema** (Struct)  

    
* **options** (Struct)  

    
* **tags** (Struct)  

    <br>
