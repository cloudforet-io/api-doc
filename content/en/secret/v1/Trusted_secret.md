---
title: "Trusted_secret"
linkTitle: "Trusted_secret"
weight: 3
bookFlatSection: true
---
# [Trusted_secret](#Trusted_secret)
A Trusted Secret is an external data, encrypted by CloudForet.


>  **Package : spaceone.api.secret.v1**

<br>
<br>

## Trusted_secret





**TrustedSecret Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./TrustedSecret#create) | [CreateTrustedSecretRequest](TrustedSecret#createtrustedsecretrequest) | [TrustedSecretInfo](./TrustedSecret#trustedsecretinfo) |
| [**update**](./TrustedSecret#update) | [UpdateTrustedSecretRequest](TrustedSecret#updatetrustedsecretrequest) | [TrustedSecretInfo](./TrustedSecret#trustedsecretinfo) |
| [**delete**](./TrustedSecret#delete) | [TrustedSecretRequest](TrustedSecret#trustedsecretrequest) | [Empty](./TrustedSecret#empty) |
| [**update_data**](./TrustedSecret#update_data) | [UpdateTrustedSecretDataRequest](TrustedSecret#updatetrustedsecretdatarequest) | [Empty](./TrustedSecret#empty) |
| [**get**](./TrustedSecret#get) | [GetTrustedSecretRequest](TrustedSecret#gettrustedsecretrequest) | [TrustedSecretInfo](./TrustedSecret#trustedsecretinfo) |
| [**list**](./TrustedSecret#list) | [TrustedSecretQuery](TrustedSecret#trustedsecretquery) | [TrustedSecretsInfo](./TrustedSecret#trustedsecretsinfo) |
| [**stat**](./TrustedSecret#stat) | [TrustedSecretStatQuery](TrustedSecret#trustedsecretstatquery) | [Struct](./TrustedSecret#struct) |



    
<br>

### create

Creates a new Trusted Secret. When creating the resource, external `data` is encrypted, and a `trusted_secret_id` is issued for data access by other microservices.



> **POST** /secret/v1/trusted-secret/create
>





 {{< tabs " create " >}}

 {{< tab "Request Example" >}}



[CreateTrustedSecretRequest](./TrustedSecret#createtrustedsecretrequest)

* **name** (string)  `Required` 


* **data** (Struct)  `Required` 


* **domain_id** (string)  `Required` 


* **tags** (Struct) 


* **schema** (string) 


* **service_account_id** (string) 





{{< highlight json >}}
{
   "name": "aws-dev",
   "data": "********",
   "schema": "aws_access_key",
   "service_account_id": "sa-123456789012",
   "tags": {},
   "domain_id": "domain-123456789012"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[TrustedSecretInfo](#TRUSTEDSECRETINFO)
* **trusted_secret_id** (string)  `Required` 

* **name** (string)  `Required` 

* **tags** (Struct)  `Required` 

* **schema** (string)  `Required` 

* **provider** (string)  `Required` 

* **service_account_id** (string)  `Required` 

* **project_id** (string)  `Required` 

* **domain_id** (string)  `Required` 

* **created_at** (string)  `Required` 



{{< highlight json >}}
{
   "trusted_secret_id": "trusted-secret-123456789012",
   "name": "aws-dev",
   "tags": {},
   "schema": "aws_access_key",
   "provider": "aws",
   "service_account_id": "sa-123456789012",
   "domain_id": "domain-123456789012",
   "created_at": "2022-01-01T06:10:14.851Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### update

Updates a specific Secret. You can make changes in Secret settings, including `name` and`tags`.



> **POST** /secret/v1/trusted-secret/update
>





 {{< tabs " update " >}}

 {{< tab "Request Example" >}}



[UpdateTrustedSecretRequest](./TrustedSecret#updatetrustedsecretrequest)

* **trusted_secret_id** (string)  `Required` 


* **domain_id** (string)  `Required` 


* **name** (string) 


* **tags** (Struct) 





{{< highlight json >}}
{
   "trusted_secret_id": "trusted-secret-123456789012",
   "name": "aws-dev2",
   "tags": { "a": "b"},
   "domain_id": "domain-123456789012"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[TrustedSecretInfo](#TRUSTEDSECRETINFO)
* **trusted_secret_id** (string)  `Required` 

* **name** (string)  `Required` 

* **tags** (Struct)  `Required` 

* **schema** (string)  `Required` 

* **provider** (string)  `Required` 

* **service_account_id** (string)  `Required` 

* **project_id** (string)  `Required` 

* **domain_id** (string)  `Required` 

* **created_at** (string)  `Required` 



{{< highlight json >}}
{
   "trusted_secret_id": "trusted-secret-123456789012",
   "name": "aws-dev",
   "tags": {},
   "schema": "aws_access_key",
   "provider": "aws",
   "service_account_id": "sa-123456789012",
   "domain_id": "domain-123456789012",
   "created_at": "2022-01-01T06:10:14.851Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### delete

Deletes a specific Secret. You must specify the `secret_id` of the Secret to delete.



> **POST** /secret/v1/trusted-secret/delete
>





 {{< tabs " delete " >}}

 {{< tab "Request Example" >}}



[TrustedSecretRequest](./TrustedSecret#trustedsecretrequest)

* **trusted_secret_id** (string)  `Required` 


* **domain_id** (string)  `Required` 





{{< highlight json >}}
{
   "trusted_secret_id": "trusted-secret-123456789012",
   "domain_id": "domain-123456789012"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### update_data

Updates encrypted data of a specific Secret resource. For example, to change the parameter `data`, external data to encrypt, you can use `update_data` to create new encrypted data based on the changed `data` and store it in the Secret resource.



> **POST** /secret/v1/trusted-secret/update-data
>





 {{< tabs " update_data " >}}

 {{< tab "Request Example" >}}



[UpdateTrustedSecretDataRequest](./TrustedSecret#updatetrustedsecretdatarequest)

* **trusted_secret_id** (string)  `Required` 


* **data** (Struct)  `Required` 


* **domain_id** (string)  `Required` 


* **schema** (string) 





{{< highlight json >}}
{
   "trusted_secret_id": "trusted-secret-123456789012",
   "data": "********",
   "domain_id": "domain-123456789012"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### get

Gets a specific Post. You must specify the `post_id` of the Post to get, and the `board_id` of the Board where the child Post to get belongs. Prints detailed information about the Post.



> **POST** /secret/v1/trusted-secret/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[GetTrustedSecretRequest](./TrustedSecret#gettrustedsecretrequest)

* **trusted_secret_id** (string)  `Required` 


* **domain_id** (string)  `Required` 


* **only** (string) 





{{< highlight json >}}
{
   "trusted_secret_id": "trusted-secret-123456789012",
   "domain_id": "domain-123456789012"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[TrustedSecretInfo](#TRUSTEDSECRETINFO)
* **trusted_secret_id** (string)  `Required` 

* **name** (string)  `Required` 

* **tags** (Struct)  `Required` 

* **schema** (string)  `Required` 

* **provider** (string)  `Required` 

* **service_account_id** (string)  `Required` 

* **project_id** (string)  `Required` 

* **domain_id** (string)  `Required` 

* **created_at** (string)  `Required` 



{{< highlight json >}}
{
   "trusted_secret_id": "trusted-secret-123456789012",
   "name": "aws-dev",
   "tags": {},
   "schema": "aws_access_key",
   "provider": "aws",
   "service_account_id": "sa-123456789012",
   "domain_id": "domain-123456789012",
   "created_at": "2022-01-01T06:10:14.851Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### list

Gets a list of all Posts. You can use a query to get a filtered list of Posts.



> **POST** /secret/v1/trusted-secret/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[TrustedSecretQuery](./TrustedSecret#trustedsecretquery)

* **domain_id** (string)  `Required` 


* **query** (Query) 


* **trusted_secret_id** (string) 


* **name** (string) 


* **schema** (string) 


* **provider** (string) 


* **service_account_id** (string) 





{{< highlight json >}}
{
   "query": {},
   "domain_id": "domain-123456789012"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[TrustedSecretsInfo](#TRUSTEDSECRETSINFO)
* **results** (TrustedSecretInfo)  `Required` 

* **total_count** (int32)  `Required` 



{{< highlight json >}}
{
   "results": [
       {
          "trusted_secret_id": "trusted-secret-123456789012",
          "name": "aws-dev",
          "tags": {},
          "schema": "aws_access_key",
          "provider": "aws",
          "service_account_id": "sa-123456789012",
          "domain_id": "domain-123456789012",
          "created_at": "2022-01-01T06:10:14.851Z"
       },
       {
           "trusted_secret_id": "trusted-secret-987654321098",
           "name": "plugin-credentials",
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





> **POST** /secret/v1/trusted-secret/stat
>






    


<br>
<br>

## Message



### CreateTrustedSecretRequest
* **name** (string)  `Required` 

    
* **data** (Struct)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **tags** (Struct) 

    
* **schema** (string) 

    
* **service_account_id** (string) 

    <br>

### GetTrustedSecretRequest
* **trusted_secret_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **only** (string) 

    <br>

### TrustedSecretInfo
* **trusted_secret_id** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **tags** (Struct)  `Required` 

    
* **schema** (string)  `Required` 

    
* **provider** (string)  `Required` 

    
* **service_account_id** (string)  `Required` 

    
* **project_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    <br>

### TrustedSecretQuery
* **domain_id** (string)  `Required` 

    
* **query** (Query) 

    
* **trusted_secret_id** (string) 

    
* **name** (string) 

    
* **schema** (string) 

    
* **provider** (string) 

    
* **service_account_id** (string) 

    <br>

### TrustedSecretRequest
* **trusted_secret_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    <br>

### TrustedSecretStatQuery
* **query** (StatisticsQuery)  `Required` 

    
* **domain_id** (string)  `Required` 

    <br>

### TrustedSecretsInfo
* **results** (TrustedSecretInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### UpdateTrustedSecretDataRequest
* **trusted_secret_id** (string)  `Required` 

    
* **data** (Struct)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **schema** (string) 

    <br>

### UpdateTrustedSecretRequest
* **trusted_secret_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **name** (string) 

    
* **tags** (Struct) 

    <br>
