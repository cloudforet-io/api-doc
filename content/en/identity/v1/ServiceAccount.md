---
title: "ServiceAccount"
linkTitle: "ServiceAccount"
weight: 3
bookFlatSection: true
---
# [ServiceAccount](#ServiceAccount)



>  **Package : spaceone.api.identity.v1**

<br>
<br>

## ServiceAccount





**ServiceAccount Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./ServiceAccount#create) | [CreateServiceAccountRequest](ServiceAccount#createserviceaccountrequest) | [ServiceAccountInfo](./ServiceAccount#serviceaccountinfo) |
| [**update**](./ServiceAccount#update) | [UpdateServiceAccountRequest](ServiceAccount#updateserviceaccountrequest) | [ServiceAccountInfo](./ServiceAccount#serviceaccountinfo) |
| [**delete**](./ServiceAccount#delete) | [ServiceAccountRequest](ServiceAccount#serviceaccountrequest) | [Empty](./ServiceAccount#empty) |
| [**get**](./ServiceAccount#get) | [GetServiceAccountRequest](ServiceAccount#getserviceaccountrequest) | [ServiceAccountInfo](./ServiceAccount#serviceaccountinfo) |
| [**list**](./ServiceAccount#list) | [ServiceAccountQuery](ServiceAccount#serviceaccountquery) | [ServiceAccountsInfo](./ServiceAccount#serviceaccountsinfo) |
| [**stat**](./ServiceAccount#stat) | [ServiceAccountStatQuery](ServiceAccount#serviceaccountstatquery) | [Struct](./ServiceAccount#struct) |



    
<br>

### create





> **POST** /identity/v1/service-account/create
>






    
<br>

### update





> **POST** /identity/v1/service-account/update
>






    
<br>

### delete





> **POST** /identity/v1/service-account/delete
>






    
<br>

### get





> **POST** /identity/v1/service-account/get
>






    
<br>

### list





> **POST** /identity/v1/service-accounts/list
>






    
<br>

### stat





> **POST** /identity/v1/service-accounts/stat
>






    


<br>
<br>

## Message



### CreateServiceAccountRequest
* **name** (string)  `Required` 

    
* **data** (Struct)  `Required` 

    
* **provider** (string)  `Required` 

    
* **service_account_type** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **project_id** (string) 

    
* **tags** (Struct) 

    
* **trusted_service_account_id** (string) 

    <br>

### GetServiceAccountRequest
* **service_account_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **only** (string) 

    <br>

### ServiceAccountInfo
* **service_account_id** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **service_account_type** (string)  `Required` 

    
* **data** (Struct)  `Required` 

    
* **provider** (string)  `Required` 

    
* **trusted_service_account_id** (string)  `Required` 

    
* **project_info** (ProjectInfo)  `Required` 

    
* **scope** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **tags** (Struct)  `Required` 

    
* **created_at** (string)  `Required` 

    <br>

### ServiceAccountQuery
* **query** (Query) 

    
* **service_account_id** (string) 

    
* **name** (string) 

    
* **service_account_type** (string) 

    
* **provider** (string) 

    
* **trusted_service_account_id** (string) 

    
* **project_id** (string) 

    
* **scope** (string) 

    
* **domain_id** (string) 

    <br>

### ServiceAccountRequest
* **service_account_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    <br>

### ServiceAccountStatQuery
* **query** (StatisticsQuery)  `Required` 

    
* **domain_id** (string)  `Required` 

    <br>

### ServiceAccountsInfo
* **results** (ServiceAccountInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### UpdateServiceAccountRequest
* **service_account_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **name** (string) 

    
* **data** (Struct) 

    
* **project_id** (string) 

    
* **tags** (Struct) 

    
* **trusted_service_account_id** (string) 

    
* **release_trusted_service_account** (bool) 

    <br>
