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
| [**create_app**](./ServiceAccount#create_app) | [CreateAppServiceAccountRequest](ServiceAccount#createappserviceaccountrequest) | [AppInfo](ServiceAccount#appinfo) |
| [**update**](./ServiceAccount#update) | [UpdateServiceAccountRequest](ServiceAccount#updateserviceaccountrequest) | [ServiceAccountInfo](ServiceAccount#serviceaccountinfo) |
| [**update_secret_data**](./ServiceAccount#update_secret_data) | [UpdateServiceAccountSecretRequest](ServiceAccount#updateserviceaccountsecretrequest) | [ServiceAccountInfo](ServiceAccount#serviceaccountinfo) |
| [**delete_secret_data**](./ServiceAccount#delete_secret_data) | [ServiceAccountRequest](ServiceAccount#serviceaccountrequest) | [ServiceAccountInfo](ServiceAccount#serviceaccountinfo) |
| [**delete**](./ServiceAccount#delete) | [ServiceAccountRequest](ServiceAccount#serviceaccountrequest) | [Empty](ServiceAccount#empty) |
| [**enable_app**](./ServiceAccount#enable_app) | [ServiceAccountRequest](ServiceAccount#serviceaccountrequest) | [AppInfo](ServiceAccount#appinfo) |
| [**disable_app**](./ServiceAccount#disable_app) | [ServiceAccountRequest](ServiceAccount#serviceaccountrequest) | [AppInfo](ServiceAccount#appinfo) |
| [**regenerate_app**](./ServiceAccount#regenerate_app) | [ServiceAccountRequest](ServiceAccount#serviceaccountrequest) | [AppInfo](ServiceAccount#appinfo) |
| [**delete_app**](./ServiceAccount#delete_app) | [ServiceAccountRequest](ServiceAccount#serviceaccountrequest) | [Empty](ServiceAccount#empty) |
| [**get**](./ServiceAccount#get) | [ServiceAccountRequest](ServiceAccount#serviceaccountrequest) | [ServiceAccountInfo](ServiceAccount#serviceaccountinfo) |
| [**list**](./ServiceAccount#list) | [ServiceAccountSearchQuery](ServiceAccount#serviceaccountsearchquery) | [ServiceAccountsInfo](ServiceAccount#serviceaccountsinfo) |
| [**stat**](./ServiceAccount#stat) | [ServiceAccountStatQuery](ServiceAccount#serviceaccountstatquery) | [Struct](ServiceAccount#struct) |



    
<br>

### create





> **POST** /identity/v2/service-account/create
>






    
<br>

### create_app





> **POST** /identity/v2/service-account/create-app
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

### enable_app





> **POST** /identity/v2/service-account/enable-app
>






    
<br>

### disable_app





> **POST** /identity/v2/service-account/disable-app
>






    
<br>

### regenerate_app





> **POST** /identity/v2/service-account/regenerate-app
>






    
<br>

### delete_app





> **POST** /identity/v2/service-account/delete-app
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



### CreateAppServiceAccountRequest
* **service_account_id** (string)   `Required` 

    
* **options** (Struct)  

    <br>

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

    
* **options** (Struct)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **reference_id** (string)   `Required` 

    
* **is_managed** (bool)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **project_id** (string)   `Required` 

    
* **trusted_account_id** (string)   `Required` 

    
* **secret_schema_id** (string)   `Required` 

    
* **secret_id** (string)   `Required` 

    
* **app_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **last_synced_at** (string)   `Required` 

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

    
* **secret_schema_id** (string)   `Required` 

    
* **secret_data** (Struct)   `Required` 

    
* **trusted_account_id** (string)  

    <br>
