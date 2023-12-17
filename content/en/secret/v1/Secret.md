---
title: "Secret"
linkTitle: "Secret"
weight: 3
bookFlatSection: true
---
# [Secret](#Secret)
Secret is a service that stores and manages credentials.
Secret is used to access data in other microservices.


>  **Package : spaceone.api.secret.v1**

<br>
<br>

## Secret





**Secret Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Secret#create) | [CreateSecretRequest](Secret#createsecretrequest) | [SecretInfo](Secret#secretinfo) |
| [**update**](./Secret#update) | [UpdateSecretRequest](Secret#updatesecretrequest) | [SecretInfo](Secret#secretinfo) |
| [**delete**](./Secret#delete) | [SecretRequest](Secret#secretrequest) | [Empty](Secret#empty) |
| [**update_data**](./Secret#update_data) | [UpdateSecretDataRequest](Secret#updatesecretdatarequest) | [Empty](Secret#empty) |
| [**get_data**](./Secret#get_data) | [SecretRequest](Secret#secretrequest) | [SecretDataInfo](Secret#secretdatainfo) |
| [**get**](./Secret#get) | [SecretRequest](Secret#secretrequest) | [SecretInfo](Secret#secretinfo) |
| [**list**](./Secret#list) | [SecretQuery](Secret#secretquery) | [SecretsInfo](Secret#secretsinfo) |
| [**stat**](./Secret#stat) | [SecretStatQuery](Secret#secretstatquery) | [Struct](Secret#struct) |



    
<br>

### create

Create a new secret.
Created secret is encrypted and stored securely.
It can be used to link to a trusted secret if you request it with 'trusted_secret_id' in the parameter.



> **POST** /secret/v1/secret/create
>





 {{< tabs " create " >}}

 {{< tab "Request Example" >}}



[CreateSecretRequest](./Secret#createsecretrequest)

* **name** (string)   `Required` 


* **data** (Struct)   `Required` 


* **resource_group** (ResourceGroup)   `Required` 


* **schema_id** (string)  


* **tags** (Struct)  


* **project_id** (string)  


* **service_account_id** (string)  


* **trusted_secret_id** (string)  





{{< highlight json >}}
{
   "name": "Cloudforet AWS Dev",
   "data": "********",
   "schema_id": "aws_access_key",
   "resource_group": "PROJECT",
   "service_account_id": "sa-123456789012",
   "project_id": "project-123456789012"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[SecretInfo](#SECRETINFO)
* **secret_id** (string)   `Required` 

* **name** (string)   `Required` 

* **schema_id** (string)   `Required` 

* **provider** (string)   `Required` 

* **tags** (Struct)   `Required` 

* **resource_group** (ResourceGroup)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **project_id** (string)   `Required` 

* **service_account_id** (string)   `Required` 

* **trusted_secret_id** (string)   `Required` 

* **created_at** (string)   `Required` 



{{< highlight json >}}
{
   "secret_id": "secret-123456789012",
   "name": "aws-dev",
   "tags": {},
   "schema_id": "aws_access_key",
   "provider": "aws",
   "service_account_id": "sa-123456789012",
   "resource_group": "PROJECT",
   "project_id": "project-123456789012",
   "workspace_id": "workspace-123456789012",
   "domain_id": "domain-123456789012",
   "created_at": "2022-01-01T06:10:14.851Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### update

Updates a specific secret's information.
You can only change the 'name' and 'tags', and to change the data you must use the update_data API.



> **POST** /secret/v1/secret/update
>





 {{< tabs " update " >}}

 {{< tab "Request Example" >}}



[UpdateSecretRequest](./Secret#updatesecretrequest)

* **secret_id** (string)   `Required` 


* **name** (string)  


* **tags** (Struct)  


* **project_id** (string)  





{{< highlight json >}}
{
   "secret_id": "secret-123456789012",
   "name": "aws-dev2",
   "tags": { "a": "b"},
   "project_id": "project-123456789012"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[SecretInfo](#SECRETINFO)
* **secret_id** (string)   `Required` 

* **name** (string)   `Required` 

* **schema_id** (string)   `Required` 

* **provider** (string)   `Required` 

* **tags** (Struct)   `Required` 

* **resource_group** (ResourceGroup)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **project_id** (string)   `Required` 

* **service_account_id** (string)   `Required` 

* **trusted_secret_id** (string)   `Required` 

* **created_at** (string)   `Required` 



{{< highlight json >}}
{
   "secret_id": "secret-123456789012",
   "name": "aws-dev",
   "tags": {},
   "schema_id": "aws_access_key",
   "provider": "aws",
   "service_account_id": "sa-123456789012",
   "resource_group": "PROJECT",
   "project_id": "project-123456789012",
   "workspace_id": "workspace-123456789012",
   "domain_id": "domain-123456789012",
   "created_at": "2022-01-01T06:10:14.851Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### delete

Deletes a specific secret.



> **POST** /secret/v1/secret/delete
>





 {{< tabs " delete " >}}

 {{< tab "Request Example" >}}



[SecretRequest](./Secret#secretrequest)

* **secret_id** (string)   `Required` 





{{< highlight json >}}
{
   "secret_id": "secret-123456789012"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### update_data

Updates a specific secret's data.
Updated secret is encrypted and stored securely.



> **POST** /secret/v1/secret/update-data
>





 {{< tabs " update_data " >}}

 {{< tab "Request Example" >}}



[UpdateSecretDataRequest](./Secret#updatesecretdatarequest)

* **secret_id** (string)   `Required` 


* **schema_id** (string)   `Required` 


* **data** (Struct)   `Required` 





{{< highlight json >}}
{
   "secret_id": "secret-123456789012",
    "data": "********"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### get_data

Updates a specific secret's data.
This API is for internal system use only.







 {{< tabs " get_data " >}}

 {{< tab "Request Example" >}}



[SecretRequest](./Secret#secretrequest)

* **secret_id** (string)   `Required` 





{{< highlight json >}}
{
   "secret_id": "secret-123456789012"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### get

Get a specific secret's information.



> **POST** /secret/v1/secret/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[SecretRequest](./Secret#secretrequest)

* **secret_id** (string)   `Required` 





{{< highlight json >}}
{
   "secret_id": "secret-123456789012"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[SecretInfo](#SECRETINFO)
* **secret_id** (string)   `Required` 

* **name** (string)   `Required` 

* **schema_id** (string)   `Required` 

* **provider** (string)   `Required` 

* **tags** (Struct)   `Required` 

* **resource_group** (ResourceGroup)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **project_id** (string)   `Required` 

* **service_account_id** (string)   `Required` 

* **trusted_secret_id** (string)   `Required` 

* **created_at** (string)   `Required` 



{{< highlight json >}}
{
   "secret_id": "secret-123456789012",
   "name": "aws-dev",
   "tags": {},
   "schema_id": "aws_access_key",
   "provider": "aws",
   "service_account_id": "sa-123456789012",
   "resource_group": "PROJECT",
   "project_id": "project-123456789012",
   "workspace_id": "workspace-123456789012",
   "domain_id": "domain-123456789012",
   "created_at": "2022-01-01T06:10:14.851Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### list

Queries a list of secrets.
You can use a query to get a filtered list of secrets.



> **POST** /secret/v1/secret/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[SecretQuery](./Secret#secretquery)

* **query** (Query)  


* **secret_id** (string)  


* **name** (string)  


* **schema_id** (string)  


* **provider** (string)  


* **workspace_id** (string)  


* **project_id** (string)  


* **service_account_id** (string)  


* **trusted_secret_id** (string)  





{{< highlight json >}}
{
   "query": {},
   "domain_id": "domain-12345abcde"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[SecretsInfo](#SECRETSINFO)
* **results** (SecretInfo)  `Repeated`   `Required` 

* **total_count** (int32)   `Required` 



{{< highlight json >}}
{
   "results": [
       {
          "secret_id": "secret-123456789012",
          "name": "aws-dev",
          "tags": {},
          "schema": "aws_access_key",
          "provider": "aws",
          "service_account_id": "sa-123456789012",
          "resource_group": "PROJECT",
          "workspace_id": "workspace-123456789012",
          "project_id": "project-123456789012",
          "domain_id": "domain-123456789012",
          "created_at": "2022-01-01T06:10:14.851Z"
       },
       {
           "secret_id": "secret-987654321098",
           "name": "plugin-credentials",
           "tags": {},
           "resource_group": "WORKSPACE",
           "workspace_id": "workspace-123456789012",
           "domain_id": "domain-123456789012",
           "created_at": "2022-01-01T02:31:01.709Z"
       }
   ],
   "total_count": 2
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### stat





> **POST** /secret/v1/secret/stat
>






    


<br>
<br>

## Message



### CreateSecretRequest
* **name** (string)   `Required` 

    
* **data** (Struct)   `Required` 

    
* **resource_group** (ResourceGroup)   `Required` 

    
* **schema_id** (string)  

    
* **tags** (Struct)  

    
* **project_id** (string)  

    
* **service_account_id** (string)  

    
* **trusted_secret_id** (string)  

    <br>

### SecretDataInfo
* **encrypted** (bool)   `Required` 

    
* **encrypt_options** (Struct)   `Required` 

    
* **data** (Struct)   `Required` 

    <br>

### SecretInfo
* **secret_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **schema_id** (string)   `Required` 

    
* **provider** (string)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **resource_group** (ResourceGroup)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **project_id** (string)   `Required` 

    
* **service_account_id** (string)   `Required` 

    
* **trusted_secret_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    <br>

### SecretQuery
* **query** (Query)  

    
* **secret_id** (string)  

    
* **name** (string)  

    
* **schema_id** (string)  

    
* **provider** (string)  

    
* **workspace_id** (string)  

    
* **project_id** (string)  

    
* **service_account_id** (string)  

    
* **trusted_secret_id** (string)  

    <br>

### SecretRequest
* **secret_id** (string)   `Required` 

    <br>

### SecretStatQuery
* **query** (StatisticsQuery)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### SecretsInfo
* **results** (SecretInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### UpdateSecretDataRequest
* **secret_id** (string)   `Required` 

    
* **schema_id** (string)   `Required` 

    
* **data** (Struct)   `Required` 

    <br>

### UpdateSecretRequest
* **secret_id** (string)   `Required` 

    
* **name** (string)  

    
* **tags** (Struct)  

    
* **project_id** (string)  

    <br>
