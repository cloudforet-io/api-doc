---
title: "Domain"
linkTitle: "Domain"
weight: 3
bookFlatSection: true
---
# [Domain](#Domain)



>  **Package : spaceone.api.identity.v2**

<br>
<br>

## Domain





**Domain Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Domain#create) | [CreateDomainRequest](Domain#createdomainrequest) | [DomainInfo](Domain#domaininfo) |
| [**update**](./Domain#update) | [UpdateDomainRequest](Domain#updatedomainrequest) | [DomainInfo](Domain#domaininfo) |
| [**delete**](./Domain#delete) | [DomainRequest](Domain#domainrequest) | [Empty](Domain#empty) |
| [**enable**](./Domain#enable) | [DomainRequest](Domain#domainrequest) | [DomainInfo](Domain#domaininfo) |
| [**disable**](./Domain#disable) | [DomainRequest](Domain#domainrequest) | [DomainInfo](Domain#domaininfo) |
| [**get**](./Domain#get) | [DomainRequest](Domain#domainrequest) | [DomainInfo](Domain#domaininfo) |
| [**get_auth_info**](./Domain#get_auth_info) | [GetDomainAuthRequest](Domain#getdomainauthrequest) | [DomainAuthInfo](Domain#domainauthinfo) |
| [**get_public_key**](./Domain#get_public_key) | [AuthenticationRequest](Domain#authenticationrequest) | [AuthenticationResponse](Domain#authenticationresponse) |
| [**list**](./Domain#list) | [DomainSearchQuery](Domain#domainsearchquery) | [DomainsInfo](Domain#domainsinfo) |
| [**stat**](./Domain#stat) | [DomainStatQuery](Domain#domainstatquery) | [Struct](Domain#struct) |



    
<br>

### create





> **POST** /identity/v2/domain/create
>






    
<br>

### update





> **POST** /identity/v2/domain/update
>






    
<br>

### delete





> **POST** /identity/v2/domain/delete
>






    
<br>

### enable





> **POST** /identity/v2/domain/enable
>






    
<br>

### disable





> **POST** /identity/v2/domain/disable
>






    
<br>

### get





> **POST** /identity/v2/domain/get
>






    
<br>

### get_auth_info





> **POST** /identity/v2/domain/get-auth-info
>






    
<br>

### get_public_key










    
<br>

### list





> **POST** /identity/v2/domain/list
>






    
<br>

### stat










    


<br>
<br>

## Message



### Admin
* **user_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **password** (string)   `Required` 

    
* **email** (string)  

    
* **language** (string)  

    
* **timezone** (string)  

    
* **tags** (Struct)  

    <br>

### CreateDomainRequest
* **name** (string)   `Required` 

    
* **admin** (Admin)   `Required` 

    
* **tags** (Struct)  

    <br>

### DomainAuthInfo
* **domain_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **external_auth_state** (ExternalAuthState)   `Required` 

    
* **metadata** (Struct)   `Required` 

    <br>

### DomainInfo
* **domain_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **state** (State)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **deleted_at** (string)   `Required` 

    <br>

### DomainRequest
* **domain_id** (string)   `Required` 

    <br>

### DomainSearchQuery
* **query** (Query)  

    
* **domain_id** (string)  

    
* **name** (string)  

    
* **state** (State)  

    <br>

### DomainStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### DomainsInfo
* **results** (DomainInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### GetDomainAuthRequest
* **name** (string)   `Required` 

    <br>

### UpdateDomainRequest
* **domain_id** (string)   `Required` 

    
* **name** (string)  

    
* **tags** (Struct)  

    <br>
