---
title: "Schema"
linkTitle: "Schema"
weight: 3
bookFlatSection: true
---
# [Schema](#Schema)
A Schema is a data structure used in all domains. For example, data forms of Google OAuth2 credentials or AWS access keys can be a Schema resource.


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

Creates a new Schema. You must specify the parameters: `service_type`, `name`, and `schema`(data structure). With the parameter `domain_id`, you can choose whether you will create a Schema in `Local` or externally. The Schema created includes `repository_info`, information about where the resource is managed.



> **POST** /repository/v1/schema/create
>





 {{< tabs " create " >}}

 {{< tab "Request Example" >}}



[CreateSchemaRequest](./Schema#createschemarequest)

* **name** (string)  `Required` 


* **service_type** (string)  `Required` 


* **schema_id** (string)  `Required` 


* **schema** (Struct)  `Required` 


* **domain_id** (string)  `Required` 


* **labels** (ListValue) 


* **tags** (Struct) 


* **project_id** (string) 





{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[SchemaInfo](#SCHEMAINFO)
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



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### update

Updates a specific Schema. You can make changes in Schema settings, including `name`, `schema`, `labels`, and `tags`.



> **POST** /repository/v1/schema/update
>





 {{< tabs " update " >}}

 {{< tab "Request Example" >}}



[UpdateSchemaRequest](./Schema#updateschemarequest)

* **name** (string)  `Required` 


* **domain_id** (string)  `Required` 


* **schema** (Struct) 


* **labels** (ListValue) 


* **tags** (Struct) 





{{< highlight json >}}
{
   "name": "slack_webhook_test",
   "schema": {},
   "labels": [],
   "tags": {},
   "domain_id": "domain-987654321098"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[SchemaInfo](#SCHEMAINFO)
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



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### delete

Deletes a specific Schema. You must specify the `name` of the Schema to delete, as the `name` is an identifier of Schema resources.



> **POST** /repository/v1/schema/delete
>





 {{< tabs " delete " >}}

 {{< tab "Request Example" >}}



[SchemaRequest](./Schema#schemarequest)

* **name** (string)  `Required` 


* **domain_id** (string)  `Required` 


* **schema_id** (string) 





{{< highlight json >}}
{
   "name": "slack_webhook"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### get

Gets a specific Schema. You must specify the `name` of the Schema to get, as the `name` is an identifier of Schema resources. You can use the parameter `repository_id` to limit the scope of the method to a specific Repository.



> **POST** /repository/v1/schema/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[GetRepositorySchemaRequest](./Schema#getrepositoryschemarequest)

* **name** (string)  `Required` 


* **domain_id** (string)  `Required` 


* **repository_id** (string) 


* **only** (string) 


* **schema_id** (string) 





{{< highlight json >}}
{
   "name": "slack_webhook",
   "repository_id": "repo-123456789012"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[SchemaInfo](#SCHEMAINFO)
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



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### list

Gets a list of all Schemas in a specific Repository. The parameter `repository_id` is used as an identifier of a Repository to get its list of Schemas. You can use a query to get a filtered list of Schemas.



> **POST** /repository/v1/schema/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[SchemaQuery](./Schema#schemaquery)

* **project_id** (string)  `Required` 


* **repository_id** (string)  `Required` 


* **domain_id** (string)  `Required` 


* **query** (Query) 


* **name** (string) 


* **service_type** (string) 


* **schema_id** (string) 


* **state** (State) 





{{< highlight json >}}
{
   "query": {},
   "name": "slack_webhook",
   "service_type": "secret.credentials",
   "repository_id": "repo-123456789012"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[SchemasInfo](#SCHEMASINFO)
* **results** (SchemaInfo)  `Required` 

* **total_count** (int32)  `Required` 



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### stat





> **POST** /repository/v1/schema/stat
>






    


<br>
<br>

## Message



### CreateSchemaRequest
* **name** (string)  `Required` 

    
* **service_type** (string)  `Required` 

    
* **schema_id** (string)  `Required` 

    
* **schema** (Struct)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **labels** (ListValue) 

    
* **tags** (Struct) 

    
* **project_id** (string) 

    <br>

### GetRepositorySchemaRequest
* **name** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **repository_id** (string) 

    
* **only** (string) 

    
* **schema_id** (string) 

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
* **project_id** (string)  `Required` 

    
* **repository_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **query** (Query) 

    
* **name** (string) 

    
* **service_type** (string) 

    
* **schema_id** (string) 

    
* **state** (State) 

    <br>

### SchemaRequest
* **name** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **schema_id** (string) 

    <br>

### SchemaStatQuery
* **query** (StatisticsQuery)  `Required` 

    
* **repository_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    <br>

### SchemasInfo
* **results** (SchemaInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### UpdateSchemaRequest
* **name** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **schema** (Struct) 

    
* **labels** (ListValue) 

    
* **tags** (Struct) 

    <br>
