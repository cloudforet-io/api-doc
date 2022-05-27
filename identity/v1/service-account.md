---
description:  
---
# Service account

>  **Package : spaceone.api.identity.v1**

## ServiceAccount

{% hint style="info" %}
**ServiceAccount Methods:**

{%  endhint %}


| Method | Request | Response | Description |
| :--- | :--- | :--- | :--- |
| [**create**](service-account.md#create)|   [CreateServiceAccountRequest](service-account.md#createserviceaccountrequest) |   [ServiceAccountInfo](service-account.md#serviceaccountinfo) |  |
| [**update**](service-account.md#update)|   [UpdateServiceAccountRequest](service-account.md#updateserviceaccountrequest) |   [ServiceAccountInfo](service-account.md#serviceaccountinfo) |  |
| [**delete**](service-account.md#delete)|   [ServiceAccountRequest](service-account.md#serviceaccountrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| [**get**](service-account.md#get)|   [GetServiceAccountRequest](service-account.md#getserviceaccountrequest) |   [ServiceAccountInfo](service-account.md#serviceaccountinfo) |  |
| [**list**](service-account.md#list)|   [ServiceAccountQuery](service-account.md#serviceaccountquery) |   [ServiceAccountsInfo](service-account.md#serviceaccountsinfo) |  |
| [**stat**](service-account.md#stat)|   [ServiceAccountStatQuery](service-account.md#serviceaccountstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 

 
### create
> **POST** /identity/v1/service-accounts
>


| Type | Message |
| :--- | :--- |
| Request | [CreateServiceAccountRequest](service-account.md#createserviceaccountrequest) |
| Response |  [ServiceAccountInfo](service-account.md#serviceaccountinfo)  |
 
 

 
### update
> **PUT** /identity/v1/service-account/{service_account_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateServiceAccountRequest](service-account.md#updateserviceaccountrequest) |
| Response |  [ServiceAccountInfo](service-account.md#serviceaccountinfo)  |
 
 

 
### delete
> **DELETE** /identity/v1/service-account/{service_account_id}
>


| Type | Message |
| :--- | :--- |
| Request | [ServiceAccountRequest](service-account.md#serviceaccountrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /identity/v1/service-account/{service_account_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetServiceAccountRequest](service-account.md#getserviceaccountrequest) |
| Response |  [ServiceAccountInfo](service-account.md#serviceaccountinfo)  |
 
 

 
### list
> **GET** /identity/v1/service-accounts
>
> **POST** /identity/v1/service-accounts/search



| Type | Message |
| :--- | :--- |
| Request | [ServiceAccountQuery](service-account.md#serviceaccountquery) |
| Response |  [ServiceAccountsInfo](service-account.md#serviceaccountsinfo)  |
 
 

 
### stat
> **POST** /identity/v1/service-accounts/stat
>


| Type | Message |
| :--- | :--- |
| Request | [ServiceAccountStatQuery](service-account.md#serviceaccountstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CreateServiceAccountRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| name |string|✅| |
| data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| provider |string|✅| |
| project_id |string|❌| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| domain_id |string|✅| |

### GetServiceAccountRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| service_account_id |string|✅| |
| domain_id |string|✅| |
| only |list of string|❌| |

### ServiceAccountInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| service_account_id |string | |
| name |string | |
| data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| provider |string | |
| project_info |[ProjectInfo](service-account.md#projectinfo) | |
| domain_id |string | |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| created_at |string | |

### ServiceAccountQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| service_account_id |string|❌| |
| name |string|❌| |
| provider |string|❌| |
| project_id |string|❌| |
| domain_id |string|❌| |

### ServiceAccountRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| service_account_id |string|✅| |
| domain_id |string|✅| |

### ServiceAccountStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| domain_id |string|✅| |

### ServiceAccountsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of ServiceAccountInfo](service-account.md#serviceaccountinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### UpdateServiceAccountRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| service_account_id |string|✅| |
| name |string|❌| |
| data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| project_id |string|❌| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| domain_id |string|✅| |
| release_project |bool|❌| |
