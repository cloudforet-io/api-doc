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
| :-----: | :--------: | :--------: | :-------------------- |
| [**create**](service-account.md#create)|   [CreateServiceAccountRequest](service-account.md#createserviceaccountrequest) |   [ServiceAccountInfo](service-account.md#serviceaccountinfo) |  |
| [**update**](service-account.md#update)|   [UpdateServiceAccountRequest](service-account.md#updateserviceaccountrequest) |   [ServiceAccountInfo](service-account.md#serviceaccountinfo) |  |
| [**delete**](service-account.md#delete)|   [ServiceAccountRequest](service-account.md#serviceaccountrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| [**get**](service-account.md#get)|   [GetServiceAccountRequest](service-account.md#getserviceaccountrequest) |   [ServiceAccountInfo](service-account.md#serviceaccountinfo) |  |
| [**list**](service-account.md#list)|   [ServiceAccountQuery](service-account.md#serviceaccountquery) |   [ServiceAccountsInfo](service-account.md#serviceaccountsinfo) |  |
| [**stat**](service-account.md#stat)|   [ServiceAccountStatQuery](service-account.md#serviceaccountstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |TEST

<table style="border-collapse: collapse; text-align: left; line-height: 1.5;">
    <thead>
    <tr>
      <th scope="cols" style="padding: 10px; font-weight: bold; vertical-align: top; color: #369; border-bottom: 3px solid #036;">Method</th>
      <th scope="cols" style="padding: 10px; font-weight: bold; vertical-align: top; color: #369; border-bottom: 3px solid #036;">Request</th>
      <th scope="cols" style="padding: 10px; font-weight: bold; vertical-align: top; color: #369; border-bottom: 3px solid #036;">Response</th>
      <th scope="cols" style="padding: 10px; font-weight: bold; vertical-align: top; color: #369; border-bottom: 3px solid #036;">Description</th>
    </tr>
    </thead>
    <tbody>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">create</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   CreateServiceAccountRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ServiceAccountInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">update</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   UpdateServiceAccountRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ServiceAccountInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">delete</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ServiceAccountRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   google.protobuf.Empty </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">get</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   GetServiceAccountRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ServiceAccountInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">list</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ServiceAccountQuery </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ServiceAccountsInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">stat</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ServiceAccountStatQuery </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   google.protobuf.Struct </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr></tbody>
</table> 
 

 
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
