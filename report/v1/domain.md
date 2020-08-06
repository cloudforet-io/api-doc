---
description:  
---
# Domain

>  **Package : spaceone.api.report.v1**

## Domain

{% hint style="info" %}
**Domain Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**get**](domain.md#get)|   [GetDomainRequest](domain.md#getdomainrequest) |   [DomainInfo](domain.md#domaininfo) |  |
| 2 | [**list**](domain.md#list)|   [DomainQuery](domain.md#domainquery) |   [DomainsInfo](domain.md#domainsinfo) |  |
| 3 | [**enable**](domain.md#enable)|   [EnableDomainRequest](domain.md#enabledomainrequest) |   [DomainInfo](domain.md#domaininfo) |  |
| 4 | [**disable**](domain.md#disable)|   [DisableDomainRequest](domain.md#disabledomainrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  | 
 

 
### get
> **GET** /report/v1/domain/{domain_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetDomainRequest](domain.md#getdomainrequest) |
| Response |  [DomainInfo](domain.md#domaininfo)  |
 
 

 
### list
> **GET** /report/v1/domains
>
> **POST** /report/v1/domains/search



| Type | Message |
| :--- | :--- |
| Request | [DomainQuery](domain.md#domainquery) |
| Response |  [DomainsInfo](domain.md#domainsinfo)  |
 
 

 
### enable
> **PUT** /report/v1/domain/{domain_id}/enable
>


| Type | Message |
| :--- | :--- |
| Request | [EnableDomainRequest](domain.md#enabledomainrequest) |
| Response |  [DomainInfo](domain.md#domaininfo)  |
 
 

 
### disable
> **PUT** /report/v1/domain/{domain_id}/disable
>


| Type | Message |
| :--- | :--- |
| Request | [DisableDomainRequest](domain.md#disabledomainrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |


## 

## Message

### DisableDomainRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | domain_id |string|✅| |

### DomainInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | domain_id |string| |
| 2 | register_templates |string| |
| 3 | relation_resources |[RelationResourceInfo](domain.md#relationresourceinfo)| |

### DomainQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | domain_id |string|❌| |
| 2 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |

### DomainsInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[DomainInfo](domain.md#domaininfo)| |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)| |

### EnableDomainRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | domain_id |string|✅| |

### GetDomainRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | domain_id |string|✅| |
| 2 | only |string|❌| |

### IdentityInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | key |string| |
| 2 | value |string| |

### RelationResourceInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | service |string| |
| 2 | resource |string| |
| 3 | identity |[IdentityInfo](domain.md#identityinfo)| |
| 4 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| |
