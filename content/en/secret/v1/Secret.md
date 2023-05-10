---
title: "Secret"
linkTitle: "Secret"
weight: 3
bookFlatSection: true
---
# [Secret](#Secret)
A Secret is an external data, encrypted by CloudForet.


>  **Package : spaceone.api.secret.v1**

<br>
<br>

## Secret





**Secret Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Secret#create) | [CreateSecretRequest](Secret#createsecretrequest) | [SecretInfo](./Secret#secretinfo) |
| [**update**](./Secret#update) | [UpdateSecretRequest](Secret#updatesecretrequest) | [SecretInfo](./Secret#secretinfo) |
| [**delete**](./Secret#delete) | [SecretRequest](Secret#secretrequest) | [Empty](./Secret#empty) |
| [**update_data**](./Secret#update_data) | [UpdateSecretDataRequest](Secret#updatesecretdatarequest) | [Empty](./Secret#empty) |
| [**get_data**](./Secret#get_data) | [SecretRequest](Secret#secretrequest) | [SecretDataInfo](./Secret#secretdatainfo) |
| [**get**](./Secret#get) | [GetSecretRequest](Secret#getsecretrequest) | [SecretInfo](./Secret#secretinfo) |
| [**list**](./Secret#list) | [SecretQuery](Secret#secretquery) | [SecretsInfo](./Secret#secretsinfo) |
| [**stat**](./Secret#stat) | [SecretStatQuery](Secret#secretstatquery) | [Struct](./Secret#struct) |



    
<br>

### create

Creates a new Secret. When creating the resource, external `data` is encrypted, and a `secret_id` is issued for data access by other microservices.



> **POST** /secret/v1/secret/create
>





 {{< tabs " create " >}}

 {{< tab "Request Example" >}}



[CreateSecretRequest](./Secret#createsecretrequest)

* **name** (string)  `Required` 


* **data** (Struct)  `Required` 


* **secret_type** (SecretType)  `Required` 


* **domain_id** (string)  `Required` 


* **tags** (Struct) 


* **schema** (string) 


* **service_account_id** (string) 


* **project_id** (string) 


* **trusted_secret_id** (string) 





{{< highlight json >}}
{
   "name": "aws-dev",
   "data": "********",
   "secret_type": "CREDENTIALS",
   "schema": "aws_access_key",
   "service_account_id": "sa-123456789012",
   "project_id": "project-123456789012",
   "domain_id": "domain-123456789012"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[SecretInfo](#SECRETINFO)
* **secret_id** (string)  `Required` 

* **name** (string)  `Required` 

* **secret_type** (SecretType)  `Required` 

* **tags** (Struct)  `Required` 

* **schema** (string)  `Required` 

* **provider** (string)  `Required` 

* **service_account_id** (string)  `Required` 

* **project_id** (string)  `Required` 

* **trusted_secret_id** (string)  `Required` 

* **domain_id** (string)  `Required` 

* **created_at** (string)  `Required` 



{{< highlight json >}}
{
   "secret_id": "secret-123456789012",
   "name": "aws-dev",
   "secret_type": "CREDENTIALS",
   "tags": {},
   "schema": "aws_access_key",
   "provider": "aws",
   "service_account_id": "sa-123456789012",
   "project_id": "project-123456789012",
   "domain_id": "domain-123456789012",
   "created_at": "2022-01-01T06:10:14.851Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### update

Updates a specific Secret. You can make changes in Secret settings, including `name` and`tags`.



> **POST** /secret/v1/secret/update
>





 {{< tabs " update " >}}

 {{< tab "Request Example" >}}



[UpdateSecretRequest](./Secret#updatesecretrequest)

* **secret_id** (string)  `Required` 


* **domain_id** (string)  `Required` 


* **name** (string) 


* **tags** (Struct) 


* **project_id** (string) 


* **release_project** (bool) 





{{< highlight json >}}
{
   "secret_id": "secret-123456789012",
   "name": "aws-dev2",
   "tags": { "a": "b"},
   "project_id": "project-123456789012",
   "release_project": true,
   "domain_id": "domain-123456789012"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[SecretInfo](#SECRETINFO)
* **secret_id** (string)  `Required` 

* **name** (string)  `Required` 

* **secret_type** (SecretType)  `Required` 

* **tags** (Struct)  `Required` 

* **schema** (string)  `Required` 

* **provider** (string)  `Required` 

* **service_account_id** (string)  `Required` 

* **project_id** (string)  `Required` 

* **trusted_secret_id** (string)  `Required` 

* **domain_id** (string)  `Required` 

* **created_at** (string)  `Required` 



{{< highlight json >}}
{
   "secret_id": "secret-123456789012",
   "name": "aws-dev",
   "secret_type": "CREDENTIALS",
   "tags": {},
   "schema": "aws_access_key",
   "provider": "aws",
   "service_account_id": "sa-123456789012",
   "project_id": "project-123456789012",
   "domain_id": "domain-123456789012",
   "created_at": "2022-01-01T06:10:14.851Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### delete

Deletes a specific Secret. You must specify the `secret_id` of the Secret to delete.



> **POST** /secret/v1/secret/delete
>





 {{< tabs " delete " >}}

 {{< tab "Request Example" >}}



[SecretRequest](./Secret#secretrequest)

* **secret_id** (string)  `Required` 


* **domain_id** (string)  `Required` 





{{< highlight json >}}
{
   "secret_id": "secret-123456789012",
   "domain_id": "domain-123456789012"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### update_data

Updates encrypted data of a specific Secret resource. For example, to change the parameter `data`, external data to encrypt, you can use `update_data` to create new encrypted data based on the changed `data` and store it in the Secret resource.



> **POST** /secret/v1/secret/update-data
>





 {{< tabs " update_data " >}}

 {{< tab "Request Example" >}}



[UpdateSecretDataRequest](./Secret#updatesecretdatarequest)

* **secret_id** (string)  `Required` 


* **data** (Struct)  `Required` 


* **domain_id** (string)  `Required` 


* **schema** (string) 





{{< highlight json >}}
{
   "secret_id": "secret-123456789012",
    "data": "********",
    "domain_id": "domain-123456789012"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### get_data

Gets a specific Secret. Prints detailed information about the Secret, including  `name`, `tags`, `schema`, and `provider`.



> **POST** /secret/v1/secret/get-data
>





 {{< tabs " get_data " >}}

 {{< tab "Request Example" >}}



[SecretRequest](./Secret#secretrequest)

* **secret_id** (string)  `Required` 


* **domain_id** (string)  `Required` 





{{< highlight json >}}
{
   "secret_id": "secret-123456789012",
   "domain_id": "domain-123456789012"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### get

Gets a specific Post. You must specify the `post_id` of the Post to get, and the `board_id` of the Board where the child Post to get belongs. Prints detailed information about the Post.



> **POST** /secret/v1/secret/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[GetSecretRequest](./Secret#getsecretrequest)

* **secret_id** (string)  `Required` 


* **domain_id** (string)  `Required` 


* **only** (string) 





{{< highlight json >}}
{
   "secret_id": "secret-123456789012",
   "domain_id": "domain-123456789012"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[SecretInfo](#SECRETINFO)
* **secret_id** (string)  `Required` 

* **name** (string)  `Required` 

* **secret_type** (SecretType)  `Required` 

* **tags** (Struct)  `Required` 

* **schema** (string)  `Required` 

* **provider** (string)  `Required` 

* **service_account_id** (string)  `Required` 

* **project_id** (string)  `Required` 

* **trusted_secret_id** (string)  `Required` 

* **domain_id** (string)  `Required` 

* **created_at** (string)  `Required` 



{{< highlight json >}}
{
   "secret_id": "secret-123456789012",
   "name": "aws-dev",
   "secret_type": "CREDENTIALS",
   "tags": {},
   "schema": "aws_access_key",
   "provider": "aws",
   "service_account_id": "sa-123456789012",
   "project_id": "project-123456789012",
   "domain_id": "domain-123456789012",
   "created_at": "2022-01-01T06:10:14.851Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### list

Gets a list of all Posts. You can use a query to get a filtered list of Posts.



> **POST** /secret/v1/secret/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[SecretQuery](./Secret#secretquery)

* **domain_id** (string)  `Required` 


* **query** (Query) 


* **secret_id** (string) 


* **name** (string) 


* **secret_type** (SecretType) 


* **schema** (string) 


* **provider** (string) 


* **service_account_id** (string) 


* **trusted_secret_id** (string) 





{{< highlight json >}}
{
   "query": {},
   "domain_id": "domain-123456789012"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[SecretsInfo](#SECRETSINFO)
* **results** (SecretInfo)  `Required` 

* **total_count** (int32)  `Required` 



{{< highlight json >}}
{
   "results": [
       {
          "secret_id": "secret-123456789012",
          "name": "aws-dev",
          "secret_type": "CREDENTIALS",
          "tags": {},
          "schema": "aws_access_key",
          "provider": "aws",
          "service_account_id": "sa-123456789012",
          "project_id": "project-123456789012",
          "domain_id": "domain-123456789012",
          "created_at": "2022-01-01T06:10:14.851Z"
       },
       {
           "secret_id": "secret-987654321098",
           "name": "plugin-credentials",
           "secret_type": "CREDENTIALS",
           "tags": {},
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
* **name** (string)  `Required` 

    
* **data** (Struct)  `Required` 

    
* **secret_type** (SecretType)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **tags** (Struct) 

    
* **schema** (string) 

    
* **service_account_id** (string) 

    
* **project_id** (string) 

    
* **trusted_secret_id** (string) 

    <br>

### GetSecretRequest
* **secret_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **only** (string) 

    <br>

### SecretDataInfo
* **data** (Struct)  `Required` 

    
* **encrypted** (bool)  `Required` 

    
* **encrypt_options** (Struct)  `Required` 

    <br>

### SecretInfo
* **secret_id** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **secret_type** (SecretType)  `Required` 

    
* **tags** (Struct)  `Required` 

    
* **schema** (string)  `Required` 

    
* **provider** (string)  `Required` 

    
* **service_account_id** (string)  `Required` 

    
* **project_id** (string)  `Required` 

    
* **trusted_secret_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    <br>

### SecretQuery
* **domain_id** (string)  `Required` 

    
* **query** (Query) 

    
* **secret_id** (string) 

    
* **name** (string) 

    
* **secret_type** (SecretType) 

    
* **schema** (string) 

    
* **provider** (string) 

    
* **service_account_id** (string) 

    
* **trusted_secret_id** (string) 

    <br>

### SecretRequest
* **secret_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    <br>

### SecretStatQuery
* **query** (StatisticsQuery)  `Required` 

    
* **domain_id** (string)  `Required` 

    <br>

### SecretsInfo
* **results** (SecretInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### UpdateSecretDataRequest
* **secret_id** (string)  `Required` 

    
* **data** (Struct)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **schema** (string) 

    <br>

### UpdateSecretRequest
* **secret_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **name** (string) 

    
* **tags** (Struct) 

    
* **project_id** (string) 

    
* **release_project** (bool) 

    <br>
