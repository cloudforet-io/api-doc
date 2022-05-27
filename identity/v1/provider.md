---
description:  
---
# Provider

>  **Package : spaceone.api.identity.v1**

## Provider

{% hint style="info" %}
**Provider Methods:**

{%  endhint %}


| Method | Request | Response | Description |
| :--- | :--- | :--- | :--- |
| [**create**](provider.md#create)|   [CreateProviderRequest](provider.md#createproviderrequest) |   [ProviderInfo](provider.md#providerinfo) |  |
| [**update**](provider.md#update)|   [UpdateProviderRequest](provider.md#updateproviderrequest) |   [ProviderInfo](provider.md#providerinfo) |  |
| [**delete**](provider.md#delete)|   [ProviderRequest](provider.md#providerrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| [**get**](provider.md#get)|   [GetProviderRequest](provider.md#getproviderrequest) |   [ProviderInfo](provider.md#providerinfo) |  |
| [**list**](provider.md#list)|   [ProviderQuery](provider.md#providerquery) |   [ProvidersInfo](provider.md#providersinfo) |  |
| [**stat**](provider.md#stat)|   [ProviderStatQuery](provider.md#providerstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 

 
### create
> **POST** /identity/v1/providers
>


| Type | Message |
| :--- | :--- |
| Request | [CreateProviderRequest](provider.md#createproviderrequest) |
| Response |  [ProviderInfo](provider.md#providerinfo)  |
 
 

 
### update
> **PUT** /identity/v1/provider/{provider_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateProviderRequest](provider.md#updateproviderrequest) |
| Response |  [ProviderInfo](provider.md#providerinfo)  |
 
 

 
### delete
> **DELETE** /identity/v1/provider/{provider_id}
>


| Type | Message |
| :--- | :--- |
| Request | [ProviderRequest](provider.md#providerrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /identity/v1/provider/{provider_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetProviderRequest](provider.md#getproviderrequest) |
| Response |  [ProviderInfo](provider.md#providerinfo)  |
 
 

 
### list
> **GET** /identity/v1/providers
>
> **POST** /identity/v1/providers/search



| Type | Message |
| :--- | :--- |
| Request | [ProviderQuery](provider.md#providerquery) |
| Response |  [ProvidersInfo](provider.md#providersinfo)  |
 
 

 
### stat
> **POST** /identity/v1/providers/stat
>


| Type | Message |
| :--- | :--- |
| Request | [ProviderStatQuery](provider.md#providerstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CreateProviderRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| provider |string|✅| |
| name |string|✅| |
| template |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| capability |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| domain_id |string|✅| |

### GetProviderRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| provider |string|✅| |
| only |list of string|❌| |
| domain_id |string|✅| |

### ProviderInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| provider |string | |
| name |string | |
| template |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| capability |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| created_at |string | |

### ProviderQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| provider |string|❌| |
| name |string|❌| |
| domain_id |string|✅| |

### ProviderRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| provider |string|✅| |
| domain_id |string|✅| |

### ProviderStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| domain_id |string|✅| |

### ProvidersInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of ProviderInfo](provider.md#providerinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### UpdateProviderRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| provider |string|✅| |
| name |string|❌| |
| template |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| capability |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| domain_id |string|✅| |
