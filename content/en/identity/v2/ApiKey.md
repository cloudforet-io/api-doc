---
title: "ApiKey"
linkTitle: "ApiKey"
weight: 3
bookFlatSection: true
---
# [ApiKey](#ApiKey)



>  **Package : spaceone.api.identity.v2**

<br>
<br>

## ApiKey





**APIKey Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./APIKey#create) | [CreateAPIKeyRequest](APIKey#createapikeyrequest) | [APIKeyInfo](APIKey#apikeyinfo) |
| [**update**](./APIKey#update) | [UpdateAPIKeyRequest](APIKey#updateapikeyrequest) | [APIKeyInfo](APIKey#apikeyinfo) |
| [**enable**](./APIKey#enable) | [APIKeyRequest](APIKey#apikeyrequest) | [APIKeyInfo](APIKey#apikeyinfo) |
| [**disable**](./APIKey#disable) | [APIKeyRequest](APIKey#apikeyrequest) | [APIKeyInfo](APIKey#apikeyinfo) |
| [**delete**](./APIKey#delete) | [APIKeyRequest](APIKey#apikeyrequest) | [Empty](APIKey#empty) |
| [**verify**](./APIKey#verify) | [VerifyAPIKeyRequest](APIKey#verifyapikeyrequest) | [APIKeyInfo](APIKey#apikeyinfo) |
| [**get**](./APIKey#get) | [APIKeyRequest](APIKey#apikeyrequest) | [APIKeyInfo](APIKey#apikeyinfo) |
| [**list**](./APIKey#list) | [APIKeySearchQuery](APIKey#apikeysearchquery) | [APIKeysInfo](APIKey#apikeysinfo) |
| [**stat**](./APIKey#stat) | [APIKeyStatQuery](APIKey#apikeystatquery) | [Struct](APIKey#struct) |



    
<br>

### create





> **POST** /identity/v2/api-key/create
>






    
<br>

### update





> **POST** /identity/v2/api-key/update
>






    
<br>

### enable





> **POST** /identity/v2/api-key/enable
>






    
<br>

### disable





> **POST** /identity/v2/api-key/disable
>






    
<br>

### delete





> **POST** /identity/v2/api-key/delete
>






    
<br>

### verify





> **POST** /identity/v2/api-key/verify
>






    
<br>

### get





> **POST** /identity/v2/api-key/get
>






    
<br>

### list





> **POST** /identity/v2/api-key/list
>






    
<br>

### stat





> **POST** /identity/v2/api-key/stat
>






    


<br>
<br>

## Message



### APIKeyInfo
* **api_key_id** (string)   `Required` 

    
* **api_key** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **state** (State)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **user_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **last_accessed_at** (string)   `Required` 

    
* **expired_at** (string)   `Required` 

    <br>

### APIKeyRequest
* **api_key_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### APIKeySearchQuery
* **domain_id** (string)   `Required` 

    
* **query** (Query)  

    
* **api_key_id** (string)  

    
* **state** (State)  

    
* **user_id** (string)  

    <br>

### APIKeyStatQuery
* **query** (StatisticsQuery)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### APIKeysInfo
* **results** (APIKeyInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### CreateAPIKeyRequest
* **user_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **name** (string)  

    
* **expired_at** (string)  

    <br>

### UpdateAPIKeyRequest
* **api_key_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **name** (string)  

    <br>

### VerifyAPIKeyRequest
* **api_key_id** (string)   `Required` 

    
* **api_key_type** (API_KEY_TYPE)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **app_id** (string)   `Required` 

    
* **user_id** (string)   `Required` 

    <br>
