---
description: null
---

# Service Account

> **Package : spaceone.api.identity.v1**

## ServiceAccount

{% hint style="info" %}
**ServiceAccount Methods:**
{% endhint %}

| NO | Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [create](service-account.md#create) | [CreateServiceAccountRequest](service-account.md#createserviceaccountrequest) | [ServiceAccountInfo](service-account.md#serviceaccountinfo) |  |
| 2 | [update](service-account.md#update) | [UpdateServiceAccountRequest](service-account.md#updateserviceaccountrequest) | [ServiceAccountInfo](service-account.md#serviceaccountinfo) |  |
| 3 | [delete](service-account.md#delete) | [ServiceAccountRequest](service-account.md#serviceaccountrequest) | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |  |
| 4 | [get](service-account.md#get) | [GetServiceAccountRequest](service-account.md#getserviceaccountrequest) | [ServiceAccountInfo](service-account.md#serviceaccountinfo) |  |
| 5 | [list](service-account.md#list) | [ServiceAccountQuery](service-account.md#serviceaccountquery) | [ServiceAccountsInfo](service-account.md#serviceaccountsinfo) |  |
| 6 | [stat](service-account.md#stat) | [ServiceAccountStatQuery](service-account.md#serviceaccountstatquery) | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  |

### create

> **POST** /identity/v1/service-accounts

| Type | Message |
| :--- | :--- |
| Request | [CreateServiceAccountRequest](service-account.md#createserviceaccountrequest) |
| Response | [ServiceAccountInfo](service-account.md#serviceaccountinfo) |

### update

> **PUT** /identity/v1/service-account/{service\_account\_id}

| Type | Message |
| :--- | :--- |
| Request | [UpdateServiceAccountRequest](service-account.md#updateserviceaccountrequest) |
| Response | [ServiceAccountInfo](service-account.md#serviceaccountinfo) |

### delete

> **DELETE** /identity/v1/service-account/{service\_account\_id}

| Type | Message |
| :--- | :--- |
| Request | [ServiceAccountRequest](service-account.md#serviceaccountrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |

### get

> **GET** /identity/v1/service-account/{service\_account\_id}

| Type | Message |
| :--- | :--- |
| Request | [GetServiceAccountRequest](service-account.md#getserviceaccountrequest) |
| Response | [ServiceAccountInfo](service-account.md#serviceaccountinfo) |

### list

> **GET** /identity/v1/service-accounts
>
> **POST** /identity/v1/service-accounts/search

| Type | Message |
| :--- | :--- |
| Request | [ServiceAccountQuery](service-account.md#serviceaccountquery) |
| Response | [ServiceAccountsInfo](service-account.md#serviceaccountsinfo) |

### stat

> **POST** /identity/v1/service-accounts/stat

| Type | Message |
| :--- | :--- |
| Request | [ServiceAccountStatQuery](service-account.md#serviceaccountstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |

## Message

### CreateServiceAccountRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name | string |  | required |
| 2 | data | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  | required |
| 3 | provider | string |  | required |
| 4 | project\_id | string |  | optional |
| 5 | tags | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  | optional |
| 6 | domain\_id | string |  | required |

### GetServiceAccountRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | service\_account\_id | string |  | required |
| 2 | domain\_id | string |  | required |
| 3 | only | string |  | optional |

### ServiceAccountInfo

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | service\_account\_id | string |  |  |
| 2 | name | string |  |  |
| 3 | data | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  |  |
| 4 | provider | string |  |  |
| 5 | project\_info | [ProjectInfo](service-account.md#projectinfo) |  |  |
| 6 | domain\_id | string |  |  |
| 7 | tags | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  |  |
| 8 | created\_at | [google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) |  |  |

### ServiceAccountQuery

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query | [spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query) |  | optional |
| 2 | service\_account\_id | string |  | optional |
| 3 | name | string |  | optional |
| 4 | provider | string |  | optional |
| 5 | project\_id | string |  | optional |
| 6 | domain\_id | string |  | optional |

### ServiceAccountRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | service\_account\_id | string |  | required |
| 2 | domain\_id | string |  | required |

### ServiceAccountStatQuery

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query | [spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query) |  | required |
| 2 | domain\_id | string |  | required |

### ServiceAccountsInfo

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | results | [ServiceAccountInfo](service-account.md#serviceaccountinfo) |  |  |
| 2 | total\_count | [int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) |  |  |

### UpdateServiceAccountRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | service\_account\_id | string |  | required |
| 2 | name | string |  | optional |
| 3 | data | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  | optional |
| 4 | project\_id | string |  | optional |
| 5 | tags | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  | optional |
| 6 | domain\_id | string |  | required |
| 7 | release\_project | bool |  | optional |

