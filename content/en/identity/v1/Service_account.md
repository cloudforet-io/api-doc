---
title: "Service_account"
linkTitle: "Service_account"
weight: 3
bookFlatSection: true
---
# [Service_account](#Service_account)



>  **Package : spaceone.api.identity.v1**

<br>
<br>

## Service_account





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

  *is_required: true*

    
* **data** (Struct)  `Required` 

  *is_required: true*

    
* **provider** (string)  `Required` 

  *is_required: true*

    
* **project_id** (string)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **service_account_type** (string)  `Required` 

  *is_required: true*

    
* **trusted_service_account_id** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### GetServiceAccountRequest
* **service_account_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **only** (string)  `Required` 

  *is_required: false*

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
* **query** (Query)  `Required` 

  *is_required: false*

    
* **service_account_id** (string)  `Required` 

  *is_required: false*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **service_account_type** (string)  `Required` 

  *is_required: false*

    
* **provider** (string)  `Required` 

  *is_required: false*

    
* **trusted_service_account_id** (string)  `Required` 

  *is_required: false*

    
* **project_id** (string)  `Required` 

  *is_required: false*

    
* **scope** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: false*

    <br>

### ServiceAccountRequest
* **service_account_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### ServiceAccountStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### ServiceAccountsInfo
* **results** (ServiceAccountInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### UpdateServiceAccountRequest
* **service_account_id** (string)  `Required` 

  *is_required: true*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **data** (Struct)  `Required` 

  *is_required: false*

    
* **project_id** (string)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **trusted_service_account_id** (string)  `Required` 

  *is_required: false*

    
* **release_trusted_service_account** (bool)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>
