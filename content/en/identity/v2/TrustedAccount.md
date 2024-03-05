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
| [**sync**](./TrustedAccount#sync) | [TrustedAccountRequest](TrustedAccount#trustedaccountrequest) | [Empty](TrustedAccount#empty) |
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


* **tags** (Struct)  


* **workspace_id** (string)  





{{< highlight json >}}
{
 "name": "Trusted Account",
 "data": {
   "account_id": "123456789",
  }
 "provider": "aws",
 "secret_schema_id": "aws-secret-access-key",
 "schedule": {
   "state": "ENABLED",
   "hours": [3, 15]
 },
 "resource_group": "DOMAIN",
 "workspace_id": "*"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### update





> **POST** /identity/v2/trusted-account/update
>






    
<br>

### update_secret_data





> **POST** /identity/v2/trusted-account/update-secret-data
>






    
<br>

### delete





> **POST** /identity/v2/trusted-account/delete
>






    
<br>

### sync





> **POST** /identity/v2/trusted-account/sync
>






    
<br>

### get





> **POST** /identity/v2/trusted-account/get
>






    
<br>

### list





> **POST** /identity/v2/trusted-account/list
>






    
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

    
* **name** (string)  

    
* **data** (Struct)  

    
* **schedule** (Scheduled)  

    
* **sync_options** (Struct)  

    
* **tags** (Struct)  

    <br>

### UpdateTrustedAccountSecretRequest
* **trusted_account_id** (string)   `Required` 

    
* **secret_schema_id** (string)   `Required` 

    
* **secret_data** (Struct)   `Required` 

    <br>
