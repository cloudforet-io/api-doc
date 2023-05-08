---
title: "Schema"
linkTitle: "Schema"
weight: 3
bookFlatSection: true
---
# [Schema](#Schema)
desc: A Schema is a data structure used in all domains. For example, data forms of Google OAuth2 credentials or AWS access keys can be a Schema resource.


>  **Package : spaceone.api.repository.v1**

<br>
<br>

## Schema


**Schema Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Schema#create) | [CreateSchemaRequest](Schema#createschemarequest) | [SchemaInfo](./Schema#schemainfo) |
| [**update**](./Schema#update) | [UpdateSchemaRequest](Schema#updateschemarequest) | [SchemaInfo](./Schema#schemainfo) |
| [**delete**](./Schema#delete) | [SchemaRequest](Schema#schemarequest) | [Empty](./Schema#empty) |
| [**get**](./Schema#get) | [GetRepositorySchemaRequest](Schema#getrepositoryschemarequest) | [SchemaInfo](./Schema#schemainfo) |
| [**list**](./Schema#list) | [SchemaQuery](Schema#schemaquery) | [SchemasInfo](./Schema#schemasinfo) |
| [**stat**](./Schema#stat) | [SchemaStatQuery](Schema#schemastatquery) | [Struct](./Schema#struct) |



    
<br>

### create

> **POST** /repository/v1/schema/create
>




 {{< tabs " create " >}}




{{< /tabs >}}

    
<br>

### update

> **POST** /repository/v1/schema/update
>




 {{< tabs " update " >}}




{{< /tabs >}}

    
<br>

### delete

> **POST** /repository/v1/schema/delete
>




 {{< tabs " delete " >}}




{{< /tabs >}}

    
<br>

### get

> **POST** /repository/v1/schema/get
>




 {{< tabs " get " >}}




{{< /tabs >}}

    
<br>

### list

> **POST** /repository/v1/schema/list
>




 {{< tabs " list " >}}




{{< /tabs >}}

    
<br>

### stat

> **POST** /repository/v1/schema/stat
>




 {{< tabs " stat " >}}




{{< /tabs >}}

    


<br>
<br>

## Message



### CreateSchemaRequest
* **name** (string)  `Required` 

  *is_required: true*

    
* **service_type** (string)  `Required` 

  *is_required: true*

    
* **schema_id** (string)  `Required` 

  *is_required: true*

    
* **schema** (Struct)  `Required` 

  *is_required: true*

    
* **labels** (ListValue)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **project_id** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### GetRepositorySchemaRequest
* **name** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **repository_id** (string)  `Required` 

  *is_required: false*

    
* **only** (string)  `Required` 

  *is_required: false*

    
* **schema_id** (string)  `Required` 

  *is_required: false*

    <br>

### SchemaInfo
* **name** (string)  `Required` 

    
* **service_type** (string)  `Required` 

    
* **schema_id** (string)  `Required` 

    
* **schema** (Struct)  `Required` 

    
* **labels** (ListValue)  `Required` 

    
* **tags** (Struct)  `Required` 

    
* **repository_info** (RepositoryInfo)  `Required` 

    
* **project_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    
* **updated_at** (string)  `Required` 

    <br>

### SchemaQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **service_type** (string)  `Required` 

  *is_required: false*

    
* **project_id** (string)  `Required` 

  *is_required: true*

    
* **repository_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **schema_id** (string)  `Required` 

  *is_required: false*

    
* **state** (State)  `Required` 

  *is_required: false*

    <br>

### SchemaRequest
* **name** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **schema_id** (string)  `Required` 

  *is_required: false*

    <br>

### SchemaStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **repository_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### SchemasInfo
* **results** (SchemaInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### UpdateSchemaRequest
* **name** (string)  `Required` 

  *is_required: true*

    
* **schema** (Struct)  `Required` 

  *is_required: false*

    
* **labels** (ListValue)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>
