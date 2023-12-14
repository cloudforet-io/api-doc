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
| [**update_secret_data**](./ServiceAccount#update_secret_data) | [UpdateServiceAccountSecretRequest](ServiceAccount#updateserviceaccountsecretrequest) | [ServiceAccountInfo](ServiceAccount#serviceaccountinfo) |
| [**delete_secret_data**](./ServiceAccount#delete_secret_data) | [ServiceAccountRequest](ServiceAccount#serviceaccountrequest) | [ServiceAccountInfo](ServiceAccount#serviceaccountinfo) |
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

### update_secret_data





> **POST** /identity/v2/service-account/update-secret-data
>






    
<br>

### delete_secret_data





> **POST** /identity/v2/service-account/delete-secret-data
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



### CreateServiceAccountRequest
* **name** (string)   `Required` 

    
* **data** (Struct)   `Required` 

    
* **provider** (string)   `Required` 

    
* **project_id** (string)   `Required` 

    
* **secret_schema_id** (string)  

    
* **secret_data** (Struct)  

    
* **tags** (Struct)  

    
* **trusted_account_id** (string)  

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

    
* **secret_schema_id** (string)   `Required` 

    
* **secret_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    <br>

### ServiceAccountRequest
* **service_account_id** (string)   `Required` 

    <br>

### ServiceAccountSearchQuery
* **query** (Query)  

    
* **service_account_id** (string)  

    
* **name** (string)  

    
* **provider** (string)  

    
* **workspace_id** (string)  

    
* **project_id** (string)  

    
* **trusted_account_id** (string)  

    
* **secret_schema_id** (string)  

    
* **secret_id** (string)  

    <br>

### ServiceAccountStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### ServiceAccountsInfo
* **results** (ServiceAccountInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### UpdateServiceAccountRequest
* **service_account_id** (string)   `Required` 

    
* **name** (string)  

    
* **data** (Struct)  

    
* **tags** (Struct)  

    
* **project_id** (string)  

    <br>

### UpdateServiceAccountSecretRequest
* **service_account_id** (string)   `Required` 

    
* **secret_data** (Struct)   `Required` 

    
* **trusted_account_id** (string)   `Required` 

    <br>
