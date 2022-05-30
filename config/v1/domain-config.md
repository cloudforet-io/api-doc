---
description: DomainConfig API which configure environments for domain
---
# Domain config

>  **Package : spaceone.api.config.v1**

## DomainConfig

{% hint style="info" %}
**DomainConfig Methods:**

{%  endhint %}


| Method | Request | Response |
| :-----: | :--------: | :--------: |
| [**create**](domain-config.md#create)|   [SetDomainConfigRequest](domain-config.md#setdomainconfigrequest) |   [DomainConfigInfo](domain-config.md#domainconfiginfo) |
| [**update**](domain-config.md#update)|   [SetDomainConfigRequest](domain-config.md#setdomainconfigrequest) |   [DomainConfigInfo](domain-config.md#domainconfiginfo) |
| [**set**](domain-config.md#set)|   [SetDomainConfigRequest](domain-config.md#setdomainconfigrequest) |   [DomainConfigInfo](domain-config.md#domainconfiginfo) |
| [**delete**](domain-config.md#delete)|   [DomainConfigRequest](domain-config.md#domainconfigrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**get**](domain-config.md#get)|   [GetDomainConfigRequest](domain-config.md#getdomainconfigrequest) |   [DomainConfigInfo](domain-config.md#domainconfiginfo) |
| [**list**](domain-config.md#list)|   [DomainConfigQuery](domain-config.md#domainconfigquery) |   [DomainConfigsInfo](domain-config.md#domainconfigsinfo) |
| [**stat**](domain-config.md#stat)|   [DomainConfigStatQuery](domain-config.md#domainconfigstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### create
> **POST** /config/v1/domain-configs
>


| Type | Message |
| :--- | :--- |
| Request | [SetDomainConfigRequest](domain-config.md#setdomainconfigrequest) |
| Response |  [DomainConfigInfo](domain-config.md#domainconfiginfo)  |
 
 

 
### update
> **PUT** /config/v1/domain-config/{name}
>


| Type | Message |
| :--- | :--- |
| Request | [SetDomainConfigRequest](domain-config.md#setdomainconfigrequest) |
| Response |  [DomainConfigInfo](domain-config.md#domainconfiginfo)  |
 
 

 
### set
> **POST** /config/v1/domain-config/{name}
>


| Type | Message |
| :--- | :--- |
| Request | [SetDomainConfigRequest](domain-config.md#setdomainconfigrequest) |
| Response |  [DomainConfigInfo](domain-config.md#domainconfiginfo)  |
 
 

 
### delete
> **DELETE** /config/v1/domain-config/{name}
>


| Type | Message |
| :--- | :--- |
| Request | [DomainConfigRequest](domain-config.md#domainconfigrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /config/v1/domain-config/{name}
>


| Type | Message |
| :--- | :--- |
| Request | [GetDomainConfigRequest](domain-config.md#getdomainconfigrequest) |
| Response |  [DomainConfigInfo](domain-config.md#domainconfiginfo)  |
 
 

 
### list
> **GET** /config/v1/domain-config
>
> **POST** /config/v1/domain-config/search



| Type | Message |
| :--- | :--- |
| Request | [DomainConfigQuery](domain-config.md#domainconfigquery) |
| Response |  [DomainConfigsInfo](domain-config.md#domainconfigsinfo)  |
 
 

 
### stat
> **POST** /config/v1/domain-config/stat
>


| Type | Message |
| :--- | :--- |
| Request | [DomainConfigStatQuery](domain-config.md#domainconfigstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### DomainConfigInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| name |string | |
| data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| domain_id |string | |
| created_at |string | |
| updated_at |string | |

### DomainConfigQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| name |string|❌| |
| domain_id |string|✅| |

### DomainConfigRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| name |string|✅| |
| domain_id |string|✅| |

### DomainConfigStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| domain_id |string|✅| |

### DomainConfigsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of DomainConfigInfo](domain-config.md#domainconfiginfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### GetDomainConfigRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| name |string|✅| |
| domain_id |string|✅| |
| only |list of string|❌| |

### SetDomainConfigRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| name |string|✅| |
| data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| domain_id |string|✅| |
