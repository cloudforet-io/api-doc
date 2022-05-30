---
description:  
---
# Service account

>  **Package : spaceone.api.identity.v1**

## ServiceAccount

{% hint style="info" %}
**ServiceAccount Methods:**

{%  endhint %}


| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
| [**create**](service-account.md#create)|   [CreateServiceAccountRequest](service-account.md#createserviceaccountrequest) |   [ServiceAccountInfo](service-account.md#serviceaccountinfo) |  |
| [**update**](service-account.md#update)|   [UpdateServiceAccountRequest](service-account.md#updateserviceaccountrequest) |   [ServiceAccountInfo](service-account.md#serviceaccountinfo) |  |
| [**delete**](service-account.md#delete)|   [ServiceAccountRequest](service-account.md#serviceaccountrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| [**get**](service-account.md#get)|   [GetServiceAccountRequest](service-account.md#getserviceaccountrequest) |   [ServiceAccountInfo](service-account.md#serviceaccountinfo) |  |
| [**list**](service-account.md#list)|   [ServiceAccountQuery](service-account.md#serviceaccountquery) |   [ServiceAccountsInfo](service-account.md#serviceaccountsinfo) |  |
| [**stat**](service-account.md#stat)|   [ServiceAccountStatQuery](service-account.md#serviceaccountstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |TEST

| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
|<div style="width:70px; text-align:center;">  [**create**](service-account.md#create) </div> | <div style="width:200px; text-align:center;">    [CreateServiceAccountRequest](service-account.md#createserviceaccountrequest)  </div> | <div style="width:200px; text-align:center;">   [ServiceAccountInfo](service-account.md#serviceaccountinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**update**](service-account.md#update) </div> | <div style="width:200px; text-align:center;">    [UpdateServiceAccountRequest](service-account.md#updateserviceaccountrequest)  </div> | <div style="width:200px; text-align:center;">   [ServiceAccountInfo](service-account.md#serviceaccountinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**delete**](service-account.md#delete) </div> | <div style="width:200px; text-align:center;">    [ServiceAccountRequest](service-account.md#serviceaccountrequest)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**get**](service-account.md#get) </div> | <div style="width:200px; text-align:center;">    [GetServiceAccountRequest](service-account.md#getserviceaccountrequest)  </div> | <div style="width:200px; text-align:center;">   [ServiceAccountInfo](service-account.md#serviceaccountinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**list**](service-account.md#list) </div> | <div style="width:200px; text-align:center;">    [ServiceAccountQuery](service-account.md#serviceaccountquery)  </div> | <div style="width:200px; text-align:center;">   [ServiceAccountsInfo](service-account.md#serviceaccountsinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**stat**](service-account.md#stat) </div> | <div style="width:200px; text-align:center;">    [ServiceAccountStatQuery](service-account.md#serviceaccountstatquery)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) </div> | <div style="width:400px;">  </div> | 
 

 
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
