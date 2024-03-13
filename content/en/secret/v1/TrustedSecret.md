---
title: "TrustedSecret"
linkTitle: "TrustedSecret"
weight: 3
bookFlatSection: true
---
# [TrustedSecret](#TrustedSecret)
Trusted secret is a resource that stores and manages credentials.
Trusted secret is merged with linked secret and used to access data in other microservices.


>  **Package : spaceone.api.secret.v1**

<br>
<br>

## TrustedSecret





**TrustedSecret Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./TrustedSecret#create) | [CreateTrustedSecretRequest](TrustedSecret#createtrustedsecretrequest) | [TrustedSecretInfo](TrustedSecret#trustedsecretinfo) |
| [**update**](./TrustedSecret#update) | [UpdateTrustedSecretRequest](TrustedSecret#updatetrustedsecretrequest) | [TrustedSecretInfo](TrustedSecret#trustedsecretinfo) |
| [**delete**](./TrustedSecret#delete) | [TrustedSecretRequest](TrustedSecret#trustedsecretrequest) | [Empty](TrustedSecret#empty) |
| [**update_data**](./TrustedSecret#update_data) | [UpdateTrustedSecretDataRequest](TrustedSecret#updatetrustedsecretdatarequest) | [Empty](TrustedSecret#empty) |
| [**get_data**](./TrustedSecret#get_data) | [GetTrustedSecretDataRequest](TrustedSecret#gettrustedsecretdatarequest) | [TrustedSecretDataInfo](TrustedSecret#trustedsecretdatainfo) |
| [**get**](./TrustedSecret#get) | [TrustedSecretRequest](TrustedSecret#trustedsecretrequest) | [TrustedSecretInfo](TrustedSecret#trustedsecretinfo) |
| [**list**](./TrustedSecret#list) | [TrustedSecretQuery](TrustedSecret#trustedsecretquery) | [TrustedSecretsInfo](TrustedSecret#trustedsecretsinfo) |
| [**stat**](./TrustedSecret#stat) | [TrustedSecretStatQuery](TrustedSecret#trustedsecretstatquery) | [Struct](TrustedSecret#struct) |



    
<br>

### create

Create a new trusted secret.
Created trusted secret is encrypted and stored securely.



> **POST** /secret/v1/trusted-secret/create
>





 {{< tabs " create " >}}

 {{< tab "Request Example" >}}



[CreateTrustedSecretRequest](./TrustedSecret#createtrustedsecretrequest)

* **name** (string)   `Required` 


* **data** (Struct)   `Required` 


* **resource_group** (ResourceGroup)   `Required` 


* **schema_id** (string)  


* **tags** (Struct)  


* **workspace_id** (string)  


* **trusted_account_id** (string)  





{{< highlight json >}}
{
   "name": "Cloudforet Broker Account - Managed",
   "data": "********",
   "schema_id": "aws_access_key",
   "trusted_account_id": "trusted-sa-123456789012",
   "tags": {}
   "resource_group": "DOMAIN"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[TrustedSecretInfo](#TRUSTEDSECRETINFO)
* **trusted_secret_id** (string)   `Required` 

* **name** (string)   `Required` 

* **schema_id** (string)   `Required` 

* **tags** (Struct)   `Required` 

* **provider** (string)   `Required` 

* **resource_group** (ResourceGroup)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **trusted_account_id** (string)   `Required` 

* **created_at** (string)   `Required` 



{{< highlight json >}}
{
   "trusted_secret_id": "trusted-secret-123456789012",
   "name": "aws-dev",
   "tags": {},
   "schema": "aws_access_key",
   "provider": "aws",
   "resource_group": "DOMAIN",
   "trusted_account_id": "ta-123456789012",
   "domain_id": "domain-123456789012",
   "created_at": "2022-01-01T06:10:14.851Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### update

Updates a specific trusted secret's information.
You can only change the 'name' and 'tags', and to change the data you must use the update_data API.



> **POST** /secret/v1/trusted-secret/update
>





 {{< tabs " update " >}}

 {{< tab "Request Example" >}}



[UpdateTrustedSecretRequest](./TrustedSecret#updatetrustedsecretrequest)

* **trusted_secret_id** (string)   `Required` 


* **name** (string)  


* **tags** (Struct)  





{{< highlight json >}}
{
   "trusted_secret_id": "trusted-secret-123456789012",
   "name": "aws-dev2",
   "tags": { "a": "b"}
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[TrustedSecretInfo](#TRUSTEDSECRETINFO)
* **trusted_secret_id** (string)   `Required` 

* **name** (string)   `Required` 

* **schema_id** (string)   `Required` 

* **tags** (Struct)   `Required` 

* **provider** (string)   `Required` 

* **resource_group** (ResourceGroup)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **trusted_account_id** (string)   `Required` 

* **created_at** (string)   `Required` 



{{< highlight json >}}
{
   "trusted_secret_id": "trusted-secret-123456789012",
   "name": "aws-dev",
   "tags": {},
   "schema": "aws_access_key",
   "provider": "aws",
   "resource_group": "DOMAIN",
   "trusted_account_id": "ta-123456789012",
   "domain_id": "domain-123456789012",
   "created_at": "2022-01-01T06:10:14.851Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### delete

Deletes a specific trusted secret.
If a trusted secret is attached to a Secret, it cannot be deleted.



> **POST** /secret/v1/trusted-secret/delete
>





 {{< tabs " delete " >}}

 {{< tab "Request Example" >}}



[TrustedSecretRequest](./TrustedSecret#trustedsecretrequest)

* **trusted_secret_id** (string)   `Required` 





{{< highlight json >}}
{
   "trusted_secret_id": "trusted-secret-123456789012"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### update_data

Updates a specific trusted secret's data.
Updated trusted secret is encrypted and stored securely.



> **POST** /secret/v1/trusted-secret/update-data
>





 {{< tabs " update_data " >}}

 {{< tab "Request Example" >}}



[UpdateTrustedSecretDataRequest](./TrustedSecret#updatetrustedsecretdatarequest)

* **trusted_secret_id** (string)   `Required` 


* **schema_id** (string)   `Required` 


* **data** (Struct)   `Required` 





{{< highlight json >}}
{
   "trusted_secret_id": "trusted-secret-12345abcde",
   "data": "********",
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### get_data

Get a specific secret's data.
This API is for internal system use only.







 {{< tabs " get_data " >}}

 {{< tab "Request Example" >}}



[GetTrustedSecretDataRequest](./TrustedSecret#gettrustedsecretdatarequest)

* **trusted_secret_id** (string)   `Required` 


* **domain_id** (string)   `Required` 





{{< highlight json >}}
{
   "trusted_secret_id": "ta-123456789012",
   "domain_id": "domain-12345abcde"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### get

Get a specific trusted secret's information.



> **POST** /secret/v1/trusted-secret/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[TrustedSecretRequest](./TrustedSecret#trustedsecretrequest)

* **trusted_secret_id** (string)   `Required` 





{{< highlight json >}}
{
   "trusted_secret_id": "trusted-secret-123456789012"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[TrustedSecretInfo](#TRUSTEDSECRETINFO)
* **trusted_secret_id** (string)   `Required` 

* **name** (string)   `Required` 

* **schema_id** (string)   `Required` 

* **tags** (Struct)   `Required` 

* **provider** (string)   `Required` 

* **resource_group** (ResourceGroup)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **trusted_account_id** (string)   `Required` 

* **created_at** (string)   `Required` 



{{< highlight json >}}
{
   "trusted_secret_id": "trusted-secret-123456789012",
   "name": "aws-dev",
   "tags": {},
   "schema": "aws_access_key",
   "provider": "aws",
   "resource_group": "DOMAIN",
   "trusted_account_id": "ta-123456789012",
   "domain_id": "domain-123456789012",
   "created_at": "2022-01-01T06:10:14.851Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### list

Queries a list of trusted secrets.
You can use a query to get a filtered list of trusted secrets.



> **POST** /secret/v1/trusted-secret/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[TrustedSecretQuery](./TrustedSecret#trustedsecretquery)

* **query** (Query)  


* **trusted_secret_id** (string)  


* **name** (string)  


* **schema_id** (string)  


* **provider** (string)  


* **workspace_id** (string)  


* **trusted_account_id** (string)  





{{< highlight json >}}
{
   "query": {}
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[TrustedSecretsInfo](#TRUSTEDSECRETSINFO)
* **results** (TrustedSecretInfo)  `Repeated`   `Required` 

* **total_count** (int32)   `Required` 



{{< highlight json >}}
{
   "results": [
       {
           "trusted_secret_id": "trusted-secret-12345abcde",
           "name": "Cloudforet Broker Account - Managed",
           "schema_id": "aws-secret-access-key",
           "tags": {"foo": "bar"},
           "provider": "aws",
           "resource_group": "DOMAIN",
           "trusted_account_id": "ta-12345abcde",
           "domain_id": "domain-12345abcde",
           "created_at": "2022-01-01T06:10:14Z"
       },
       {
           "trusted_secret_id": "trusted-secret-56789abcde",
           "name": "Customer Broker Account",
           "schema_id": "aws-secret-access-key",
           "provider": "aws",
           "resource_group": "WORKSPACE",
           "trusted_account_id": "ta-56789abcde",
           "domain_id": "domain-12345abcde",
           "workspace_id": "workspace-12345abcde",
           "created_at": "2023-11-04T00:00:00Z"
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
* **name** (string)   `Required` 

    
* **data** (Struct)   `Required` 

    
* **resource_group** (ResourceGroup)   `Required` 

    
* **schema_id** (string)  

    
* **tags** (Struct)  

    
* **workspace_id** (string)  

    
* **trusted_account_id** (string)  

    <br>

### GetTrustedSecretDataRequest
* **trusted_secret_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### TrustedSecretDataInfo
* **encrypted** (bool)   `Required` 

    
* **encrypt_options** (Struct)   `Required` 

    
* **data** (Struct)   `Required` 

    <br>

### TrustedSecretInfo
* **trusted_secret_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **schema_id** (string)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **provider** (string)   `Required` 

    
* **resource_group** (ResourceGroup)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **trusted_account_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    <br>

### TrustedSecretQuery
* **query** (Query)  

    
* **trusted_secret_id** (string)  

    
* **name** (string)  

    
* **schema_id** (string)  

    
* **provider** (string)  

    
* **workspace_id** (string)  

    
* **trusted_account_id** (string)  

    <br>

### TrustedSecretRequest
* **trusted_secret_id** (string)   `Required` 

    <br>

### TrustedSecretStatQuery
* **query** (StatisticsQuery)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### TrustedSecretsInfo
* **results** (TrustedSecretInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### UpdateTrustedSecretDataRequest
* **trusted_secret_id** (string)   `Required` 

    
* **schema_id** (string)   `Required` 

    
* **data** (Struct)   `Required` 

    <br>

### UpdateTrustedSecretRequest
* **trusted_secret_id** (string)   `Required` 

    
* **name** (string)  

    
* **tags** (Struct)  

    <br>
