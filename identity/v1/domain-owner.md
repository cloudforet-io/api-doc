---
description:  
---
# Domain owner

>  **Package : spaceone.api.identity.v1**

## DomainOwner

{% hint style="info" %}
**DomainOwner Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](domain-owner.md#create)|   [CreateDomainOwner](domain-owner.md#createdomainowner) |   [DomainOwnerInfo](domain-owner.md#domainownerinfo) |
| [**update**](domain-owner.md#update)|   [UpdateDomainOwner](domain-owner.md#updatedomainowner) |   [DomainOwnerInfo](domain-owner.md#domainownerinfo) |
| [**delete**](domain-owner.md#delete)|   [DomainOwnerRequest](domain-owner.md#domainownerrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**get**](domain-owner.md#get)|   [GetDomainOwnerRequest](domain-owner.md#getdomainownerrequest) |   [DomainOwnerInfo](domain-owner.md#domainownerinfo) | 
 

 
### create
> **POST** /identity/v1/domain-owner/create
>


| Type | Message |
| :--- | :--- |
| Request | [CreateDomainOwner](domain-owner.md#createdomainowner) |
| Response |  [DomainOwnerInfo](domain-owner.md#domainownerinfo)  |
 
 

 
### update
> **POST** /identity/v1/domain-owner/update
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateDomainOwner](domain-owner.md#updatedomainowner) |
| Response |  [DomainOwnerInfo](domain-owner.md#domainownerinfo)  |
 
 

 
### delete
> **POST** /identity/v1/domain-owner/delete
>


| Type | Message |
| :--- | :--- |
| Request | [DomainOwnerRequest](domain-owner.md#domainownerrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **POST** /identity/v1/domain-owner/get
>


| Type | Message |
| :--- | :--- |
| Request | [GetDomainOwnerRequest](domain-owner.md#getdomainownerrequest) |
| Response |  [DomainOwnerInfo](domain-owner.md#domainownerinfo)  |


## 

## Message

### CreateDomainOwner
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| owner_id |string|✘| |
| password |string|✔| |
| name |string|✘| |
| email |string|✘| |
| language |string|✘| |
| timezone |string|✘| |
| domain_id |string|✔| |

### DomainOwnerInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| owner_id |string | |
| name |string | |
| email |string | |
| language |string | |
| timezone |string | |
| last_accessed_at |string | |
| created_at |string | |
| domain_id |string | |

### DomainOwnerRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| domain_id |string|✔| |
| owner_id |string|✔| |

### GetDomainOwnerRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| domain_id |string|✔| |
| owner_id |string|✔| |
| only |list of string|✘| |

### UpdateDomainOwner
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| owner_id |string|✔| |
| password |string|✘| |
| name |string|✘| |
| email |string|✘| |
| language |string|✘| |
| timezone |string|✘| |
| domain_id |string|✔| |
