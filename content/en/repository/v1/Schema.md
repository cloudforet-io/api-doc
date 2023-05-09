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

desc: Creates a new Schema. You must specify the parameters: `service_type`, `name`, and `schema`(data structure). With the parameter `domain_id`, you can choose whether you will create a Schema in `Local` or externally. The Schema created includes `repository_info`, information about where the resource is managed.
request_example: >-
{
"name": "slack_webhook",
"service_type": "secret.credentials",
"schema": {},
"labels": [],
"tags": {
"description": "Slack Webhook"
},
"domain_id": "domain-987654321098"
}
response_example: >-
{
"name": "slack_webhook",
"service_type": "secret.credentials",
"schema": {},
"labels": [],
"tags": {
"description": "Slack Webhook"
},
"repository_info": {
"repository_id": "repo-123456789012",
"name": "Local",
"repository_type": "local"
},
"domain_id": "domain-987654321098",
"created_at": "2022-01-01T05:46:49.929Z",
"updated_at": "2022-01-01T05:46:49.929Z"
}



> **POST** /repository/v1/schema/create
>






    
<br>

### update

desc: Updates a specific Schema. You can make changes in Schema settings, including `name`, `schema`, `labels`, and `tags`.
request_example: >-
{
"name": "slack_webhook_test",
"schema": {},
"labels": [],
"tags": {},
"domain_id": "domain-987654321098"
}
response_example: >-
{
"name": "slack_webhook_test",
"service_type": "secret.credentials",
"schema": {},
"labels": [],
"tags": {
"description": "Slack Webhook"
},
"repository_info": {
"repository_id": "repo-123456789012",
"name": "Local",
"repository_type": "local"
},
"domain_id": "domain-987654321098",
"created_at": "2022-01-01T05:46:49.929Z",
"updated_at": "2022-01-01T05:46:49.929Z"
}



> **POST** /repository/v1/schema/update
>






    
<br>

### delete

desc: Deletes a specific Schema. You must specify the `name` of the Schema to delete, as the `name` is an identifier of Schema resources.
request_example: >-
{
"name": "slack_webhook"
}



> **POST** /repository/v1/schema/delete
>






    
<br>

### get

desc: Gets a specific Schema. You must specify the `name` of the Schema to get, as the `name` is an identifier of Schema resources. You can use the parameter `repository_id` to limit the scope of the method to a specific Repository.
request_example: >-
{
"name": "slack_webhook",
"repository_id": "repo-123456789012"
}
response_example: >-
{
"name": "slack_webhook",
"service_type": "secret.credentials",
"schema": {},
"labels": [],
"tags": {
"description": "Slack Webhook"
},
"repository_info": {
"repository_id": "repo-123456789012",
"name": "Local",
"repository_type": "local"
},
"domain_id": "domain-987654321098",
"created_at": "2022-01-01T10:20:09.064Z",
"updated_at": "2022-01-01T10:20:09.064Z"
}



> **POST** /repository/v1/schema/get
>






    
<br>

### list

desc: Gets a list of all Schemas in a specific Repository. The parameter `repository_id` is used as an identifier of a Repository to get its list of Schemas. You can use a query to get a filtered list of Schemas.
request_example: >-
{
"query": {},
"name": "slack_webhook",
"service_type": "secret.credentials",
"repository_id": "repo-123456789012"
}
response_example: >-
{
"results": [
{
"name": "slack_webhook",
"service_type": "secret.credentials",
"schema": {},
"labels": [],
"tags": {
"description": "Slack Webhook"
},
"repository_info": {
"repository_id": "repo-123456789012",
"name": "Local",
"repository_type": "local"
},
"domain_id": "domain-987654321098",
"created_at": "2022-01-01T10:20:09.064Z",
"updated_at": "2022-01-01T10:20:09.064Z"
}
],
"total_count": 1
}



> **POST** /repository/v1/schema/list
>






    
<br>

### stat





> **POST** /repository/v1/schema/stat
>






    


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
