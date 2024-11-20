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





 {{< tabs " create " >}}

 {{< tab "Request Example" >}}



[CreateSchemaRequest](./Schema#createschemarequest)

* **schema_id** (string)   `Required` 


* **name** (string)   `Required` 


* **schema_type** (SchemaType)   `Required` 


* **provider** (string)   `Required` 


* **schema** (Struct)  


* **related_schemas** (string)  `Repeated`   


* **options** (Struct)  


* **tags** (Struct)  





{{< highlight json >}}
{
 "schema_id": "aws-secret-access-key",
 "name": "AWS Access Key",
 "schema_type": "SECRET",
 "provider": "aws"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[SchemaInfo](#SCHEMAINFO)
* **schema_id** (string)   `Required` 

* **name** (string)   `Required` 

* **schema_type** (SchemaType)   `Required` 

* **schema** (Struct)   `Required` 

* **provider** (string)   `Required` 

* **related_schemas** (string)  `Repeated`   `Required` 

* **options** (Struct)   `Required` 

* **tags** (Struct)   `Required` 

* **is_managed** (bool)   `Required` 

* **domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 



{{< highlight json >}}
{
 "created_at": "2024-11-18T01:59:00.407Z",
 "domain_id": "domain-a1b2c3d4e5f6",
 "name": "AWS Access Key",
 "provider": "aws",
 "schema": {
   "order": [
     "aws_access_key_id",
     "aws_secret_access_key"
   ],
   "properties": {
     "aws_access_key_id": {
       "format": "password",
       "minLength": 4.0,
       "title": "AWS Access Key",
       "type": "string"
     },
     "aws_secret_access_key": {
       "format": "password",
       "minLength": 4.0,
       "title": "AWS Secret Key",
       "type": "string"
     }
   },
   "required": [
     "aws_access_key_id",
     "aws_secret_access_key"
   ],
   "type": "object"
 },
 "schema_id": "aws-secret-access-key",
 "schema_type": "SECRET",
 "updated_at": "2024-11-18T02:00:45.792Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### update





> **POST** /identity/v2/schema/update
>





 {{< tabs " update " >}}

 {{< tab "Request Example" >}}



[UpdateSchemaRequest](./Schema#updateschemarequest)

* **schema_id** (string)   `Required` 


* **name** (string)  


* **schema** (Struct)  


* **related_schemas** (string)  `Repeated`   


* **options** (Struct)  


* **tags** (Struct)  





{{< highlight json >}}
{
 "schema_id": "aws-secret-access-key1",
 "schema": {
   "order": [
     "aws_access_key_id",
     "aws_secret_access_key"
   ],
   "properties": {
     "aws_access_key_id": {
       "format": "password",
       "minLength": 4.0,
       "title": "AWS Access Key",
       "type": "string"
     },
     "aws_secret_access_key": {
       "format": "password",
       "minLength": 4.0,
       "title": "AWS Secret Key",
       "type": "string"
     }
   },
   "required": [
     "aws_access_key_id",
     "aws_secret_access_key"
   ],
   "type": "object"
 }
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[SchemaInfo](#SCHEMAINFO)
* **schema_id** (string)   `Required` 

* **name** (string)   `Required` 

* **schema_type** (SchemaType)   `Required` 

* **schema** (Struct)   `Required` 

* **provider** (string)   `Required` 

* **related_schemas** (string)  `Repeated`   `Required` 

* **options** (Struct)   `Required` 

* **tags** (Struct)   `Required` 

* **is_managed** (bool)   `Required` 

* **domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 



{{< highlight json >}}
{
 "created_at": "2024-11-18T01:59:00.407Z",
 "domain_id": "domain-a1b2c3d4e5f6",
 "name": "AWS Access Key",
 "provider": "aws",
 "schema": {
   "order": [
     "aws_access_key_id",
     "aws_secret_access_key"
   ],
   "properties": {
     "aws_access_key_id": {
       "format": "password",
       "minLength": 4.0,
       "title": "AWS Access Key",
       "type": "string"
     },
     "aws_secret_access_key": {
       "format": "password",
       "minLength": 4.0,
       "title": "AWS Secret Key",
       "type": "string"
     }
   },
   "required": [
     "aws_access_key_id",
     "aws_secret_access_key"
   ],
   "type": "object"
 },
 "schema_id": "aws-secret-access-key",
 "schema_type": "SECRET",
 "updated_at": "2024-11-18T02:00:45.792Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### delete





> **POST** /identity/v2/schema/delete
>





 {{< tabs " delete " >}}

 {{< tab "Request Example" >}}



[SchemaRequest](./Schema#schemarequest)

* **schema_id** (string)   `Required` 





{{< highlight json >}}
{
 "schema_id": "aws-secret-access-key"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### get





> **POST** /identity/v2/schema/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[SchemaRequest](./Schema#schemarequest)

* **schema_id** (string)   `Required` 





{{< highlight json >}}
{
 "schema_id": "aws-secret-access-key"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[SchemaInfo](#SCHEMAINFO)
* **schema_id** (string)   `Required` 

* **name** (string)   `Required` 

* **schema_type** (SchemaType)   `Required` 

* **schema** (Struct)   `Required` 

* **provider** (string)   `Required` 

* **related_schemas** (string)  `Repeated`   `Required` 

* **options** (Struct)   `Required` 

* **tags** (Struct)   `Required` 

* **is_managed** (bool)   `Required` 

* **domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 



{{< highlight json >}}
{
 "created_at": "2024-11-18T01:59:00.407Z",
 "domain_id": "domain-a1b2c3d4e5f6",
 "name": "AWS Access Key",
 "provider": "aws",
 "schema": {
   "order": [
     "aws_access_key_id",
     "aws_secret_access_key"
   ],
   "properties": {
     "aws_access_key_id": {
       "format": "password",
       "minLength": 4.0,
       "title": "AWS Access Key",
       "type": "string"
     },
     "aws_secret_access_key": {
       "format": "password",
       "minLength": 4.0,
       "title": "AWS Secret Key",
       "type": "string"
     }
   },
   "required": [
     "aws_access_key_id",
     "aws_secret_access_key"
   ],
   "type": "object"
 },
 "schema_id": "aws-secret-access-key",
 "schema_type": "SECRET",
 "updated_at": "2024-11-18T02:00:45.792Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### list





> **POST** /identity/v2/schema/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[SchemaSearchQuery](./Schema#schemasearchquery)

* **query** (Query)  


* **schema_id** (string)  


* **name** (string)  


* **schema_type** (SchemaType)  


* **provider** (string)  


* **related_schema_id** (string)  


* **is_managed** (bool)  





{{< highlight json >}}
{
 "provider": "aws",
 "query": {
   "page": {
     "start": 1,
     "limit": 10
   },
   "sort": [
     {
       "key": "created_at",
       "desc": true
     }
   ]
 }
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[SchemasInfo](#SCHEMASINFO)
* **results** (SchemaInfo)  `Repeated`   `Required` 

* **total_count** (int32)   `Required` 



{{< highlight json >}}
{
 "results": [
   {
     "created_at": "2024-11-18T02:08:10.216Z",
     "domain_id": "domain-a1b2c3d4e5f6",
     "name": "AWS Trusted Account",
     "provider": "aws",
     "schema": {
       "properties": {
         "account_id": {
           "minLength": 4.0,
           "title": "Account ID",
           "type": "string"
         }
       },
       "required": [
         "account_id"
       ],
       "type": "object"
     },
     "schema_id": "aws-trusted-account",
     "schema_type": "TRUSTED_ACCOUNT",
     "updated_at": "2024-11-18T02:08:10.216Z"
   },
   {
     "created_at": "2024-11-18T01:59:00.407Z",
     "domain_id": "domain-a1b2c3d4e5f6",
     "name": "AWS Access Key",
     "provider": "aws",
     "schema": {
       "order": [
         "aws_access_key_id",
         "aws_secret_access_key"
       ],
       "properties": {
         "aws_access_key_id": {
           "format": "password",
           "minLength": 4.0,
           "title": "AWS Access Key",
           "type": "string"
         },
         "aws_secret_access_key": {
           "format": "password",
           "minLength": 4.0,
           "title": "AWS Secret Key",
           "type": "string"
         }
       },
       "required": [
         "aws_access_key_id",
         "aws_secret_access_key"
       ],
       "type": "object"
     },
     "schema_id": "aws-secret-access-key",
     "schema_type": "SECRET",
     "updated_at": "2024-11-18T02:00:45.792Z"
   }
 ],
 "total_count": 2
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
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

    
* **provider** (string)   `Required` 

    
* **schema** (Struct)  

    
* **related_schemas** (string)  `Repeated`   

    
* **options** (Struct)  

    
* **tags** (Struct)  

    <br>

### SchemaInfo
* **schema_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **schema_type** (SchemaType)   `Required` 

    
* **schema** (Struct)   `Required` 

    
* **provider** (string)   `Required` 

    
* **related_schemas** (string)  `Repeated`    `Required` 

    
* **options** (Struct)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **is_managed** (bool)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    <br>

### SchemaRequest
* **schema_id** (string)   `Required` 

    <br>

### SchemaSearchQuery
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

    <br>

### SchemasInfo
* **results** (SchemaInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### UpdateSchemaRequest
* **schema_id** (string)   `Required` 

    
* **name** (string)  

    
* **schema** (Struct)  

    
* **related_schemas** (string)  `Repeated`   

    
* **options** (Struct)  

    
* **tags** (Struct)  

    <br>
