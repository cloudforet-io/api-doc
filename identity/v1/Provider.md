---
description:  
---
# Provider

>  **Package : spaceone.api.identity.v1**

## Provider

{% hint style="info" %}
**Provider Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [create](Provider.md#create)| [CreateProviderRequest](Provider.md#createproviderrequest) | [ProviderInfo](Provider.md#providerinfo) |  |
| 2 | [update](Provider.md#update)| [UpdateProviderRequest](Provider.md#updateproviderrequest) | [ProviderInfo](Provider.md#providerinfo) |  |
| 3 | [delete](Provider.md#delete)| [ProviderRequest](Provider.md#providerrequest) |[google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 4 | [get](Provider.md#get)| [GetProviderRequest](Provider.md#getproviderrequest) | [ProviderInfo](Provider.md#providerinfo) |  |
| 5 | [list](Provider.md#list)| [ProviderQuery](Provider.md#providerquery) | [ProvidersInfo](Provider.md#providersinfo) |  |
| 6 | [stat](Provider.md#stat)| [ProviderStatQuery](Provider.md#providerstatquery) |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |

### create
> **POST** /identity/v1/providers
>



| Type | Message |
| :--- | :--- |
| Request | [CreateProviderRequest](Provider.md#createproviderrequest) |
| Response |  [ProviderInfo](Provider.md#providerinfo)  |



### update
> **PUT** /identity/v1/provider/{provider_id}
>



| Type | Message |
| :--- | :--- |
| Request | [UpdateProviderRequest](Provider.md#updateproviderrequest) |
| Response |  [ProviderInfo](Provider.md#providerinfo)  |



### delete
> **DELETE** /identity/v1/provider/{provider_id}
>



| Type | Message |
| :--- | :--- |
| Request | [ProviderRequest](Provider.md#providerrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |



### get
> **GET** /identity/v1/provider/{provider_id}
>



| Type | Message |
| :--- | :--- |
| Request | [GetProviderRequest](Provider.md#getproviderrequest) |
| Response |  [ProviderInfo](Provider.md#providerinfo)  |



### list
> **GET** /identity/v1/providers
>
> **POST** /identity/v1/providers/search




| Type | Message |
| :--- | :--- |
| Request | [ProviderQuery](Provider.md#providerquery) |
| Response |  [ProvidersInfo](Provider.md#providersinfo)  |



### stat
> **POST** /identity/v1/providers/stat
>



| Type | Message |
| :--- | :--- |
| Request | [ProviderStatQuery](Provider.md#providerstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |





## Message

### CreateProviderRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | provider |string |✅ ||
| 2 | name |string |✅ ||
| 3 | template |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 4 | metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 5 | capability |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 6 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 7 | domain_id |string |❌ ||

### GetProviderRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | provider |string |✅ ||
| 2 | only |string |❌ ||
| 3 | domain_id |string |❌ ||

### ProviderInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | provider |string | ||
| 2 | name |string | ||
| 3 | template |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||
| 4 | metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||
| 5 | capability |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||
| 6 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||
| 7 | created_at |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) | ||

### ProviderQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query) |❌ ||
| 2 | provider |string |❌ ||
| 3 | name |string |❌ ||
| 4 | domain_id |string |❌ ||

### ProviderRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | provider |string |✅ ||
| 2 | domain_id |string |❌ ||

### ProviderStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query) |✅ ||

### ProvidersInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | results |[ProviderInfo](Provider.md#providerinfo) | ||
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | ||

### UpdateProviderRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | provider |string |✅ ||
| 2 | name |string |❌ ||
| 3 | template |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 4 | metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 5 | capability |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 6 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 7 | domain_id |string |❌ ||
