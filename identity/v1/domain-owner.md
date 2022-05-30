---
description:  
---
# Domain owner

>  **Package : spaceone.api.identity.v1**

## DomainOwner

{% hint style="info" %}
**DomainOwner Methods:**

{%  endhint %}


| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
| [**create**](domain-owner.md#create)|   [CreateDomainOwner](domain-owner.md#createdomainowner) |   [DomainOwnerInfo](domain-owner.md#domainownerinfo) |  |
| [**update**](domain-owner.md#update)|   [UpdateDomainOwner](domain-owner.md#updatedomainowner) |   [DomainOwnerInfo](domain-owner.md#domainownerinfo) |  |
| [**delete**](domain-owner.md#delete)|   [DomainOwnerRequest](domain-owner.md#domainownerrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| [**get**](domain-owner.md#get)|   [GetDomainOwnerRequest](domain-owner.md#getdomainownerrequest) |   [DomainOwnerInfo](domain-owner.md#domainownerinfo) |  |TEST

| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
|<div style="width:70px; text-align:center;">  [**create**](domain-owner.md#create) </div> | <div style="width:200px; text-align:center;">    [CreateDomainOwner](domain-owner.md#createdomainowner)  </div> | <div style="width:200px; text-align:center;">   [DomainOwnerInfo](domain-owner.md#domainownerinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**update**](domain-owner.md#update) </div> | <div style="width:200px; text-align:center;">    [UpdateDomainOwner](domain-owner.md#updatedomainowner)  </div> | <div style="width:200px; text-align:center;">   [DomainOwnerInfo](domain-owner.md#domainownerinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**delete**](domain-owner.md#delete) </div> | <div style="width:200px; text-align:center;">    [DomainOwnerRequest](domain-owner.md#domainownerrequest)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**get**](domain-owner.md#get) </div> | <div style="width:200px; text-align:center;">    [GetDomainOwnerRequest](domain-owner.md#getdomainownerrequest)  </div> | <div style="width:200px; text-align:center;">   [DomainOwnerInfo](domain-owner.md#domainownerinfo)  </div> | <div style="width:400px;">  </div> | 
 

 
### create
> **POST** /identity/v1/domain/{domain_id}/owner
>


| Type | Message |
| :--- | :--- |
| Request | [CreateDomainOwner](domain-owner.md#createdomainowner) |
| Response |  [DomainOwnerInfo](domain-owner.md#domainownerinfo)  |
 
 

 
### update
> **PUT**  /identity/v1/domain/{domain_id}/owner
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateDomainOwner](domain-owner.md#updatedomainowner) |
| Response |  [DomainOwnerInfo](domain-owner.md#domainownerinfo)  |
 
 

 
### delete
> **DELETE** /identity/v1/domain/{domain_id}/owner
>


| Type | Message |
| :--- | :--- |
| Request | [DomainOwnerRequest](domain-owner.md#domainownerrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /identity/v1/domain/{domain_id}/owner
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
| owner_id |string|❌| |
| password |string|✅| |
| name |string|❌| |
| email |string|❌| |
| language |string|❌| |
| timezone |string|❌| |
| domain_id |string|✅| |

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
| domain_id |string|✅| |
| owner_id |string|✅| |

### GetDomainOwnerRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| domain_id |string|✅| |
| owner_id |string|✅| |
| only |list of string|❌| |

### UpdateDomainOwner
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| owner_id |string|✅| |
| password |string|❌| |
| name |string|❌| |
| email |string|❌| |
| language |string|❌| |
| timezone |string|❌| |
| domain_id |string|✅| |
