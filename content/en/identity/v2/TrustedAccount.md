---
title: "TrustedAccount"
linkTitle: "TrustedAccount"
weight: 3
bookFlatSection: true
---
# [TrustedAccount](#TrustedAccount)



>  **Package : spaceone.api.identity.v2**

<br>
<br>

## TrustedAccount





**TrustedAccount Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./TrustedAccount#create) | [CreateTrustedAccountRequest](TrustedAccount#createtrustedaccountrequest) | [TrustedAccountInfo](TrustedAccount#trustedaccountinfo) |
| [**update**](./TrustedAccount#update) | [UpdateTrustedAccountRequest](TrustedAccount#updatetrustedaccountrequest) | [TrustedAccountInfo](TrustedAccount#trustedaccountinfo) |
| [**update_secret_data**](./TrustedAccount#update_secret_data) | [UpdateTrustedAccountSecretRequest](TrustedAccount#updatetrustedaccountsecretrequest) | [TrustedAccountInfo](TrustedAccount#trustedaccountinfo) |
| [**delete**](./TrustedAccount#delete) | [TrustedAccountRequest](TrustedAccount#trustedaccountrequest) | [Empty](TrustedAccount#empty) |
| [**sync**](./TrustedAccount#sync) | [TrustedAccountRequest](TrustedAccount#trustedaccountrequest) | [JobInfo](TrustedAccount#jobinfo) |
| [**get**](./TrustedAccount#get) | [TrustedAccountRequest](TrustedAccount#trustedaccountrequest) | [TrustedAccountInfo](TrustedAccount#trustedaccountinfo) |
| [**list**](./TrustedAccount#list) | [TrustedAccountSearchQuery](TrustedAccount#trustedaccountsearchquery) | [TrustedAccountsInfo](TrustedAccount#trustedaccountsinfo) |
| [**stat**](./TrustedAccount#stat) | [TrustedAccountStatQuery](TrustedAccount#trustedaccountstatquery) | [Struct](TrustedAccount#struct) |



    
<br>

### create





> **POST** /identity/v2/trusted-account/create
>





 {{< tabs " create " >}}

 {{< tab "Request Example" >}}



[CreateTrustedAccountRequest](./TrustedAccount#createtrustedaccountrequest)

* **name** (string)   `Required` 


* **data** (Struct)   `Required` 

  *Base Information of Trusted Account. It depends on provider.*


* **provider** (string)   `Required` 


* **secret_schema_id** (string)   `Required` 


* **secret_data** (Struct)   `Required` 


* **resource_group** (ResourceGroup)   `Required` 


* **schedule** (Scheduled)  


* **sync_options** (Struct)  


* **plugin_options** (Struct)  


* **tags** (Struct)  


* **workspace_id** (string)  





{{< highlight json >}}
{
 "name": "Trusted Account",
 "data": {
   "account_id": "a1b2c3d4e5f6"
  },
 "provider": "aws",
 "secret_schema_id": "aws-secret-access-key",
 "secret_data": {
   "aws_access_key_id": "a1b2c3d4e5f6",
   "aws_secret_access_key": "a1b2c3d4e5f6"
 },
 "schedule": {
   "state": "ENABLED",
   "hours": [3, 15]
 },
 "resource_group": "DOMAIN"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[TrustedAccountInfo](#TRUSTEDACCOUNTINFO)
* **trusted_account_id** (string)   `Required` 

* **name** (string)   `Required` 

* **data** (Struct)   `Required` 

* **provider** (string)   `Required` 

* **schedule** (Scheduled)   `Required` 

* **sync_options** (Struct)   `Required` 

* **plugin_options** (Struct)   `Required` 

* **tags** (Struct)   `Required` 

* **resource_group** (ResourceGroup)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **secret_schema_id** (string)   `Required` 

* **trusted_secret_id** (string)   `Required` 

* **created_at** (string)   `Required` 



{{< highlight json >}}
{
 "created_at": "2024-11-18T07:53:57.897Z",
 "data": {
   "account_id": "a1b2c3d4e5f6"
 },
 "domain_id": "domain-a1b2c3d4e5f6",
 "name": "Trusted Account",
 "provider": "aws",
 "resource_group": "DOMAIN",
 "schedule": {
   "hours": [3, 15],
   "state": "ENABLED"
 },
 "secret_schema_id": "aws-secret-access-key",
 "trusted_account_id": "ta-a1b2c3d4e5f6",
 "trusted_secret_id": "trusted-secret-a1b2c3d4e5f6",
 "workspace_id": "*"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### update





> **POST** /identity/v2/trusted-account/update
>





 {{< tabs " update " >}}

 {{< tab "Request Example" >}}



[UpdateTrustedAccountRequest](./TrustedAccount#updatetrustedaccountrequest)

* **trusted_account_id** (string)   `Required` 


* **tags** (Struct)   `Required` 


* **name** (string)  


* **data** (Struct)  


* **schedule** (Scheduled)  


* **sync_options** (Struct)  


* **plugin_options** (Struct)  





{{< highlight json >}}
{
 "trusted_account_id": "ta-a1b2c3d4e5f6",
 "name": "Trusted Account"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[TrustedAccountInfo](#TRUSTEDACCOUNTINFO)
* **trusted_account_id** (string)   `Required` 

* **name** (string)   `Required` 

* **data** (Struct)   `Required` 

* **provider** (string)   `Required` 

* **schedule** (Scheduled)   `Required` 

* **sync_options** (Struct)   `Required` 

* **plugin_options** (Struct)   `Required` 

* **tags** (Struct)   `Required` 

* **resource_group** (ResourceGroup)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **secret_schema_id** (string)   `Required` 

* **trusted_secret_id** (string)   `Required` 

* **created_at** (string)   `Required` 



{{< highlight json >}}
{
 "created_at": "2024-11-18T07:53:57.897Z",
 "data": {
   "account_id": "a1b2c3d4e5f6"
 },
 "domain_id": "domain-a1b2c3d4e5f6",
 "name": "Trusted Account",
 "provider": "aws",
 "resource_group": "DOMAIN",
 "schedule": {
   "hours": [3, 15],
   "state": "ENABLED"
 },
 "secret_schema_id": "aws-secret-access-key",
 "trusted_account_id": "ta-a1b2c3d4e5f6",
 "trusted_secret_id": "trusted-secret-a1b2c3d4e5f6",
 "workspace_id": "*"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### update_secret_data





> **POST** /identity/v2/trusted-account/update-secret-data
>





 {{< tabs " update_secret_data " >}}

 {{< tab "Request Example" >}}



[UpdateTrustedAccountSecretRequest](./TrustedAccount#updatetrustedaccountsecretrequest)

* **trusted_account_id** (string)   `Required` 


* **secret_schema_id** (string)   `Required` 


* **secret_data** (Struct)   `Required` 





{{< highlight json >}}
{
 "trusted_account_id": "ta-a1b2c3d4e5f6",
 "secretSchemaId": "aws-secret-access-key",
 "secretData": {
   "aws_access_key_id": "a1b2c3d4e5f6",
   "aws_secret_access_key": "a1b2c3d4e5f6"
 }
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[TrustedAccountInfo](#TRUSTEDACCOUNTINFO)
* **trusted_account_id** (string)   `Required` 

* **name** (string)   `Required` 

* **data** (Struct)   `Required` 

* **provider** (string)   `Required` 

* **schedule** (Scheduled)   `Required` 

* **sync_options** (Struct)   `Required` 

* **plugin_options** (Struct)   `Required` 

* **tags** (Struct)   `Required` 

* **resource_group** (ResourceGroup)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **secret_schema_id** (string)   `Required` 

* **trusted_secret_id** (string)   `Required` 

* **created_at** (string)   `Required` 



{{< highlight json >}}
{
 "created_at": "2024-11-18T07:53:57.897Z",
 "data": {
   "account_id": "a1b2c3d4e5f6"
 },
 "domain_id": "domain-a1b2c3d4e5f6",
 "name": "Trusted Account",
 "provider": "aws",
 "resource_group": "DOMAIN",
 "schedule": {
   "hours": [3, 15],
   "state": "ENABLED"
 },
 "secret_schema_id": "aws-secret-access-key",
 "trusted_account_id": "ta-a1b2c3d4e5f6",
 "trusted_secret_id": "trusted-secret-a1b2c3d4e5f6",
 "workspace_id": "*"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### delete





> **POST** /identity/v2/trusted-account/delete
>





 {{< tabs " delete " >}}

 {{< tab "Request Example" >}}



[TrustedAccountRequest](./TrustedAccount#trustedaccountrequest)

* **trusted_account_id** (string)   `Required` 





{{< highlight json >}}
{
 "trusted_account_id": "ta-a1b2c3d4e5f6"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### sync





> **POST** /identity/v2/trusted-account/sync
>





 {{< tabs " sync " >}}

 {{< tab "Request Example" >}}



[TrustedAccountRequest](./TrustedAccount#trustedaccountrequest)

* **trusted_account_id** (string)   `Required` 





{{< highlight json >}}
{
 "trusted_account_id": "ta-a1b2c3d4e5f6"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### get





> **POST** /identity/v2/trusted-account/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[TrustedAccountRequest](./TrustedAccount#trustedaccountrequest)

* **trusted_account_id** (string)   `Required` 





{{< highlight json >}}
{
 "trusted_account_id": "ta-a1b2c3d4e5f6"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[TrustedAccountInfo](#TRUSTEDACCOUNTINFO)
* **trusted_account_id** (string)   `Required` 

* **name** (string)   `Required` 

* **data** (Struct)   `Required` 

* **provider** (string)   `Required` 

* **schedule** (Scheduled)   `Required` 

* **sync_options** (Struct)   `Required` 

* **plugin_options** (Struct)   `Required` 

* **tags** (Struct)   `Required` 

* **resource_group** (ResourceGroup)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **secret_schema_id** (string)   `Required` 

* **trusted_secret_id** (string)   `Required` 

* **created_at** (string)   `Required` 



{{< highlight json >}}
{
 "created_at": "2024-11-18T07:53:57.897Z",
 "data": {
   "account_id": "a1b2c3d4e5f6"
 },
 "domain_id": "domain-a1b2c3d4e5f6",
 "name": "Trusted Account",
 "provider": "aws",
 "resource_group": "DOMAIN",
 "schedule": {
   "hours": [3, 15],
   "state": "ENABLED"
 },
 "secret_schema_id": "aws-secret-access-key",
 "trusted_account_id": "ta-a1b2c3d4e5f6",
 "trusted_secret_id": "trusted-secret-a1b2c3d4e5f6",
 "workspace_id": "*"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### list





> **POST** /identity/v2/trusted-account/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[TrustedAccountSearchQuery](./TrustedAccount#trustedaccountsearchquery)

* **query** (Query)  


* **trusted_account_id** (string)  


* **name** (string)  


* **provider** (string)  


* **workspace_id** (string)  


* **secret_schema_id** (string)  


* **trusted_secret_id** (string)  





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

[TrustedAccountsInfo](#TRUSTEDACCOUNTSINFO)
* **results** (TrustedAccountInfo)  `Repeated`   `Required` 

* **total_count** (int32)   `Required` 



{{< highlight json >}}
{
 "results": [
   {
     "created_at": "2024-11-18T07:47:02.789Z",
     "data": {
       "account_id": "a1b2c3d4e5f6"
     },
     "domain_id": "domain-a1b2c3d4e5f6",
     "name": "Trusted Account",
     "provider": "aws",
     "resource_group": "DOMAIN",
     "secret_schema_id": "aws-secret-access-key",
     "trusted_account_id": "ta-a1b2c3d4e5f6",
     "trusted_secret_id": "trusted-secret-a1b2c3d4e5f6",
     "workspace_id": "*"
   },
   {
     "created_at": "2024-11-18T07:10:17.114Z",
     "data": {
       "account_id": "g7h8i9j1k2l3"
     },
     "domain_id": "domain-a1b2c3d4e5f6",
     "name": "Wonny Trusted Account",
     "provider": "aws",
     "resource_group": "DOMAIN",
     "secret_schema_id": "aws-secret-access-key",
     "trusted_account_id": "ta-g7h8i9j1k2l3",
     "trusted_secret_id": "trusted-secret-g7h8i9j1k2l3",
     "workspace_id": "*"
   }
 ],
 "total_count": 2
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### stat





> **POST** /identity/v2/trusted-account/stat
>






    


<br>
<br>

## Message



### CreateTrustedAccountRequest
* **name** (string)   `Required` 

    
* **data** (Struct)   `Required` 

  *Base Information of Trusted Account. It depends on provider.*

    
* **provider** (string)   `Required` 

    
* **secret_schema_id** (string)   `Required` 

    
* **secret_data** (Struct)   `Required` 

    
* **resource_group** (ResourceGroup)   `Required` 

    
* **schedule** (Scheduled)  

    
* **sync_options** (Struct)  

    
* **plugin_options** (Struct)  

    
* **tags** (Struct)  

    
* **workspace_id** (string)  

    <br>

### Scheduled
* **state** (ScheduledState)   `Required` 

    
* **hours** (int32)  `Repeated`    `Required` 

    <br>

### TrustedAccountInfo
* **trusted_account_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **data** (Struct)   `Required` 

    
* **provider** (string)   `Required` 

    
* **schedule** (Scheduled)   `Required` 

    
* **sync_options** (Struct)   `Required` 

    
* **plugin_options** (Struct)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **resource_group** (ResourceGroup)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **secret_schema_id** (string)   `Required` 

    
* **trusted_secret_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    <br>

### TrustedAccountRequest
* **trusted_account_id** (string)   `Required` 

    <br>

### TrustedAccountSearchQuery
* **query** (Query)  

    
* **trusted_account_id** (string)  

    
* **name** (string)  

    
* **provider** (string)  

    
* **workspace_id** (string)  

    
* **secret_schema_id** (string)  

    
* **trusted_secret_id** (string)  

    <br>

### TrustedAccountStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### TrustedAccountsInfo
* **results** (TrustedAccountInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### UpdateTrustedAccountRequest
* **trusted_account_id** (string)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **name** (string)  

    
* **data** (Struct)  

    
* **schedule** (Scheduled)  

    
* **sync_options** (Struct)  

    
* **plugin_options** (Struct)  

    <br>

### UpdateTrustedAccountSecretRequest
* **trusted_account_id** (string)   `Required` 

    
* **secret_schema_id** (string)   `Required` 

    
* **secret_data** (Struct)   `Required` 

    <br>
