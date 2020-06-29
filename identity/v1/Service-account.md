---
description:  
---
# Service account

>  **Package : spaceone.api.identity.v1**

## ServiceAccount

{% hint style="info" %}
**ServiceAccount Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [create](Service-account.md#create)| [CreateServiceAccountRequest](Service-account.md#createserviceaccountrequest) | [ServiceAccountInfo](Service-account.md#serviceaccountinfo) |  |
| 2 | [update](Service-account.md#update)| [UpdateServiceAccountRequest](Service-account.md#updateserviceaccountrequest) | [ServiceAccountInfo](Service-account.md#serviceaccountinfo) |  |
| 3 | [delete](Service-account.md#delete)| [ServiceAccountRequest](Service-account.md#serviceaccountrequest) |[google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 4 | [get](Service-account.md#get)| [GetServiceAccountRequest](Service-account.md#getserviceaccountrequest) | [ServiceAccountInfo](Service-account.md#serviceaccountinfo) |  |
| 5 | [list](Service-account.md#list)| [ServiceAccountQuery](Service-account.md#serviceaccountquery) | [ServiceAccountsInfo](Service-account.md#serviceaccountsinfo) |  |
| 6 | [stat](Service-account.md#stat)| [ServiceAccountStatQuery](Service-account.md#serviceaccountstatquery) |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |

### create
> **POST** /identity/v1/service-accounts
>



| Type | Message |
| :--- | :--- |
| Request | [CreateServiceAccountRequest](Service-account.md#createserviceaccountrequest) |
| Response |  [ServiceAccountInfo](Service-account.md#serviceaccountinfo)  |



### update
> **PUT** /identity/v1/service-account/{service_account_id}
>



| Type | Message |
| :--- | :--- |
| Request | [UpdateServiceAccountRequest](Service-account.md#updateserviceaccountrequest) |
| Response |  [ServiceAccountInfo](Service-account.md#serviceaccountinfo)  |



### delete
> **DELETE** /identity/v1/service-account/{service_account_id}
>



| Type | Message |
| :--- | :--- |
| Request | [ServiceAccountRequest](Service-account.md#serviceaccountrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |



### get
> **GET** /identity/v1/service-account/{service_account_id}
>



| Type | Message |
| :--- | :--- |
| Request | [GetServiceAccountRequest](Service-account.md#getserviceaccountrequest) |
| Response |  [ServiceAccountInfo](Service-account.md#serviceaccountinfo)  |



### list
> **GET** /identity/v1/service-accounts
>
> **POST** /identity/v1/service-accounts/search




| Type | Message |
| :--- | :--- |
| Request | [ServiceAccountQuery](Service-account.md#serviceaccountquery) |
| Response |  [ServiceAccountsInfo](Service-account.md#serviceaccountsinfo)  |



### stat
> **POST** /identity/v1/service-accounts/stat
>



| Type | Message |
| :--- | :--- |
| Request | [ServiceAccountStatQuery](Service-account.md#serviceaccountstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |





## Message

### CreateServiceAccountRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name |string |✅ ||
| 2 | data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |✅ ||
| 3 | provider |string |✅ ||
| 4 | project_id |string |❌ ||
| 5 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 6 | domain_id |string |✅ ||

### GetServiceAccountRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | service_account_id |string |✅ ||
| 2 | domain_id |string |✅ ||
| 3 | only |string |❌ ||

### ServiceAccountInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | service_account_id |string | ||
| 2 | name |string | ||
| 3 | data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||
| 4 | provider |string | ||
| 5 | project_info |[ProjectInfo](Service-account.md#projectinfo) | ||
| 6 | domain_id |string | ||
| 7 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||
| 8 | created_at |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) | ||

### ServiceAccountQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query) |❌ ||
| 2 | service_account_id |string |❌ ||
| 3 | name |string |❌ ||
| 4 | provider |string |❌ ||
| 5 | project_id |string |❌ ||
| 6 | domain_id |string |❌ ||

### ServiceAccountRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | service_account_id |string |✅ ||
| 2 | domain_id |string |✅ ||

### ServiceAccountStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query) |✅ ||
| 2 | domain_id |string |✅ ||

### ServiceAccountsInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | results |[ServiceAccountInfo](Service-account.md#serviceaccountinfo) | ||
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | ||

### UpdateServiceAccountRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | service_account_id |string |✅ ||
| 2 | name |string |❌ ||
| 3 | data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 4 | project_id |string |❌ ||
| 5 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 6 | domain_id |string |✅ ||
| 7 | release_project |bool |❌ ||
