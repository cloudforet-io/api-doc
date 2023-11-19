---
title: "TrustedServiceAccount"
linkTitle: "TrustedServiceAccount"
weight: 3
bookFlatSection: true
---
# [TrustedServiceAccount](#TrustedServiceAccount)



>  **Package : spaceone.api.identity.v2**

<br>
<br>

## TrustedServiceAccount





**TrustedServiceAccount Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./TrustedServiceAccount#create) | [CreateTrustedServiceAccountRequest](TrustedServiceAccount#createtrustedserviceaccountrequest) | [TrustedServiceAccountInfo](TrustedServiceAccount#trustedserviceaccountinfo) |
| [**update**](./TrustedServiceAccount#update) | [UpdateTrustedServiceAccountRequest](TrustedServiceAccount#updatetrustedserviceaccountrequest) | [TrustedServiceAccountInfo](TrustedServiceAccount#trustedserviceaccountinfo) |
| [**delete**](./TrustedServiceAccount#delete) | [TrustedServiceAccountRequest](TrustedServiceAccount#trustedserviceaccountrequest) | [Empty](TrustedServiceAccount#empty) |
| [**get**](./TrustedServiceAccount#get) | [TrustedServiceAccountRequest](TrustedServiceAccount#trustedserviceaccountrequest) | [TrustedServiceAccountInfo](TrustedServiceAccount#trustedserviceaccountinfo) |
| [**list**](./TrustedServiceAccount#list) | [TrustedServiceAccountSearchQuery](TrustedServiceAccount#trustedserviceaccountsearchquery) | [TrustedServiceAccountsInfo](TrustedServiceAccount#trustedserviceaccountsinfo) |
| [**stat**](./TrustedServiceAccount#stat) | [TrustedServiceAccountStatQuery](TrustedServiceAccount#trustedserviceaccountstatquery) | [Struct](TrustedServiceAccount#struct) |



    
<br>

### create





> **POST** /identity/v2/trusted-account/create
>






    
<br>

### update





> **POST** /identity/v2/trusted-account/update
>






    
<br>

### delete





> **POST** /identity/v2/trusted-account/delete
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



### CreateTrustedServiceAccountRequest
* **name** (string)   `Required` 

    
* **data** (Struct)   `Required` 

    
* **provider** (string)   `Required` 

    
* **scope** (Scope)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **tags** (Struct)  

    
* **workspace_id** (string)  

    <br>

### TrustedServiceAccountInfo
* **trusted_service_account_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **data** (Struct)   `Required` 

    
* **provider** (string)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **scope** (Scope)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    <br>

### TrustedServiceAccountRequest
* **trusted_service_account_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)  

    <br>

### TrustedServiceAccountSearchQuery
* **domain_id** (string)   `Required` 

    
* **query** (Query)  

    
* **trusted_service_account_id** (string)  

    
* **name** (string)  

    
* **provider** (string)  

    
* **scope** (Scope)  

    
* **workspace_id** (string)  

    <br>

### TrustedServiceAccountStatQuery
* **query** (StatisticsQuery)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)  

    <br>

### TrustedServiceAccountsInfo
* **results** (TrustedServiceAccountInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### UpdateTrustedServiceAccountRequest
* **trusted_service_account_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **name** (string)  

    
* **data** (Struct)  

    
* **tags** (Struct)  

    
* **workspace_id** (string)  

    <br>
