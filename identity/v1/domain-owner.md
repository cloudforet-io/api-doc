---
description: null
---

# Domain Owner

> **Package : spaceone.api.identity.v1**

## DomainOwner

{% hint style="info" %}
**DomainOwner Methods:**
{% endhint %}

| NO | Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [create](domain-owner.md#create) | [CreateDomainOwner](domain-owner.md#createdomainowner) | [DomainOwnerInfo](domain-owner.md#domainownerinfo) |  |
| 2 | [update](domain-owner.md#update) | [UpdateDomainOwner](domain-owner.md#updatedomainowner) | [DomainOwnerInfo](domain-owner.md#domainownerinfo) |  |
| 3 | [delete](domain-owner.md#delete) | [DomainOwnerRequest](domain-owner.md#domainownerrequest) | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |  |
| 4 | [get](domain-owner.md#get) | [GetDomainOwnerRequest](domain-owner.md#getdomainownerrequest) | [DomainOwnerInfo](domain-owner.md#domainownerinfo) |  |

### create

> **POST** /identity/v1/domain/{domain\_id}/owner

| Type | Message |
| :--- | :--- |
| Request | [CreateDomainOwner](domain-owner.md#createdomainowner) |
| Response | [DomainOwnerInfo](domain-owner.md#domainownerinfo) |

### update

> **PUT** /identity/v1/domain/{domain\_id}/owner

| Type | Message |
| :--- | :--- |
| Request | [UpdateDomainOwner](domain-owner.md#updatedomainowner) |
| Response | [DomainOwnerInfo](domain-owner.md#domainownerinfo) |

### delete

> **DELETE** /identity/v1/domain/{domain\_id}/owner

| Type | Message |
| :--- | :--- |
| Request | [DomainOwnerRequest](domain-owner.md#domainownerrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |

### get

> **GET** /identity/v1/domain/{domain\_id}/owner

| Type | Message |
| :--- | :--- |
| Request | [GetDomainOwnerRequest](domain-owner.md#getdomainownerrequest) |
| Response | [DomainOwnerInfo](domain-owner.md#domainownerinfo) |

## Message

### CreateDomainOwner

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | owner\_id | string | ✅ |  |
| 2 | password | string | ✅ |  |
| 3 | name | string | ❌ |  |
| 4 | email | string | ❌ |  |
| 5 | mobile | string | ❌ |  |
| 6 | language | string | ❌ |  |
| 7 | timezone | string | ❌ |  |
| 8 | domain\_id | string | ✅ |  |

### DomainOwnerInfo

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | owner\_id | string |  |  |
| 2 | name | string |  |  |
| 3 | email | string |  |  |
| 4 | mobile | string |  |  |
| 5 | language | string |  |  |
| 6 | timezone | string |  |  |
| 7 | last\_accessed\_at | [google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) |  |  |
| 8 | created\_at | [google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) |  |  |
| 9 | domain\_id | string |  |  |

### DomainOwnerRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | domain\_id | string | ✅ |  |
| 2 | owner\_id | string | ✅ |  |

### GetDomainOwnerRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | domain\_id | string |  | required |
| 2 | owner\_id | string |  | required |
| 3 | only | string |  | optional |

### UpdateDomainOwner

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | owner\_id | string | ✅ |  |
| 2 | password | string | ❌ |  |
| 3 | name | string | ❌ |  |
| 4 | email | string | ❌ |  |
| 5 | mobile | string | ❌ |  |
| 6 | language | string | ❌ |  |
| 7 | timezone | string | ❌ |  |
| 8 | domain\_id | string | ✅ |  |

