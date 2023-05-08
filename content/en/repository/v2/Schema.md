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
| [**create**](./Schema#create) | [CreateSchemaRequest](Schema#createschemarequest) | [SchemaInfo](./Schema#schemainfo) |
| [**update**](./Schema#update) | [UpdateSchemaRequest](Schema#updateschemarequest) | [SchemaInfo](./Schema#schemainfo) |
| [**sync**](./Schema#sync) | [SchemaRequest](Schema#schemarequest) | [SchemaInfo](./Schema#schemainfo) |
| [**delete**](./Schema#delete) | [SchemaRequest](Schema#schemarequest) | [Empty](./Schema#empty) |
| [**get**](./Schema#get) | [GetSchemaRequest](Schema#getschemarequest) | [SchemaInfo](./Schema#schemainfo) |
| [**list**](./Schema#list) | [SchemaQuery](Schema#schemaquery) | [SchemasInfo](./Schema#schemasinfo) |
| [**stat**](./Schema#stat) | [SchemaStatQuery](Schema#schemastatquery) | [Struct](./Schema#struct) |



    
<br>

### create

> **POST** /repository/v2/schema/create
>




 {{< tabs " create " >}}




{{< /tabs >}}

    
<br>

### update

> **POST** /repository/v2/schema/update
>




 {{< tabs " update " >}}




{{< /tabs >}}

    
<br>

### sync

> **POST** /repository/v2/schema/sync
>




 {{< tabs " sync " >}}




{{< /tabs >}}

    
<br>

### delete

> **POST** /repository/v2/schema/delete
>




 {{< tabs " delete " >}}




{{< /tabs >}}

    
<br>

### get

> **POST** /repository/v2/schema/get
>




 {{< tabs " get " >}}




{{< /tabs >}}

    
<br>

### list

> **POST** /repository/v2/schema/list
>




 {{< tabs " list " >}}




{{< /tabs >}}

    
<br>

### stat

> **POST** /repository/v2/schema/stat
>




 {{< tabs " stat " >}}




{{< /tabs >}}

    


<br>
<br>

## Message



### CreateSchemaRequest
* **schema_id** (string)  `Required` 

  *is_required: true*

    
* **name** (string)  `Required` 

  *is_required: true*

    
* **sync_mode** (SyncMode)  `Required` 

  *is_required: false*

    
* **sync_options** (SyncOptions)  `Required` 

  *is_required: false*

    
* **schema** (Struct)  `Required` 

  *is_required: true*

    
* **labels** (ListValue)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### GetSchemaRequest
* **schema_id** (string)  `Required` 

  *is_required: true*

    
* **only** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### SchemaInfo
* **schema_id** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **sync_mode** (SyncMode)  `Required` 

    
* **sync_options** (SyncOptions)  `Required` 

    
* **schema** (Struct)  `Required` 

    
* **labels** (ListValue)  `Required` 

    
* **tags** (Struct)  `Required` 

    
* **remote_repository** (Struct)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    <br>

### SchemaQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **schema_id** (string)  `Required` 

  *is_required: false*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **sync_mode** (SyncMode)  `Required` 

  *is_required: false*

    
* **remote_repository_name** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### SchemaRequest
* **schema_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### SchemaStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### SchemasInfo
* **results** (SchemaInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### UpdateSchemaRequest
* **schema_id** (string)  `Required` 

  *is_required: true*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **sync_mode** (SyncMode)  `Required` 

  *is_required: false*

    
* **sync_options** (SyncOptions)  `Required` 

  *is_required: false*

    
* **schema** (Struct)  `Required` 

  *is_required: flase*

    
* **labels** (ListValue)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>
