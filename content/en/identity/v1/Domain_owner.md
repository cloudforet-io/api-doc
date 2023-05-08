---
title: "Domain_owner"
linkTitle: "Domain_owner"
weight: 3
bookFlatSection: true
---
# [Domain_owner](#Domain_owner)



>  **Package : spaceone.api.identity.v1**

<br>
<br>

## Domain_owner


**DomainOwner Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./DomainOwner#create) | [CreateDomainOwner](DomainOwner#createdomainowner) | [DomainOwnerInfo](./DomainOwner#domainownerinfo) |
| [**update**](./DomainOwner#update) | [UpdateDomainOwner](DomainOwner#updatedomainowner) | [DomainOwnerInfo](./DomainOwner#domainownerinfo) |
| [**delete**](./DomainOwner#delete) | [DomainOwnerRequest](DomainOwner#domainownerrequest) | [Empty](./DomainOwner#empty) |
| [**get**](./DomainOwner#get) | [GetDomainOwnerRequest](DomainOwner#getdomainownerrequest) | [DomainOwnerInfo](./DomainOwner#domainownerinfo) |



    
<br>

### create

> **POST** /identity/v1/domain-owner/create
>




 {{< tabs " create " >}}




{{< /tabs >}}

    
<br>

### update

> **POST** /identity/v1/domain-owner/update
>




 {{< tabs " update " >}}




{{< /tabs >}}

    
<br>

### delete

> **POST** /identity/v1/domain-owner/delete
>




 {{< tabs " delete " >}}




{{< /tabs >}}

    
<br>

### get

> **POST** /identity/v1/domain-owner/get
>




 {{< tabs " get " >}}




{{< /tabs >}}

    


<br>
<br>

## Message



### CreateDomainOwner
* **owner_id** (string)  `Required` 

  *is_required: false*

    
* **password** (string)  `Required` 

  *is_required: true*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **email** (string)  `Required` 

  *is_required: false*

    
* **language** (string)  `Required` 

  *is_required: false*

    
* **timezone** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### DomainOwnerInfo
* **owner_id** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **email** (string)  `Required` 

    
* **language** (string)  `Required` 

    
* **timezone** (string)  `Required` 

    
* **last_accessed_at** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    <br>

### DomainOwnerRequest
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **owner_id** (string)  `Required` 

  *is_required: true*

    <br>

### GetDomainOwnerRequest
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **owner_id** (string)  `Required` 

  *is_required: true*

    
* **only** (string)  `Required` 

  *is_required: false*

    <br>

### UpdateDomainOwner
* **owner_id** (string)  `Required` 

  *is_required: true*

    
* **password** (string)  `Required` 

  *is_required: false*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **email** (string)  `Required` 

  *is_required: false*

    
* **language** (string)  `Required` 

  *is_required: false*

    
* **timezone** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>
