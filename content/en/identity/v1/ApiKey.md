---
title: "ApiKey"
linkTitle: "ApiKey"
weight: 3
bookFlatSection: true
---
# [ApiKey](#ApiKey)



>  **Package : spaceone.api.identity.v1**

<br>
<br>

## ApiKey





**APIKey Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./APIKey#create) | [CreateAPIKeyRequest](APIKey#createapikeyrequest) | [APIKeyInfo](./APIKey#apikeyinfo) |
| [**enable**](./APIKey#enable) | [APIKeyRequest](APIKey#apikeyrequest) | [APIKeyInfo](./APIKey#apikeyinfo) |
| [**disable**](./APIKey#disable) | [APIKeyRequest](APIKey#apikeyrequest) | [APIKeyInfo](./APIKey#apikeyinfo) |
| [**delete**](./APIKey#delete) | [APIKeyRequest](APIKey#apikeyrequest) | [Empty](./APIKey#empty) |
| [**get**](./APIKey#get) | [GetAPIKeyRequest](APIKey#getapikeyrequest) | [APIKeyInfo](./APIKey#apikeyinfo) |
| [**list**](./APIKey#list) | [APIKeyQuery](APIKey#apikeyquery) | [APIKeysInfo](./APIKey#apikeysinfo) |
| [**stat**](./APIKey#stat) | [APIKeyStatQuery](APIKey#apikeystatquery) | [Struct](./APIKey#struct) |



    
<br>

### create





> **POST** /identity/v1/api-key/create
>






    
<br>

### enable





> **POST** /identity/v1/api-key/enable
>






    
<br>

### disable





> **POST** /identity/v1/api-key/disable
>






    
<br>

### delete





> **POST** /identity/v1/api-key/delete
>






    
<br>

### get





> **POST** /identity/v1/api-key/get
>






    
<br>

### list





> **POST** /identity/v1/api-key/list
>






    
<br>

### stat





> **POST** /identity/v1/api-key/stat
>






    


<br>
<br>

## Message



### APIKeyInfo
* **api_key_id** (string)  `Required` 

    
* **api_key** (string)  `Required` 

    
* **state** (State)  `Required` 

    
* **user_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **last_accessed_at** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    <br>

### APIKeyQuery
* **domain_id** (string)  `Required` 

    
* **query** (Query) 

    
* **api_key_id** (string) 

    
* **state** (State) 

    
* **user_id** (string) 

    <br>

### APIKeyRequest
* **api_key_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    <br>

### APIKeyStatQuery
* **query** (StatisticsQuery)  `Required` 

    
* **domain_id** (string)  `Required` 

    <br>

### APIKeysInfo
* **results** (APIKeyInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### CreateAPIKeyRequest
* **user_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    <br>

### GetAPIKeyRequest
* **api_key_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **only** (string) 

    <br>
