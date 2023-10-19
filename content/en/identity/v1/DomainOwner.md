---
title: "DomainOwner"
linkTitle: "DomainOwner"
weight: 3
bookFlatSection: true
---
# [DomainOwner](#DomainOwner)



>  **Package : spaceone.api.identity.v1**

<br>
<br>

## DomainOwner





**DomainOwner Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./DomainOwner#create) | [CreateDomainOwner](DomainOwner#createdomainowner) | [DomainOwnerInfo](DomainOwner#domainownerinfo) |
| [**update**](./DomainOwner#update) | [UpdateDomainOwner](DomainOwner#updatedomainowner) | [DomainOwnerInfo](DomainOwner#domainownerinfo) |
| [**delete**](./DomainOwner#delete) | [DomainOwnerRequest](DomainOwner#domainownerrequest) | [Empty](DomainOwner#empty) |
| [**get**](./DomainOwner#get) | [GetDomainOwnerRequest](DomainOwner#getdomainownerrequest) | [DomainOwnerInfo](DomainOwner#domainownerinfo) |



    
<br>

### create










    
<br>

### update





> **POST** /identity/v1/domain-owner/update
>






    
<br>

### delete










    
<br>

### get





> **POST** /identity/v1/domain-owner/get
>






    


<br>
<br>

## Message



### CreateDomainOwner
* **password** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **owner_id** (string)  

    
* **name** (string)  

    
* **email** (string)  

    
* **language** (string)  

    
* **timezone** (string)  

    <br>

### DomainOwnerInfo
* **owner_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **email** (string)   `Required` 

    
* **language** (string)   `Required` 

    
* **timezone** (string)   `Required` 

    
* **last_accessed_at** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### DomainOwnerRequest
* **domain_id** (string)   `Required` 

    
* **owner_id** (string)   `Required` 

    <br>

### GetDomainOwnerRequest
* **domain_id** (string)   `Required` 

    
* **owner_id** (string)   `Required` 

    
* **only** (string)  `Repeated`   

    <br>

### UpdateDomainOwner
* **owner_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **password** (string)  

    
* **name** (string)  

    
* **email** (string)  

    
* **language** (string)  

    
* **timezone** (string)  

    <br>
