---
title: "ServiceAccount"
linkTitle: "ServiceAccount"
weight: 3
bookFlatSection: true
---
# [ServiceAccount](#ServiceAccount)



>  **Package : spaceone.api.identity.v2**

<br>
<br>

## ServiceAccount





**ServiceAccount Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./ServiceAccount#create) | [CreateServiceAccountRequest](ServiceAccount#createserviceaccountrequest) | [ServiceAccountInfo](ServiceAccount#serviceaccountinfo) |
| [**update**](./ServiceAccount#update) | [UpdateServiceAccountRequest](ServiceAccount#updateserviceaccountrequest) | [ServiceAccountInfo](ServiceAccount#serviceaccountinfo) |
| [**change_trusted_account**](./ServiceAccount#change_trusted_account) | [ChangeTrustedAccountRequest](ServiceAccount#changetrustedaccountrequest) | [ServiceAccountInfo](ServiceAccount#serviceaccountinfo) |
| [**delete**](./ServiceAccount#delete) | [ServiceAccountRequest](ServiceAccount#serviceaccountrequest) | [Empty](ServiceAccount#empty) |
| [**get**](./ServiceAccount#get) | [ServiceAccountRequest](ServiceAccount#serviceaccountrequest) | [ServiceAccountInfo](ServiceAccount#serviceaccountinfo) |
| [**list**](./ServiceAccount#list) | [ServiceAccountSearchQuery](ServiceAccount#serviceaccountsearchquery) | [ServiceAccountsInfo](ServiceAccount#serviceaccountsinfo) |
| [**stat**](./ServiceAccount#stat) | [ServiceAccountStatQuery](ServiceAccount#serviceaccountstatquery) | [Struct](ServiceAccount#struct) |



    
<br>

### create





> **POST** /identity/v2/service-account/create
>






    
<br>

### update





> **POST** /identity/v2/service-account/update
>






    
<br>

### change_trusted_account





> **POST** /identity/v2/service-account/change-trusted-account
>






    
<br>

### delete





> **POST** /identity/v2/service-account/delete
>






    
<br>

### get





> **POST** /identity/v2/service-account/get
>






    
<br>

### list





> **POST** /identity/v2/service-account/list
>






    
<br>

### stat





> **POST** /identity/v2/service-account/stat
>






    


<br>
<br>

## Message



### ChangeTrustedAccountRequest
* **service_account_id** (string)   `Required` 

    
* **trusted_account_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    <br>

### CreateServiceAccountRequest
* **name** (string)   `Required` 

    
* **data** (Struct)   `Required` 

    
* **provider** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **project_id** (string)   `Required` 

    
* **trusted_account_id** (string)   `Required` 

  *+optional`*

    
* **tags** (Struct)  

    
* **domain_id** (string)  

    <br>

### ServiceAccountInfo
* **service_account_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **data** (Struct)   `Required` 

    
* **provider** (string)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **project_id** (string)   `Required` 

    
* **trusted_account_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    <br>

### ServiceAccountRequest
* **service_account_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    <br>

### ServiceAccountSearchQuery
* **domain_id** (string)   `Required` 

    
* **query** (Query)  

    
* **service_account_id** (string)  

    
* **name** (string)  

    
* **provider** (string)  

    
* **has_secret** (bool)  

    
* **workspace_id** (string)  

    
* **project_id** (string)  

    
* **trusted_account_id** (string)  

    <br>

### ServiceAccountStatQuery
* **query** (StatisticsQuery)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)  

    <br>

### ServiceAccountsInfo
* **results** (ServiceAccountInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### UpdateServiceAccountRequest
* **service_account_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **name** (string)  

    
* **data** (Struct)  

    
* **tags** (Struct)  

    
* **project_id** (string)  

    <br>
