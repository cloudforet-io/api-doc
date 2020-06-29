---
description:  
---
# Domain owner

>  **Package : spaceone.api.identity.v1**

## DomainOwner

{% hint style="info" %}
**DomainOwner Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [create](Domain-owner.md#create)| [CreateDomainOwner](Domain-owner.md#createdomainowner) | [DomainOwnerInfo](Domain-owner.md#domainownerinfo) |  |
| 2 | [update](Domain-owner.md#update)| [UpdateDomainOwner](Domain-owner.md#updatedomainowner) | [DomainOwnerInfo](Domain-owner.md#domainownerinfo) |  |
| 3 | [delete](Domain-owner.md#delete)| [DomainOwnerRequest](Domain-owner.md#domainownerrequest) |[google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 4 | [get](Domain-owner.md#get)| [GetDomainOwnerRequest](Domain-owner.md#getdomainownerrequest) | [DomainOwnerInfo](Domain-owner.md#domainownerinfo) |  |

### create
> **POST** /identity/v1/domain/{domain_id}/owner
>



| Type | Message |
| :--- | :--- |
| Request | [CreateDomainOwner](Domain-owner.md#createdomainowner) |
| Response |  [DomainOwnerInfo](Domain-owner.md#domainownerinfo)  |



### update
> **PUT**  /identity/v1/domain/{domain_id}/owner
>



| Type | Message |
| :--- | :--- |
| Request | [UpdateDomainOwner](Domain-owner.md#updatedomainowner) |
| Response |  [DomainOwnerInfo](Domain-owner.md#domainownerinfo)  |



### delete
> **DELETE** /identity/v1/domain/{domain_id}/owner
>



| Type | Message |
| :--- | :--- |
| Request | [DomainOwnerRequest](Domain-owner.md#domainownerrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |



### get
> **GET** /identity/v1/domain/{domain_id}/owner
>



| Type | Message |
| :--- | :--- |
| Request | [GetDomainOwnerRequest](Domain-owner.md#getdomainownerrequest) |
| Response |  [DomainOwnerInfo](Domain-owner.md#domainownerinfo)  |





## Message

### CreateDomainOwner
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | owner_id |string |✅ ||
| 2 | password |string |✅ ||
| 3 | name |string |❌ ||
| 4 | email |string |❌ ||
| 5 | mobile |string |❌ ||
| 6 | language |string |❌ ||
| 7 | timezone |string |❌ ||
| 8 | domain_id |string |✅ ||

### DomainOwnerInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | owner_id |string | ||
| 2 | name |string | ||
| 3 | email |string | ||
| 4 | mobile |string | ||
| 5 | language |string | ||
| 6 | timezone |string | ||
| 7 | last_accessed_at |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) | ||
| 8 | created_at |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) | ||
| 9 | domain_id |string | ||

### DomainOwnerRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | domain_id |string |✅ ||
| 2 | owner_id |string |✅ ||

### GetDomainOwnerRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | domain_id |string | |required|
| 2 | owner_id |string | |required|
| 3 | only |string | |optional|

### UpdateDomainOwner
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | owner_id |string |✅ ||
| 2 | password |string |❌ ||
| 3 | name |string |❌ ||
| 4 | email |string |❌ ||
| 5 | mobile |string |❌ ||
| 6 | language |string |❌ ||
| 7 | timezone |string |❌ ||
| 8 | domain_id |string |✅ ||
