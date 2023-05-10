---
title: "Domain"
linkTitle: "Domain"
weight: 3
bookFlatSection: true
---
# [Domain](#Domain)



>  **Package : spaceone.api.identity.v1**

<br>
<br>

## Domain





**Domain Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Domain#create) | [CreateDomainRequest](Domain#createdomainrequest) | [DomainInfo](./Domain#domaininfo) |
| [**update**](./Domain#update) | [UpdateDomainRequest](Domain#updatedomainrequest) | [DomainInfo](./Domain#domaininfo) |
| [**change_auth_plugin**](./Domain#change_auth_plugin) | [ChangeAuthRequest](Domain#changeauthrequest) | [DomainInfo](./Domain#domaininfo) |
| [**update_plugin**](./Domain#update_plugin) | [UpdatePluginRequest](Domain#updatepluginrequest) | [DomainInfo](./Domain#domaininfo) |
| [**verify_plugin**](./Domain#verify_plugin) | [DomainRequest](Domain#domainrequest) | [Empty](./Domain#empty) |
| [**delete**](./Domain#delete) | [DomainRequest](Domain#domainrequest) | [Empty](./Domain#empty) |
| [**enable**](./Domain#enable) | [DomainRequest](Domain#domainrequest) | [DomainInfo](./Domain#domaininfo) |
| [**disable**](./Domain#disable) | [DomainRequest](Domain#domainrequest) | [DomainInfo](./Domain#domaininfo) |
| [**get**](./Domain#get) | [GetDomainRequest](Domain#getdomainrequest) | [DomainInfo](./Domain#domaininfo) |
| [**list**](./Domain#list) | [DomainQuery](Domain#domainquery) | [DomainsInfo](./Domain#domainsinfo) |
| [**stat**](./Domain#stat) | [DomainStatQuery](Domain#domainstatquery) | [Struct](./Domain#struct) |
| [**get_public_key**](./Domain#get_public_key) | [AuthenticationRequest](Domain#authenticationrequest) | [AuthenticationResponse](./Domain#authenticationresponse) |



    
<br>

### create





> **POST** /identity/v1/domain/create
>






    
<br>

### update





> **POST** /identity/v1/domain/update
>






    
<br>

### change_auth_plugin





> **POST** /identity/v1/domain/change-auth-plugin
>






    
<br>

### update_plugin





> **POST** /identity/v1/domain/update-plugin
>






    
<br>

### verify_plugin





> **POST** /identity/v1/domain/verify-plugin
>






    
<br>

### delete





> **POST** /identity/v1/domain/delete
>






    
<br>

### enable





> **POST** /identity/v1/domain/enable
>






    
<br>

### disable





> **POST** /identity/v1/domain/disable
>






    
<br>

### get





> **POST** /identity/v1/domain/get
>






    
<br>

### list





> **POST** /identity/v1/domain/list
>






    
<br>

### stat





> **POST** /identity/v1/domain/stat
>






    
<br>

### get_public_key





> **POST** /identity/v1/domain/get-public-key
>






    


<br>
<br>

## Message



### ChangeAuthRequest
* **domain_id** (string)  `Required` 

    
* **plugin_info** (PluginInfo) 

    
* **release_auth_plugin** (bool) 

    <br>

### CreateDomainRequest
* **name** (string)  `Required` 

    
* **plugin_info** (PluginInfo) 

    
* **config** (Struct) 

    
* **tags** (Struct) 

    <br>

### DomainInfo
* **domain_id** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **state** (State)  `Required` 

    
* **plugin_info** (PluginInfo)  `Required` 

    
* **config** (Struct)  `Required` 

    
* **tags** (Struct)  `Required` 

    
* **created_at** (string)  `Required` 

    
* **deleted_at** (string)  `Required` 

    <br>

### DomainQuery
* **query** (Query) 

    
* **domain_id** (string) 

    
* **name** (string) 

    
* **state** (State) 

    <br>

### DomainRequest
* **domain_id** (string)  `Required` 

    <br>

### DomainStatQuery
* **query** (StatisticsQuery)  `Required` 

    <br>

### DomainsInfo
* **results** (DomainInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### GetDomainRequest
* **domain_id** (string)  `Required` 

    
* **only** (string) 

    <br>

### PluginInfo
* **plugin_id** (string)  `Required` 

    
* **version** (string)  `Required` 

    
* **secret_id** (string)  `Required` 

    
* **options** (Struct)  `Required` 

    
* **secret_data** (Struct)  `Required` 

    
* **schema** (string)  `Required` 

    
* **metadata** (Struct)  `Required` 

    
* **upgrade_mode** (UpgradeMode)  `Required` 

    <br>

### UpdateDomainRequest
* **domain_id** (string)  `Required` 

    
* **plugin_info** (PluginInfo) 

    
* **config** (Struct) 

    
* **tags** (Struct) 

    <br>

### UpdatePluginRequest
* **domain_id** (string)  `Required` 

    
* **version** (string) 

    
* **options** (Struct) 

    
* **upgrade_mode** (UpgradeMode) 

    <br>
