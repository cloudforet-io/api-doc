---
description: DomainConfig API which configure environments for domain
---
# Domain config

>  **Package : spaceone.api.config.v1**

## DomainConfig

{% hint style="info" %}
**DomainConfig Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**create**](domain-config.md#create)|   [SetDomainConfigRequest](domain-config.md#setdomainconfigrequest) |   [DomainConfigInfo](domain-config.md#domainconfiginfo) |  |
| 2 | [**update**](domain-config.md#update)|   [SetDomainConfigRequest](domain-config.md#setdomainconfigrequest) |   [DomainConfigInfo](domain-config.md#domainconfiginfo) |  |
| 3 | [**set**](domain-config.md#set)|   [SetDomainConfigRequest](domain-config.md#setdomainconfigrequest) |   [DomainConfigInfo](domain-config.md#domainconfiginfo) |  |
| 4 | [**delete**](domain-config.md#delete)|   [DomainConfigRequest](domain-config.md#domainconfigrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 5 | [**get**](domain-config.md#get)|   [GetDomainConfigRequest](domain-config.md#getdomainconfigrequest) |   [DomainConfigInfo](domain-config.md#domainconfiginfo) |  |
| 6 | [**list**](domain-config.md#list)|   [DomainConfigQuery](domain-config.md#domainconfigquery) |   [DomainConfigsInfo](domain-config.md#domainconfigsinfo) |  |
| 7 | [**stat**](domain-config.md#stat)|   [DomainConfigStatQuery](domain-config.md#domainconfigstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 

 
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
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | name |string | |
| 2 | data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| 3 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| 4 | domain_id |string | |
| 5 | created_at |string | |
| 6 | updated_at |string | |

### DomainConfigQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| 2 | name |string|❌| |
| 3 | domain_id |string|✅| |

### DomainConfigRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | name |string|✅| |
| 2 | domain_id |string|✅| |

### DomainConfigStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| 2 | domain_id |string|✅| |

### DomainConfigsInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[list of DomainConfigInfo](domain-config.md#domainconfiginfo) | |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### GetDomainConfigRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | name |string|✅| |
| 2 | domain_id |string|✅| |
| 3 | only |list of string|❌| |

### SetDomainConfigRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | name |string|✅| |
| 2 | data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| 3 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 4 | domain_id |string|✅| |
